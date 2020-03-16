from dataclasses import dataclass

# Tutorial https://realpython.com/python-data-classes/

@dataclass
class Document:
    filename: str
    text: str