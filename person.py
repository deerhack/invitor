from typing import Optional
import pydantic


class Person(pydantic.BaseModel):
    uuid: Optional[str] = None
    first_name: str
    last_name: str
    email: str
    team: Optional[str]
