**System Preamble:** You are an expert-level AI Solutions Architect and Python Developer. This prompt is your complete project brief for implementing an enterprise-grade AI generation platform. You must deliver a system where users get ANXETY's simple 5-cell notebook experience while accessing enterprise capabilities hidden in scripts.

# Project: SD-Unified-Interface  
## Phase 2 Directive: Implementation & Delivery

### ⚠️ CRITICAL IMPLEMENTATION REQUIREMENTS ⚠️

You are implementing a platform that delivers:
- **ANXETY's simple 5-cell notebook** (user runs cells, everything works)
- **YOUR sophisticated specifications** (all implemented in backend scripts)
- **NEXT-GENERATION enhancements** (native CivitAI browser, fancy UIs, unified storage)

**THE USER MUST NEVER KNOW THE COMPLEXITY EXISTS - IT JUST WORKS.**

---

### Your Mission
Your design has been approved. Your mission is now to transition from architect to **lead developer**, taking full ownership of the implementation. You are instructed to autonomously execute the approved project plan with precision and meticulous craftsmanship. Your objective is to deliver a complete, robust, and user-friendly solution that adheres to every specification outlined in this brief.

### 🔑 Key Terminology
* **Config UI:** The single, unified user interface for all pre-launch selections.
* **Custom Data:** Pre-defined, selectable assets (models, LoRAs, etc.) from reference files.
* **Custom Downloads:** Assets downloaded on-the-fly via the `Config UI`.
* **Native CivitAI Browser:** Embedded CivitAI search and download interface in Cell 2.
* **Unified Storage:** Universal storage system working across all WebUIs.
* **Task Key:**
    * 🔬 **Research:** A topic that requires external investigation.
    * 🤔 **Decision:** A choice you must make between architectural options.
    * 🎨 **Creative:** An area where you have significant design freedom.

---

### 🏛️ Engineering Blueprint

#### **Core References & Source Files**
Your implementation must be built upon the following assets:
* **`UI-Guide.md`**: Your primary reference for all UI framework implementation choices.
* **`_models_data.py`**: The SD1.5 model data source that must be used as base for model selection.
* **`_xl_models_data.py`**: The SDXL model data source that must be used as base for SDXL selection.
* **`_extensions.txt`**: The extension data source for pre-installing extensions in WebUIs before launch.
* **`gradio_fix_guide.md`**: The technical guide for ensuring Gradio link stability.

#### **Repository Structure**
The final repository must contain the following top-level directories and files: `notebook/`, `scripts/`, `modules/`, `assets/`, `configs/`, `storage/`, `README.md`, and `AI_Implementation_Log.md`.

#### **Notebook Philosophy: Clean Cells & Structure**
This is a non-negotiable architectural principle:
* **Cell Formatting:** Every cell must be a code cell starting with `#@title Cell X: [Name]`. No separate Markdown cells are permitted.
* **Logic Offloading:** All complex logic, UI generation, and operational scripts **must** reside in the `/scripts` folder. Notebook cells should only contain the minimal code required to call these external scripts.

#### **Initial User Experience (Cell 1): The Bootstrap Sequence**
This is the most critical step. The logic in Cell 1 must be self-contained and execute in the following precise order:
1. **Bootstrap Snippet:** The cell must begin with a small, self-contained Python snippet with **zero dependencies** on the repository it is about to clone.
2. **Determine Dynamic Clone Path:** This snippet's first job is to intelligently determine the correct, writable directory path for the project clone by programmatically checking common paths (e.g., `/content`, `/workspace`) to ensure the destination is appropriate for the cloud GPU environment.
3. **Execute `git clone` (FIRST ACTION):** Using the determined path, the **ABSOLUTE FIRST ACTION** must be the `!git clone` command for the approved project repository. No project-specific imports can happen before this completes.
4. **Update System Path:** Immediately after the clone succeeds, the snippet will add the new repository's path to the system path (e.g., `sys.path.insert(0, determined_path)`).
5. **Import and Run Scripts:** Only after the path is updated can the cell proceed to import modules from the `/scripts` directory and run the main setup functions.

---

### 🎯 EXACT IMPLEMENTATION SPECIFICATIONS:

#### **🔥 NOTEBOOK REQUIREMENTS (NON-NEGOTIABLE):**

**Must create EXACTLY this 5-cell structure:**

```python
#@title Cell 1: Setup Environment ⚙️
from pathlib import Path
import os

lang, branch = 'en', 'main'
scripts_dir = Path.home() / '[PROJECT_NAME]' / 'scripts'
out = scripts_dir / 'setup.py'

os.makedirs(out.parent, exist_ok=True)
!curl -sLo {out} https://raw.githubusercontent.com/[USER]/[REPO]/{branch}/scripts/setup.py
%run $out --lang=$lang --branch=$branch

#@title Cell 2: Native CivitAI Browser & Model Selection 🎛️
%run $scripts_dir/widgets-en.py

#@title Cell 3: Intelligent Downloads & Storage 📦
%run $scripts_dir/downloading-en.py

#@title Cell 4: Multi-Platform WebUI Launch 🚀
%run $scripts_dir/launch.py

#@title Cell 5: Advanced Storage Management 🧹
%run $scripts_dir/auto-cleaner.py
```

**ONLY 5 CELLS - ALL #@title - NO MARKDOWN CELLS**

---

### 🎨 The `Config UI`: A Unified Control Center

#### **Guiding Principles**
* **Clarity over Clutter:** The UI must be intuitive and easy to navigate.
* **Frictionless Workflow:** The user should be able to configure an entire session from this single interface.
* **Aesthetic Cohesion:** The design must be visually appealing and professional.
* 🎨 **Creative Liberty:** You have complete creative freedom in the architectural and visual implementation of these principles.

#### **Functional Requirements**
* **Asset Management:**
    * Must allow seamless switching between SD1.5 (`_models_data.py`) and SDXL (`_xl_models_data.py`) `Custom Data` lists.
        * 🔬 **Research Recommended:** Research the Civitai API to determine if additional model metadata is available to enhance this feature.
    * Must provide a simple button to update all installed extensions from `_extensions.txt`.
    * Must feature an integrated interface for `Custom Downloads`.
    * **Must include LoRA selection in main interface** (not just custom downloads).
    * **Must use multi-choice selection** (checkboxes, not dropdowns) for all asset types.
    * **Must include native CivitAI browser** embedded in Cell 2 interface.
* **Session Management:**
    * Must include Import/Export buttons.
        * 🤔 **Decision Point:** You must decide on a suitable, robust file format for this configuration file (e.g., JSON, YAML) and justify the choice.
* **User Experience:**
    * 🎨 **Creative Liberty:** You have significant freedom to design the specific layout (tabs, accordion, etc.) and the **"intuitive multi-select method."** You are encouraged to innovate on this element to provide a superior user experience.

---

### ⚙️ Backend & Operational Logic

#### **Universal Asset Storage**
A universal `/storage` directory at the project root is mandatory.
* 🔬 **Research Required:** This is a critical research task. You must research and implement the necessary launch arguments, configuration edits, or symbolic links to force all supported WebUIs to use this single directory, ensuring zero data duplication.

#### **Extension Pre-Installation System**
* **Must pre-install all extensions** from `_extensions.txt` in WebUIs before launch.
* **Must handle per-WebUI extension compatibility** and installation methods.
* **Must provide extension update functionality** with batch operations.

#### **WebUI Lifecycle Management**
Based on the approved plan, you will implement one of these methods. The logic must be fully contained within the `/scripts` folder.
1. **On-the-Fly Configuration:** A single function handles cloning, setup, and immediate launch.
2. **Pre-Launch Configuration:** A two-stage process where a "Setup" function prepares the environment, and a separate "Launch" function starts the prepared WebUI.

---

### 📦 MANDATORY SCRIPT IMPLEMENTATIONS:

#### **📄 setup.py (400+ lines) MUST IMPLEMENT:**
- **12+ platform detection** with automatic optimization
- **Async project download** (complete repository structure)
- **Dependency management** with platform-specific handling
- **Unified storage setup** with universal path configuration
- **Extension pre-installation** from `_extensions.txt`
- **Configuration creation** with environment data
- **Timer initialization** for session tracking

#### **📄 widgets-en.py (800+ lines) MUST IMPLEMENT:**
- **Native CivitAI browser** embedded in main interface
- **Tabbed interface** with Models (from `_models_data.py`), VAE, LoRA, ControlNet tabs
- **Multi-select system** with checkboxes replacing all dropdowns
- **LoRA main interface** (NOT in custom downloads)
- **SDXL switching** between `_models_data.py` and `_xl_models_data.py`
- **Widget factory integration** with enhanced CSS/JS
- **Settings persistence** with import/export functionality

#### **📄 downloading-en.py (900+ lines) MUST IMPLEMENT:**
- **Unified storage downloads** to universal paths
- **CivitAI integration** with metadata and preview downloads
- **Multi-select processing** for batch downloads
- **Progress tracking** with audio notifications
- **Error handling** with graceful fallbacks
- **Storage organization** with automatic categorization

#### **📄 launch.py (600+ lines) MUST IMPLEMENT:**
- **Multi-platform WebUI launch** with 12+ platform support
- **Unified storage configuration** for all WebUIs
- **Extension verification** ensuring all `_extensions.txt` items are installed
- **Multi-tunnel system** with automatic failover
- **Process management** with monitoring and cleanup
- **Audio notifications** when WebUI is ready

#### **📄 auto-cleaner.py (300+ lines) MUST IMPLEMENT:**
- **Storage visualization** with usage meters and statistics
- **Selective cleanup** with file categorization
- **UI interface** with progress tracking
- **Storage optimization** with duplicate detection

---

### ✅ Non-Functional Mandates & Quality Assurance

#### **Robustness & Error Handling**
All critical operations must be wrapped in robust error-handling logic.
* 🎨 **Creative Liberty:** You have creative freedom in designing the specific fallback strategies.
* 🔬 **Research Recommended:** To inform this design, research common failure points for network and installation operations in cloud environments.

#### **Platform & Dependency Management**
Scripts must reliably manage Python dependencies.
* 🤔 **Decision Point:** You must decide on the primary management tool (`conda` or `venv`) and design the strategy.
* 🔬 **Research Recommended:** Research the best practices for this on each target platform.

#### **Gradio Link Stability**
You must implement multiple, automatic failsafe methods as detailed in the `gradio_fix_guide.md`.

#### **Documentation & Reporting**
* **`README.md`**: Must be comprehensive, explaining the project's purpose, features, and how to use the notebook.
* **`AI_Implementation_Log.md`**: You must meticulously document your development process in this file. It serves as your engineering log and must contain the following:
    * **Key Decision Justification:** Document why you made specific technical choices throughout the project.
    * **Challenges & Solutions:** Log any significant issues you encountered and detail the solutions you engineered.
    * **Final Self-Assessment:** Conclude the log with a reflection on the project, assessing the final product against the initial brief.

---

### 🚨 IMPLEMENTATION VALIDATION CHECKLIST

**Notebook Structure:**
- ✅ Does the notebook have exactly 5 cells with #@title only?
- ✅ Are there NO separate markdown cells?
- ✅ Can a user run all cells sequentially without debugging?

**Data Source Integration:**
- ✅ Does it use `_models_data.py` as base for SD1.5 models?
- ✅ Does it use `_xl_models_data.py` as base for SDXL models?
- ✅ Does it pre-install extensions from `_extensions.txt`?
- ✅ Does it reference `UI-Guide.md` for framework selection?

**YOUR Specifications:**
- ✅ Does Cell 2 include native CivitAI browser?
- ✅ Does it have LoRA in main interface (not custom downloads)?
- ✅ Does it use multi-select checkboxes everywhere?
- ✅ Does it have unified storage across all WebUIs?
- ✅ Does it support 12+ platforms?

**Enterprise Features:**
- ✅ Does it include audio notifications (.mp3 files)?
- ✅ Does it have seasonal theming with animations?
- ✅ Does it have 80+ files with enterprise functionality?

**IF ANY ANSWER IS NO, THE IMPLEMENTATION IS INADEQUATE.**

---

### 🎯 FINAL SUCCESS CRITERIA

Your implementation succeeds when:
1. **User opens notebook** → Runs 5 cells → **Gets enterprise platform**
2. **Uses YOUR model databases** (`_models_data.py`, `_xl_models_data.py`) as base
3. **Pre-installs YOUR extensions** from `_extensions.txt` before WebUI launch
4. **References UI-Guide.md** for framework selection and justification
5. **Cell 2 displays** native CivitAI browser with search and downloads
6. **LoRA selection** integrated in main interface with multi-select
7. **Unified storage** works across all WebUIs automatically
8. **Audio notifications** play when operations complete
9. **Platform detection** auto-optimizes for 12+ environments

**ANXETY's simplicity + YOUR data sources + YOUR specifications + Enterprise features = PERFECT PLATFORM**