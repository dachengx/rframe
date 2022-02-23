
import datetime
import pandas as pd
from typing import Generic, Mapping, TypeVar
from numpy import isin

from pydantic import BaseModel, ValidationError

LabelType = TypeVar('LabelType', int, str, datetime.datetime)


class Interval(BaseModel):
    left: LabelType
    right: LabelType = None

    @classmethod
    def __get_validators__(cls):
        yield cls.validate_field

    @classmethod
    def validate_field(cls, v, field):
        
        if isinstance(v, tuple):
            left, right = v
        elif isinstance(v, Mapping):
            left = v.get('left', None)
            right = v.get('right', None)
        elif isinstance(v, (pd.Interval, Interval)):
            left = v.left
            right = v.right
        else:
            left, right = v, v
        
        if right is not None and left>right:
            left, right = right, left
        return cls(left=left, right=right)

    def __class_getitem__(cls, type_):
        if issubclass(type_, int):
            return IntegerInterval
        if issubclass(type_, datetime.datetime):
            return TimeInterval
        raise TypeError(type_)
        
class IntegerInterval(Interval):
    left: int
    right: int = None
    
class TimeInterval(Interval):
    left: datetime.datetime
    right: datetime.datetime = None