# This file is the entry point for Hugging Face Spaces deployment.
# It simply imports and runs the main Gradio app from src/run.py

import sys
import os

# Add src to path so imports work
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Run the app
exec(open('src/run.py').read())
