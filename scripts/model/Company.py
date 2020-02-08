from dataclasses import dataclass
from typing import List
import Document

# Tutorial https://realpython.com/python-data-classes/

@dataclass
class Company:
    docs: List[Document]