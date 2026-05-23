import sys
import os
import time

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "src"))

import gradio as gr
from dotenv import load_dotenv
from generating_syllabus import generate_syllabus
from teaching_agent import teaching_agent

load_dotenv()

if not os.getenv("GROQ_API_KEY"):
    print("WARNING: GROQ_API_KEY not set.")


def perform_task(input_text):
    if not input_text.strip():
        return "Please enter a topic first!"
    task = "Generate a course syllabus to teach the topic: " + input_text
    syllabus = generate_syllabus(input_text, task)
    teaching_agent.seed_agent(syllabus, task)
    return syllabus


def chat(message, history):
    teaching_agent.human_step(message)
    response = teaching_agent.instructor_step()
    response = response.replace("<END_OF_TURN>", "")
    return response


with gr.Blocks(title="EduGPT — Your AI Instructor") as demo:
    gr.Markdown("# 📚 EduGPT — Your Personal AI Instructor")
    gr.Markdown(
        "Powered by **Groq + LLaMA 3.3 70B**. "
        "Enter a topic to get a custom syllabus, then chat with your AI instructor!"
    )

    with gr.Tab("📋 Step 1: Build Your Syllabus"):
        gr.Markdown(
            "Enter any topic and click **Build My Syllabus**. "
            "Two AI agents will collaborate to design a full course (~30 seconds)."
        )
        text_input = gr.Textbox(
            label="What topic do you want to learn?",
            placeholder="e.g. Machine Learning, Python, Guitar, Quantum Physics...",
        )
        text_button = gr.Button("🚀 Build My Syllabus!", variant="primary")
        text_output = gr.Textbox(label="Your Custom Syllabus:", lines=18)
        text_button.click(perform_task, inputs=text_input, outputs=text_output)

    with gr.Tab("💬 Step 2: Chat with Your Instructor"):
        gr.Markdown(
            "✅ Complete Step 1 first, then chat with your AI instructor here."
        )
        gr.ChatInterface(
            fn=chat,
            chatbot=gr.Chatbot(height=420, label="Your AI Instructor"),
            textbox=gr.Textbox(
                placeholder="e.g. Start teaching! / Explain that again / Give me an example",
                label="Your message:",
            ),
        )

demo.queue().launch()
