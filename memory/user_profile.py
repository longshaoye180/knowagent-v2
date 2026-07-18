from typing import List

from pydantic import BaseModel, ConfigDict, Field


class UserProfile(BaseModel):

    model_config = ConfigDict(
        extra="forbid"
    )

    name: str | None = None
    age: int | None = None
    gender: str | None = None
    job: str | None = None
    hobbies: List[str] = Field(default_factory=list)