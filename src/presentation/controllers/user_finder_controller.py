from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.use_cases.user_finder import UserFinder as UserFinderInterface
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse

class UserFinderController(ControllerInterface):
    def __init__(self, user_finder: UserFinderInterface):
        self.__use_case = user_finder

    def handle(self, request: HttpRequest) -> HttpResponse:
        first_name = request.query_params.get('first_name')

        response = self.__use_case.find(first_name)

        return HttpResponse(
            status_code=200,
            body={"data": response}
        )
