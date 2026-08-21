from sqlalchemy import (
    BigInteger,
    CheckConstraint,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    SmallInteger,
    String,
    UUID,
    func,
)
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Persons(Base):
    __tablename__ = "M_Persons"

    id = Column("id", BigInteger, primary_key=True, autoincrement=True)
    uuid = Column("uuid", UUID(as_uuid=True), nullable=False, unique=True, server_default=func.gen_random_uuid())

    name = Column("name", String(255), nullable=False)
    full_name = Column("fullName", String(255), nullable=False)

    # Format YYYYMMDD (vd 19991231) - la INTEGER, khong phai DATE, dung theo business design
    birth_date = Column("birthDate", Integer, nullable=False)

    gender = Column("gender", SmallInteger, nullable=False, server_default="0")

    citizen_identity_card = Column("citizenIdentityCard", String(12), nullable=False, index=True)
    phone_number = Column("phoneNumber", String(20), nullable=False, index=True)
    email = Column("email", String(255), nullable=False, index=True)

    address = Column("address", String(255), nullable=False)
    city = Column("city", String(255), nullable=True)
    state = Column("state", String(255), nullable=True)
    country = Column("country", String(255), nullable=True)
    postal_code = Column("postalCode", String(20), nullable=True)

    create_at = Column("createAt", DateTime(timezone=True), nullable=False, server_default=func.now())
    created_by = Column(
        "createdBy", BigInteger,
        ForeignKey("M_Users.id", use_alter=True, name="FK_M_Persons_CreatedBy"),
        nullable=True,
    )
    updated_at = Column(
        "updatedAt", DateTime(timezone=True), nullable=False,
        server_default=func.now(), onupdate=func.now(),
    )
    updated_by = Column(
        "updatedBy", BigInteger,
        ForeignKey("M_Users.id", use_alter=True, name="FK_M_Persons_UpdatedBy"),
        nullable=True,
    )

    __table_args__ = (
        CheckConstraint('"gender" IN (0, 1)', name="CHK_M_Persons_Gender"),
        CheckConstraint(
            '"birthDate" BETWEEN 19000101 AND 29991231',
            name="CHK_M_Persons_BirthDate",
        ),
    )

    def to_dict(self):
        return {
            "id": self.id,
            "uuid": str(self.uuid) if self.uuid else None,
            "name": self.name,
            "fullName": self.full_name,
            "birthDate": self.birth_date,
            "gender": self.gender,
            "email": self.email,
            "phoneNumber": self.phone_number,
        }