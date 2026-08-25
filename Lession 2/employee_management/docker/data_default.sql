BEGIN;

-- =========================================================
-- 1. Employees
-- =========================================================
INSERT INTO public."M_Employees" (
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
  "isDeleted",
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
  0,
  1,
  1
);

COMMIT;