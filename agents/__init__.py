# agents/__init__.py
from .business_analyst import BusinessAnalyst
from .designer import Designer
from .developer import Developer
from .tester import Tester  # <-- Correct import

__all__ = [
    'BusinessAnalyst',
    'Designer',
    'Developer',
    'Tester'  # <-- Make sure to include
]