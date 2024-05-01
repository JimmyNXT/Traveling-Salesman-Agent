from enum import Enum
 
class LogLevel(Enum):
    DEBUG = 0
    INFORMATION = 1
    WARNING = 2
    ERROR = 3

class Logger:
    def __init__(self, name:str, enabled:bool = True) -> None:
        self.name = name
        self.enabled = enabled
    
    def log(self, msg:str, level:LogLevel = LogLevel.INFORMATION) -> None:
        if self.enabled:
            print(self.name + ":\t" + msg)