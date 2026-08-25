from dao.employees_dao import EmployeesDao
from dto import (
    EmployeeRequestDto,
    EmployeeUpdateRequestDto
)
from service.employees_service import EmployeesService


from database import get_session
from database.tables import Employees


class EmployeesServiceImpl(EmployeesService):
    def __init__(self, employees_dao: EmployeesDao):
        self.session = get_session()
        self.employees_dao = employees_dao


    def get_all_employees(self):
        # convert to json data
        employees = self.employees_dao.get_all_employees()
        return [employee.to_dict() for employee in employees]


    def get_employee_by_id(self, employee_id: int):
        employee = self.employees_dao.get_employee_by_id(employee_id)

        return employee.to_dict() if employee else None


    def insert_employee(self, request_dto: EmployeeRequestDto):
        try:
            # convert to json data
            print(f"Employee data: {request_dto}")
            employee = Employees(
                name=request_dto.name,            
                full_name= request_dto.full_name,
                birth_date= request_dto.birth_date,
                gender= request_dto.gender,
                citizen_identity_card= request_dto.citizen_identity_card,
                phone_number= request_dto.phone_number,
                email= request_dto.email,
                address= request_dto.address,
                city= request_dto.city,
                state= request_dto.state,
                country= request_dto.country,
                postal_code= request_dto.postal_code,
                created_by= 1,
                updated_by= 1,
            )
            self.employees_dao.insert_employee(employee)
            self.session.commit()
            return employee
        except Exception as e:
            print(f"Error inserting employee: {e}")
            self.session.rollback()
            raise e


    def update_employee(self, request_dto: EmployeeUpdateRequestDto):
        try:
            print(f"Employee data: {request_dto}")
            employee = self.employees_dao.get_employee_by_uuid(request_dto.employee_uuid)
            if not employee:
                raise ValueError(f"Employee with UUID {request_dto.employee_uuid} not found.")

            employee.name=request_dto.name,            
            employee.full_name= request_dto.full_name,
            employee.birth_date= request_dto.birth_date,
            employee.gender= request_dto.gender,
            employee.citizen_identity_card= request_dto.citizen_identity_card,
            employee.phone_number= request_dto.phone_number,
            employee.email= request_dto.email,
            employee.address= request_dto.address,
            employee.city= request_dto.city,
            employee.state= request_dto.state,
            employee.country= request_dto.country,
            employee.postal_code= request_dto.postal_code,

            self.session.commit()
            return employee
        except ValueError as ve:
            raise ve
        except Exception as e:
            print(f"Error updating employee: {e}")
            self.session.rollback()
            raise e


    def delete_employee(self, employee_uuid: str) -> bool:
        try:
            print("-------------------- [START] Delete employee --------------------")
            print(f"Employee UUID: {employee_uuid}")
            result = self.employees_dao.delete_employee(employee_uuid)
            self.session.commit()
            print("-------------------- [END] Delete employee --------------------")
            return result
        except Exception as e:
            print(f"Error deleting employee: {e}")
            self.session.rollback()
            raise e
