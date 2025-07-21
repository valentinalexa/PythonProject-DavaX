from pydantic import BaseModel
from typing import Optional, Literal, Union


class PowRequest(BaseModel):
    x: float
    y: float

class FibonacciRequest(BaseModel):
    n: int

class FactorialRequest(BaseModel):
    n: int

class OperationResult(BaseModel):
    result: Union[int, float]


# Folosit eventual pentru salvare sau log
class OperationRecord(BaseModel):
    operation: Literal["pow", "fibonacci", "factorial"]
    input_1: float
    input_2: Optional[float] = None
    result: float
    timestamp: str