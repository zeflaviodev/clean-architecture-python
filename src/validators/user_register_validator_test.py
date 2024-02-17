from .user_register_validator import user_register_validator

class MockRequest:
    def __init__(self) -> None:
        self.json = None

def test_user_register_validator():
    mock_request = MockRequest()
    mock_request.json = {
        "first_name": "John",
        "last_name": "Doe",
        "age": 12
    }

    user_register_validator(mock_request)
