from sqlalchemy import (
    BigInteger,
    Column,
    DateTime,
    ForeignKey,
    String,
    func,
)
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Role(Base):
    __tablename__ = "M_Roles"

    id = Column("id", BigInteger, primary_key=True, autoincrement=True)
    code = Column("code", String(50), nullable=False, unique=True)
    name = Column("name", String(255), nullable=False)
    description = Column("description", String(1000), nullable=True)

    create_at = Column("createAt", DateTime(timezone=True), nullable=False, server_default=func.now())
    created_by = Column(
        "createdBy", BigInteger,
        ForeignKey("M_Users.id", use_alter=True, name="FK_M_Roles_CreatedBy"),
        nullable=True,
    )
    updated_at = Column(
        "updatedAt", DateTime(timezone=True), nullable=False,
        server_default=func.now(), onupdate=func.now(),
    )
    updated_by = Column(
        "updatedBy", BigInteger,
        ForeignKey("M_Users.id", use_alter=True, name="FK_M_Roles_UpdatedBy"),
        nullable=True,
    )

    def to_dict(self):
        return {
            "id": self.id,
            "code": self.code,
            "name": self.name,
            "description": self.description,
        }