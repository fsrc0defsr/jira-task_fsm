from jira_task import task, states, transitions 
from transitions.extensions import GraphMachine
import graphviz




machine = GraphMachine(task, states=states, transitions=transitions, initial='open')

machine.get_graph().draw('jira_task_state_diagram.png', prog='/home/fsrcodefsr/Desktop/projects/.venv/lib/python3.10/site-packages/graphviz/dot.py')