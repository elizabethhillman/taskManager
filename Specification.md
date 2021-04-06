Github URL: https://github.com/elizabethhillman/taskManager

Users: Elizabeth Hillman (elizabethhillman), Isabella Solis (isolis1210), Sungjea Kwak (Jaykkwak), Thien Tran (thientran1999)

Product Name: S.I.T.E

Non-Functional Requirements:

    1. The system will be able to manage at least 10 users
    2. The system will respond to each user input within 5 seconds
    3.

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
    
    4. Assign Task To Other User In Team
    
    5. Create Subtask
    
    6. Create task categories
		**Product Name: S.I.T.E
		**Problem Statement:**
		SITE is a task manager where users can keep track of daily tasks: sorting the tasks by their priority, category and how long they will take.
		**Use Case Name:**
		Create task categories
		**Date:**
		4/5/2021
		## Summary
		User can edit category functions when creating or editing tasks. The user can organize and view tasks of the same classification by using this category feature. If a user does not have the desired category, the user can create and classify the desired category.
		## Actors
		*User of this application
		## Preconditions
		*The user has logged in.
		*The task was created or be created.
		## Triggers
		Select category button or create new category button by user.
		## Primary Sequence
		1. User create or edit tasks.
		2. The user places the task in the category that the user wants.
		## Primary Postconditions
		1. The system categorizes tasks according to the categories that you create.
		2. The user can view tasks categorized by category.
		3. The systems are listed by priority when classifying them into categories.
		## Alternate Sequences
		*If the user does not have the desired category, the user creates a new category.
		### Alternate Trigger
		*Select the create new category button by user.
		### Alternate Postconditions
		*A new category is created in the category list.
		## Non-functional Requirements
		*Users can create up to 10 categories.
		## Glossary
		*User = a person who want to classify the tasks
		*Category = division tasks that have shared characteristics by user.
    
    7. Giving priority to certain task
    	**Product Name: S.I.T.E
		**Problem Statement:**
		SITE is a task manager where users can keep track of daily tasks: sorting the tasks by their priority, category and how long they will take.
		**Use Case Name:**
		Giving priority to certain task
		**Date:**
		 4/5/2021
		## Summary
		Entering many tasks makes it difficult for users to determine which task to start with. In addition, users cannot perform multiple tasks at once. Therefore, users can prioritize tasks based on user criteria to perform important tasks first. The system first lists tasks with high priority according to user-defined priorities.
		## Actors
		*User of this application
		## Preconditions
		*The user has logged in.
		*The task was created or be created.
		## Triggers
		*Select a number to set a priority for the user.
		## Primary Sequence
		1. The user creates or edits tasks.
		2. The user sets priority 1 to 5 (1 is highest priority)
		## Primary Postconditions
		*The system lists the tasks according to their priority highest to lowest.
		## Non-functional Requirements
		*Priority can only be adjusted by one of the users.
		## Glossary
		*User = a person who wants to set priority for each tasks
		*Priority = The user sets the task to a higher priority if it is important   by the user's criteria. 1 is highest priority and 5 is lowest priority.

    8. Change password
		**Product Name: S.I.T.E
		**Problem Statement:**
		SITE is a task manager where users can keep track of daily tasks: sorting the tasks by their priority, category and how long they will take
		**Use Case Name:**
		Change password
		**Date:**
		 4/5/2021
		## Summary
		Users can use this feature to change their passwords. This function is used when a user forgets a password or wants to change a new password.
		## Actors
		*User of this application
		## Preconditions
		*The user has already registered with this application server.
		## Triggers
		*Select the button to change the password by user.
		## Primary Sequence
		1. The user presses the password change button.
		2. The user writes the registered he/her email.
		3. The system sends a link to the new password to the email you registered.
		4. The link guides the user to a screen where the user can change a new password.
		5. The user logs in using the new password.
		## Primary Postconditions
		*Users can log in using the new password they changed.
		## Alternate Sequences
		1. Shows an error message when a user enters an email that is not registered on the server.
		2. Users can register as new users.
		### Alternate Trigger
		*Select button to register new user by user.
		### Alternate Postconditions
		*Users are registered as new users on the server.
		## Non-functional Requirements
		*The user must have at least 12 digits of the password.
		## Glossary
		*User = a person who wants to change a new password.

    9. Register new user
		**Product Name: S.I.T.E
		**Problem Statement:**
		SITE is a task manager where users can keep track of daily tasks: sorting the tasks by their priority, category and how long they will take.
		**Use Case Name:**
		Register new user
		**Date:**
		 4/5/2021
		## Summary
		Users must log in to use this application. If you have never used this application, the user should register with the server as a new user. Users must register their names, emails, and passwords when registering as new users. 
		## Actors
		*New user
		## Preconditions
		*Users should never have used or registered this application.
		## Triggers
		*Select button to register new user by user.
		## Primary Sequence
		1. The user presses the Register button to register as a new user.
		2. The user registers their names, emails, and passwords.
		3. The user presses the submit button.
		## Primary Postconditions
		*After registering a new user, the user can use this application. The user can create a task list or be invited by someone else.
		## Alternate Sequences
		1. If the user has already registered an email on the server, the error message displays to the user.
		2. The system guides the user through the process of finding a password if the user forgot his/her password.
		### Alternate Trigger
		*Select the button to change the password by user.
		### Alternate Postconditions
		*Users can log in using the new password they changed.
		## Non-functional Requirements
		*New users must have at least 12 digits of the password.
		## Glossary
		*New users = A person who has never used this application or has not registered with the server as a new user.

    10. Login user
		**Product Name: S.I.T.E
		**Problem Statement:**
		SITE is a task manager where users can keep track of daily tasks: sorting the tasks by their priority, category and how long they will take.
		**Use Case Name:**
		Login user
		**Date:**
		 4/5/2021
		## Summary
		Users must log in to use this application. By logging in, the application can retrieve information and history of users registered on the server. 
		## Actors
		*User of this application
		## Preconditions
		*The user must be registered with the application server.
		## Triggers
		*"Log in" is selected by user
		## Primary Sequence
		1. The user clicks the login button.
		2. Users enter their email and password and select the submit button.
		## Primary Postconditions
		*User can see their task list.
		## Alternate Sequences
		1. The system displays error messages when the user input the wrong password or not registered email.
		2. The user returns to the login page and enters the information again.
		3. If the user does not remember the password, the user will be guided to “change password uscase”.
		4. If the user have not registered, the user will be guided to “Register new user”
		### Alternate Trigger
		*“Change password” or “New register” is selected by user
		### Alternate Postconditions
		*Users can log in using the new password they changed.
		*If a user registers a new user, the user can use this application. The user can create a task list or be invited by someone else.
		## Non-functional Requirements
		## Glossary
		User = a person who want to use this application

    11. Log out user
    
    12. Reorder tasks
    
    13. Reminders
    
    14. Plan for specific days
    
    15. Estimate and note time to complete tasks

UML Diagram: 
![uml use case (2)](https://user-images.githubusercontent.com/69373637/113670946-91198280-966a-11eb-84f2-f0f51557b602.jpg)
