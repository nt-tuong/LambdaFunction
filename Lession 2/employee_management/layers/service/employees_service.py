from abc import ABC, abstractmethod

from dto import (
    EmployeeRequestDto,
    EmployeeUpdateRequestDto
)


# Interface
class EmployeesService(ABC):
    @abstractmethod
    def get_all_employees(self):
        pass
    

    @abstractmethod
    def get_employee_by_id(self, employee_id: int):
        pass


    @abstractmethod
    def insert_employee(self, request_dto: EmployeeRequestDto):
        pass


    @abstractmethod
    def update_employee(self, request_dto: EmployeeUpdateRequestDto):
        pass


    @abstractmethod
    def delete_employee(self, employee_uuid: str) -> bool:
        pass
