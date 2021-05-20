**S.I.T.E**

**Introduction**

This task manager application allows a user to create an account and add tasks to their taskboard that can later be removed once the user completes that task. 

**Installation**

Once the repository is cloned on a users own computer, the website can then be accessed. Make sure that the following are installed:

     * Python v3.9.1
     * Flask
     * Celery 
     * Redis 

On your python shell, run the following command:

     * python3 run.py

After that, a website will be provided that can be copied and ran on any web browser. This will then bring you to S.I.T.E

**How to use S.I.T.E**

When you first open the website, first choose the sign in option and log in with the correct credentials. On this page, there is also a link to register as a new user. From there, you are brought to the dashboard that displays the instructions on how to use S.I.T.E. The "My Account" tab shows you your username and email, as well as an option to change your password. The "My Taskboard" tab brings you to see all of your tasks, as well as creating new ones, editing existing ones and removing completed tasks. Finally, the "Sign out" tab allows the user to sign out of their account and saves all of the tasks.

**Implemented Use Cases**

    1. Creating New task
        - To ensure this works, we tried creating multiple tasks to see if they appear. 
        In addition, we made sure that after we sign out and sign back in, that the tasks 
        are still visible.
   
    2. Remove Completed Task
       - To ensure this works, we tried removing existing tasks to make sure they 
       are no longer visible. 
 
    3. Edit Task
       - To ensure this works, after creating a task, we made sure that the task data 
       only shows the changes by the user. We tried logging out and coming signing back 
       in to make sure these changes are saved. We also implemented a 'Cancel' button 
       if the user wishes to no longer edit the task.  
  
    4. Register New User
       - To ensure this works, we created a new user with username "test" 
       and password "1234" and tried logging that account in. 

    5. Change Password
       - To ensure this works, we tried changing the password of an existing user 
       and then tried signing them in with the old password to make sure that one 
       did not work. We then tried logging them in with the new password to make 
       sure that would work.  
       
    6. Add Subtask
       - To ensure this works, we tried adding different subtasks for different tasks that
       are apart of the taskboard to make sure the subtask was only visible on the certain
       task. In addition, we ensured this works by adding multiple subtasks. 
       
    7. Add Estimate Time
       - To ensure this works, we tried adding different estimated times for each task to 
       verify that it is visible for each task.
       
    8. Create Test Categories
       - To ensure this works, we tried creating a multitude of categories in order to verify
       that each task would display the category that they are assigned to. In addition, we allowed 
       the user to organize the tasks by category and we verified that worked by choosing one
       category and making sure that every task assigned that category is visible.
       
    9. Give Task Priority
       - To ensure this works, we assigned tasks different priorities to make sure that they will be 
       visible in order of priority (priority 1 being the highest). In addition, after the tasks were 
       organized by category, we ensured that the user could still reorganize the tasks by their
       priority. 
       
    10. Invite Other User
        - To ensure this works, we created another user -test2- that we added as a collaborator on our 
        first user -test's- taskboard. We ensured that the collaborated tasks can be seen under 
        "Collaborate Task" and the personal tasks remain hidden from the collaborating user. 
        
    11. Assign Task to User
        - To ensure this works, we assigned a collaborating task to the user -test- and ensured the task 
        was seen under "collaborate task" on the "my taskboard" page. We also tested that only usernames 
        of collaborating user can be assigned a task. The collaborating user can still see collaborating 
        tasks that are not assigned to them.
        
    12. Reminder for Task
        - To ensure this works, we have set the reminder on the task in "taskboard". Also, we set the 
        timer for reminder to send mail to user on the time and date that had been set. After, we set 
        reminder it will redirect to "taskboard" when it done with set the reminder.
        
    13. Plan for Specific Day
        - To ensure this works, after navigating to the calendar, we added events for specific days and 
        checked that the events appeared on the assigned dates.
        
    14. Log in
        - To ensure this works, after registering a new user, we made sure that the user could view
        their task board by logging in with their credentials. 
        
    15. Log out 
        - To ensure this works, we made sure that after selecting the "Sign out" button, the user
        could no longer view their taskboard. 
