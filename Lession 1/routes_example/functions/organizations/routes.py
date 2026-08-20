from aws_lambda_powertools.event_handler.api_gateway import Router
from aws_lambda_powertools.event_handler.exceptions import NotFoundError

router = Router()

# free sample
ORGANIZATIONS = [
    {"org_cd": "0001", "name": "Cong ty TNHH ABC", "address": "Quan 1, TP.HCM"},
    {"org_cd": "0002", "name": "Cong ty Co phan XYZ", "address": "Quan 3, TP.HCM"},
    {"org_cd": "0003", "name": "Cong ty TNHH DEF", "address": "Quan 7, TP.HCM"},
]


@router.get("/organizations")
def get_all_organizations():
    return {"data": ORGANIZATIONS, "total": len(ORGANIZATIONS)}


@router.get("/organizations/<org_cd>")
def get_organization_by_cd(org_cd: str):
    org = next((o for o in ORGANIZATIONS if o["org_cd"] == org_cd), None)
    if not org:
        raise NotFoundError(f"Organization '{org_cd}' not found")
    return {"data": org}
