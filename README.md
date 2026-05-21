# Smart File Organizer

A lightweight, fully customizable Python script that automatically sorts your files into folders based on their file extensions. 

Instead of hardcoding paths, this project is completely driven by a `config.yaml` file, making it easy to change sorting rules without ever touching the Python code.

## Features
* **Rule-Based Sorting:** Define source directories, target destinations, and file extensions in a clean YAML file.
* **Collision Handling:** Automatically handles duplicate file names by either renaming (e.g., `file_1.pdf`), overwriting, or skipping them.
* **OS Agnostic:** Built using Python's `pathlib`, meaning it works flawlessly on Windows, macOS, and Linux without slash-formatting issues.
* **Safe Execution:** Catch-and-log architecture ensures the script won't crash if a file is currently open or locked by another program.

## Prerequisites

You need Python installed on your system. This project requires one external library to parse the configuration file:

```bash
pip install pyyaml
