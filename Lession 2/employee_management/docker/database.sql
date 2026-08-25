-- =========================================================
-- Database : employee_management
-- Engine   : PostgreSQL
-- Purpose  : HR / Identity / Employees Management
-- =========================================================

-- =========================================================
-- Extensions
-- =========================================================
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

SET search_path TO public;

-- =========================================================
-- Drop tables (optional for local/dev only)
-- =========================================================
DROP TABLE IF EXISTS "M_Employees" CASCADE;

-- =========================================================
-- Table: M_Employees
-- =========================================================
CREATE TABLE "M_Employees" (
    "id"                    BIGSERIAL PRIMARY KEY,
    "uuid"                  UUID NOT NULL UNIQUE DEFAULT gen_random_uuid(),

    "name"                  VARCHAR(255) NOT NULL,
    "fullName"              VARCHAR(255) NOT NULL,

    -- Format: YYYYMMDD (example: 19991231)
    "birthDate"             INTEGER NOT NULL,

    "gender"                SMALLINT NOT NULL DEFAULT 0
                            CHECK ("gender" IN (0, 1)),

    "citizenIdentityCard"   VARCHAR(12) NOT NULL,
    "phoneNumber"           VARCHAR(20) NOT NULL,
    "email"                 VARCHAR(255) NOT NULL,

    "address"               VARCHAR(255) NOT NULL,
    "city"                  VARCHAR(255),
    "state"                 VARCHAR(255),
    "country"               VARCHAR(255),
    "postalCode"            VARCHAR(20),

    
    "isDeleted"             SMALLINT NOT NULL DEFAULT 0,
    "createAt"              TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    "createdBy"             BIGINT,
    "updatedAt"             TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    "updatedBy"             BIGINT,

    CONSTRAINT "CHK_M_Employees_BirthDate"
        CHECK ("birthDate" BETWEEN 19000101 AND 29991231)
);

-- =========================================================
-- Indexes
-- =========================================================

-- M_Employees
CREATE INDEX "IDX_M_Employees_BirthDate"    ON "M_Employees" ("birthDate");
CREATE INDEX "IDX_M_Employees_Email"        ON "M_Employees" ("email");
CREATE INDEX "IDX_M_Employees_PhoneNumber"  ON "M_Employees" ("phoneNumber");
CREATE INDEX "IDX_M_Employees_CitizenId"    ON "M_Employees" ("citizenIdentityCard");

-- =========================================================
-- Notes
-- =========================================================
-- 1. Database Name:
--      employee_management
--
-- 2. UUID is used as external/public identifier.
--
-- 3. BIGINT id is used for internal PK/FK joins.
--
-- 4. birthDate uses INTEGER format YYYYMMDD by business design.
--
-- 5. citizenIdentityCard is intentionally NOT UNIQUE by business rule.