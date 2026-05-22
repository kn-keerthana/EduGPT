import os
import time

import gradio as gr
from dotenv import load_dotenv

from generating_syllabus import generate_syllabus
from teaching_agent import teaching_agent

# Load environment variables from .env file (works locally)
# On Hugging Face Spaces, key is set via Secrets dashboard
load_dotenv()

# Validate that the API key exists
if not os.getenv("GROQ_API_KEY"):
    raise EnvironmentError(
        "GROQ_API_KEY not found. Please create a .env file with your Groq API key.\n"
        "Get your free key at: https://console.groq.com"
    )

with gr.Blocks(title="EduGPT - Your AI Instructor") as demo:
    gr.Markdown("# 📚 EduGPT — Your Personal AI Instructor")
    gr.Markdown(
        "Powered by **Groq + LLaMA 3.3 70B**. Enter a topic to get a custom syllabus, then chat with your AI instructor!"
    )

    with gr.Tab("📋 Step 1: Build Your Syllabus"):
        gr.Markdown("Enter any topic below. The AI agents will design a full course syllabus for you.")

        def perform_task(input_text):
            if not input_text.strip():
                return "Please enter a topic first!"
            task = "Generate a course syllabus to teach the topic: " + input_text
            syllabus = generate_syllabus(input_text, task)
            teaching_agent.seed_agent(syllabus, task)
            return syllabus

        text_input = gr.Textbox(
            label="What topic do you want to learn?",
            placeholder="e.g. Machine Learning, Python, Quantum Physics, Guitar...",
        )
        text_output = gr.Textbox(
            label="Your Custom Syllabus:",
            lines=15,
        )
        text_button = gr.Button("🚀 Build My Syllabus!", variant="primary")
        text_button.click(perform_task, text_input, text_output)

    with gr.Tab("💬 Step 2: Chat with Your Instructor"):
        gr.Markdown("Complete Step 1 first, then chat with your AI instructor below!")

        chatbot = gr.Chatbot(height=400)
        msg = gr.Textbox(
            label="Ask your instructor anything:",
            placeholder="e.g. Can you explain that again? Give me an example.",
        )
        clear = gr.Button("🗑️ Clear Chat")

        def user(user_message, history):
            teaching_agent.human_step(user_message)
            return "", history + [[user_message, None]]

        def bot(history):
            bot_message = teaching_agent.instructor_step()
            bot_message = bot_message.replace("<END_OF_TURN>", "")
            history[-1][1] = ""
            for character in bot_message:
                history[-1][1] += character
                time.sleep(0.02)
                yield history

        msg.submit(user, [msg, chatbot], [msg, chatbot], queue=False).then(
            bot, chatbot, chatbot
        )
        clear.click(lambda: None, None, chatbot, queue=False)


# Only auto-launch when run directly (not imported by app.py)
if __name__ == "__main__":
    demo.queue().launch(debug=True)
