#!/usr/bin/env python3
"""
Test script to verify all installed packages are working correctly
"""

import sys
import traceback

def test_imports():
    """Test all critical package imports"""
    print("🧪 Testing package imports...")
    
    # Core ML stack
    try:
        import torch
        print(f"✅ PyTorch {torch.__version__}")
    except Exception as e:
        print(f"❌ PyTorch failed: {e}")
        return False
    
    try:
        import torchvision
        print(f"✅ TorchVision {torchvision.__version__}")
    except Exception as e:
        print(f"❌ TorchVision failed: {e}")
        return False
    
    try:
        import diffusers
        print(f"✅ Diffusers {diffusers.__version__}")
    except Exception as e:
        print(f"❌ Diffusers failed: {e}")
        return False
    
    try:
        import transformers
        print(f"✅ Transformers {transformers.__version__}")
    except Exception as e:
        print(f"❌ Transformers failed: {e}")
        return False
    
    # Computer vision
    try:
        import cv2
        print(f"✅ OpenCV {cv2.__version__}")
    except Exception as e:
        print(f"❌ OpenCV failed: {e}")
        return False
    
    try:
        import matplotlib
        print(f"✅ Matplotlib {matplotlib.__version__}")
    except Exception as e:
        print(f"❌ Matplotlib failed: {e}")
        return False
    
    # Notebook tools
    try:
        import nbformat
        print(f"✅ nbformat {nbformat.__version__}")
    except Exception as e:
        print(f"❌ nbformat failed: {e}")
        return False
    
    try:
        import jupyterlab
        print(f"✅ JupyterLab {jupyterlab.__version__}")
    except Exception as e:
        print(f"❌ JupyterLab failed: {e}")
        return False
    
    # UI frameworks
    try:
        import gradio
        print(f"✅ Gradio {gradio.__version__}")
    except Exception as e:
        print(f"❌ Gradio failed: {e}")
        return False
    
    try:
        import streamlit
        print(f"✅ Streamlit {streamlit.__version__}")
    except Exception as e:
        print(f"❌ Streamlit failed: {e}")
        return False
    
    try:
        import panel
        print(f"✅ Panel {panel.__version__}")
    except Exception as e:
        print(f"❌ Panel failed: {e}")
        return False
    
    # Development tools
    try:
        import black
        print(f"✅ Black {black.__version__}")
    except Exception as e:
        print(f"❌ Black failed: {e}")
        return False
    
    try:
        import isort
        print(f"✅ isort {isort.__version__}")
    except Exception as e:
        print(f"❌ isort failed: {e}")
        return False
    
    try:
        import fastapi
        print(f"✅ FastAPI {fastapi.__version__}")
    except Exception as e:
        print(f"❌ FastAPI failed: {e}")
        return False
    
    try:
        import flask
        print(f"✅ Flask {flask.__version__}")
    except Exception as e:
        print(f"❌ Flask failed: {e}")
        return False
    
    # Testing tools
    try:
        import pytest
        print(f"✅ pytest {pytest.__version__}")
    except Exception as e:
        print(f"❌ pytest failed: {e}")
        return False
    
    try:
        import nbconvert
        print(f"✅ nbconvert {nbconvert.__version__}")
    except Exception as e:
        print(f"❌ nbconvert failed: {e}")
        return False
    
    return True

def test_basic_functionality():
    """Test basic functionality of key packages"""
    print("\n🔧 Testing basic functionality...")
    
    # Test PyTorch CPU
    try:
        import torch
        x = torch.randn(2, 3)
        y = torch.randn(2, 3)
        z = x + y
        print("✅ PyTorch CPU operations working")
    except Exception as e:
        print(f"❌ PyTorch CPU operations failed: {e}")
        return False
    
    # Test notebook creation
    try:
        import nbformat as nbf
        nb = nbf.v4.new_notebook()
        nb.cells.append(nbf.v4.new_markdown_cell("# Test Notebook"))
        nb.cells.append(nbf.v4.new_code_cell("print('Hello from notebook!')"))
        print("✅ Notebook creation working")
    except Exception as e:
        print(f"❌ Notebook creation failed: {e}")
        return False
    
    # Test Gradio interface creation
    try:
        import gradio as gr
        def greet(name):
            return f"Hello {name}!"
        
        demo = gr.Interface(fn=greet, inputs="text", outputs="text")
        print("✅ Gradio interface creation working")
    except Exception as e:
        print(f"❌ Gradio interface creation failed: {e}")
        return False
    
    return True

def main():
    """Main test function"""
    print("🚀 Starting SD WebUI Tools Installation Test")
    print("=" * 50)
    
    success = True
    
    # Test imports
    if not test_imports():
        success = False
    
    # Test functionality
    if not test_basic_functionality():
        success = False
    
    print("\n" + "=" * 50)
    if success:
        print("🎉 All tests passed! Installation is complete and working.")
        print("\n📦 Installed packages:")
        print("   • PyTorch (CPU) - ML framework")
        print("   • Diffusers & Transformers - AI models")
        print("   • OpenCV & Matplotlib - Computer vision")
        print("   • JupyterLab & nbformat - Notebook development")
        print("   • Gradio, Streamlit, Panel - UI frameworks")
        print("   • FastAPI, Flask - Web frameworks")
        print("   • Black, isort - Code formatting")
        print("   • pytest, nbconvert - Testing tools")
        print("\n✨ Ready for SD WebUI ecosystem development!")
    else:
        print("❌ Some tests failed. Please check the errors above.")
        sys.exit(1)

if __name__ == "__main__":
    main()