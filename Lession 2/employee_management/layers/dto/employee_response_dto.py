class EmployeeListResponse:
    def __init__(self, data: list, total: int):
        self.data = data
        self.total = total

    def to_dict(self):
        return {
            "data": [user.to_dict() for user in self.data],
            "total": self.total
        }
    