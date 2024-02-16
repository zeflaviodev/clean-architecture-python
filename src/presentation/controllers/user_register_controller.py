from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.use_cases.user_register import UserRegister as UserRegisterInterface
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse

class UserRegisterController(ControllerInterface):
    def __init__(self, user_finder: UserRegisterInterface):
        self.__use_case = user_finder

    def handle(self, request: HttpRequest) -> HttpResponse:
        first_name = request.body["first_name"]
        last_name = request.body["last_name"]
        age = request.body["age"]

        response = self.__use_case.register(first_name, last_name, age)

        return HttpResponse(
            status_code=200,
            body={"data": response}
        )
