# Focus-Flow: Priority Task Manager

Focus-Flow is a Python-based CLI application designed to help users manage and prioritize their daily tasks. The system uses a Priority Scoring logic based on Urgency and Importance to rank tasks automatically.

## Core Features
- Priority Calculation: Automatically calculates scores based on user input.
- Task Sorting: Displays tasks from highest to lowest priority.
- Data Persistence: Saves all task data in a JSON file for future sessions.
- Input Validation: Handles incorrect user inputs to prevent program crashes.
- Summary Reporting: Provides a quick overview of task statistics.

## Technical Specifications
- Language: Python 3.x
- Environment: Virtual Environment (.venv)
- Libraries: Rich (for terminal formatting)
- Storage: JSON

## Installation and Usage

1. Clone the repository:
   git clone https://github.com/jahidunfarabi/FocusFlow-Python-Project.git
   cd focus-flow

2. Create and activate a virtual environment:
   python -m venv .venv
   source .venv/Scripts/activate  # On Windows: .venv\Scripts\activate

3. Install dependencies:
   pip install -r requirements.txt

4. Run the application:
   python main.py

## Project Architecture
The project follows Object-Oriented Programming (OOP) principles with four main classes:
- Task: Defines the data model for individual tasks.
- TaskManager: Handles the logic for CRUD operations and sorting.
- Storage: Manages reading and writing to the JSON data file.
- Main: Controls the user interface and main program loop.

## Developer
Md. Jahidun Muntaka Farabi
Computer Science & Engineering, AIUB
