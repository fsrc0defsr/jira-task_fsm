from transitions import Machine, MachineError
from user import UserStorage

import json

# import logging
# logging.basicConfig(level=logging.DEBUG)

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
machine = Machine(model=task, states=states, transitions=transitions, initial='open')

# testing
#logging.getLogger('transitions').setLevel(logging.DEBUG)

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

  # Выгрузка состояний и переходов в JSON
  # Форируется словарь 'machine_data', который представляет собой конфигурацию конечного автомата (информацию о состояниях и переходах)      
    machine_data = {'states': states,
                    'transitions': [{'trigger': transition['trigger'],
                                     'source': transition['source'],
                                     'dest': transition['dest'],
                                     'conditions': transition.get('conditions', [None])[0]} # Если условие не указано (get('conditions', [None])), то присваивается значение [None], и затем берется первый элемент из этого списка [None][0].
                                    for transition in transitions]}
    
    with open('state_machine.json', 'w') as json_file:
        json.dump(machine_data, json_file, indent=2)

    # Загрузка состояний и переходов из JSON
    with open('state_machine.json', 'r') as json_file:
        loaded_data = json.load(json_file)

    # Создание нового объекта state machine на основе загруженных данных
    loaded_machine = Machine(model=task, states=loaded_data['states'],
                             transitions=loaded_data['transitions'], initial='open')
    

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