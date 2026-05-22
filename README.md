# 📚 EduGPT — Your Personal AI Instructor

> An intelligent tutoring system powered by **Groq + LLaMA 3.3 70B** that designs a custom syllabus for any topic and then teaches it to you interactively.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Gradio](https://img.shields.io/badge/UI-Gradio-orange)
![LangChain](https://img.shields.io/badge/Framework-LangChain-green)
![Groq](https://img.shields.io/badge/LLM-Groq%20%7C%20LLaMA%203.3-purple)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 🎯 What Does It Do?

EduGPT acts as your personal AI instructor. You tell it a topic — it designs a full course syllabus using two AI agents that debate and collaborate, then a third agent teaches you step-by-step in an interactive chat.

**Example:** Type `"Machine Learning"` → get a structured syllabus → chat with your AI instructor who teaches you the whole course.

---

## ✨ Key Features

- 🧠 **Multi-Agent Syllabus Design** — Two AI agents (Instructor + Teaching Assistant) collaborate to create a structured course syllabus for any topic
- 📖 **Adaptive Instruction** — A dedicated instructor agent teaches you topic-by-topic, adapting to your questions and pace
- ⚡ **Powered by Groq** — Uses Groq's free, blazing-fast API with LLaMA 3.3 70B
- 🖥️ **Clean Gradio UI** — Simple browser-based interface with two tabs: Syllabus Builder and AI Chat
- 🔄 **Context-Aware Chat** — Remembers conversation history to provide continuity across your learning session

---

## 🏗️ Architecture

```
User Input (Topic)
      │
      ▼
┌─────────────────────────────────┐
│   Syllabus Generation Phase     │
│  ┌──────────┐  ┌─────────────┐  │
│  │Instructor│◄►│  Teaching   │  │
│  │  Agent   │  │  Assistant  │  │
│  └──────────┘  └─────────────┘  │
│     (5 dialogue turns)          │
│         ▼                       │
│   Summarizer Agent              │
│   → Structured Syllabus         │
└─────────────────────────────────┘
      │
      ▼
┌─────────────────────────────────┐
│   Teaching Phase                │
│   TeachingGPT Agent             │
│   - Follows syllabus order      │
│   - Interactive Q&A chat        │
└─────────────────────────────────┘
```

---

## 🚀 Quick Start

### 1. Prerequisites
- Python 3.10 or higher
- A free [Groq API key](https://console.groq.com) (takes 30 seconds to get)

### 2. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/EduGPT.git
cd EduGPT
```

### 3. Create a Virtual Environment
```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On Mac/Linux:
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Set Up Your API Key
Copy the example env file and add your key:
```bash
cp .env.example .env
```
Then open `.env` and replace the placeholder with your real key:
```
GROQ_API_KEY=your_groq_api_key_here
```
> 💡 Get your free Groq API key at [console.groq.com](https://console.groq.com)

### 6. Run the App
```bash
python src/run.py
```
Then open the link shown in your terminal (e.g. `http://127.0.0.1:7860`).

---

## 🎮 How to Use

1. **Tab 1 — "Input Your Information"**
   - Type the topic you want to learn (e.g. `Python`, `Quantum Physics`, `Guitar`)
   - Click **"Build the Bot!!!"**
   - Wait ~30 seconds while the AI agents design your custom syllabus
   - Your syllabus appears in the output box

2. **Tab 2 — "AI Instructor"**
   - Chat with your AI instructor
   - It teaches you topic by topic, following the syllabus
   - Ask questions, request examples, or ask for clarification anytime

---

## 📁 Project Structure

```
EduGPT/
├── src/
│   ├── run.py                  # Main app entry point (Gradio UI)
│   ├── generating_syllabus.py  # Multi-agent syllabus generation logic
│   └── teaching_agent.py       # Instructor agent and conversation chain
├── .env.example                # Template for environment variables
├── .gitignore                  # Files excluded from git
├── requirements.txt            # Python dependencies
├── README.md                   # This file
└── LICENSE                     # MIT License
```

---

## 🔧 Tech Stack

| Component | Technology |
|-----------|-----------|
| LLM Provider | [Groq](https://groq.com) (Free tier available) |
| LLM Model | LLaMA 3.3 70B Versatile |
| Agent Framework | [LangChain](https://langchain.com) |
| UI | [Gradio](https://gradio.app) |
| Language | Python 3.10+ |
| Architecture | Multi-Agent (CAMEL-inspired) |

---

## 🌐 Live Demo

> 🔗 [Try it on Hugging Face Spaces](https://huggingface.co/spaces/YOUR_USERNAME/EduGPT)

*(Update this link after deployment)*

---

## 🛠️ Configuration

You can tweak these settings in the source files:

| Setting | File | Default | Description |
|---------|------|---------|-------------|
| `chat_turn_limit` | `generating_syllabus.py` | `5` | Agent dialogue turns for syllabus generation |
| `word_limit` | `generating_syllabus.py` | `50` | Word limit for task specification |
| `model_name` | Both agent files | `llama-3.3-70b-versatile` | Groq model used |
| `temperature` | Both agent files | `0.9 / 0.2` | Creativity of responses |

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork this repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m "Add: your feature description"`
4. Push to your fork: `git push origin feature/your-feature-name`
5. Open a Pull Request

### Ideas for Contributions
- [ ] Add support for other LLM providers (OpenAI, Anthropic)
- [ ] Save and load conversation history
- [ ] Export syllabus as PDF
- [ ] Add quiz/flashcard generation after each topic
- [ ] Support multiple languages

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgements

- Original project by [hqanhh](https://github.com/hqanhh/EduGPT)
- Agent architecture inspired by [CAMEL](https://github.com/camel-ai/camel)
- Built with [LangChain](https://github.com/langchain-ai/langchain) and [Gradio](https://github.com/gradio-app/gradio)

---

## 📬 Contact

Have questions or ideas? Open an [issue](https://github.com/YOUR_USERNAME/EduGPT/issues) on GitHub.
