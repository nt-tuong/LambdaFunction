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
from sqlalchemy.orm import declarative_base, relationship
from database.tables.organizations import Organizations
from database.tables.role import Role
from database.tables.persons import Persons


Base = declarative_base()


class Users(Base):
    __tablename__ = "M_Users"

    id = Column("id", BigInteger, primary_key=True, autoincrement=True)
    uuid = Column("uuid", UUID(as_uuid=True), nullable=False, unique=True, server_default=func.gen_random_uuid())

    code = Column("code", String(50), nullable=False, unique=True)

    organization_id = Column(
        "organizationId", BigInteger,
        ForeignKey("M_Organizations.id", name="FK_M_Users_Organization"),
        nullable=False, index=True,
    )
    role_id = Column(
        "roleId", BigInteger,
        ForeignKey("M_Roles.id", name="FK_M_Users_Role"),
        nullable=False, index=True,
    )
    person_id = Column(
        "personId", BigInteger,
        ForeignKey("M_Persons.id", name="FK_M_Users_Person"),
        nullable=False, index=True,
    )

    user_name = Column("userName", String(255), nullable=False, unique=True)
    password = Column("password", String(255), nullable=False)  # hash bcrypt/argon2, khong luu plaintext

    status = Column("status", SmallInteger, nullable=False, server_default="1", index=True)

    create_at = Column("createAt", DateTime(timezone=True), nullable=False, server_default=func.now())
    created_by = Column(
        "createdBy", BigInteger,
        # Self-referencing FK: dung use_alter de tranh loi circular khi create_all()
        ForeignKey("M_Users.id", use_alter=True, name="FK_M_Users_CreatedBy"),
        nullable=True,
    )
    updated_at = Column(
        "updatedAt", DateTime(timezone=True), nullable=False,
        server_default=func.now(), onupdate=func.now(),
    )
    updated_by = Column(
        "updatedBy", BigInteger,
        ForeignKey("M_Users.id", use_alter=True, name="FK_M_Users_UpdatedBy"),
        nullable=True,
    )

    __table_args__ = (
        CheckConstraint('"status" IN (0, 1)', name="CHK_M_Users_Status"),
    )

    # # Quan he - dung foreign_keys=[...] vi co nhieu FK cung tro ve M_Users.id
    # organization = relationship("Organizations", foreign_keys=[organization_id])
    # role = relationship("Role", foreign_keys=[role_id])
    # person = relationship("Persons", foreign_keys=[person_id])

    def to_dict(self):
        return {
            "id": self.id,
            "uuid": str(self.uuid) if self.uuid else None,
            "code": self.code,
            "organizationId": self.organization_id,
            "roleId": self.role_id,
            "personId": self.person_id,
            "userName": self.user_name,
            "status": self.status,
            "createAt": self.create_at.isoformat() if self.create_at else None,
            "createdBy": self.created_by,
            "updatedAt": self.updated_at.isoformat() if self.updated_at else None,
            "updatedBy": self.updated_by,
        }

