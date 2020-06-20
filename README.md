# customersupport
This is the Agent Selector problem's solution.
I would suggest to check out the live version of the project at: https://cstsupport.herokuapp.com/ if you want to navigate to admin page just append "/admin/" at the end of the main URL and use "admin" as both username and password for login.

Users can create new issues and they will be assigned to the appropriate agents.

The algorithm assigning the agents is inside pages/algorithms.py,it is a function that takes issue as an argument and returns the agent selected for the task(selected on the basis of selection_modes).

1.Create Issues:
  User can create issues from the form in the left.
  
2.Complete assignments:
  Once completed the assignments can be deleted using the delete button and the agents will be set to available.

