from aws_lambda_powertools.event_handler.api_gateway import Router
from aws_lambda_powertools.event_handler.exceptions import NotFoundError
from aws_lambda_powertools import Tracer

from dao.impl.employees_dao_impl import EmployeesDaoImpl
from dto import (
    EmployeeRequestDto,
    EmployeeUpdateRequestDto
)

from service.impl.employees_service_impl import EmployeesServiceImpl


router = Router()
tracer = Tracer()


employees_dao = EmployeesDaoImpl()
employees_service = EmployeesServiceImpl(employees_dao)


@router.get("/employees")
def get_all_employees():
    employees = employees_service.get_all_employees()
    print(employees)
    return {"data": employees, "total": len(employees)}


@router.get("/employees/<employee_id>")
def get_employee_by_id(employee_id: int):
    employee = employees_service.get_employee_by_id(employee_id)
    return {"data": employee}


@router.post("/employees/insert")
def insert_employee(request_dto: EmployeeRequestDto):
    employees = employees_service.insert_employee(request_dto)
    return {"data": "OK! Hãy kiểm tra!"}


@router.put("/employees/update")
def update_employee(request_dto: EmployeeUpdateRequestDto):
    employees = employees_service.update_employee(request_dto)
    return {"data": "Update thành công! Hãy kiểm tra!"}


@router.delete("/employees/<employee_uuid>")
def delete_employee(employee_uuid: str):
    result = employees_service.delete_employee(employee_uuid)
    msg_delete = f"Failed to delete employee with UUID {employee_uuid}."
    if result:
        msg_delete = f"Employee with UUID {employee_uuid} has been deleted."
    return {"data": msg_delete}
