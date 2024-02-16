from typing import Dict

class UserFinderSpy:
    def __init__(self) -> None:
        self.find_params = {}

    def find(self, first_name: str) -> Dict:
        self.find_params['first_name'] = first_name

        return {
            "type": "Users",
            "count": 1,
            "attributes": [
                { "first_name": first_name, "last_name": "Doe" },
            ]
        }
