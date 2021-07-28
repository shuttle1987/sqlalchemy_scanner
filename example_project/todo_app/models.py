import enum

from sqlalchemy import Column, Integer, String, Text, Enum
from sqlalchemy.types import Date

from .database import Base

class DictMixIn:
    """Convenience mixin for creating a JSON representation for a SQL row result
    where that row is defined by a SQLAlchemy model"""
    def to_dict(self) -> dict:
        return {
            column.name: getattr(self, column.name)
            if not isinstance(
                getattr(self, column.name), (datetime.datetime, datetime.date)
            )
            else getattr(self, column.name).isoformat()
            for column in self.__table__.columns
        }

class TaskStatusEnum(enum.Enum):
    not_started = 1
    in_progress = 2
    completed = 3
    cancelled = 4


def string_to_taskstatusenum(s: str) -> TaskStatusEnum:
    res = TaskStatusEnum[s.lower().replace(' ','_')]
    return res


class Task(Base, DictMixIn):
    """DB model for a TODO list task"""

    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(60), nullable=False)
    description = Column(Text)
    due_date = Column(Date(), nullable=False)
    status = Column(Enum(TaskStatusEnum))
