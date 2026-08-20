# AWS Lambda Routes Example (Python) — aws-lambda-powertools

Project mẫu minh hoạ cách tổ chức nhiều Lambda function theo route, dùng chung
1 Lambda Layer chứa `aws-lambda-powertools`, không kết nối database (trả JSON mẫu).

## Cấu trúc thư mục

```
aws-lambda-routes-example/
├── template.yaml                     # SAM: layer + 2 function + API Gateway
├── layers/
│   └── common/
│       └── requirements.txt          # aws-lambda-powertools (SAM tự pip install khi build)
└── functions/
    ├── users/
    │   ├── app.py                    # lambda_handler dùng APIGatewayRestResolver
    │   └── routes.py                 # Router: GET /users, GET /users/{id}
    └── organizations/
        ├── app.py
        └── routes.py                 # Router: GET /organizations, GET /organizations/{id}
```

## Vì sao dùng `aws_lambda_powertools.event_handler.api_gateway.Router`?

- Mỗi function có `routes.py` riêng, dùng `Router()` + decorator `@router.get(...)`
  để đăng ký path — tách biệt route của từng domain (users, organizations).
- `app.py` gộp router lại bằng `APIGatewayRestResolver().include_router(router)`,
  và `lambda_handler` chỉ cần gọi `app.resolve(event, context)`.
- Path param dùng cú pháp `<id>` (Powertools tự parse thành kwarg cho handler).
- Lỗi 404 dùng `NotFoundError` (từ `aws_lambda_powertools.event_handler.exceptions`),
  Powertools tự format response chuẩn, không cần tự viết `build_response`.
- `Logger` (Powertools) tự inject request_id, cold start, structured logging.

## Danh sách route

| Method | Path                    | Mô tả                              | Function      |
|--------|--------------------------|-------------------------------------|---------------|
| GET    | /users                  | Lấy toàn bộ users                   | UsersFunction |
| GET    | /users/{id}             | Lấy thông tin user theo mã          | UsersFunction |
| GET    | /organizations          | Lấy toàn bộ organizations           | OrganizationsFunction |
| GET    | /organizations/{id}     | Lấy thông tin organization theo mã  | OrganizationsFunction |

## Build & Deploy (AWS SAM)

```bash
sam build
sam deploy --guided
```

SAM sẽ build layer bằng cách `pip install -r layers/common/requirements.txt`
vào layer, rồi gắn layer đó cho cả 2 function.

Sau khi deploy:

```bash
curl https://<api-id>.execute-api.<region>.amazonaws.com/Prod/users
curl https://<api-id>.execute-api.<region>.amazonaws.com/Prod/users/u001
curl https://<api-id>.execute-api.<region>.amazonaws.com/Prod/organizations
curl https://<api-id>.execute-api.<region>.amazonaws.com/Prod/organizations/o001
```

## Test local (không cần deploy)

```bash
pip install aws-lambda-powertools

cd functions/users
python3 -c "
from app import lambda_handler

class FakeContext:
    function_name = 'users-function'
    memory_limit_in_mb = 128
    invoked_function_arn = 'arn:aws:lambda:ap-southeast-1:123456789012:function:users-function'
    aws_request_id = 'test-request-id'

event = {'httpMethod': 'GET', 'path': '/users/u001'}
print(lambda_handler(event, FakeContext()))
"
```

## Mở rộng thêm route/function mới

1. Tạo thư mục mới trong `functions/`, ví dụ `functions/products/`.
2. Trong `routes.py`, tạo `router = Router()` và dùng `@router.get("/products")`,
   `@router.get("/products/<id>")` ... để đăng ký handler.
3. Trong `app.py`, tạo `APIGatewayRestResolver()` rồi `app.include_router(router)`.
4. Thêm function + Layers + Events (path) tương ứng vào `template.yaml`.
