from datetime import datetime
from uuid import uuid4

from pydantic import BaseModel, Field


class MemoryItem(BaseModel):

    id: str = Field(default_factory=lambda: str(uuid4()))

    content: str

    importance: float = 0.5

    created_at: datetime = Field(default_factory=datetime.utcnow)

    updated_at: datetime = Field(default_factory=datetime.utcnow)

    source: str = "conversation"

    metadata: dict = Field(default_factory=dict)



class LongMemory(BaseModel):

    memories: list[MemoryItem] = Field(default_factory=list)