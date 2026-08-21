from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, ConfigDict


class UserDto(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    uuid: UUID
    code: str
    organizationId: int
    roleId: int
    personId: int
    userName: str
    status: int
    createAt: datetime
    createdBy: int
    updatedAt: datetime
    updatedBy: int
