# Expose the db module functions
from .llm import LocalLLM

from .db import (
    init_db,
    get_tickets,
    create_ticket,
    delete_ticket
)

__all__ = [
    'init_db',
    'get_tickets',
    'create_ticket',
    'delete_ticket',
    'LocalLLM'
]

