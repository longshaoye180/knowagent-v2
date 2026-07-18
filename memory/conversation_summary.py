from pydantic import Field, BaseModel


class ConversationSummary(BaseModel):

    summary: str | None = Field(default=None, description="当前会话摘要")