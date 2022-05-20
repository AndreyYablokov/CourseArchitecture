from framework.data_classes import Routes
from page_controllers import Homepage, Contacts

routes = [
    Routes('/', Homepage),
    Routes('/contacts', Contacts),
]
