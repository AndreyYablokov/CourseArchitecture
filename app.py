from framework.core import Framework
from routes import routes
from front_controllers import front_controllers


app = Framework(routes, front_controllers)
