from framework.front_controller import FrontController


class UserFrontController(FrontController):
    def autorization(self, request):
        print('User authorization is complete')
        return request


front_controller = UserFrontController()

front_controllers = [
    front_controller.logging,
    front_controller.autorization,
]
