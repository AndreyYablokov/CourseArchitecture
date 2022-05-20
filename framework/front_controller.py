from datetime import datetime


class FrontController:

    def logging(self, request):
        print(f'[{datetime.now()}] [INFO] Call url: {request.route}')
        return request
