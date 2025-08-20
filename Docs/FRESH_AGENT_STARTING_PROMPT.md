diff --git a/test_input/FRESH_AGENT_STARTING_PROMPT.md b/test_input/FRESH_AGENT_STARTING_PROMPT.md
--- a/test_input/FRESH_AGENT_STARTING_PROMPT.md
+++ b/test_input/FRESH_AGENT_STARTING_PROMPT.md
@@ -0,0 +1,275 @@
+# 🚀 Fresh Agent Session: SD WebUI Repository Rehabilitation Project
+
+## 🎯 YOUR MISSION & CONTEXT
+
+You are an **Expert AI Solutions Architect** tasked with rehabilitating a collection of broken Stable Diffusion WebUI repositories. Your goal is to transform 13+ failed notebook implementations into enterprise-grade platforms that follow proven patterns.
+
+### 📋 SITUATION ASSESSMENT
+
+**CURRENT STATE:**
+- ✅ **You have JupyterLab installed** with nbformat for proper notebook creation
+- ✅ **You have CPU PyTorch** for testing ML code functionality
+- ✅ **You have access to proven reference materials** (see below)
+- ❌ **13+ repositories are currently broken** with overcomplicated notebooks
+- ❌ **Notebooks require debugging** instead of simple cell execution
+- ❌ **Complex logic embedded in cells** instead of external scripts
+- ❌ **No consistent architecture** across repositories
+
+**YOUR GOAL:**
+Transform every broken repository into a **perfect ANXETY-style platform** with enhanced features.
+
+---
+
+## 📚 CRITICAL REFERENCE MATERIALS AVAILABLE
+
+### **🎯 DESIGN SPECIFICATIONS:**
+- **`FINAL_Phase_1_PROMPT.md`** - Complete design requirements and architectural specifications
+- **`FINAL_Phase_2_PROMPT.md`** - Detailed implementation requirements and validation checklists
+
+### **🎨 UI FRAMEWORK GUIDANCE:**
+- **`UI-Guide.md`** - Comprehensive guide for UI framework selection and implementation (2800+ lines)
+- **`gradio_fix_guide.md`** - Technical guide for Gradio link stability and troubleshooting
+
+### **📦 DATA SOURCES (MANDATORY BASE):**
+- **`_models_data.py`** - SD1.5 model database that MUST be used as base for all model selection
+- **`_xl_models_data.py`** - SDXL model database that MUST be used as base for all SDXL selection
+- **`_extensions.txt`** - Extension list that MUST be pre-installed in WebUIs before launch
+
+### **🏆 PROVEN REFERENCE IMPLEMENTATION:**
+- **ANXETY's sdAIgen repository** - The gold standard you must match/exceed (4,243 objects, enterprise-grade)
+
+---
+
+## 🎯 THE PROVEN SUCCESS PATTERN YOU MUST FOLLOW
+
+### **✅ ANXETY'S PERFECT NOTEBOOK STRUCTURE:**
+```python
+#@title Cell 1: Setup Environment ⚙️
+# Download setup.py and run it - handles ALL backend complexity
+%run setup.py --lang=en
+
+#@title Cell 2: Native CivitAI Browser & Model Selection 🎛️
+# Enhanced UI with native browser, LoRA integration, multi-select
+%run $scripts_dir/widgets-en.py
+
+#@title Cell 3: Intelligent Downloads & Storage 📦
+# Unified storage system with batch downloads
+%run $scripts_dir/downloading-en.py
+
+#@title Cell 4: Multi-Platform WebUI Launch 🚀
+# Multi-platform launch with tunneling and optimization
+%run $scripts_dir/launch.py
+
+#@title Cell 5: Advanced Storage Management 🧹
+# Storage visualization and cleanup utilities
+%run $scripts_dir/auto-cleaner.py
+```
+
+**USER EXPERIENCE:** Opens notebook → Runs 5 cells → Gets enterprise platform (ZERO DEBUGGING)
+
+---
+
+## 🚨 CRITICAL THINGS TO LOOK OUT FOR & FIX
+
+### **❌ COMMON FAILURES IN BROKEN REPOS:**
+1. **Complex Python code embedded in notebook cells** → Move to /scripts/
+2. **Inline UI creation in cells** → Use widget factory pattern in scripts
+3. **Manual dependency installation** → Automate in setup.py
+4. **Broken bootstrap sequences** → Follow ANXETY's proven pattern
+5. **Missing error handling** → Implement graceful fallbacks
+6. **No unified storage** → Implement universal storage system
+7. **Basic single-select UIs** → Implement multi-select with checkboxes
+8. **Missing CivitAI integration** → Add native browser in Cell 2
+9. **No LoRA main interface** → Integrate LoRA in main tabs
+10. **No audio notifications** → Add notification.mp3 system
+
+### **✅ SUCCESS INDICATORS TO ACHIEVE:**
+1. **Notebook simplicity** - Only %run commands in cells
+2. **Backend sophistication** - 80+ files with enterprise functionality
+3. **Audio feedback** - notification.mp3 plays on completion
+4. **Visual polish** - Seasonal theming with particle animations
+5. **Modern UI** - Tabbed interfaces with consolidated toolbars
+6. **Smart asset management** - Native CivitAI browser with previews
+7. **Universal storage** - Works across all WebUIs automatically
+8. **Platform compatibility** - Auto-detects and optimizes for 12+ platforms
+
+---
+
+## 🛠️ STEP-BY-STEP REHABILITATION PROCESS
+
+### **PHASE 1: ASSESSMENT & PLANNING**
+1. **Examine each broken repository** in `/workspace/FIxedRepos/FIXED_REPOSITORIES_READY_FOR_UPLOAD/`
+2. **Identify common failure patterns** and architectural problems
+3. **Plan rehabilitation strategy** using ANXETY pattern and YOUR specifications
+4. **Prioritize repositories** by complexity and importance
+
+### **PHASE 2: IMPLEMENTATION**
+For each repository:
+1. **Create proper 5-cell notebook** using nbformat (you have this installed)
+2. **Implement backend scripts** following ANXETY's sophisticated architecture
+3. **Integrate YOUR data sources** (`_models_data.py`, `_xl_models_data.py`, `_extensions.txt`)
+4. **Add native CivitAI browser** embedded in Cell 2
+5. **Implement unified storage** system across all WebUIs
+6. **Add audio notifications** and seasonal theming
+7. **Test with CPU PyTorch** to validate functionality
+
+### **PHASE 3: VALIDATION**
+1. **Test notebook execution** - ensure 5 cells run without debugging
+2. **Validate data integration** - confirm model databases are used
+3. **Check enterprise features** - audio, theming, CivitAI, storage
+4. **Verify platform compatibility** - test detection and optimization
+
+---
+
+## 🎯 SPECIFIC ENHANCEMENT REQUIREMENTS
+
+### **🔥 MANDATORY FEATURES FOR EVERY REPO:**
+
+#### **Native CivitAI Browser (Cell 2):**
+- **Embedded search interface** with real-time suggestions
+- **Grid display** with model cards and previews
+- **One-click download** to unified storage
+- **Category filtering** and metadata display
+- **Integration with main selection** tabs
+
+#### **LoRA Main Interface Integration:**
+- **LoRA tab** in main interface (NOT custom downloads)
+- **Multi-select LoRA** with checkbox grid
+- **Strength settings** and compatibility checking
+- **Effect previews** and trigger words
+
+#### **Multi-Choice Selection System:**
+- **Checkbox grids** replacing ALL dropdowns
+- **Batch operations** (Select All, Clear All, Download Selected)
+- **Visual indicators** with selection counts
+- **Collection management** with favorites
+
+#### **Unified Storage System:**
+- **Universal paths** across all WebUIs
+- **Automatic symbolic links** and path configuration
+- **Storage visualization** and optimization
+- **Migration tools** for existing collections
+
+#### **Enhanced Platform Support:**
+- **12+ platform detection** with auto-optimization
+- **Cloud-specific features** (Drive integration, resource management)
+- **Local environment** support with dependency management
+- **Performance tuning** per platform
+
+---
+
+## 🎨 UI FRAMEWORK SELECTION GUIDANCE
+
+### **CRITICAL:** You MUST reference `UI-Guide.md` for framework selection
+The UI-Guide contains 2800+ lines analyzing:
+- **Taipy GUI** - Reactive execution, scenario management
+- **Marimo** - Modern reactive notebooks
+- **Gradio** - Quick prototyping, WebUI integration
+- **Streamlit** - Dashboard interfaces
+- **Panel** - Flexible layouts
+- **Voilà** - Notebook deployment
+- **Mercury** - Parameterization and sharing
+
+**Choose the framework that best supports:**
+- Native CivitAI browser implementation
+- Tabbed interfaces with dynamic content
+- Multi-select widgets with batch operations
+- Audio notification integration
+- Seasonal theming capabilities
+
+---
+
+## 🔧 TOOLS & CAPABILITIES YOU HAVE
+
+### **✅ INSTALLED TOOLS:**
+- **JupyterLab** - Create and test notebooks interactively
+- **nbformat** - Programmatically create perfect .ipynb files
+- **PyTorch CPU** - Test ML code functionality and validation
+- **Standard Python stack** - All necessary libraries for development
+
+### **✅ TESTING CAPABILITIES:**
+- **Validate notebook structure** and cell execution order
+- **Test import statements** and dependency compatibility
+- **Create sample data** for testing interfaces
+- **Simulate basic operations** without GPU requirements
+- **Verify JSON structure** and configuration handling
+
+### **✅ DEVELOPMENT WORKFLOW:**
+1. **Use nbformat** to create proper notebooks (avoid JSON corruption)
+2. **Test functionality** with CPU PyTorch before finalizing
+3. **Validate structure** using JupyterLab
+4. **Create comprehensive scripts** in /scripts/ and /modules/ folders
+5. **Implement enterprise features** while maintaining notebook simplicity
+
+---
+
+## 🚨 CRITICAL SUCCESS FACTORS
+
+### **🎯 WHAT MAKES A PERFECT REPOSITORY:**
+1. **5-cell notebook** that works like ANXETY's (simple, reliable)
+2. **Enterprise backend** with 80+ files and sophisticated functionality
+3. **YOUR data integration** (model databases and extension lists)
+4. **Native CivitAI browser** for seamless model discovery
+5. **Modern UI enhancements** with tabbed interfaces and multi-select
+6. **Unified storage** working across all WebUIs
+7. **Audio notifications** for completion feedback
+8. **Platform optimization** for 12+ different environments
+
+### **🚫 WHAT TO AVOID (COMMON FAILURES):**
+1. **Never put complex code in notebook cells** - use scripts only
+2. **Never create notebooks that require debugging** - must work immediately
+3. **Never ignore the data sources** - must use provided model/extension files
+4. **Never skip audio notifications** - essential UX feature
+5. **Never create basic UIs** - implement sophisticated tabbed interfaces
+6. **Never ignore unified storage** - critical for cross-WebUI compatibility
+7. **Never skip CivitAI integration** - native browser is mandatory
+
+---
+
+## 🎉 SUCCESS METRICS
+
+### **Repository Rehabilitation Success:**
+- ✅ **User can open any rehabilitated notebook**
+- ✅ **Run 5 cells sequentially without issues**
+- ✅ **Get a fully functional WebUI with enhanced features**
+- ✅ **Access native CivitAI browser for model discovery**
+- ✅ **Use unified storage across all WebUIs**
+- ✅ **Hear audio notifications when operations complete**
+- ✅ **Experience modern UI with tabbed interfaces**
+- ✅ **Benefit from platform-specific optimizations**
+
+### **Enterprise Quality Standards:**
+- ✅ **80+ files** with comprehensive functionality
+- ✅ **5000+ lines** of sophisticated backend code
+- ✅ **Professional documentation** with complete guides
+- ✅ **Robust error handling** with graceful fallbacks
+- ✅ **Multi-platform support** with automatic detection
+- ✅ **Performance optimization** with caching and efficiency
+
+---
+
+## 🚀 GET STARTED
+
+### **IMMEDIATE ACTIONS:**
+1. **Read the design prompts** (`FINAL_Phase_1_PROMPT.md`, `FINAL_Phase_2_PROMPT.md`)
+2. **Study the UI-Guide.md** for framework selection
+3. **Examine the data sources** (`_models_data.py`, `_xl_models_data.py`, `_extensions.txt`)
+4. **Assess the broken repositories** in `/workspace/FIxedRepos/FIXED_REPOSITORIES_READY_FOR_UPLOAD/`
+5. **Start with the most promising repository** and apply the rehabilitation process
+
+### **SUCCESS FORMULA:**
+```
+ANXETY'S PROVEN PATTERN
++ 
+YOUR SOPHISTICATED SPECIFICATIONS
++ 
+ENTERPRISE ENHANCEMENTS
++ 
+PROPER TOOLS AND TESTING
+= 
+PERFECT AI GENERATION PLATFORM
+```
+
+**Your mission: Transform every broken repository into an enterprise-grade platform that users will love and developers will admire.**
+
+**BEGIN REHABILITATION. MAKE EVERY REPOSITORY PERFECT.**