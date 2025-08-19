# 🛠️ SD WebUI Tools Quick Reference

## 🚀 **Activation**
```bash
cd /workspace
source sd_webui_env/bin/activate
```

## 📊 **Core ML Stack**

### **PyTorch (CPU)**
```python
import torch
import torchvision

# Basic tensor operations
x = torch.randn(2, 3)
y = torch.randn(2, 3)
z = x + y

# Model loading
model = torch.hub.load('pytorch/vision:v0.10.0', 'resnet18', pretrained=True)
```

### **Hugging Face Ecosystem**
```python
from diffusers import StableDiffusionPipeline
from transformers import AutoTokenizer, AutoModel

# Load diffusion model
pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")

# Load transformer model
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModel.from_pretrained("bert-base-uncased")
```

## 🖼️ **Computer Vision**

### **OpenCV**
```python
import cv2
import numpy as np

# Read image
img = cv2.imread('image.jpg')

# Basic operations
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
resized = cv2.resize(img, (512, 512))

# Save image
cv2.imwrite('output.jpg', img)
```

### **Matplotlib**
```python
import matplotlib.pyplot as plt
import numpy as np

# Create plot
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.title('Sine Wave')
plt.show()
```

## 📓 **Notebook Development**

### **nbformat - Create Notebooks**
```python
import nbformat as nbf

# Create new notebook
nb = nbf.v4.new_notebook()

# Add markdown cell
nb.cells.append(nbf.v4.new_markdown_cell("# My Notebook"))

# Add code cell
nb.cells.append(nbf.v4.new_code_cell("print('Hello World!')"))

# Save notebook
with open('my_notebook.ipynb', 'w') as f:
    nbf.write(nb, f)
```

### **JupyterLab**
```bash
# Start JupyterLab
jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root
```

## 🎨 **UI Frameworks**

### **Gradio - Quick WebUI**
```python
import gradio as gr

def greet(name):
    return f"Hello {name}!"

# Create interface
demo = gr.Interface(
    fn=greet,
    inputs="text",
    outputs="text",
    title="Greeting App"
)

# Launch
demo.launch(share=True)
```

### **Streamlit - Dashboard**
```python
import streamlit as st
import pandas as pd

st.title("My Dashboard")

# Add widgets
name = st.text_input("Enter your name")
if st.button("Greet"):
    st.write(f"Hello {name}!")

# Display data
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
st.dataframe(df)
```

### **Panel - Reactive Apps**
```python
import panel as pn
import numpy as np

# Create reactive app
def plot_data(n_points=100):
    x = np.linspace(0, 10, n_points)
    y = np.sin(x)
    return pn.pane.Matplotlib(plt.plot(x, y)[0])

# Create interface
slider = pn.widgets.IntSlider(name='Points', start=10, end=200, value=100)
plot = pn.bind(plot_data, n_points=slider)

# Layout
app = pn.Column(slider, plot)
app.show()
```

### **FastAPI - Web API**
```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/items/")
def create_item(item: Item):
    return item

# Run with: uvicorn main:app --reload
```

### **Flask - Lightweight Web**
```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/api/data', methods=['POST'])
def receive_data():
    data = request.get_json()
    return jsonify({"received": data})

if __name__ == '__main__':
    app.run(debug=True)
```

## 🔧 **Development Tools**

### **Black - Code Formatting**
```bash
# Format a file
black my_file.py

# Format directory
black .

# Check formatting
black --check my_file.py
```

### **isort - Import Sorting**
```bash
# Sort imports in file
isort my_file.py

# Sort imports in directory
isort .

# Check import order
isort --check-only my_file.py
```

### **pytest - Testing**
```python
# test_example.py
def test_addition():
    assert 2 + 2 == 4

def test_string():
    assert "hello" + " world" == "hello world"
```

```bash
# Run tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest test_example.py
```

### **nbconvert - Notebook Conversion**
```bash
# Convert to Python
jupyter nbconvert --to python notebook.ipynb

# Convert to HTML
jupyter nbconvert --to html notebook.ipynb

# Convert to Markdown
jupyter nbconvert --to markdown notebook.ipynb
```

## 🎯 **Common Patterns**

### **SD WebUI Integration Pattern**
```python
import torch
from diffusers import StableDiffusionPipeline
import gradio as gr

def generate_image(prompt, negative_prompt="", num_inference_steps=20):
    # Load model
    pipe = StableDiffusionPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5",
        torch_dtype=torch.float16
    )
    
    # Generate image
    image = pipe(
        prompt=prompt,
        negative_prompt=negative_prompt,
        num_inference_steps=num_inference_steps
    ).images[0]
    
    return image

# Create Gradio interface
demo = gr.Interface(
    fn=generate_image,
    inputs=[
        gr.Textbox(label="Prompt"),
        gr.Textbox(label="Negative Prompt"),
        gr.Slider(minimum=1, maximum=50, value=20, label="Steps")
    ],
    outputs=gr.Image(),
    title="SD WebUI Generator"
)

demo.launch()
```

### **Notebook Creation Pattern**
```python
import nbformat as nbf

def create_sd_notebook():
    nb = nbf.v4.new_notebook()
    
    # Title
    nb.cells.append(nbf.v4.new_markdown_cell("# Stable Diffusion WebUI Notebook"))
    
    # Setup cell
    setup_code = """
# Install dependencies
!pip install diffusers transformers torch
"""
    nb.cells.append(nbf.v4.new_code_cell(setup_code))
    
    # Import cell
    import_code = """
import torch
from diffusers import StableDiffusionPipeline
import matplotlib.pyplot as plt
"""
    nb.cells.append(nbf.v4.new_code_cell(import_code))
    
    # Model loading cell
    model_code = """
# Load model
pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
"""
    nb.cells.append(nbf.v4.new_code_cell(model_code))
    
    return nb

# Create and save notebook
notebook = create_sd_notebook()
with open('sd_webui_notebook.ipynb', 'w') as f:
    nbf.write(notebook, f)
```

## 📝 **Environment Variables**
```bash
# Set CUDA device (if using GPU)
export CUDA_VISIBLE_DEVICES=0

# Set Hugging Face cache directory
export HF_HOME=/path/to/cache

# Set Jupyter config
export JUPYTER_CONFIG_DIR=/path/to/config
```

## 🔍 **Troubleshooting**

### **Common Issues**
1. **Import errors**: Make sure virtual environment is activated
2. **CUDA errors**: Use CPU PyTorch for testing
3. **Memory issues**: Reduce batch sizes or use CPU
4. **Port conflicts**: Change port numbers in launch commands

### **Useful Commands**
```bash
# Check installed packages
pip list

# Check Python version
python --version

# Check PyTorch version and CUDA
python -c "import torch; print(torch.__version__); print(torch.cuda.is_available())"

# Update packages
pip install --upgrade package_name
```

---

**Quick Reference for SD WebUI Ecosystem Development**
**All tools installed and tested successfully**