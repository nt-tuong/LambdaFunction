
from typing import List
from abc import ABC, abstractmethod
from database.tables.employees import Employees


# Interface
class EmployeesDao(ABC):
    @abstractmethod
    def get_all_employees(self) -> List[Employees]:
        pass


    @abstractmethod
    def get_employee_by_id(self, employee_id: int) -> Employees:
        pass


    @abstractmethod
    def get_employee_by_uuid(self, employee_uuid: str) -> Employees:
        pass


    @abstractmethod
    def insert_employee(self, employee: Employees) -> Employees:
        pass


    @abstractmethod
    def delete_employee(self, employee_uuid: str) -> bool:
        pass
