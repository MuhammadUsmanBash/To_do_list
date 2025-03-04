def add_task(task_text, tasks_list):
    """
    Add a new task to the tasks list
    
    Args:
        task_text (str): The text of the task to add
        tasks_list (list): The list of current tasks
        
    Returns:
        str or None: The added task text if successful, None otherwise
    """
    # Check if task is empty
    if not task_text.strip():
        return None
    
    # Add the task to the list
    task_to_add = task_text.strip()
    tasks_list.append(task_to_add)
    
    return task_to_add