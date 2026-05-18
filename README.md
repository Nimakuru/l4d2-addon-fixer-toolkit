# Left 4 Dead 2 Addon Fixer Toolkit 🧟‍♂️🛠️

An automated Python toolkit designed to solve a specific issue in Left 4 Dead 2 modding: identifying and repairing VPK files that are missing the required `addoninfo.txt` metadata.

## 📌 Overview

When downloading custom addons or mods for Left 4 Dead 2, some VPK files lack the `addoninfo.txt` file, making them difficult to manage or edit. This toolkit consists of two specialized Python scripts that follow the Unix philosophy (do one thing and do it well):

1. **Scanner (`scanner.py`):** Scans the game's addon directory, identifies VPKs missing the `addoninfo.txt` file, and isolates them into a target folder.
2. **Repair Tool (`repair.py`):** Automatically extracts the isolated VPKs, generates standard `addoninfo.txt` metadata, and repacks them in their original format using the official L4D2 `vpk.exe` tool via the command line.

## 🚀 Features

* **Automated File I/O:** Efficiently parses large directories of VPK files.
* **Error Handling:** Safe extraction and repacking processes to prevent data loss or crashes from corrupted files.
* **Subprocess Integration:** Programmatically controls the official `vpk.exe` via Python's `subprocess` module.
* **Clean Execution:** Automatically cleans up temporary extraction folders after a successful repack.

## 🛠️ Prerequisites

* Python 3.x
* `vpk` Python library (`pip install vpk`)
* Left 4 Dead 2 Authoring Tools (for `vpk.exe`)

## 👨‍💻 About the Project

This toolkit was developed to automate a tedious manual process, demonstrating problem-solving skills, file manipulation in Python, and external tool integration.
