from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.types import Date

from .database import Base


class TaskStatusEnum(enum.Enum):
    not_started = 1
    in_progess = 2
    completed = 3
    cancelled = 4

class Task(Base):
    """DB model for a TODO list task"""

    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(60), nullable=False)
    description = Column(Text)
    due_date = Column(Date(), nullable=False)
    status = Column(Enum(TaskStatusEnum))
