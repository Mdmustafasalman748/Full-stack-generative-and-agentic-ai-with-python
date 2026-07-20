from typing import Optional, List
from pydantic import BaseModel

class Comment(BaseModel):
    id: int
    content:str
    replies:Optional[List["Comment"]]=None
    
Comment.model_rebuild()
comment=Comment(
    id=1,
    content="First comment",
    replies=[
        Comment(id=2, content="First reply"),
        Comment(id=3, content="Second reply",replies=[
                Comment(id=4, content="nestedy")
    ])
]
)