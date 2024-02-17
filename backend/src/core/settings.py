from functools import cache
from typing import NoReturn as _NoReturn
from decouple import config as _config
from src.constant.envs import ENV_LIST

class _Settings:
    
    def __init__(self) -> _NoReturn:
        self.__set_variables(*ENV_LIST)
        
    def __set_variables(self, *args):
        for arg in args:
            setattr(self, arg[0], _config(arg[0], default=arg[1]))
            
    def get_db_url(self):
        if self.DB_TYPE == "pgsql":
            yield f"postgresql://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/"
        elif self.DB_TYPE == "mysql":
            yield f"mysql://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/"
        elif self.DB_TYPE == "sqlite":
            yield f"sqlite:///{self.DB_USER}.db"
        elif self.DB_TYPE == "mssql":
            yield f"mssql+pyodbc://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/"
        elif self.DB_TYPE == "oracle":
            yield f"oracle://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/"
        else:
            raise ValueError("Unsupported database type")
            

@cache
def load_settings()->_Settings:
    return _Settings()
