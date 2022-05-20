from framework.page_controller import PageController
from framework.templates import render


class Homepage(PageController):
    def get(self, request, *args, **kwargs):
        return '200 OK', render('index.html')


class Contacts(PageController):
    def get(self, request, *args, **kwargs):
        return '200 OK', render('contacts.html', contacts='Yablokov Andrey (E-mail: AndrewYablokov@yandex.ru)')
