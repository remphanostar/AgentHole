# Wan2GP Gradio Compatibility Fix Guide for Google Colab

## Problem Overview
The error occurs because `gr.Row(height=17)` is using an unsupported parameter in your Gradio version. The `height` parameter is not accepted by the `Row` component.

## Multiple Solution Methods

### Method 1: Quick Sed Command Fix
```bash
cd /content/Wan2GP
sed -i 's/gr.Row(height=17)/gr.Row()/g' wgp.py
sed -i 's/gr.Row(height=[0-9]*)/gr.Row()/g' wgp.py
```

### Method 2: Python Script Auto-Fix
```python
import re

# Read the file
with open('/content/Wan2GP/wgp.py', 'r') as file:
    content = file.read()

# Fix all gr.Row instances with height parameter
content = re.sub(r'gr\.Row\(height=\d+\)', 'gr.Row()', content)
content = re.sub(r'gr\.Row\(height=\d+,\s*', 'gr.Row(', content)
content = re.sub(r'gr\.Row\(\s*height=\d+\s*\)', 'gr.Row()', content)

# Write back to file
with open('/content/Wan2GP/wgp.py', 'w') as file:
    file.write(content)

print("✅ Fixed Gradio Row height parameters")
```

### Method 3: Manual Edit with Nano
```bash
cd /content/Wan2GP
nano +6305 wgp.py
```
Then manually remove `height=17` from the Row declaration.

### Method 4: Find and Replace All Instances
```bash
cd /content/Wan2GP
grep -n "gr.Row(height=" wgp.py
# Then use sed to fix each line found
sed -i 's/with gr.Row(height=17):/with gr.Row():/g' wgp.py
```

### Method 5: Advanced Python Fix Script
```python
import os
import re

def fix_gradio_rows(file_path):
    """Fix all Gradio Row height parameter issues"""
    
    # Backup original file
    backup_path = file_path + '.backup'
    os.system(f'cp {file_path} {backup_path}')
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Multiple regex patterns to catch different formats
    patterns = [
        (r'gr\.Row\(height=\d+\)', 'gr.Row()'),
        (r'gr\.Row\(height=\d+,\s*([^)]+)\)', r'gr.Row(\1)'),
        (r'gr\.Row\(\s*height=\d+\s*,\s*([^)]+)\)', r'gr.Row(\1)'),
        (r'gr\.Row\(\s*([^),]+),\s*height=\d+\s*\)', r'gr.Row(\1)'),
    ]
    
    for pattern, replacement in patterns:
        content = re.sub(pattern, replacement, content)
    
    # Write fixed content
    with open(file_path, 'w') as f:
        f.write(content)
    
    print(f"✅ Fixed {file_path}")
    print(f"📁 Backup saved as {backup_path}")

# Run the fix
fix_gradio_rows('/content/Wan2GP/wgp.py')
```

### Method 6: One-liner Colab Cell
```bash
!cd /content/Wan2GP && sed -i 's/gr\.Row(height=[0-9]*)/gr.Row()/g' wgp.py && echo "✅ Fixed Gradio compatibility"
```

### Method 7: Check and Fix Multiple Files
```bash
cd /content/Wan2GP
find . -name "*.py" -exec grep -l "gr.Row(height=" {} \;
find . -name "*.py" -exec sed -i 's/gr\.Row(height=[0-9]*)/gr.Row()/g' {} \;
```

## Alternative CSS Styling Method
If you need height control, replace with CSS classes:

```python
# Instead of: gr.Row(height=17)
# Use: gr.Row(elem_classes="custom-row")

# Then add CSS in your interface
css = """
.custom-row {
    height: 17px;
}
"""

# Apply to your Gradio interface
demo = gr.Interface(..., css=css)
```

## Verification Commands

### Check if fix was applied:
```bash
cd /content/Wan2GP
grep -n "gr.Row(height=" wgp.py || echo "✅ No height parameters found"
```

### Count fixed instances:
```bash
cd /content/Wan2GP
grep -c "gr.Row()" wgp.py
```

## Run After Fix
```bash
cd /content/Wan2GP
conda run python run_wgp.py --share --listen
```

## Error Handling Notes

- **ALSA errors**: These are harmless audio warnings in containerized environments
- **XDG_RUNTIME_DIR**: Normal warning in Colab, doesn't affect functionality
- **FP16 warnings**: Normal GPU optimization messages

## Complete Fix Script for Colab
```python
# Complete automated fix
import os
import re

def complete_gradio_fix():
    os.chdir('/content/Wan2GP')
    
    # Method 1: Simple sed replacement
    os.system('sed -i "s/gr\.Row(height=[0-9]*)/gr.Row()/g" wgp.py')
    
    # Method 2: Python regex for complex cases
    with open('wgp.py', 'r') as f:
        content = f.read()
    
    # Fix various Row parameter formats
    patterns = [
        (r'gr\.Row\(height=\d+\)', 'gr.Row()'),
        (r'gr\.Row\(height=\d+,\s*([^)]+)\)', r'gr.Row(\1)'),
        (r'gr\.Row\(\s*height=\d+\s*,\s*([^)]+)\)', r'gr.Row(\1)'),
    ]
    
    for pattern, replacement in patterns:
        content = re.sub(pattern, replacement, content)
    
    with open('wgp.py', 'w') as f:
        f.write(content)
    
    print("✅ All Gradio Row fixes applied")
    
    # Verify fix
    result = os.system('grep -q "gr.Row(height=" wgp.py')
    if result == 0:
        print("⚠️  Some height parameters may still exist")
    else:
        print("✅ No height parameters found - fix successful")

# Run the complete fix
complete_gradio_fix()
```

Choose the method that works best for your situation. The sed command (Method 1) is usually the quickest for simple fixes.



# Why Gradio Public Links Fail in Colab/Jupyter

## Network & Firewall Issues

**Corporate/University Firewalls**
- Block outbound connections to Gradio tunneling services
- Restrict access to specific ports (7860, 7861, etc.)
- Deep packet inspection blocking tunnel protocols

**Network Configuration**
- NAT/proxy servers interfering with tunnel establishment
- IPv6/IPv4 routing conflicts
- DNS resolution issues for gradio.live domains

**ISP Restrictions**
- Some ISPs block peer-to-peer or tunneling protocols
- Throttling connections to cloud services
- Geographic restrictions on certain services

## Colab-Specific Limitations

**Runtime Environment**
- Colab containers have limited outbound network access
- Temporary container IPs may be blacklisted
- Resource sharing affecting tunnel stability

**Port Binding Issues**
- Default port 7860 already occupied by other processes
- Colab's internal port management conflicts
- Multiple notebooks sharing same port space

**Authentication Problems**
- Colab's authentication interfering with Gradio's
- Session tokens expiring during tunnel setup
- OAuth redirects getting blocked

## Code/Configuration Problems

**Gradio Version Conflicts**
- Outdated Gradio versions lacking tunnel support
- Breaking changes between versions
- Incompatible dependency versions

**Launch Parameters**
- Missing `share=True` parameter
- Incorrect server_name/server_port settings
- Wrong combination of launch options

**Environment Variables**
- Missing required environment variables
- Conflicting environment settings
- Incorrect path configurations

## Service-Side Issues

**Gradio Infrastructure**
- Gradio tunneling servers overloaded
- Maintenance windows affecting service
- Regional server availability issues

**Rate Limiting**
- Too many tunnel requests from same IP
- Gradio's abuse prevention triggering
- Service quota exceeded

**SSL/TLS Issues**
- Certificate validation failures
- Outdated SSL protocols
- Mixed content security policies

## Resource Constraints

**Memory Limitations**
- Insufficient memory for tunnel establishment
- Memory leaks in long-running processes
- Competing processes consuming resources

**CPU Throttling**
- Colab CPU limits affecting tunnel performance
- Background processes consuming cycles
- Thermal throttling in extended sessions

**Storage Issues**
- Temporary files filling disk space
- Permission issues with temp directories
- Log files consuming storage

## Python Environment Issues

**Package Conflicts**
- Conflicting versions of networking libraries
- Incompatible asyncio implementations
- Threading conflicts between packages

**Import Problems**
- Missing required dependencies
- Circular import issues
- Module path conflicts

**Runtime Errors**
- Unhandled exceptions during tunnel setup
- Race conditions in async operations
- Timeout issues in network operations

## Browser/Client Issues

**Browser Security**
- CORS policies blocking access
- Mixed content warnings
- Browser extensions interfering

**Client-Side Firewalls**
- Local firewall blocking access
- Antivirus software interference
- Parental controls affecting access

## Debugging Strategies

**Network Diagnostics**
```python
import requests
import socket

# Test connectivity
try:
    response = requests.get('https://gradio.app', timeout=10)
    print(f"Gradio.app accessible: {response.status_code == 200}")
except Exception as e:
    print(f"Connection failed: {e}")

# Test port availability
def check_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('127.0.0.1', port))
    sock.close()
    return result != 0

print(f"Port 7860 available: {check_port(7860)}")
```

**Environment Check**
```python
import os
import sys
import gradio as gr

print(f"Python version: {sys.version}")
print(f"Gradio version: {gr.__version__}")
print(f"Environment variables:")
for key in ['GRADIO_SERVER_NAME', 'GRADIO_SERVER_PORT', 'GRADIO_SHARE']:
    print(f"  {key}: {os.environ.get(key, 'Not set')}")
```

## Common Solutions

**Force Different Ports**
```python
import random
port = random.randint(7000, 8000)
demo.launch(share=True, server_port=port)
```

**Alternative Tunneling**
```python
# Use ngrok as backup
try:
    from pyngrok import ngrok
    public_url = ngrok.connect(7860)
    print(f"Ngrok URL: {public_url}")
except:
    print("Ngrok not available")
```

**Environment Reset**
```python
# Clear conflicting environment
import os
for key in list(os.environ.keys()):
    if key.startswith('GRADIO_'):
        del os.environ[key]

# Set clean environment
os.environ['GRADIO_SERVER_NAME'] = '0.0.0.0'
os.environ['GRADIO_ANALYTICS_ENABLED'] = 'False'
```

**Retry with Backoff**
```python
import time
import random

def retry_launch(demo, max_attempts=5):
    for attempt in range(max_attempts):
        try:
            return demo.launch(share=True)
        except Exception as e:
            if attempt < max_attempts - 1:
                wait_time = 2 ** attempt + random.uniform(0, 1)
                time.sleep(wait_time)
            else:
                raise e
```

## Prevention Measures

**Pre-Launch Checks**
- Verify network connectivity
- Check available ports
- Validate Gradio installation
- Test environment variables

**Robust Launch Pattern**
```python
def robust_gradio_launch(demo):
    # Environment setup
    setup_gradio_environment()
    
    # Port discovery
    port = find_available_port()
    
    # Launch with fallbacks
    try:
        return demo.launch(share=True, server_port=port)
    except Exception as e:
        print(f"Primary launch failed: {e}")
        return emergency_launch(demo)
```

**Monitoring & Recovery**
```python
def monitor_and_recover(demo):
    while True:
        try:
            if not demo.share_url:
                print("Link lost, attempting recovery...")
                demo.launch(share=True)
        except:
            pass
        time.sleep(30)
```