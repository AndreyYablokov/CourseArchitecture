from dataclasses import dataclass
from typing import Type

from framework.page_controller import PageController


@dataclass
class Routes:
    route: str
    page_controller: Type[PageController]
