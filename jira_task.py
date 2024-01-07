from transitions import Machine, MachineError
from transitions.extensions import GraphMachine
import graphviz

class JiraTaskWorkFlow:
    pass

task = JiraTaskWorkFlow()

# init states and transitions
states = ['open', 'closed', 'resolved', 'inprogress', 'reopened']

transitions = [
    {'trigger': 'start_progress', 'source': 'open', 'dest': 'inprogress'},
    {'trigger': 'resolve_and_close', 'source': 'inprogress', 'dest': 'closed'},
    {'trigger': 'stop_progress', 'source': 'inprogress', 'dest': 'open'},
    {'trigger': 'resolve', 'source': 'inprogress', 'dest': 'resolved'},
    {'trigger': 'resolve_and_close', 'source': 'open', 'dest': 'closed'},
    {'trigger': 'close', 'source': 'resolved', 'dest': 'closed'},
    {'trigger': 'reopen', 'source': 'closed', 'dest': 'reopened'},
    {'trigger': 'resolve', 'source': 'reopened', 'dest': 'resolved'},
    {'trigger': 'resolve_and_close', 'source': 'reopened', 'dest': 'closed'},
    {'trigger': 'start_progress', 'source': 'reopened', 'dest': 'inprogress'}
]

# init fsm and bind it
machine = Machine(task, states=states, transitions=transitions, initial='open')

# testing
try:
    task.start_progress()
    print(task.state)

    task.resolve()
    print(task.state)

    task.close()
    print(task.state)

    task.reopen()
    print(task.state)

    task.start_progress()
    print(task.state)

    task.resolve_and_close()
    print(task.state)

    task.reopen()
    print(task.state)

    task.start_progress()
    print(task.state)

    task.stop_progress()
    print(task.state)

    task.start_progress()
    print(task.state)

    task.reopen()
    print(task.state)


except MachineError as error:
    print(error)