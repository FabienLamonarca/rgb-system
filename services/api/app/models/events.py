from pydantic import BaseModel, Field


class rgbEvent(BaseModel):
    color: str = Field(
        title="The color of the event",
        regex= "^red|green|blue$"
    )
    count: int = Field(
        title="The number of event to send",
        ge=0,
        lt=10000
    )
