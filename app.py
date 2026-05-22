import sys
import os

# Add src directory to Python path so imports work correctly
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Import and run the Gradio app
from run import demo

demo.queue().launch()
