from jira_task import task, states, transitions 
from transitions.extensions import GraphMachine
import graphviz


machine = GraphMachine(task, states=states, transitions=transitions, initial='open')

machine.get_graph().draw('jira_task_fsm_visualization.png', prog='dot')