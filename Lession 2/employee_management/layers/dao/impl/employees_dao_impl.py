from typing import List
from database import get_session
from database.tables import Employees
from dao.employees_dao import EmployeesDao

from utils.enum.common import DeletionStatus


class EmployeesDaoImpl(EmployeesDao):
    def __init__(self):
        session = get_session()
        self.session = session


    def get_all_employees(self) -> List[Employees]:
        return (self.session.query(Employees)
                .filter(Employees.is_deleted == DeletionStatus.NOT_DELETED)
                .all())


    def get_employee_by_id(self, employee_id: int) -> Employees:
        return (self.session.query(Employees)
                .filter(Employees.id == employee_id,
                        Employees.is_deleted == DeletionStatus.NOT_DELETED)
                .first())


    def get_employee_by_uuid(self, employee_uuid: str) -> Employees:
        return (self.session.query(Employees)
                .filter(Employees.uuid == employee_uuid,
                        Employees.is_deleted == DeletionStatus.NOT_DELETED)
                .first())


    def insert_employee(self, employee: Employees) -> Employees:
        try:
            self.session.add(employee)
            self.session.flush()
            self.session.refresh(employee)
            return employee
        except Exception as e:
            raise e


    def delete_employee(self, employee_uuid: str) -> bool:
        try:
            employee = self.get_employee_by_uuid(employee_uuid)
            if employee is None:
                return False
            
            employee.is_deleted = DeletionStatus.DELETED
            self.session.flush()
            return True
        except Exception:
            self.session.rollback()
            raise
