from tkinter import messagebox

def remove_task(selected_index, tasks_list, listbox):
    """
    Remove a task from the tasks list
    
    Args:
        selected_index (tuple): The index of the selected task in the listbox
        tasks_list (list): The list of current tasks
        listbox (tk.Listbox): The listbox widget to update
        
    Returns:
        bool: True if a task was removed, False otherwise
    """
    # Check if a task is selected
    if not selected_index:
        messagebox.showwarning("No Selection", "Please select a task to remove.")
        return False
    
    # Get the index of the selected task
    index = selected_index[0]
    
    # Remove the task from the list and listbox
    tasks_list.pop(index)
    listbox.delete(index)
    
    return True