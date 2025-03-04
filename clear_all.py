from tkinter import messagebox


def clear_all(tasks_list, listbox):
    """
    Clear all tasks from the list and listbox

    Args:
        tasks_list (list): The list of current tasks
        listbox (tk.Listbox): The listbox widget to update

    Returns:
        bool: True if tasks were cleared, False otherwise
    """
    # Confirm with the user
    result = messagebox.askyesno(
        "Confirm Clear", "Are you sure you want to clear all tasks?")

    if result:
        # Clear the tasks list and listbox
        tasks_list.clear()
        listbox.delete(0, "end")
        return True

    return False
