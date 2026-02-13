# ClinicaSync: AI-Powered Medical Scribe

![ClinicaSync Banner](https://img.shields.io/badge/Status-Production_Ready-success?style=for-the-badge) ![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge) ![OpenAI](https://img.shields.io/badge/AI-Powered-green?style=for-the-badge)

**ClinicaSync** is a professional-grade, voice-controlled medical scribe application designed for doctors and healthcare professionals. It leverages **OpenAI Whisper** and **GPT-3.5** to transcribe, correct, and format clinical notes in real-time, completely hands-free.

## 🚀 Key Features

*   **🎙️ Intelligent Voice Transcription**: Speak naturally. The AI captures your dictation with high accuracy using Whisper-1.
*   **🧠 AI Scribe Correction**: Automatically corrects medical terminology, grammar, and structures "shorthand" notes into professional clinical language.
*   **🏥 Premium Medical UI**: A "Glassmorphism" design system tailored for a modern clinical environment (Navy/Teal palette).
*   **📊 Patient Records Dashboard**: A searchable, sortable history of all patient interactions.
*   **💾 Robust Data Storage**: Automatically saves every session to both CSV and Excel for easy integration with EMR systems.
*   **📄 PDF Prescriptions (Optional)**: Generate print-ready prescriptions instantly.

## 🛠️ Installation

### Prerequisites
*   Python 3.10+
*   FFmpeg (Installed and added to PATH)
*   OpenAI API Key

### Setup

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/ARUN-GR05/voice-to-text-html-form.git
    cd voice-to-text-html-form
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: Ensure you have `flask`, `openai`, `python-dotenv`, `openpyxl`, `pydub`, `imageio-ffmpeg` installed if requirements.txt is missing)*

3.  **Configure Environment**
    Create a `.env` file in the root directory:
    ```env
    OPENAI_API_KEY=your_api_key_here
    ```

4.  **Run the Application**
    ```bash
    python app.py
    ```

5.  **Access the Dashboard**
    Open your browser to `http://127.0.0.1:5000`.

## 🖥️ Usage Guide

1.  **Start a Session**: Open the app. The form is ready for input.
2.  **Dictate**: Click a field (Symptoms, Diagnosis, etc.) and click "Start Recording". Speak your observations.
3.  **Review & Submit**: The AI will transcribe and correct your text. Review the form and click "Submit to Records".
4.  **Manage Patients**: Click "Dashboard" to view history or search for past records.

## 📂 Project Structure

```
├── app.py                  # Main Flask Application
├── benchmark_*.py          # Accuracy Testing Scripts
├── data.csv/.xlsx          # Local Data Storage
├── static/
│   ├── css/style.css       # Premium Medical Styles
│   └── js/script.js        # Voice Recording Logic
└── templates/
    ├── form.html           # Main Scribe Interface
    └── dashboard.html      # Patient Records View
```

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements.

## 📄 License

This project is open-source and available under the request of the user.
