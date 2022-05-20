class Request:
    def __init__(self, environ):
        self.method = environ['REQUEST_METHOD'].lower()
        self.route = environ['PATH_INFO']
        self.query_params = self._get_query_params(environ)
        self.headers = self._get_headers(environ)

    @staticmethod
    def _get_headers(environ):
        headers = {}
        for key, value in environ.items():
            if key.startswith('HTTP'):
                headers[key[5:]] = value

        return headers

    @staticmethod
    def _get_query_params(environ):
        query_params = {}
        elements = environ['QUERY_STRING'].split('&')
        for element in elements:
            if element:
                key, value = element.split('=')
                if query_params.get(key):
                    query_params[key].append(value)
                else:
                    query_params[key] = [value]

        return query_params


class Response:
    pass
