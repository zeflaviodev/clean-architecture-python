from typing import Dict

class UserRegisterSpy:
    def __init__(self) -> None:
        self.register_params = {}

    def register(self, first_name: str, last_name: str, age: int) -> Dict:
        self.register_params['first_name'] = first_name
        self.register_params['last_name'] = last_name
        self.register_params['age'] = age

        return {
            "type": 'Users',
            'count': 1,
            'attributes': {
                "first_name": first_name,
                "last_name": last_name,
                "age": age
            }
        }
