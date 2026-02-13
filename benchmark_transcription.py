"""
Benchmark Transcription Script

This script uses the OpenAI Whisper API to transcribe a list of audio files
and benchmarks the performance (WER, duration, etc.) against ground truth text.
"""
import os
import tempfile
import pandas as pd
from openpyxl import Workbook
from jiwer import wer
from openai import OpenAI
from dotenv import load_dotenv
import imageio_ffmpeg

load_dotenv()

# Configure pydub to use imageio-ffmpeg BEFORE importing pydub
from pydub import AudioSegment
from pydub.utils import make_chunks
AudioSegment.converter = imageio_ffmpeg.get_ffmpeg_exe()
AudioSegment.ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
AudioSegment.ffprobe = imageio_ffmpeg.get_ffmpeg_exe()

# --- Configuration ---
API_KEY = os.environ.get("OPENAI_API_KEY", "YOUR_API_KEY_HERE")
BASE_URL = os.environ.get("OPENAI_BASE_URL", "YOUR_BASE_URL_HERE")

client = OpenAI(
    api_key=API_KEY,
    base_url=BASE_URL
)

def convert_to_wav(input_path):
    audio = AudioSegment.from_file(input_path)
    wav_path = input_path + ".wav"
    audio.export(wav_path, format="wav")
    return wav_path

def split_text_by_chunks(text, n_chunks):
    words = text.split()
    if n_chunks == 0:
        return []
    chunk_size = len(words) // n_chunks
    remainder = len(words) % n_chunks
    chunks = []
    start = 0
    for i in range(n_chunks):
        extra = 1 if i < remainder else 0
        end = start + chunk_size + extra
        chunk = " ".join(words[start:end])
        chunks.append(chunk)
        start = end
    return chunks

def transcribe_with_api(audio_path, chunk_len=15):
    """
    Transcribes audio using the OpenAI API, chunk by chunk.
    """
    audio = AudioSegment.from_file(audio_path)
    chunk_ms = chunk_len * 1000
    chunks = make_chunks(audio, chunk_ms)
    transcripts, durations, word_counts = [], [], []

    print(f"Transcribing {os.path.basename(audio_path)} in {len(chunks)} chunks...")

    for i, chunk in enumerate(chunks):
        # export chunk to temp file
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_file:
            chunk.export(temp_file.name, format="wav")
            temp_path = temp_file.name
        
        try:
            with open(temp_path, "rb") as audio_file:
                # Call OpenAI API
                transcript = client.audio.transcriptions.create(
                    model="whisper-1", 
                    file=audio_file,
                    response_format="text"
                )
                text = transcript.strip()
        except Exception as e:
            print(f"Error transcribing chunk {i}: {e}")
            text = ""
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)

        transcripts.append(text)
        durations.append(len(chunk) / 1000)
        word_counts.append(len(text.split()))
        
    return transcripts, durations, word_counts

def calculate_table_for_audio(audio_path, reference_text, chunk_len=15):
    results = []
    
    # Ensure wav format
    created_wav = False
    if not audio_path.lower().endswith(".wav"):
        try:
            wav_path = convert_to_wav(audio_path)
            created_wav = True
        except Exception as e:
            print(f"Error converting {audio_path}: {e}")
            return []
    else:
        wav_path = audio_path

    try:
        audio = AudioSegment.from_file(wav_path)
        chunk_ms = chunk_len * 1000
        n_chunks = len(make_chunks(audio, chunk_ms))
        
        # Split ground truth text into chunks to match audio chunks
        gt_chunks = split_text_by_chunks(reference_text, n_chunks)
        
        # Transcribe
        hyps, durs, wrds = transcribe_with_api(wav_path, chunk_len)
        
        # Verification: Handle case where API fails or returns empty
        if not hyps:
             print(f"No transcription results for {audio_path}")
             return []

        seg_count = len(hyps)
        total_dur_h = sum(durs) / 3600
        avg_dur = sum(durs) / seg_count if seg_count > 0 else 0
        avg_words = sum(wrds) / seg_count if seg_count > 0 else 0
        
        # Calculate WER
        wers = []
        for gt, hyp in zip(gt_chunks, hyps):
            try:
                wers.append(wer(gt, hyp))
            except:
                wers.append(1.0) # Penalty for error

        avg_wer = sum(wers) / seg_count * 100 if seg_count > 0 else 0
        std_wer = pd.Series(wers).std() * 100 if seg_count > 1 else 0
        
        total_gt_words = sum(len(gt.split()) for gt in gt_chunks)
        if total_gt_words > 0:
            wer_wrd = sum(wer(gt, hyp) * len(gt.split()) for gt, hyp in zip(gt_chunks, hyps)) / total_gt_words * 100
        else:
            wer_wrd = 0

        results.append([
            os.path.basename(audio_path),
            "openai-whisper",
            seg_count,
            round(total_dur_h, 2),
            round(avg_dur, 2),
            round(avg_words, 2),
            f"{round(avg_wer, 2)}%",
            f"{round(std_wer, 2)}%",
            f"{round(wer_wrd, 2)}%"
        ])

    except Exception as e:
        print(f"Error processing {audio_path}: {e}")
    finally:
        if created_wav and os.path.exists(wav_path):
            os.remove(wav_path)
            
    return results

def process_multiple_audios(audio_paths, ref_texts, chunk_len=15):
    all_results = []
    for audio_path, ref_text in zip(audio_paths, ref_texts):
        if os.path.exists(audio_path):
            results = calculate_table_for_audio(audio_path, ref_text, chunk_len)
            all_results.extend(results)
        else:
            print(f"File not found: {audio_path}")

    df = pd.DataFrame(all_results, columns=[
        "Audio File", "Model", "#Seg.", "Total Dur. (h)", "Avg. Dur.",
        "Avg. #Wrd.", "Avg. WER", "Std. Dev. of WER", "WER_wrd"])
    
    output_file = "benchmark_transcription_stats.xlsx"
    df.to_excel(output_file, index=False)
    print(df)
    print(f"Saved results to {output_file}")

# Example Usage
audio_paths = [
    r"C:\Users\linge\OneDrive\Desktop\audio\audio1.opus",
    r"C:\Users\linge\OneDrive\Desktop\audio\audio2.opus",
    r"C:\Users\linge\OneDrive\Desktop\audio\audio3.opus"
]

ref_texts = [
    """In the 16th century, an age of great marine and terrestrial exploration, Ferdinand Magellan led the first expedition to sail around the world. As a young Portuguese noble, he served the king of Portugal, but he became involved in the quagmire of political intrigue at court and lost the king’s favor. After he was dismissed from service by the king of Portugal, he offered to serve the future Emperor Charles V of Spain. A papal decree of 1493 had assigned all land in the New World west of 50 degrees W longitude to Spain and all the land east of that line to Portugal. Magellan offered to prove that the East Indies fell under Spanish authority.""",
    """Open your eyes in sea water and it is difficult to see much more than a murky, bleary green colour. Sounds, too, are garbled and difficult to comprehend. Without specialised equipment humans would be lost in these deep sea habitats, so how do fish make it seem so easy? Much of this is due to a biological phenomenon known as electroreception – the ability to perceive and act upon electrical stimuli as part of the overall senses. This ability is only found in aquatic or amphibious species because water is an efficient conductor of electricity.""",
    """Other creatures can go further still, however. Animals with active electroreception possess bodily organs that generate special electric signals on cue. These can be used for mating signals and territorial displays as well as locating objects in the water. Active electroreceptors can differentiate between the various resistances that their electrical currents encounter. This can help them identify whether another creature is prey, predator or something that is best left alone. Active electroreception has a range of about one body length – usually just enough to give its host time to get out of the way or go in for the kill."""
]

if __name__ == "__main__":
    process_multiple_audios(audio_paths, ref_texts)
