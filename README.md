# EliteTask: A CLI-Based Priority Task Scheduler

EliteTask is a robust, command-line interface (CLI) application built in Python designed to manage and optimize daily tasks using an automated priority queue engine. Unlike traditional strict sequential task lists, EliteTask organizes workloads dynamically by calculating structural importance, ensuring high-priority objectives remain at the top of the stack while providing persistent data storage.

# 🎥 Video Demonstration & Defense
Click the link below to watch the technical walk-through, architectural defense, and project reflection:
👉 **[Watch the Final Project Defense on YouTube](PASTE_YOUR_UNLISTED_YOUTUBE_LINK_HERE)**

# ✨ Features
 "Dynamic Multi-Level Sorting:" Tasks are automatically ordered using a multi-level algorithm (Priority level 1-5 first, followed by an alphabetical sort by title if priorities match).
 "Persistent JSON Storage:" Automatic data state synchronization. Uses structured file handling context managers to read and write to disk in real-time.
 "Crash-Proof Input Validation:" Built-in loop filters trap invalid entries (such as alphabetical strings entered into integer priority fields) without crashing the runtime environment.
 "Clean Separation of Concerns:" Architected using decoupled Python modules separating user interactions (`main.py`), processing rules (`scheduler.py`), and data entities (`task.py`).

# 🛠️ Installation & Setup Guide
# Prerequisites
Ensure you have Python 3.8 or higher installed on your computer. You can check your version by running:
```bash
python --version
