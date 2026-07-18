from pydantic import BaseModel, Field


class UserPreference(BaseModel):

    language: str | None = Field(default=None, description="回答语言")

    response_style: str | None = Field(
        default=None,
        description="回答风格"
    )

    code_style: str | None = Field(
        default=None,
        description="代码输出风格"
    )