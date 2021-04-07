Github URL: https://github.com/elizabethhillman/taskManager

Users: Elizabeth Hillman (elizabethhillman), Isabella Solis (isolis1210), Sungjea Kwak (Jaykkwak), Thien Tran (thientran1999)

Product Name: S.I.T.E

Non-Functional Requirements:

    1. The system will be able to manage at least 10 tasks on a task board
    2. The system will respond to each user input within 5 seconds
    3. The system will be able to manage at least one collaborator on a user's task board

Use Cases:

    1. Create new task
**Product Name:** S.I.T.E

**Problem Statement:** S.I.T.E is a task manager where users can keep track of daily tasks: sorting the tasks by their priority, category and how long they will take.

**Use Case Name:** Create new task

**Date:** April 6th, 2021


\## Summary

The user can create a new task to their task board.


\## Actors

1. the user
2. the task board

\## Preconditions

\* The user must be signed in

\* The task trying to be created should not already exist


\## Triggers

User selects "create new task" option


\## Primary Sequence

1. System prompts user to detail what the new task is.
2. User adds in a string of what their task is.
3. System verifies that this task does not already exist in task board.
4. The new task is added to the task board, if it doesn't exist. Otherwise, error shows to user that task is already in the task board and nothing happens. 
 

\## Primary Postconditions

\* The task is shown on the task board, if the task has not been created yet

**OR** 

\* The task board remains the same, if the task has already been created


\## Non-functional Requirements

\* Task board can manage adding a new task, no matter how long the task is 


\## Glossary

\* user = a person who wants to create a new task

\* task board = a system that maintains all of the tasks created by the user 
    
    
    2. Remove completed tasks
**Product Name:** S.I.T.E

**Problem Statement:** S.I.T.E is a task manager where users can keep track of daily tasks: sorting the tasks by their priority, category and how long they will take.

**Use Case Name:** Remove completed tasks

**Date:** April 6th, 2021

\## Summary

The user can remove a task they completed


\## Actors

1. the user
2. the task board
3. the task


\## Preconditions

\* The user must be signed in

\* The task must exist on the task board


\## Triggers

User selects "Completed task" option


\## Primary Sequence

1. User locates the task they completed 
2. User marks that they completed that task
3. System removes the task from the task board


\## Primary Postconditions

\* The task is no longer shown on the task board


\## Non-functional Requirements

\* The task will be removed from the task board within 5 seconds of user marking that the task was completed.


\## Glossary

\* user = a person who wants to create a new task

\* task board = a system that maintains all of the tasks created by the user 

\* task = an object that was created by the user and stored on the task board
    
    
    3. Invite other users to “task board”
**Product Name:** S.I.T.E

**Problem Statement:** S.I.T.E is a task manager where users can keep track of daily tasks: sorting the tasks by their priority, category and how long they will take.

**Use Case Name:** Invite other user to personal task board

**Date:** April 6th, 2021


\## Summary

The user can invite another user to their task board, so that they can both see and edit the same task board


\## Actors

1. the user
2. the invited user
3. the task board

 
\## Preconditions

\* The user must be signed in


\## Triggers

User selects "Invite Collaborator" option


\## Primary Sequence
 
1. User inputs the email of the user they want to invite
3. The invited user joins the task board of the user
4. Both the user and invited user can view and edit the task board


\## Primary Postconditions

\* The user and invited user can view and edit the same task board


\## Non-functional Requirements

\* The user will be able to send an invite to a collaborator within 5 seconds. 

 
\## Glossary

\* user = a person who wants to create a new task

\* invited user = a person who is a collaborator on a task board created by the user

\* task board = a system that maintains all of the tasks created by the user 
    
    
    4. Assign Task To Other User In Team
**Product Name:** S.I.T.E

**Problem Statement:** S.I.T.E is a task manager where users can keep track of daily tasks: sorting the tasks by their priority, category and how long they will take.

**Use Case Name:** Assign Task to certain user collaborating on a task board

**Date:** April 6th, 2021

\## Summary

The user and collaborator on a task board can assign a task to be completed by any of the customers on the task board


\## Actors

1. the user
2. the collaborator
3. the assigned customer
4. the task board


\## Preconditions

\* The user must be signed in

\* There must be a collaborator on the task board

\* The task needs to exist 


\## Triggers

User selects "Assign Task" option


\## Primary Sequence

1. User or collaborator chooses a task that needs to be assigned
2. User or collaborator chooses who is the assigned customer
3. The task board verifies that the assigned customer is either the user or a collaborator on the task board
4. The task is marked that it is assigned to the assigned customer


\## Primary Postconditions

\* The task is marked as assigned to either the user or a collaborator, if that customer is indeed the user or a collaborator on the task board

**OR**

\* An error appears to customer trying to assign the task that the assigned customer does not exist on the task board


\## Non-functional Requirements

\* The task will show who is the assigned customer within 5 seconds 


\## Glossary

\* user = a person who wants to create a new task

\* collaborator = a person who can view and edit the task board of a user

\* assigned customer = either the user or collaborator that is assigned the task

\* task = an object that exists within the task board

\* task board = a system that maintains all of the tasks created by the user 
    
    
    5. Create Subtask
**Product Name:** S.I.T.E

**Problem Statement:** S.I.T.E is a task manager where users can keep track of daily tasks: sorting the tasks by their priority, category and how long they will take.

**Use Case Name:** Create Subtask

**Date:** April 6th, 2021

\## Summary

The user can add a subtask to an already created task 


\## Actors

1. the user
2. the task
3. the task board


\## Preconditions

\* The user must be signed in

\* The task must exist


\## Triggers

User selects "Create Subtask" option within a task


\## Primary Sequence

1. System prompts user to detail what the new subtask is
2. User adds in a string of what their subtask is
3. System verifies that this subtask does not already exist in task board
4. The new subtask is added to the task on the task board, if it doesn't already exist. Otherwise, error shows to user that the subtask is already in the task and nothing happens


\## Primary Postconditions

\* The subtask is shown on the task, if the subtask has not been created yet

**OR**

\* The task and task board remains the same, if the subtask has already been created


\## Non-functional Requirements

\* Task board can manage adding a new subtask, no matter how long the subtask is.


\## Glossary

\* user = a person who wants to create a new task

\* task = an object that exists within the task board

\* subtask = an object that exists within the task

\* task board = a system that maintains all of the tasks created by the user 
  
  
    6. Create task categories
**Product Name:** S.I.T.E

**Problem Statement:** SITE is a task manager where users can keep track of daily tasks: sorting the tasks by their priority, category and how long they will take.

**Use Case Name:** Create task categories

**Date:** 4/5/2021


\## Summary
	User can edit category functions when creating or editing tasks. The user can organize and view tasks of the same classification by using this category feature. If a user does not have the desired category, the user can create and classify the desired category.
	
	
\## Actors

\*User of this application


\## Preconditions

\*The user has logged in.

\*The task was created 


\## Triggers

Select category button or create new category button by user.


\## Primary Sequence

1. The user places the task in the desired category.


\## Primary Postconditions

1. The system categorizes tasks according to the categories that the user creates.
2. The user can view tasks by category.

\## Alternate Trigger

\*User selects the create new category button.


\## Alternate Sequences

\*If the user does not have the desired category, the user creates a new category.


\## Alternate Postconditions

\*A new category is created in the category list.


\## Non-functional Requirements

\*Users can create at least 5 categories.


\## Glossary

\*User = a person who want to classify the tasks

\*Category = division tasks that have shared characteristics by user.
    
    
    7. Giving priority to certain task
**Product Name:** S.I.T.E

**Problem Statement:** SITE is a task manager where users can keep track of daily tasks: sorting the tasks by their priority, category and how long they will take.

**Use Case Name:** Giving priority to certain task

**Date:** 4/5/2021


\## Summary
	Entering many tasks makes it difficult for users to determine which task to start with. In addition, users cannot perform multiple tasks at once. Therefore, users can prioritize tasks based on user criteria to perform important tasks first. The system first lists tasks with high priority according to user-defined priorities.
	
	
\## Actors

\*User of this application

\## Preconditions

\*The user has logged in.

\*The task was created.


\## Triggers

\*Select a number to set a priority for the user.


\## Primary Sequence

1. The user sets priority 1 to 5 (1 is highest priority)


\## Primary Postconditions

\*The system lists the tasks according to their priority highest to lowest.


\## Non-functional Requirements

\*System can manage having a priority for all tasks


\## Glossary

\*User = a person who wants to set priority for each tasks

\*Priority = The user sets the task to a higher priority if it is important by the user's criteria. 1 is highest priority and 5 is lowest priority.


    8. Change password
**Product Name:** S.I.T.E

**Problem Statement:** SITE is a task manager where users can keep track of daily tasks: sorting the tasks by their priority, category and how long they will take

**Use Case Name:** Change password

**Date:** 4/5/2021


\## Summary
Users can use this feature to change their passwords. This function is used when a user forgets a password or wants to change a new password.


\## Actors

\*User of this application


\## Preconditions

\*The user has already registered with this application server.


\## Triggers

\*Select the button to change the password by user.


\## Primary Sequence

1. The user presses the password change button.
2. The user writes the registered he/her email.
3. The system sends a link to the new password to the email you registered.
4. The link guides the user to a screen where the user can change a new password.
5. The user logs in using the new password.


\## Primary Postconditions

\*Users can log in using the new password they changed.

\*The new password is saved in the system


\## Alternate Sequences

1. Shows an error message when a user enters an email that is not registered on the server.
2. Users can register as new users.


\## Alternate Trigger

\*Select button to register new user by user.


\## Alternate Postconditions

\*Users are registered as new users on the server.


\## Non-functional Requirements

\*The system can manage any length password.


\## Glossary

\*User = a person who wants to change a new password.


    9. Register new user
**Product Name:** S.I.T.E

**Problem Statement:** SITE is a task manager where users can keep track of daily tasks: sorting the tasks by their priority, category and how long they will take.

**Use Case Name:** Register new user

**Date:** 4/5/2021


\## Summary
Users must log in to use this application. If you have never used this application, the user should register with the server as a new user. Users must register their names, emails, and passwords when registering as new users. 
	
	
\## Actors

\*New user


\## Preconditions

\*Users should never have used or registered this application.


\## Triggers

\*Select button to register new user by user.


\## Primary Sequence

1. The user presses the Register button to register as a new user.
2. The user registers their names, emails, and passwords.
3. The user presses the submit button.


\## Primary Postconditions

\*User's data is saved in the system


\## Alternate Sequences

1. If the user has already registered an email on the server, the error message displays to the user.
2. The system guides the user through the process of finding a password if the user forgot his/her password.


\### Alternate Trigger

\*Select the button to change the password by user.


\### Alternate Postconditions

\*Users can log in using the new password they changed.


\## Non-functional Requirements

\*The system can manage any length password

\## Glossary

\*New users = A person who has never used this application or has not registered with the server as a new user.


    10. Login user
**Product Name:** S.I.T.E

**Problem Statement:** SITE is a task manager where users can keep track of daily tasks: sorting the tasks by their priority, category and how long they will take.

**Use Case Name:** Login user

**Date:** 4/5/2021

\## Summary
Users must log in to use this application. By logging in, the application can retrieve information and history of users registered on the server. 


\## Actors

\*User of this application


\## Preconditions

\*The user must be registered with the application server.


\## Triggers

\*"Log in" is selected by user


\## Primary Sequence

1. The user clicks the login button.
2. Users enter their email and password and select the submit button.


\## Primary Postconditions

\*User can see their task list.


\## Alternate Sequences

1. The system displays error messages when the user input the wrong password or not registered email.
2. The user returns to the login page and enters the information again.
3. If the user does not remember the password, the user will be guided to “change password uscase”.
4. If the user have not registered, the user will be guided to “Register new user”


\### Alternate Trigger

\*“Change password” or “New register” is selected by user


\### Alternate Postconditions

\*Users can log in using the new password they changed.

\*If a user registers a new user, the user can use this application. The user can create a task list or be invited by someone else.


\## Non-functional Requirements

\*The system can manage any length password

\## Glossary

\*User = a person who want to use this application


    11. Log out user
**Product Name:** S.I.T.E

**Problem Statement:** S.I.T.E is a task manager where users can keep track of daily tasks: sorting the tasks by their priority, category and how long they will take.

**Use Case Name:** Log out user

**Date:** April 6th, 2021

\## Summary

The user can log out when done working in the task manager.
This also ensures no accidental changes happen that can cause the user the miss a task.

\## Actors

1. the user


\## Preconditions

\* User must be logged in before they can be logged out.

\* Changes must be saved before logging out


\## Triggers

"Log out" is selected by user


\## Primary Sequence

1. save tasks
2. Select trigger


\## Primary Postconditions

\* A message saying "You have successfully been logged out" is displayed


\## Non-functional Requirements
The only option in the task manager once logged out, is to log in.

\## Glossary

\* user = a person who wants to create a new task

\* task = an object that exists within the task board
    
    12. Edit tasks
**Product Name:** S.I.T.E

**Problem Statement:** S.I.T.E is a task manager where users can keep track of daily tasks: sorting the tasks by their priority, category and how long they will take.

**Use Case Name:** Edit tasks

**Date:** April 7th, 2021

\## Summary

The user can edit tasks if they find they miswrote something or if they realize their task is not what it initially was.

\## Actors

1. the user
2. the tasks


\## Preconditions

\* User must be logged in.

\* At least one task must be in the task manager


\## Triggers

"Edit" is selected

\## Primary Sequence

1. User chooses the task they want to edit
2. Select the trigger
3. Change the task
4. Save changes


\## Primary Postconditions

\* The tasks edits will be saved.


\## Non-functional Requirements
\*The system will save the edit of a task within 5 seconds

\## Glossary

\* user = a person who wants to create a new task

\* task = an object that exists within the task board


    13. Reminders
**Product Name:** S.I.T.E

**Problem Statement:** S.I.T.E is a task manager where users can keep track of daily tasks: sorting the tasks by their priority, category and how long they will take.

**Use Case Name:** Reminders

**Date:** April 6th, 2021

\## Summary

The user can receive notification at a specified time before tasks should be started or completed.


\## Actor

1. the user
2. the reminder


\## Preconditions

\* The user is logged in
\* At least one task must be saved in the task manager
\* Anticipated start and end time should be saved for the task
\* User must select an amount of time before when they should start or complete a task.


\## Triggers
\*User selects "Add notification"  


\## Primary Sequence

1. The user sets a reminder
3. The user is promted to add the minutes/hours before they want to be reminded 
4. The user selects when they want to be reminded
5. The user is promted to add if they want the reminder to be when they should start or complete the task
6. The user selects an option


\## Primary Postconditions

\* A reminder for the task is sent to the user


\## Non-functional Requirements
Task reminders are optional, tasks can be saved without a reminder.

\## Glossary

\* user = a person who wants to create a new task

\* task = an object that exists within the task board

    
    14. Plan for specific days
**Product Name:** S.I.T.E

**Problem Statement:** S.I.T.E is a task manager where users can keep track of daily tasks: sorting the tasks by their priority, category and how long they will take.

**Use Case Name:** Plan for specific days

**Date:** April 6th, 2021

\## Summary

The user can set tasks for days in the future using a built in calendar.

\## Actors

1. the user
2. the calendar


\## Preconditions

\* The user is logged in
\* At least one task must be saved in the task manager


\## Triggers

A date is selected for a task in the future through the calendar option.


\## Primary Sequence

1. Log in
2. Create a task or schedule an existing task for the future.


\## Primary Postconditions

\* The scheduled task will be saved for the selected date.


\## Non-functional Requirements
Selecting a date for a task is optional, tasks can be created without a scheduled date.

\## Glossary

\* user = a person who wants to create a new task

\* task = an object that exists within the task board
    
    
    15. Estimate and note time to complete tasks
**Product Name:** S.I.T.E

**Problem Statement:** S.I.T.E is a task manager where users can keep track of daily tasks: sorting the tasks by their priority, category and how long they will take.

**Use Case Name:** Estimate and note time to complete tasks

**Date:** April 6th, 2021

\## Summary

The user can set an estimated time it will take to complete a task.
This feature can help the user gauge how many tasks they can complete each day.

\## Actors

1. the user
2. the task manager


\## Preconditions

\* At least one task must be saved in the task manager
\* The user is logged in


\## Triggers

An estimated time to complete a task is entered and saved in the "timing" option.


\## Primary Sequence

1. User chooses the task they want to add a time to
2. User is prompted to add how long the task should take or when they want to complete it
3. User enters data

\## Primary Postconditions

\* The estimated time to complete the task will be saved and displayed next to the task on the task manager.


\## Non-functional Requirements
Entering an estimated time for a task is optional, tasks can be saved without an estimated time to complete.

\## Glossary

\* user = a person who wants to create a new task

\* task = an object that exists within the task board

UML Diagram: 
![uml use case (1)](https://user-images.githubusercontent.com/69373637/113936227-5881c200-97ac-11eb-9fe5-21c09cf7e8fd.jpg)


