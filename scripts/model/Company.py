from dataclasses import dataclass
from typing import List
import scripts.model.Document

# Tutorial https://realpython.com/python-data-classes/

@dataclass
class Company:
    docs: List[scripts.model.Document]