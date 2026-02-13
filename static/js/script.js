let mediaRecorder;
let audioChunks = [];
let activeFieldId = null;

// List of voice-input field IDs
const VOICE_FIELDS = ['age', 'symptoms', 'diagnosis', 'prescription', 'place'];
let lastFocusedFieldId = null;

// Track focus on voice-input fields
document.addEventListener('focusin', (event) => {
  const id = event.target.id;
  if (VOICE_FIELDS.includes(id)) {
    lastFocusedFieldId = id;
  }
});

function startRecording(event) {
  event.preventDefault();
  activeFieldId = lastFocusedFieldId;
  if (!VOICE_FIELDS.includes(activeFieldId)) {
    alert("Please focus a voice-input field (Age, Symptoms, Diagnosis, Prescription, or Place) before recording.");
    return;
  }
  document.getElementById(activeFieldId).focus();
  audioChunks = [];
  navigator.mediaDevices.getUserMedia({ audio: true })
    .then(stream => {
      mediaRecorder = new MediaRecorder(stream);
      mediaRecorder.start();
      document.getElementById('stopBtn').disabled = false;
      document.getElementById('startBtn').disabled = true;
      document.getElementById('status').textContent = "Recording...";
      mediaRecorder.ondataavailable = e => audioChunks.push(e.data);
      mediaRecorder.onstop = () => {
        const audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
        uploadAudio(audioBlob, activeFieldId);
        document.getElementById('startBtn').disabled = false;
      };
    })
    .catch(err => alert("Microphone error: " + err));
}

function stopRecording(event) {
  event.preventDefault();
  if (mediaRecorder && mediaRecorder.state === 'recording') {
    mediaRecorder.stop();
    document.getElementById('stopBtn').disabled = true;
    document.getElementById('status').textContent = 'Stopped recording. Processing...';
  }
}

function uploadAudio(blob, fieldId) {
  const loading = document.getElementById('loading');
  const status = document.getElementById('status');

  if (loading) loading.classList.remove('hidden');
  status.textContent = 'Processing audio...';

  const formData = new FormData();
  formData.append('audio', blob, 'recording.wav');
  formData.append('field', fieldId);
  fetch('/transcribe', { method: 'POST', body: formData })
    .then(response => response.json())
    .then(data => {
      if (loading) loading.classList.add('hidden');
      if (data.error) {
        alert('Error from server: ' + data.error);
        status.textContent = 'Error during transcription.';
        return;
      }
      const field = document.getElementById(fieldId);
      if (field) {
        field.value = data.paraphrased_text;
      }
      status.textContent = 'Voice input recorded and transcribed.';
    })
    .catch(() => {
      if (loading) loading.classList.add('hidden');
      status.textContent = 'Failed to upload or transcribe audio.';
    });
}

// SUBMIT FORM: Now sends to Flask backend `/submit`
function submitForm() {
  const payload = {
    name: document.getElementById('name').value,
    place: document.getElementById('place').value,
    age: document.getElementById('age').value,
    gender: document.getElementById('gender').value,
    symptoms: document.getElementById('symptoms').value,
    diagnosis: document.getElementById('diagnosis').value,
    prescription: document.getElementById('prescription').value
  };
  fetch('/submit', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
  })
    .then(res => res.json())
    .then(data => {
      document.getElementById('status').textContent = data.message;
    })
    .catch(error => {
      document.getElementById('status').textContent = 'Failed to save data.';
    });
}

document.addEventListener('DOMContentLoaded', () => {
  document.getElementById('startBtn').addEventListener('click', startRecording);
  document.getElementById('stopBtn').addEventListener('click', stopRecording);
  document.getElementById('submitBtn').addEventListener('click', submitForm);
});
