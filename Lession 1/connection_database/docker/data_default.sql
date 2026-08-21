BEGIN;

-- =========================================================
-- 1. Role
-- =========================================================
INSERT INTO public."M_Roles" (
  "code",
  "name",
  "description",
  "createdBy",
  "updatedBy"
)
VALUES 
('0001', 'Administrator', 'Sytem Administrator', 1, 1),
('0002', 'Organization Administrator', 'Manages organization settings, users, and internal permissions', 1, 1),
('0003', 'Manager', 'Department Manager', 1, 1),
('0004', 'Supervisor', 'Team Supervisor', 1, 1),
('0005', 'Senior Staff', 'Senior Staff Member', 1, 1),
('0006', 'Staff', 'Staff Member', 1, 1),
('0007', 'HR', 'Human Resources', 1, 1),
('0008', 'Recruiter', 'Recruitment Specialist', 1, 1),
('0009', 'Accountant', 'Accounting Staff', 1, 1),
('0010', 'Finance', 'Finance Staff', 1, 1),
('0011', 'IT Support', 'IT Support Specialist', 1, 1),
('0012', 'Developer', 'Software Developer', 1, 1),
('0013', 'QA', 'Quality Assurance Engineer', 1, 1),
('0014', 'Product Owner', 'Product Owner', 1, 1),
('0015', 'Project Manager', 'Project Manager', 1, 1),
('0016', 'Sales', 'Sales Representative', 1, 1),
('0017', 'Marketing', 'Marketing Specialist', 1, 1),
('0018', 'Customer Support', 'Customer Support Staff', 1, 1),
('0019', 'Team Lead', 'Leads a team, assigns tasks, and monitors team progress', 1, 1),
('0020', 'Intern', 'Internship Role', 1, 1);

-- =========================================================
-- 2. Organization
-- =========================================================
INSERT INTO public."M_Organizations" (
  "code",
  "name",
  "description",
  "status",
  "createdBy",
  "updatedBy"
)
VALUES (
  'ORG001',
  'ISV CO.,LTD',
  'Default Organization',
  1,
  1,
  1
);

-- =========================================================
-- 3. Person
-- =========================================================
INSERT INTO public."M_Persons" (
  "name",
  "fullName",
  "birthDate",
  "gender",
  "citizenIdentityCard",
  "phoneNumber",
  "email",
  "address",
  "city",
  "state",
  "country",
  "postalCode",
  "createdBy",
  "updatedBy"
)
VALUES (
  'Itomi',
  'Itomi Keitaro',
  19750101,
  1,
  '012345678901',
  '0900000000',
  'isv-itomi@company.isv.vn',
  'Default Address',
  'Ho Chi Minh',
  'Ho Chi Minh',
  'Vietnam',
  '700000',
  1,
  1
);

-- =========================================================
-- 4. User
-- password plaintext: admin123
-- bcrypt hash: admin123
-- =========================================================
INSERT INTO public."M_Users" (
  "code",
  "organizationId",
  "roleId",
  "personId",
  "userName",
  "password",
  "status",
  "createdBy",
  "updatedBy"
)
VALUES (
  'USR001',
  (SELECT "id" FROM public."M_Organizations" WHERE "code" = 'ORG001'),
  (SELECT "id" FROM public."M_Roles" WHERE "code" = '0001'),
  (SELECT "id" FROM public."M_Persons" WHERE "email" = 'isv-itomi@company.isv.vn'),
  'admin',
  '$2b$10$rA7J7F7m8J5m0U8KJmY4QeY6lR0m6vQx2pQnYJtO8V8wK0kYxY7eG',
  1,
  1,
  1
);

COMMIT;