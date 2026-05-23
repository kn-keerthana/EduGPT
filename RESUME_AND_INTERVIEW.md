# 🎯 Resume & Interview Preparation

## Resume Bullet Points

Use these on your resume under Projects:

---

**EduGPT — AI-Powered Tutoring System** | Python, LangChain, Groq, Gradio
- Built an intelligent multi-agent tutoring application that dynamically generates personalized course syllabi for any topic using LLaMA 3.3 70B via Groq API
- Designed a CAMEL-inspired multi-agent architecture where two AI agents (Instructor + Teaching Assistant) engage in structured dialogue to collaboratively design course content
- Implemented an interactive Gradio UI with streaming chat responses, enabling real-time AI instruction with conversation history tracking
- Migrated original OpenAI-based implementation to Groq's free LLM API, reducing inference costs to zero while improving response speed
- Deployed application on Hugging Face Spaces for public access; managed environment secrets and production configuration

---

## LinkedIn Project Description

**EduGPT – Personal AI Instructor**

Built an AI tutoring app using Python, LangChain, and Groq's free LLaMA 3.3 70B API. The system uses a multi-agent architecture where two AI agents collaborate to design a custom course syllabus for any topic a user requests. A third "instructor" agent then teaches the material step-by-step through an interactive Gradio chat interface.

Key contributions:
• Adapted a CAMEL-style multi-agent dialogue system for educational syllabus generation
• Integrated Groq's API as a zero-cost, high-speed alternative to OpenAI
• Built and deployed a Gradio web app with streaming responses and session memory
• Deployed on Hugging Face Spaces with secure API key management

🔗 GitHub: https://github.com/kn-keerthana/EduGPT | 🚀 Live Demo: https://huggingface.co/spaces/kn-keerthana/EduGPT

---

## Interview Questions & Answers

### Q: What is EduGPT and what does it do?
**A:** EduGPT is an AI-powered tutoring system. You input any topic you want to learn, and the system first uses two AI agents that debate and collaborate to design a structured course syllabus. Then a dedicated instructor agent teaches you that syllabus interactively through a chat interface. It's powered by LLaMA 3.3 70B through Groq's API.

### Q: Can you explain the multi-agent architecture?
**A:** The system uses three types of agents. First, a "task specifier" agent takes the user's topic and makes the task more concrete. Then two "discussion" agents — an Instructor and a Teaching Assistant — exchange five rounds of structured dialogue to plan out the course content. Their conversation is summarized by a fourth "summarizer" agent into a clean syllabus. Finally, a "TeachingGPT" agent uses that syllabus as its system context to teach the user through ongoing conversation.

### Q: Why did you switch from OpenAI to Groq?
**A:** Groq offers a free tier with very high speed inference using the LLaMA 3.3 70B model — it's actually faster than many paid alternatives due to Groq's custom LPU hardware. For a project like this where fast responses matter for the learning experience, and where I wanted it to be freely accessible, Groq was the better choice.

### Q: What is LangChain and why did you use it?
**A:** LangChain is a framework that makes it easier to build applications with LLMs. It provides abstractions like message types (HumanMessage, SystemMessage, AIMessage), prompt templates, and chat model integrations. I used it to structure the agent conversations cleanly and to integrate with Groq via the `langchain-groq` package.

### Q: What is Gradio and why did you choose it?
**A:** Gradio is a Python library that lets you build web UIs for ML models with very little code. It was perfect for this project because the entire UI — tabs, textboxes, chatbot, buttons — was built in pure Python without any HTML/CSS/JavaScript. It also provides easy sharing with public links.

### Q: How does the conversation memory work?
**A:** The TeachingGPT agent maintains a `conversation_history` list that accumulates every message (both user and assistant). Each time the instructor is called, it passes the full conversation history into the prompt template, giving the LLM full context of everything discussed so far. This is a simple but effective form of in-session memory.

### Q: What would you improve if you had more time?
**A:** A few things: (1) Persistent storage so users can save and resume sessions, (2) PDF export of the syllabus, (3) Quiz generation after each topic to test understanding, (4) Support for other LLM providers so users can choose, and (5) A more sophisticated memory system using vector embeddings for very long conversations.

---

## Architecture Explanation (For Technical Interviews)

```
User submits topic
    → Task Specifier Agent (makes topic concrete, ~50 words)
    → Instructor Agent + Teaching Assistant Agent (5 turns of CAMEL-style dialogue)
    → Summarizer Agent (converts dialogue → structured syllabus)
    → TeachingGPT (receives syllabus as system prompt, enters chat loop)
    → Gradio UI (streams responses character-by-character)
```

**Key design patterns used:**
- **Multi-agent roleplay** (CAMEL architecture): agents given personas and strict rules about their role
- **Prompt engineering**: System prompts with delimiters (===) to separate data from instructions
- **Streaming UI**: Gradio generator function yields characters one by one for typewriter effect
- **Environment variable management**: dotenv for local dev, HF Secrets for production
