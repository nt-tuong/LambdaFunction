from sqlalchemy import (
    BigInteger,
    CheckConstraint,
    Column,
    DateTime,
    ForeignKey,
    SmallInteger,
    String,
    UUID,
    func,
)
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Organizations(Base):
    __tablename__ = "M_Organizations"

    id = Column("id", BigInteger, primary_key=True, autoincrement=True)
    uuid = Column("uuid", UUID(as_uuid=True), nullable=False, unique=True, server_default=func.gen_random_uuid())

    code = Column("code", String(50), nullable=False, unique=True)
    name = Column("name", String(255), nullable=False)
    description = Column("description", String(255), nullable=True)

    status = Column("status", SmallInteger, nullable=False, server_default="1")

    create_at = Column("createAt", DateTime(timezone=True), nullable=False, server_default=func.now())
    created_by = Column(
        "createdBy", BigInteger,
        ForeignKey("M_Users.id", use_alter=True, name="FK_M_Organizations_CreatedBy"),
        nullable=True,
    )
    updated_at = Column(
        "updatedAt", DateTime(timezone=True), nullable=False,
        server_default=func.now(), onupdate=func.now(),
    )
    updated_by = Column(
        "updatedBy", BigInteger,
        ForeignKey("M_Users.id", use_alter=True, name="FK_M_Organizations_UpdatedBy"),
        nullable=True,
    )

    __table_args__ = (
        CheckConstraint('"status" IN (0, 1)', name="CHK_M_Organizations_Status"),
    )

    def to_dict(self):
        return {
            "id": self.id,
            "uuid": str(self.uuid) if self.uuid else None,
            "code": self.code,
            "name": self.name,
            "description": self.description,
            "status": self.status,
        }
    