# %% [markdown]
# #### Task Details
# 
# ```Create a Base Class:```Define a base class called Item that will have common attributes and methods which can be inherited. For example, each item might have a description and a status (completed or not).
# 
# ```Extend the Item Class:```
# Create two derived classes from Item:
# 
# *Task:* Represents a regular task. Include specific attributes or methods that apply only to tasks.
# 
# *Event:* Represents a calendar event. Add attributes like event date and start/end times.
# 
# ```Implement Polymorphism:```
# Override a common method in both derived classes, such as a method to display the item details. Each class should format the details in a way that is appropriate for its type.
# For example, tasks might show completion status, while events show the date and time.
# 
# ```Modify TodoList Class:```
# Adapt the TodoList class to handle both Tasks and Events. Ensure that methods such as add_item, delete_item, and show_items are polymorphic and handle different item types correctly.
# 
# ``Main Method:``
# Ensure your application includes a main method that initializes the TodoList and allows users to interact with it. This will make your application modular and easier to run.
# 
# #### Example Scenario:
# Your Todo List can now handle both tasks like "Finish the OOP assignment" and events like "Team meeting on Zoom at 3 PM on Friday".
# When showing items, the output should reflect the type of item and its specific attributes.

# %%
class Item:
  """
  This is a class that creates an item.

  """
  def __init__(self, description):
      """
      This initiates the instance of the item class.
      Args:
        description: Describes the item.
        status: Specifies the completion status of the item. Default is False.

      """
      self.description = description
      self.status = False
  

  def details(self):
      """
      Prints out the details of the described item.

      """
      # self.description = description
      return f'{self.description}'
    

class Task(Item):
  """
  This is a child class of the Item class. It creates an task as an instance of an Item.

  """  
  def __init__(self, description, status=None):
    """
    This initiates the instance of the item class.
    Args:
      description: Describes the item.
      status: Identifies the status of the task. Default is False.    
    """
    super().__init__(description)
    self.status = False
    
      
  def details(self):
    """
    Prints out the details of the described task.

    """
    return f'{self.description}, while it\'s completion status is {self.status}'


class Event(Item):  
  """
  This is a child class of the Item class. It creates an event as an instance of an Item.

  """   
  def __init__(self, description, location = None , time = None, day = None ):
    """
    This initiates the instance of the item class.
    Args:
      description: Describes the item.
      location: Specifies the location of the event.
      time: Specifies the time of the day.
      day:  Specified the day of the event.
    """    
    super().__init__(description)
    self.location = location
    self.time = time
    self.day = day

  def details(self):
    """
    Prints out the details of the described task.

    """
    return f'{self.description} on {self.location} by {self.time} on {self.day}.'
    

task_1 = Event('Finish OOP Advanced Task', 'Github', '12:00', 'Saturday')
print(task_1.details())

task_2 = Task("Adele")
print(task_2.details())


class TodoList:
  """
  This is a class that creates a Todo List
  Tasks can be added, deleted, displayed and marked as completed

  """

  # choice = int(input('Select 1 for Event & 2 for Task:'))
  # description = []

  def __init__(self):
    """
    This initiates the empty to do list.
    Args:
      available_task: Newly added tasks or pending tasks.
      completed_tasks: Tasks marked as completed.
      all_tasks: Prints out all tasks ever inputed. 
      deleted_tasks: A place holder for deleted tasks incase it is to be reintroduced.
    """
    self.tasks = []



  def add_task(self, description):
    """
    This method adds a task to the todo list
    Args:
      task: designates the task to be added to the list.
    """
    item = Task(description)
    item = item.details()
    self.tasks.append(item)

  def add_event(self, description,location,time, day):
    event = Event(description,location,time, day)
    event = event.details()
    self.tasks.append(event)

  def delete_task(self, delete):
    """
    This methods deletes a listed task from the list.
    Args:
      delete: designates the task to be deleted.
    """
    # task[delete] = strike(task[delete])
    self.tasks.pop(delete)
    # self.deleted_tasks.append(delete)

  def show_tasks(self):
    """

    Returns: This method shows the available tasks in the list based on task_list entry.
          1. Available Tasks = self.available_tasks[]
          2. Completed Tasks = self.completed_tasks[]
          3. Deleted Tasks = self.deleted_tasks[]
          4. All Tasks = available_task[] + completed_tasks[] + deleted_tasks[]

    """
    return self.tasks

  def mark_as_completed(self, mark):
    """
    This method marks a task as completed.
    Args:
      mark: designates the task to be marked as complete.
    """
    print(f"Task '{self.tasks[mark]}' is completed")
    self.tasks.pop(mark)
    # self.completed_tasks.append(mark)


# TodoList().add_task('Adele')#location = 'Zoom', time = '20:48', day = 'Saturday', type = 'event'))
# TodoList().add_event('Finish OOP Advanced Task', 'Github', '12:00', 'Saturday')

# aa = TodoList()
# aa.add_task('Adele')
# aa.add_event('Finish OOP Advanced Task', 'Github', '12:00', 'Saturday')
# print(aa.show_tasks())

def main():
    # Creating TodoList Object
    todo_list = TodoList()
    
    while True:
        """


        """     
        print("\nTodo List Menu:")
        print("1. Add Task")
        print("2. Add Event")
        print("3. Delete Task")
        print("4. Show Tasks")
        print("5. Mark Task as Completed")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        """

        """        
        if choice == '1':
          task = input("Enter the task description: ")
          todo_list.add_task(task)
        elif choice == '2':
          event = input("Enter the event description: ")
          loc= input("Enter the location of the event: ")
          ti = input("Enter the time of the event: ")
          dy = input("Enter the day of the event: ")
          todo_list.add_event(event, location=loc, time=ti, day=dy)
        elif choice == '3':
          task_id = int(input("Enter the task ID to delete: "))
          todo_list.delete_task(task_id)       
        elif choice == '4':
          print(todo_list.show_tasks())
        elif choice == '5':
          task_id = int(input("Enter the task ID to mark as completed: "))
          todo_list.mark_as_completed(task_id)
        elif choice == '6':
          print("Exiting the Todo List app. Goodbye!")
          break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()




# %%

# %%


# %%


# %%


# %%


