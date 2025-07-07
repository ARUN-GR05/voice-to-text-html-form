let recognition;
let currentField = null;
let isDictating = false;

const fields = {
  "right eye observation": "right-eye",
  "right comments": "right-comments",
  "left eye observation": "left-eye",
  "left comments": "left-comments"
};

function setStatus(text, color = "green") {
  const status = document.getElementById("status");
  status.textContent = text;
  status.style.color = color;
}

function startRecognition() {
  const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
  if (!SpeechRecognition) {
    setStatus("❌ Speech Recognition not supported in this browser", "red");
    return;
  }

  recognition = new SpeechRecognition();
  recognition.continuous = true;
  recognition.interimResults = false;
  recognition.lang = "en-US";

  recognition.onstart = () => setStatus("🎤 Listening...");
  recognition.onerror = (e) => setStatus("❌ Error: " + e.error, "red");

  recognition.onresult = (event) => {
    let transcript = event.results[event.results.length - 1][0].transcript.trim().toLowerCase();

    // Fix "i" to "eye" if spoken in field names
    transcript = transcript.replace(/\bi\b/g, "eye");

    console.log("Heard:", transcript);

    if (transcript === "start" && currentField) {
      isDictating = true;
      setStatus(`🎤 Dictating into ${currentField.id}...`);
    } else if (transcript === "stop") {
      isDictating = false;
      setStatus("⏸️ Dictation stopped. Say a field name to switch.");
    } else if (fields[transcript]) {
      currentField = document.getElementById(fields[transcript]);
      currentField.focus();
      setStatus(`✅ Focused on: ${transcript}. Say "start" to begin.`);
    } else if (isDictating && currentField) {
      currentField.value += (currentField.value ? " " : "") + transcript;
    }
  };

  recognition.start();
}

window.onload = () => {
  setTimeout(() => {
    startRecognition();
  }, 1000); // start after 1 second
};
