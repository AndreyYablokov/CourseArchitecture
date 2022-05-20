class PageController:
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass

    def put(self, request, *args, **kwargs):
        pass

    def patch(self, request, *args, **kwargs):
        pass

    def delete(self, request, *args, **kwargs):
        pass


class PageNotFoundController(PageController):
    def get(self, request, *args, **kwargs):
        return '404 Page not found', '404 Page not found'
