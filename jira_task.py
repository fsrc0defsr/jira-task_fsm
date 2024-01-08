from transitions import Machine, MachineError
from user import UserStorage

import logging
logging.basicConfig(level=logging.DEBUG)

class JiraTaskWorkFlow:
    def __init__(self):
        self._user_id = 's'

    # checks if the user is tester
    def is_tester(self):
        return UserStorage().is_tester(self._user_id)

    # checks if the user is developer
    def is_developer(self):
        return UserStorage().is_developer(self._user_id)


task = JiraTaskWorkFlow()

# init states and transitions
states = ['open', 'closed', 'resolved', 'inprogress', 'reopened']

transitions = [
    {'trigger': 'start_progress', 'source': 'open', 'dest': 'inprogress'},
    {'trigger': 'resolve_and_close', 'source': 'inprogress', 'dest': 'closed', 'conditions':['is_tester']},
    {'trigger': 'stop_progress', 'source': 'inprogress', 'dest': 'open'},
    {'trigger': 'resolve', 'source': 'inprogress', 'dest': 'resolved'},
    {'trigger': 'resolve_and_close', 'source': 'open', 'dest': 'closed', 'conditions':['is_tester']},
    {'trigger': 'close', 'source': 'resolved', 'dest': 'closed', 'conditions':['is_tester']},
    {'trigger': 'reopen', 'source': 'closed', 'dest': 'reopened'},
    {'trigger': 'resolve', 'source': 'reopened', 'dest': 'resolved'},
    {'trigger': 'resolve_and_close', 'source': 'reopened', 'dest': 'closed', 'conditions':['is_tester']},
    {'trigger': 'start_progress', 'source': 'reopened', 'dest': 'inprogress'}
]

# init fsm and bind it
machine = Machine(task, states=states, transitions=transitions, initial='open')

# testing
logging.getLogger('transitions').setLevel(logging.DEBUG)

try:
    if not task.start_progress():
        print('conditions_fail')
    else:
        print(task.state)

    if not task.resolve():
        print('conditions_fail')
    else:
        print(task.state)

    if not task.close():
        print('conditions_fail')
    else:
        print(task.state)

    if not task.reopen():
        print('conditions_fail')
    else:
        print(task.state)

    if not task.start_progress():
        print('conditions_fail')
    else:
        print(task.state)

    if not task.resolve_and_close():
        print('conditions_fail')
    else:
        print(task.state)

    if not task.reopen():
        print('conditions_fail')
    else:
        print(task.state)

    if not task.start_progress():
        print('conditions_fail')
    else:
        print(task.state)

    if not task.stop_progress():
        print('conditions_fail')
    else:
        print(task.state)

    if not task.start_progress():
        print('conditions_fail')
    else:
        print(task.state)

    if not task.reopen():
        print('conditions_fail')
    else:
        print(task.state)


except MachineError as error:
    print(error)