from typing import NoReturn
from decouple import config

class Settings:
    
    def __init__(self) -> NoReturn:
        print(config.__dict__)