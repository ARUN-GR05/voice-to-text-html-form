# Voice-Controlled Eye Comments Form (Hands-Free)

A fully voice-controlled HTML web form for ophthalmology observations.  
Control the form entirely by speaking — no mouse or keyboard required!

---

## How It Works

✅ Starts recording automatically when you open the page  
✅ Always listens for voice commands  
✅ Switch fields by saying field names, for example:
   - `right eye observation`
   - `right comments`
   - `left eye observation`
   - `left comments`
✅ Say `start` to begin dictating into the focused field  
✅ Speak your observation or comments  
✅ Say `stop` to pause dictation  
✅ Repeat to change fields and continue filling text

---

## How to Use

1. Open the file `index.html` in your browser (Chrome, Edge, etc.).
2. Speak any of these **field names**:
    - `right eye observation`
    - `right comments`
    - `left eye observation`
    - `left comments`
3. The field will become active.
4. Say `start` to begin recording text into that field.
5. Speak your notes. They appear automatically in the field.
6. Say `stop` to stop dictation.
7. Speak another field name to switch.

---

## Example Voice Flow


---

## Requirements

- Internet connection is required (Web Speech API often relies on cloud services)
- Works best on:
    - Google Chrome
    - Microsoft Edge
- Windows recommended for best microphone integration

> Note: Speech recognition may ask permission to access your microphone.

---

## Flaws and Limitations

⚠ **Needs Internet:**  
   - Most browsers send your speech to online servers for transcription.
   - No offline mode without additional libraries or models.

⚠ **Language Recognition Limitations:**  
   - Windows or browser engines may misrecognize words in other languages (e.g. regional Indian languages).
   - Accuracy drops in noisy environments or with strong accents.

⚠ **Delay (~3 seconds):**  
   - You may experience a short delay between speaking and seeing the text appear.

⚠ **False Activations:**  
   - Speech recognition might incorrectly interpret background sounds as commands.

⚠ **Not a Browser Extension Yet:**  
   - Currently a standalone web page. Could be rewritten as an extension for broader integration.

---

## Advantages

✅ No backend required  
✅ Simple HTML + JavaScript  
✅ Completely voice-controlled  
✅ Works in modern browsers  
✅ Could be converted into an extension for:
   - EMR systems
   - Ophthalmology tools
   - Hands-free medical dictation

---

## Project Structure


---

## Future Improvements

- Support multiple languages more accurately
- Provide an offline option using models like Whisper.cpp
- Package as a Chrome or Edge extension
- Improve user feedback (e.g. show what was heard live)
