<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>README - Voice-Controlled Eye Comments Form</title>
  <style>
    body {
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      background-color: #f0f4f9;
      color: #333;
      margin: 0;
      padding: 40px;
    }

    .container {
      max-width: 900px;
      margin: auto;
      background: #fff;
      padding: 30px;
      border-radius: 12px;
      box-shadow: 0 0 20px rgba(0,0,0,0.1);
    }

    h1, h2, h3 {
      color: #007BFF;
    }

    pre {
      background: #f7f7f7;
      padding: 15px;
      border-radius: 6px;
      overflow-x: auto;
    }

    code {
      background: #f0f0f0;
      padding: 2px 4px;
      border-radius: 4px;
      font-size: 0.95em;
    }

    ul, ol {
      margin-left: 20px;
    }

    .badge {
      display: inline-block;
      background: #007BFF;
      color: #fff;
      padding: 2px 8px;
      border-radius: 6px;
      font-size: 0.85em;
      margin-right: 5px;
    }

    .section {
      margin-top: 30px;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Voice-Controlled Eye Comments Form (Hands-Free)</h1>

    <p>A fully voice-controlled HTML web form for ophthalmology observations.<br>
    <strong>No clicking required — control the form entirely with your voice!</strong></p>

    <p>This project uses Windows Speech Recognition via the Web Speech API directly in the browser.</p>

    <div class="section">
      <h2>Features</h2>
      <ul>
        <li><span class="badge">✅</span> Always listening for voice commands</li>
        <li><span class="badge">✅</span> Switch fields by speaking their names</li>
        <li><span class="badge">✅</span> Say <code>start</code> to begin dictation into a field</li>
        <li><span class="badge">✅</span> Speak your observation or comments</li>
        <li><span class="badge">✅</span> Say <code>stop</code> to pause dictation</li>
        <li><span class="badge">✅</span> Completely hands-free experience</li>
        <li><span class="badge">✅</span> No backend or server required</li>
      </ul>
    </div>

    <div class="section">
      <h2>How to Use</h2>
      <ol>
        <li>Open the file <code>index.html</code> in your browser (Chrome, Edge, etc.).</li>
        <li>Speak any of these <strong>field names</strong> to select where you want to type:
          <ul>
            <li><code>right eye observation</code></li>
            <li><code>right comments</code></li>
            <li><code>left eye observation</code></li>
            <li><code>left comments</code></li>
          </ul>
        </li>
        <li>Once focused on the desired field, say: <code>start</code></li>
        <li>Speak your observation or comments. Your speech will appear in the chosen field.</li>
        <li>Say: <code>stop</code> to stop dictation.</li>
        <li>Repeat the process to switch fields and continue dictation.</li>
      </ol>
    </div>

    <div class="section">
      <h2>Example Voice Flow</h2>
      <pre>
You say: "right eye observation"
→ Focus moves to the right eye observation field

You say: "start"
→ Dictation begins

You say: "conjunctival congestion noted"
→ Text appears in the field

You say: "stop"
→ Dictation stops

You say: "left comments"
→ Focus moves to the left comments field

You say: "start"
→ Dictation begins again
      </pre>
    </div>

    <div class="section">
      <h2>Requirements</h2>
      <ul>
        <li>Windows recommended (for best speech engine support)</li>
        <li>Modern browser supporting the Web Speech API:
          <ul>
            <li>Google Chrome</li>
            <li>Microsoft Edge</li>
          </ul>
        </li>
      </ul>
      <p><strong>Note:</strong> Speech recognition may ask permission to access your microphone the first time you load the page.</p>
    </div>

    <div class="section">
      <h2>Project Structure</h2>
      <pre>
voice-eye-comments-form/
├── index.html
├── README.html
└── .gitignore
      </pre>
    </div>
  </div>
</body>
</html>
