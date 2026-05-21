# Left 4 Dead 2 Addon Fixer Toolkit 🧟‍♂️🛠️

An automated toolkit designed to solve a specific issue in Left 4 Dead 2 modding: identifying and repairing VPK files that are missing the required `addoninfo.txt` metadata.

## 📌 Overview

When downloading custom addons or mods for Left 4 Dead 2, some VPK files lack the `addoninfo.txt` file, making them difficult to manage or edit. This toolkit consists of two specialized tools that follow the Unix philosophy (do one thing and do it well):

1. **Scanner (`VPKScanner`):** Scans the game's addon directory, identifies VPKs missing the `addoninfo.txt` file, and isolates them into a target folder.
2. **Repair Tool (`VPKRepair`):** Automatically extracts the isolated VPKs, generates standard `addoninfo.txt` metadata, and repacks them in their original format using the official L4D2 `vpk.exe` tool via the command line.

## 🚀 How to Use

### Option 1: Pre-compiled Executables (Recommended for Users)
1. Download the latest executables for your operating system (e.g., `.exe` for Windows).
2. **Run the Scanner:** Double-click `VPKScanner` and follow the terminal instructions to isolate missing VPKs.
3. **Run the Repair Tool:** Double-click `VPKRepair` to automatically extract, fix, and repack your VPK files.
*Note: You do NOT need Python installed to use this option!*

### Option 2: Running from Source (For Developers)
1. Clone the repository and navigate into the project directory.
2. Install the necessary Python packages (see Prerequisites).
3. Run the scanner: `VPKScanner.py`
4. Run the repair tool: `VPKRepair.py`

## 🛠️ Features

* **Automated File I/O:** Efficiently parses large directories of VPK files.
* **Error Handling:** Safe extraction and repacking processes to prevent data loss or crashes from corrupted files.
* **Subprocess Integration:** Programmatically controls the official `vpk.exe` via Python's `subprocess` module.
* **Clean Execution:** Automatically cleans up temporary extraction folders after a successful repack.

## 📋 Prerequisites

### For Executable Users:
* Left 4 Dead 2 Authoring Tools installed via Steam (required to provide the official `vpk.exe` for the repair tool).

### For Source Code Users:
* Python 3.x
* `vpk` Python library (`pip install vpk`)
* Left 4 Dead 2 Authoring Tools (for `vpk.exe`)

## 👨‍💻 About the Project

This toolkit was developed to automate a tedious manual process, demonstrating problem-solving skills, file manipulation in Python, and external tool integration.
