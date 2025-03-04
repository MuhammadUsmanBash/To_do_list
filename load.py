import json
import os
from tkinter import messagebox

def load_tasks():
    """
    Load tasks from a JSON file
    
    Returns:
        list: The list of loaded tasks, or an empty list if no tasks were loaded
    """
    try:
        # Check if the file exists
        if not os.path.exists("data/tasks.json"):
            return []
        
        # Load tasks from the file
        with open("data/tasks.json", "r") as file:
            tasks = json.load(file)
        
        return tasks
    except Exception as e:
        messagebox.showerror("Load Error", f"An error occurred while loading tasks: {str(e)}")
        return []