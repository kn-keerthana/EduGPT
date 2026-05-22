---
title: EduGPT
emoji: 📚
colorFrom: purple
colorTo: blue
sdk: gradio
sdk_version: 4.44.0
app_file: app.py
pinned: false
license: mit
---

# This file is the entry point for Hugging Face Spaces deployment.
import sys
import os

# Add src directory to Python path so imports work correctly
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Import and run the Gradio app
from run import demo

demo.queue().launch()
