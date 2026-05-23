---
title: EduGPT
emoji: 📚
colorFrom: blue
colorTo: purple
sdk: gradio
app_file: app.py
pinned: false
license: mit
short_description: Your Personal AI Instructor powered by Groq + LLaMA 3.3
---

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
git clone https://github.com/kn-keerthana/EduGPT.git
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
```bash
cp .env.example .env
```
Open `.env` and add your key:
```
GROQ_API_KEY=your_groq_api_key_here
```

### 6. Run the App
```bash
python app.py
```

---

## 📁 Project Structure

```
EduGPT/
├── src/
│   ├── generating_syllabus.py  # Multi-agent syllabus generation
│   └── teaching_agent.py       # Instructor agent and conversation chain
├── app.py                      # Main entry point (Gradio UI)
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

---

## 🌐 Live Demo

> 🔗 [Try it on Hugging Face Spaces](https://huggingface.co/spaces/KeerthanaKN/EduGPT)

---

## 🤝 Contributing

1. Fork this repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Commit: `git commit -m "Add: your feature"`
4. Push: `git push origin feature/your-feature-name`
5. Open a Pull Request

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgements

- Original project by [hqanhh](https://github.com/hqanhh/EduGPT)
- Agent architecture inspired by [CAMEL](https://github.com/camel-ai/camel)
- Built with [LangChain](https://github.com/langchain-ai/langchain) and [Gradio](https://github.com/gradio-app/gradio)

---

## 📬 Contact

Open an [issue](https://github.com/kn-keerthana/EduGPT/issues) on GitHub.
