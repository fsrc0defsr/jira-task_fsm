from enum import Enum

# init creating User entity

# init metaclass which implementating "singleton" pattern
class MetaSingleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
    
#init user's roles
class UserRoles(Enum):
    tester = 1
    developer = 2

# init UserStorage singleton class
class UserStorage(metaclass=MetaSingleton):
    def __init__(self):
        self._users = [{'id': 'v', 'name': 'Вася', 'role': UserRoles.developer},
                        {'id': 'p', 'name': 'Петя', 'role': UserRoles.developer},
                        {'id': 'm', 'name': 'Миша', 'role': UserRoles.developer},
                        {'id': 's', 'name': 'Саша', 'role': UserRoles.tester},
                        {'id': 'k', 'name': 'Катя', 'role': UserRoles.tester}
        ]

    def get_user_by_id(self, id):
        return next((item for item in self._users if item['id'] == id), None)

    def is_tester(self, id):
        user = self.get_user_by_id(id)
        if user:
            return user['role'] == UserRoles.tester
        return False

    def is_developer(self, id):
        user = self.get_user_by_id(id)
        if user:
            return user['role'] == UserRoles.developer
        return False