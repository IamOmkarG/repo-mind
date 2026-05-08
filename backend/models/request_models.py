from pydantic import BaseModel


class AskRequest(BaseModel):

    question: str

class IndexRequest(BaseModel):

    repo_url: str