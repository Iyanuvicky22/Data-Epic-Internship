# %% [markdown]
# # Create a Class:
# Define a class named TodoList.
# 
# 
# ### Methods to Implement:
# 
# ```Add Task:``` A method to add a new task to the todo list.
# 
# ```Delete Task:``` A method to delete a task from the todo list.
# 
# ```Show All Tasks:``` A method to display all tasks in the todo list.
# Mark Task as Completed: A method to mark a task as completed.
# 
# ```Version Control:```
# Make sure to make commits of your task to the Data Epic organization Git repository. Check for a reminder on how to do that in ⁠task-submission
# Follow proper commit messages and structure for your commits.
# 
# ```Deadline:```
# The task is due by Friday at 12pm.

# %%
# class TodoList:
#   """
#   This is a class that creates a Todo List
#   Tasks can be added, deleted, displayed and marked as completed

#   """

#   def __init__(self):
#     """
#     This initiates the empty to do list.

#     """
#     self.todo_list = []
#     self.completed_tasks = []
#     self.all_tasks = []


#   def add_task(self, add):
#     """
#     This method adds a task to the todo list
#     Args:
#       add: designates the task to be added to the list.
#     """
#     add = str(add)
#     self.todo_list.append(add)

#   def delete_task(self, delete):
#     """
#     This methods deletes a listed task from the list.
#     Args:
#       delete: designates the task to be deleted.
#     """
#     self.todo_list.pop(delete)

#   def show_all_task(self):
#     """

#     Returns: This method shows the available tasks in the list.

#     """
#     return self.todo_list

#   def mark_as_completed(self, mark):
#     """
#     This method marks a task as completed.
#     Args:
#       mark: designates the task to be marked as complete.
#     """
#     print(f"Task '{self.todo_list[mark]}' is completed")
#     self.todo_list.pop(mark)
#     self.completed_tasks.append(mark)




# # %%
# # Create a new todo list
# my_todo_list = TodoList()

# # Add tasks
# my_todo_list.add_task("Finish Python assignment")
# my_todo_list.add_task("Read OOP chapter")

# # Show all tasks
# my_todo_list.show_all_task()

# # Mark the first task as completed
# my_todo_list.mark_as_completed(0)

# # Show all tasks again to see the updates
# my_todo_list.show_all_task()

# # Delete the second task
# my_todo_list.delete_task(0)

# # Show all tasks again to see the updates
# my_todo_list.show_all_task()

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
      print(f'{self.description}')
    

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
    print(f'{self.description}, while it\'s completion status is {self.status}') 


class Event(Item):  
  """
  This is a child class of the Item class. It creates an event as an instance of an Item.

  """   
  def __init__(self, description, location, time, day):
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
    print(f'{self.description} on {self.location} by {self.time} on {self.day}.')
    

task_1 = Event('Finish OOP Advanced Task', 'Github', '12:00', 'Saturday')
task_1.details()


class TodoList:
  """
  This is a class that creates a Todo List
  Tasks can be added, deleted, displayed and marked as completed

  """

  def __init__(self):
    """
    This initiates the empty to do list.
    Args:
      available_task: Newly added tasks or pending tasks.
      completed_tasks: Tasks marked as completed.
      all_tasks: Prints out all tasks ever inputed. 
      deleted_tasks: A place holder for deleted tasks incase it is to be reintroduced.


    """



  def add_task(self, task):
    """
    This method adds a task to the todo list
    Args:
      task: designates the task to be added to the list.
    """
    self.available_tasks.append(task)
  
  # def strike(self):
  #   return ''.join([u'\u0336{}'.format(c) for c in self.description])

  def delete_task(self, delete):
    """
    This methods deletes a listed task from the list.
    Args:
      delete: designates the task to be deleted.
    """
    task[delete] = strike(task[delete])
    self.available_tasks.pop(delete)
    self.deleted_tasks.append(delete)

  def show_tasks(self):
    """

    Returns: This method shows the available tasks in the list based on task_list entry.
          1. Available Tasks = self.available_tasks[]
          2. Completed Tasks = self.completed_tasks[]
          3. Deleted Tasks = self.deleted_tasks[]
          4. All Tasks = available_task[] + completed_tasks[] + deleted_tasks[]

    """
    return self.available_tasks
    # while isinstance(task_list, int):
    #   if task_list == 1:
    #     return self.available_tasks
    #   elif task_list == 2:
    #     for item in self.completed_tasks:
    #       item = strike(item)
    #     return self.completed_tasks
    #   elif task_list == 3:
    #     return self.deleted_tasks
    #   elif task_list == 4:
    #     self.all_tasks = self.available_tasks + self.completed_tasks + \
    #       self.deleted_tasks
    #     return self.all_tasks
    #   else: 
    #     print('Input not recognized! Kindly choose between 1 and 4')
    #     break
    # return self.available_tasks

  def mark_as_completed(self, mark):
    """
    This method marks a task as completed.
    Args:
      mark: designates the task to be marked as complete.
    """
    task[mark] = task[mark] + u" \u2713"
    print(f"Task '{self.available_tasks[mark]}' is completed")
    self.available_tasks.pop(mark)
    self.completed_tasks.append(mark)

# todo_list = TodoList()
# todo_list.add_task(Adele)

def main():
    # Creating TodoList Object
    todo_list = TodoList()
    
    while True:
        """

        """     
        print("\nTodo List Menu:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Show Tasks")
        print("4. Mark Task as Completed")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        """

        """        
        if choice == '1':
          while True:
            item_type = {'Event' : Event(description, location, time, day), 'Task': Task(description)}
            for item in item_type:
              print('Is the item an event or task?')
              print('Press 1 for Event!')
              print('Press 2 for Task!')
              choice = input("Insert your item")
              if item == '1':
                task = Event(description, location, time, day)
              elif item == '2':
                task = Task(description)
              else:
                print('Invalid input! Try again')
                break
            description = input("Enter the task description: ")
            todo_list.add_task(task)
        elif choice == '2':
            task_id = input("Enter the task ID to delete: ")
            todo_list.delete_task(task_id)
        elif choice == '3':
            todo_list.show_tasks()
          # while True:
          #   print('\nTasks List to Show')
          #   print('1. Available Tasks')
          #   print('2. Completed Tasks')
          #   print('3. Deleted Tasks')
          #   print('4. All Tasks')

          #   choice = int(input('Enter your choice: '))

          #   if choice == 1:
          #     return todo_list.show_tasks
          #   elif choice == 2:
          #     return todo_list.show_tasks
          #   elif choice == 3:
          #     return todo_list.show_tasks
          #   elif choice == 4:
          #     return todo_list.show_tasks
          #   else:
          #     print('Wrong input! There is no such tasks list. TRY AGAIN!!!')
          #     break
        elif choice == '4':
            task_id = input("Enter the task ID to mark as completed: ")
            todo_list.mark_as_completed(task_id)
        elif choice == '5':
            print("Exiting the Todo List app. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()




# %%

# Create Class Todolist
# class Todolist:

# 	# Initiate class Todolist with "date" and list("tasks") class attributes
#     def __init__(self, date, tasks = []):
#     	self.date = date
#     	self.tasks = tasks
        
#     # Method to add task to the list where "task" attribute is the new task   
#     def add_task(self, task):
#         self.tasks.append(task)

#     # Method to mark task as complete where "x" is the index of completed task
#     def mark_as_complete(self, x):
#     	self.tasks[x] = self.tasks[x] + u" \u2713" # mark sign

#     # Method to delete task "x" is the index of task to be deleted
#     def delete_task(self, x):
#     	del(self.tasks[x])

#     # Method to make a line by line list of tasks
#     def li(self, x):
#     	for i in x:
#     		print(f"{i}\n") 

#     # Method to show tasks 
#     def show_tasks(self):
#        print(f"Your Tasks For {self.date} are:\n") # heading
#        self.li(self.tasks) # line by line list


#Test ----------------------------------------------------

# # instance of the class Todolist
# todo = Todolist("20/05/2024", [])
# # add a task
# todo.add_task("Wake up")
# # add a task
# todo.add_task("Brush teeth")
# # add a task
# todo.add_task("Perform ablution")
# # add a task
# todo.add_task('Pray')
# # add a task
# todo.add_task("Take a bath")
# # mark third task as complete
# todo.mark_as_complete(2)
# todo.mark_as_complete(3)
# # show all tasks
# todo.show_tasks()
# # delete second task
# todo.delete_task(1)
# # show all task
# todo.show_tasks()

# %%


# %%


# %%


# %%

# Edited

# As pointed out by roippi other answers so far are actually correct, and this one below is wrong. Leaving it here in case others get the same wrong idea that I did.

# Other answers so far are wrong - they do not strike out the first character of the string. Try this instead:


