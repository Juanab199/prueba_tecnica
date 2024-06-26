from pydantic import BaseModel

class ResponseSch(BaseModel):
    status: str
    msg: str