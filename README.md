# camia_AmanteNarca

# INITIAL DRAFT
# Project Title
- TaskMaster

# Problem Statement
- For many aspiring scholars, we are prone to be  overloaded with many academic requirements. More often that not, there are times we tend to lose track of tasks we need to accomplish. Hence, we aim to promote a sustainable way to mitigate the hassle of being lost in your assignments. 

# Project Objectives
- To provide fellow scholars with a quick and accessible application to track their tasks.
- To guide our peers from being burdened with overlapping academic obligations.
- To give an example of how to be organized with their homework:)
 
# Planned Features
- The user will be asked to decide if they want to add/input a task, delete a task, or to exit the program.
- Displays tasks (to-be-done, completed, future, or all tasks).
- Deleting a task removes it from the list.
- Users are allowed to assign priority levels to tasks.
- Users are allowed to set due dates to track the deadlines of each task.

# Planned Input and Outputs
  PLANNED INPUTS:
  - User selects an option (1-5).
  - For adding tasks: subject/category, task description, and if more tasks (yes/no).
  - For viewing: select category, if more tasks (yes/no).
  - For updating: select task, mark as "done" (yes/no), if more updates (yes/no).
  - For removing: select task, confirm removal (yes/no), if more removals (yes/no).
  - To exit: select option 5.

  PLANNED OUTPUTS:
  - Main menu with options.
  - "Task added successfully!" and ask for more tasks (yes/no).
  - Display categories and tasks, ask for more (yes/no).
  - "Task marked as 'done'" and ask for more updates (yes/no).
  - "Task removed" and ask for more removals (yes/no).
  - "Goodbye!" when exiting.

# Logic Plan
```
START
    repeat
        display "Main Menu"
        display "[1] Add Task, [2] View Tasks, [3] Update Task, [4] Remove Task, [5] Exit"
        input choice

        if choice = 1 then
            repeat
                input subject/category
                input task
                save task under category
                ask "Add more tasks? (yes/no)"
            until no
        else if choice = 2 then
            repeat
                show categories
                select category
                display tasks in category
                ask "View another category? (yes/no)"
            until no
        else if choice = 3 then
            repeat
                select category
                select task(s)
                update status to "done"
                ask "Update more tasks? (yes/no)"
            until no
        else if choice = 4 then
            repeat
                select category
                select task(s)
                remove task
                ask "Remove more tasks? (yes/no)"
            until no
        else if choice = 5 then
            exit
        endif
    until choice = 5
END
```
 

# FINAL DRAFT
# Project Title
- TaskMaster

# Project Description
- Have you ever experienced being drowned in what seems to be an infinite pile of schoolworks that you start thinking all the decisions you made in the past which lead you to where you right now? Truthfully, as students, it really cannot be avoided. There are some moments that you feel the need to sort out the subjects you "must" focus on more compared to another subject, choosing to "sacrifice" the latter just to handle the tormer. Sorting things out can, at times, come in hand and be useful in tackling everyday issues. In addition to that, have you ever experienced being lost and having no idea on where to start? Luckily, Python's the one for you. Due to realistic adversities we face day-to-day as aspiring scholars, we have formulated the idea to design a Python program which solves this problem; since we figured that it deals with a function that, well, sorts out elements and items. In our program, we aim to provide the necessary content by making a program that acts like a to-do list tracker to organize requirements and checks it. For us to minimize the hassle of carrying pens and papers just to cross out the schoolworks that we have finished, why not simply encode it conventionally into our smartphone? This way, we can maximize our time into focusing on our schoolworks--to get the job done.

## Features
-   This program will act as an active to-do list tracker.
-   The user will be asked to decide if they want to add/input a task, delete a task, or to exit the program.
-   Displays tasks (to-be-done, completed, future, or all tasks).
-   Deleting a task removes it from the list. allowed to assign priority levels to tasks.
-   Users are allowed to set due dates to track the deadlines of each task.

## How To Run The Program
1.    Make sure you have Python installed.
2.    Download the file 'list_tracker.py
3.    Open a terminal or command prompt.
4.    Follow the on-screen instructions. Make sure to input all the necessary information the program asked for before running the program to avoid error(s).
5.    Run the program by clicking 'Run' or pressing F5

## Example Output
```
—— TaskMaster ——
 
Add task? (y/n): Y
Enter
subject/category: MATH
Enter task: Problem Set 5
Task saved under [MATH].
 
Add more tasks? (y/n): Y
Enter
subject/category: SCIENCE
Enter task: Lab Report #2
Task saved under [SCIENCE].
 
Add more tasks? (y/n): N
Back to main menu? (y/n): Y
 
—— TaskMaster ——
 
View tasks? (y/n): Y
Categories:
1. MATH
2. SCIENCE
Select category: 1
 
Tasks in [MATH]:
- Problem Set 5
 
Back to view tasks? (y/n): N
Back to main menu? (y/n): Y
 
—— TaskMaster ——
 
Update task? (y/n): Y
Select category: SCIENCE
 
Tasks in [SCIENCE]:
1. Lab Report #2
Select task to update: 1
Task updated to "DONE".
 
Update more tasks? (y/n): N
Back to main menu? (y/n): Y
 
—— TaskMaster ——
 
Remove task? (y/n): Y
Select category: MATH
Tasks in [MATH]:
1. Problem Set 5
Select task to remove: 1
 
Task removed successfully.
 
Remove more tasks? (y/n): N
Back to main menu? (y/n): N
 
—— Program Exited Successfully ——
```
