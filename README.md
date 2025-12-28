# 🤖 Nova - AI Voice Assistant (JARVIS Clone)

A high-performance, hands-free, bilingual AI voice assistant powered by Google's Gemini AI and Bytez Cloud ASR. Designed to be fast, responsive, and intelligent—just like JARVIS.

## ✨ Features

- 🎤 **Hands-Free VAD**: No keys to press. Nova automatically detects when you start and stop speaking.
- 🇮🇳 **Bilingual Support**: Perfectly understands and speaks both **Hindi** and **English**.
- 🧠 **Turbo Brain**: Powered by Google Gemini 2.5 Flash for near-instant thinking.
- ☁️ **Cloud ASR**: Uses Bytez SDK with `Whisper-Large-V3` for superior speech recognition accuracy.
- 🗣️ **Premium Neural Voice**: Uses `edge-tts` (Swara for Hindi, Ava for English) for human-like speech.
- � **Parallel Execution**: Nova performs tasks (opening apps, etc.) _while_ she is speaking to you.
- ⚡ **Direct-to-Memory**: No slow temporary files (`.wav` or `.mp3`). Everything is processed in RAM for maximum speed.
- 📸 **Vision**: Capture photos instantly from your webcam on command.
- ✍️ **Turbo Typing**: Near-instant text automation with support for Hindi characters.
- 💻 **Smart App Control**: Opens any software using Windows Start Menu search integration.

## 🛠️ Setup

### Prerequisites

- Python 3.13+
- [uv](https://github.com/astral-sh/uv) (Fast Python package manager)
- Microphone & Webcam
- Google Gemini API Key
- Bytez API Key

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Pratham-Prog861/jarvis-clone.git
   cd jarvis-clone
   ```

2. **Install dependencies**

   ```bash
   uv sync
   ```

3. **Set up Environment Variables**
   Create a `.env` file in the root directory:

   ```env
   GEMINI_API_KEY=your_gemini_key
   BYTEZ_API_KEY=your_bytez_key
   ```

4. **Run Nova**

   ```bash
   uv run main.py
   ```

## 🎮 Usage

1. **Start Nova**: Run the script and wait for "🤖 Nova is online".
2. **Just Talk**: Simply start speaking in Hindi or English.
3. **Hands-Free**: Nova will detect your voice, process the request, and respond automatically.

### Example Commands

- **Bilingual**: "नमस्ते नोवा, तुम कैसी हो?" (Namaste Nova, how are you?)
- **App Control**: "Open Visual Studio Code" or "Chrome kholo"
- **Automation**: "Type 'Hello World' in Hindi" or "Likho 'Namaste Bharat'"
- **Web**: "Search for the latest AI news" or "Open youtube.com"
- **Camera**: "Capture a photo" or "Meri photo khicho"

## 📁 Project Structure

```bash
jarvis-clone/
├── core/
│   ├── agent.py        # Brain (Gemini 1.5 Flash)
│   ├── emotion.py      # Sentiment Analysis
│   ├── memory.py       # Conversation History
│   └── router.py       # Action Orchestrator
├── voice/
│   ├── listener.py     # Cloud ASR (Bytez + Whisper V3)
│   └── speaker.py      # Neural TTS (Edge-TTS)
├── tools/
│   ├── browser.py      # Web & Search Tools
│   ├── camera.py       # OpenCV Photo Capture
│   ├── system.py       # Start Menu App Launcher
│   └── writer.py       # Clipboard-based Turbo Typing
├── prompts/
│   └── nova_system.txt # Personality & Logic Rules
├── main.py             # Entry Point (Parallel Loop)
└── pyproject.toml      # Modern Dependency Management
```

## � Key Dependencies

- `google-genai`: AI Brain
- `bytez`: Cloud Speech Recognition
- `edge-tts`: Premium Neural Voice
- `opencv-python`: Camera functionality
- `pyautogui` & `pyperclip`: System automation
- `pygame`: Audio playback (In-memory)
- `sounddevice`: Voice Activity Detection

## 📄 License

MIT License - Feel free to use and modify!

---

**Made with ❤️ by Pratham**
