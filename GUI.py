import tkinter as tk
from tkinter import ttk, messagebox
import add_task
import remove
import save
import load
import clear_all

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")
        self.root.geometry("500x450")
        self.root.resizable(True, True)
        
        # Task list to store all tasks
        self.tasks = []
        
        # Create and configure main frame
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create title label
        self.title_label = ttk.Label(self.main_frame, text="Task Manager", font=("Arial", 16, "bold"))
        self.title_label.pack(pady=10)
        
        # Create entry for new tasks
        self.task_frame = ttk.Frame(self.main_frame)
        self.task_frame.pack(fill=tk.X, pady=5)
        
        self.task_label = ttk.Label(self.task_frame, text="New Task:")
        self.task_label.pack(side=tk.LEFT, padx=5)
        
        self.task_entry = ttk.Entry(self.task_frame, width=40)
        self.task_entry.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        self.task_entry.bind("<Return>", lambda event: self.add_task())
        
        self.add_button = ttk.Button(self.task_frame, text="Add Task", command=self.add_task)
        self.add_button.pack(side=tk.LEFT, padx=5)
        
        # Create task listbox with scrollbar
        self.list_frame = ttk.Frame(self.main_frame)
        self.list_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.listbox_label = ttk.Label(self.list_frame, text="Your Tasks:")
        self.listbox_label.pack(anchor=tk.W, padx=5)
        
        self.scrollbar = ttk.Scrollbar(self.list_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.listbox = tk.Listbox(
            self.list_frame, 
            height=15, 
            width=50, 
            selectmode=tk.SINGLE,
            yscrollcommand=self.scrollbar.set,
            font=("Arial", 10)
        )
        self.listbox.pack(fill=tk.BOTH, expand=True, padx=5)
        self.scrollbar.config(command=self.listbox.yview)
        
        # Create buttons frame
        self.buttons_frame = ttk.Frame(self.main_frame)
        self.buttons_frame.pack(fill=tk.X, pady=10)
        
        self.remove_button = ttk.Button(
            self.buttons_frame, 
            text="Remove Selected", 
            command=self.remove_task
        )
        self.remove_button.pack(side=tk.LEFT, padx=5)
        
        self.clear_button = ttk.Button(
            self.buttons_frame, 
            text="Clear All", 
            command=self.clear_all_tasks
        )
        self.clear_button.pack(side=tk.LEFT, padx=5)
        
        self.save_button = ttk.Button(
            self.buttons_frame, 
            text="Save Tasks", 
            command=self.save_tasks
        )
        self.save_button.pack(side=tk.RIGHT, padx=5)
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        self.status_bar = ttk.Label(
            self.root, 
            textvariable=self.status_var, 
            relief=tk.SUNKEN, 
            anchor=tk.W
        )
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Load tasks on startup
        self.load_tasks()
    
    def add_task(self):
        new_task = add_task.add_task(self.task_entry.get(), self.tasks)
        if new_task:
            self.listbox.insert(tk.END, new_task)
            self.task_entry.delete(0, tk.END)
            self.status_var.set(f"Task added: {new_task}")
    
    def remove_task(self):
        selected_task_index = self.listbox.curselection()
        result = remove.remove_task(selected_task_index, self.tasks, self.listbox)
        if result:
            self.status_var.set("Task removed")
    
    def save_tasks(self):
        result = save.save_tasks(self.tasks)
        if result:
            self.status_var.set("Tasks saved to file")
            messagebox.showinfo("Save Successful", "Your tasks have been saved successfully.")
    
    def load_tasks(self):
        loaded_tasks = load.load_tasks()
        if loaded_tasks:
            self.tasks = loaded_tasks
            self.update_listbox()
            self.status_var.set("Tasks loaded from file")
    
    def clear_all_tasks(self):
        result = clear_all.clear_all(self.tasks, self.listbox)
        if result:
            self.status_var.set("All tasks cleared")
    
    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            self.listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()