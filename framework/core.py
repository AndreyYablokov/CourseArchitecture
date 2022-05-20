from framework.io_classes import Request
from framework.page_controller import PageNotFoundController


class Framework:
    def __init__(self, routes, front_controllers):
        self.routes = routes
        self.front_controllers = front_controllers

    def __call__(self, environ, start_response):
        """
        :param environ: словарь данных от сервера
        :param start_response: функция для ответа серверу
        """

        request = Request(environ)
        # front controllers
        for front_controller in self.front_controllers:
            request = front_controller(request)
        # page controllers
        page_controller = self._get_page_controller(request)
        code, body = self._get_response(request, page_controller)
        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]

    def _get_page_controller(self, request):
        search_route = request.route
        for route in self.routes:
            if route.route == search_route or f'{route.route}/' == search_route:
                return route.page_controller

        return PageNotFoundController

    def _get_response(self, request, page_controller):
        if hasattr(page_controller, request.method):
            return getattr(page_controller, request.method)(page_controller, request)
        else:
            return 'Method not realised'


