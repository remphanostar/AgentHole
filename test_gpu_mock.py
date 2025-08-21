#!/usr/bin/env python3
"""
Test script to verify GPU mocking capabilities for AI/ML development
"""

import torch
import numpy as np
from accelerate import Accelerator
from diffusers import DiffusionPipeline
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

def test_device_management():
    """Test device management and fallback to CPU"""
    print("=" * 60)
    print("🔧 DEVICE MANAGEMENT TEST")
    print("=" * 60)
    
    # Check available device
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"✅ Device selected: {device}")
    print(f"✅ CUDA available: {torch.cuda.is_available()}")
    print(f"✅ PyTorch version: {torch.__version__}")
    
    # Test tensor operations on CPU (mimicking GPU operations)
    x = torch.randn(3, 3).to(device)
    y = torch.randn(3, 3).to(device)
    z = torch.matmul(x, y)
    print(f"✅ Tensor operations working on {device}")
    
    # Test Accelerator for device abstraction
    accelerator = Accelerator()
    print(f"✅ Accelerator device: {accelerator.device}")
    print(f"✅ Mixed precision: {accelerator.mixed_precision}")
    
    return True

def test_model_loading():
    """Test loading models with CPU fallback"""
    print("\n" + "=" * 60)
    print("🤖 MODEL LOADING TEST")
    print("=" * 60)
    
    # Create a simple model
    model = torch.nn.Sequential(
        torch.nn.Linear(10, 20),
        torch.nn.ReLU(),
        torch.nn.Linear(20, 1)
    )
    
    # Move to appropriate device
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = model.to(device)
    
    # Test forward pass
    input_tensor = torch.randn(5, 10).to(device)
    output = model(input_tensor)
    
    print(f"✅ Model created and moved to {device}")
    print(f"✅ Model parameters: {sum(p.numel() for p in model.parameters())}")
    print(f"✅ Forward pass successful: output shape {output.shape}")
    
    return True

def test_memory_management():
    """Test memory management (CPU simulation of GPU memory)"""
    print("\n" + "=" * 60)
    print("💾 MEMORY MANAGEMENT TEST")
    print("=" * 60)
    
    if torch.cuda.is_available():
        print(f"✅ GPU Memory allocated: {torch.cuda.memory_allocated() / 1024**2:.2f} MB")
        print(f"✅ GPU Memory cached: {torch.cuda.memory_reserved() / 1024**2:.2f} MB")
    else:
        import psutil
        process = psutil.Process()
        memory_info = process.memory_info()
        print(f"✅ CPU Memory (RSS): {memory_info.rss / 1024**2:.2f} MB")
        print(f"✅ CPU Memory (VMS): {memory_info.vms / 1024**2:.2f} MB")
        print("ℹ️  Running on CPU - GPU memory functions not available")
    
    return True

def test_mixed_precision():
    """Test mixed precision training simulation"""
    print("\n" + "=" * 60)
    print("⚡ MIXED PRECISION TEST")
    print("=" * 60)
    
    # Test with autocast (CPU compatible)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    
    # CPU autocast is available in PyTorch
    if device.type == 'cpu':
        with torch.autocast(device_type='cpu', dtype=torch.bfloat16):
            x = torch.randn(10, 10)
            y = torch.randn(10, 10)
            z = torch.matmul(x, y)
            print(f"✅ CPU autocast working with bfloat16")
    else:
        with torch.cuda.amp.autocast():
            x = torch.randn(10, 10).cuda()
            y = torch.randn(10, 10).cuda()
            z = torch.matmul(x, y)
            print(f"✅ GPU autocast working")
    
    print(f"✅ Mixed precision operations successful on {device}")
    
    return True

def test_data_parallel():
    """Test data parallel simulation"""
    print("\n" + "=" * 60)
    print("🔀 DATA PARALLEL TEST")
    print("=" * 60)
    
    model = torch.nn.Linear(10, 5)
    
    if torch.cuda.is_available() and torch.cuda.device_count() > 1:
        model = torch.nn.DataParallel(model)
        print(f"✅ DataParallel enabled with {torch.cuda.device_count()} GPUs")
    else:
        print(f"✅ Running on single device (CPU or single GPU)")
        print(f"✅ CPU threads available: {torch.get_num_threads()}")
    
    # Test forward pass
    input_data = torch.randn(32, 10)
    output = model(input_data)
    print(f"✅ Parallel forward pass successful: output shape {output.shape}")
    
    return True

def main():
    """Run all tests"""
    print("\n" + "🚀 " * 20)
    print("GPU MOCKING AND CPU FALLBACK TEST SUITE")
    print("🚀 " * 20)
    
    tests = [
        ("Device Management", test_device_management),
        ("Model Loading", test_model_loading),
        ("Memory Management", test_memory_management),
        ("Mixed Precision", test_mixed_precision),
        ("Data Parallel", test_data_parallel),
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            success = test_func()
            results.append((test_name, success))
        except Exception as e:
            print(f"❌ {test_name} failed: {e}")
            results.append((test_name, False))
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 TEST SUMMARY")
    print("=" * 60)
    
    for test_name, success in results:
        status = "✅ PASSED" if success else "❌ FAILED"
        print(f"{test_name}: {status}")
    
    all_passed = all(success for _, success in results)
    if all_passed:
        print("\n🎉 All tests passed! Environment ready for AI/ML development.")
        print("ℹ️  Note: Running on CPU - perfect for testing and development.")
        print("ℹ️  GPU code will automatically fallback to CPU execution.")
    else:
        print("\n⚠️  Some tests failed. Please check the errors above.")

if __name__ == "__main__":
    # First, install psutil if needed for memory monitoring
    try:
        import psutil
    except ImportError:
        print("Installing psutil for memory monitoring...")
        import subprocess
        subprocess.check_call(["pip", "install", "psutil"])
        import psutil
    
    main()