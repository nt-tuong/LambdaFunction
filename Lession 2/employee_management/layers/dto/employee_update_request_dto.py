from pydantic import (
BaseModel,
Field,
field_validator,
ValidationInfo
)

from dto.validator import (
    Required,
    NotNone,
    NotBlank,
    MinLength,
    MaxLength,
    Pattern,
)

from utils.constants import EMAIL_REGEX, UUID_PATTERN


class EmployeeUpdateRequestDto(BaseModel):
    employee_uuid: str = Field(description="Employee UUID")
    name: str = Field(description="Employee name")
    full_name: str  = Field(description="Employee full name")
    birth_date: int  = Field(description="birth date")
    gender: int  = Field(description="gender")
    citizen_identity_card: str  = Field(description="citizen identity card")
    phone_number: str  = Field(description="phone number")
    email: str  = Field(description="email")
    address: str  = Field(description="address")
    city: str  = Field(description="city")
    state: str  = Field(description="state")
    country: str  = Field(description="country")
    postal_code: str  = Field(description="postal code")


    @field_validator("employee_uuid")
    @classmethod
    @Required
    @NotNone
    @NotBlank
    @Pattern(UUID_PATTERN)
    def employee_uuid_validate(cls, value, info: ValidationInfo):
        return value


    @field_validator("name")
    @classmethod
    @Required
    @NotNone
    @NotBlank
    def name_validate(cls, value, info: ValidationInfo):
        return value


    @field_validator("full_name")
    @classmethod
    @Required
    @NotNone
    def full_name_validate(cls, value, info: ValidationInfo):
        return value


    @field_validator("birth_date")
    @classmethod
    @Required
    @NotNone
    @NotBlank
    def birth_date_validate(cls, value, info: ValidationInfo):
        if value < 0:
            raise ValueError("Birth date must be a positive integer!")
        
        if value > 99991231:
            raise ValueError("Birth date must be less than or equal to 99991231!")

        if value < 19000101:
            raise ValueError("Birth date must be greater than or equal to 19000101!")
        
        return value


    @field_validator("gender")
    @classmethod
    def gender_validate(cls, value, info: ValidationInfo):
        if value is not None and value not in [0, 1]:
            raise ValueError("Gender must be either 0 (male) or 1 (female).")
        return value


    @field_validator("citizen_identity_card")
    @classmethod
    @Required
    @NotNone
    @NotBlank
    def citizen_identity_card_validate(cls, value, info: ValidationInfo):
        return value


    @field_validator("phone_number")
    @classmethod
    @Required
    @NotNone
    @NotBlank
    @MinLength(10)
    @MaxLength(11)
    def phone_number_validate(cls, value, info: ValidationInfo):
        return value


    @field_validator("email")
    @classmethod
    @Required
    @NotNone
    @NotBlank
    @MaxLength(100)
    @Pattern(EMAIL_REGEX)
    def email_validate(cls, value, info: ValidationInfo):
        return value


    @field_validator("address")
    @classmethod
    @Required
    @NotNone
    @MaxLength(100)
    def address_validate(cls, value, info: ValidationInfo):
        return value


    @field_validator("city")
    @classmethod
    @Required
    @NotNone
    @MaxLength(35)
    def city_validate(cls, value, info: ValidationInfo):
        return value


    @field_validator("state")
    @classmethod
    @Required
    @NotNone
    @MaxLength(20)
    def state_validate(cls, value, info: ValidationInfo):
        return value


    @field_validator("country")
    @classmethod
    @Required
    @NotNone
    @MaxLength(10)
    def country_validate(cls, value, info: ValidationInfo):
        return value


    @field_validator("postal_code")
    @classmethod
    @Required
    @NotNone
    @MaxLength(6)
    def postal_code_validate(cls, value, info: ValidationInfo):
        return value
    