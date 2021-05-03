**S.I.T.E**

**Introduction**
This task manager application allows a user to create an account and add tasks to their taskboard that can later be removed once the user completes that task. 

**Installation**
Once the repository is cloned on a users own computer, the website can then be accessed. Make sure that the following are installed:
     * Python v3.9.1
     * Flask

On your python shell, run the following command:
     * python3 run.py

After that, a website will be provided that can be copied and ran on any web browser. This will then bring you to S.I.T.E

**How to use S.I.T.E**
When you first open the website, first choose the sign in option and log in with the correct credentials. On this page, there is also a link to register as a new user. From there, you are brought to the dashboard that displays the instructions on how to use S.I.T.E. The "My Account" tab shows you your username and password, as well as an option to change your password. The "My Taskboard" tab brings you to see all of your tasks, as well as creating new ones, editing existing ones and removing completed tasks. Finally, the "Sign out" tab allows the user to sign out of their account and saves all of the tasks.

**Implemented Use Cases**
1. Creating New task
   - To ensure this works, we tried creating multiple tasks to see if they appear. In addition, we made sure that after we sign out and sign back in, that the tasks are still visible.
   
2. Remove Completed Task
   - To ensure this works, we tried removing existing tasks to make sure they are no longer visible. 
 
3. Edit Task
   - To ensure this works, after creating a task, we made sure that the task data only shows the changes by the user. We tried logging out and coming signing back in to make sure these changes are saved. We also implemented a 'Cancel' button if the user wishes to no longer edit the task.  
  
4. Register New User
   - To ensure this works, we created a new user with username "test" and password "1234" and tried logging that account in. 

5. Change Password
   - To ensure this works, we tried changing the password of an existing user and then tried signing them in with the old password to make sure that one did not work. We then tried logging them in with the new password to make sure that would work.  
