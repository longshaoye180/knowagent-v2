from openai import BaseModel
from pydantic import ConfigDict


class WeatherResult(BaseModel):

    model_config = ConfigDict(
        extra="forbid",
    )

    city: str

    weather: str

    temperature: str

    user: str