- Finite state machine (fsm)

- Workflow — "Task" life cycle in Jira

- Transition condition logic:
    1. Create the “User” entity in the form of a dictionary with attributes: identifier, name, role;
    2. Create a registry of users "UserStorage" registered in Jira;
    3. Allow/disallow a number of transitions depending on the role of the user responsible for the task.


- Using the graphviz Python package (also, graphviz need install locally "sudo apt install graphviz") was generated a box visualization of the programmed fsm 

- Added uploading state machine to file on JSON format and, accordingly loading state machine from JSON format file