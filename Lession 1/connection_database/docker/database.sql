-- =========================================================
-- Database : TrithenDec
-- Engine   : PostgreSQL
-- Purpose  : HR / Identity / Organization Management
-- =========================================================

-- =========================================================
-- Extensions
-- =========================================================
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

SET search_path TO public;

-- =========================================================
-- Drop tables (optional for local/dev only)
-- =========================================================
DROP TABLE IF EXISTS "M_Users" CASCADE;
DROP TABLE IF EXISTS "M_Persons" CASCADE;
DROP TABLE IF EXISTS "M_Organizations" CASCADE;
DROP TABLE IF EXISTS "M_Roles" CASCADE;
DROP TABLE IF EXISTS "M_Messages " CASCADE;
DROP TABLE IF EXISTS "T_No" CASCADE;
DROP TABLE IF EXISTS "T_RefreshTokens" CASCADE;

-- =========================================================
-- Table: M_Roles
-- =========================================================
CREATE TABLE "M_Roles" (
    "id"            BIGSERIAL PRIMARY KEY,
    "code"          VARCHAR(50) NOT NULL UNIQUE,
    "name"          VARCHAR(255) NOT NULL,
    "description"   VARCHAR(1000),

    "createAt"      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    "createdBy"     BIGINT,
    "updatedAt"     TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    "updatedBy"     BIGINT
);

-- =========================================================
-- Table: M_Organizations
-- =========================================================
CREATE TABLE "M_Organizations" (
    "id"            BIGSERIAL PRIMARY KEY,
    "uuid"          UUID NOT NULL UNIQUE DEFAULT gen_random_uuid(),

    "code"          VARCHAR(50) NOT NULL UNIQUE,
    "name"          VARCHAR(255) NOT NULL,
    "description"   VARCHAR(255),

    "status"        SMALLINT NOT NULL DEFAULT 1
                    CHECK ("status" IN (0, 1)),

    "createAt"      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    "createdBy"     BIGINT,
    "updatedAt"     TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    "updatedBy"     BIGINT
);

-- =========================================================
-- Table: M_Persons
-- =========================================================
CREATE TABLE "M_Persons" (
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

    "createAt"              TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    "createdBy"             BIGINT,
    "updatedAt"             TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    "updatedBy"             BIGINT,

    CONSTRAINT "CHK_M_Persons_BirthDate"
        CHECK ("birthDate" BETWEEN 19000101 AND 29991231)
);

-- =========================================================
-- Table: M_Users
-- =========================================================
CREATE TABLE "M_Users" (
    "id"              BIGSERIAL PRIMARY KEY,
    "uuid"            UUID NOT NULL UNIQUE DEFAULT gen_random_uuid(),

    "code"            VARCHAR(50) NOT NULL UNIQUE,

    "organizationId"  BIGINT NOT NULL,
    "roleId"          BIGINT NOT NULL,
    "personId"        BIGINT NOT NULL,

    "userName"        VARCHAR(255) NOT NULL UNIQUE,
    "password"        VARCHAR(255) NOT NULL,

    "status"          SMALLINT NOT NULL DEFAULT 1
                      CHECK ("status" IN (0, 1)),

    "createAt"        TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    "createdBy"       BIGINT,
    "updatedAt"       TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    "updatedBy"       BIGINT
);

-- =========================================================
-- Table: M_Messages
-- =========================================================
CREATE TABLE "M_Messages" (
    "id"              BIGSERIAL PRIMARY KEY,
    "code"            VARCHAR(10) NOT NULL UNIQUE,
    "message"         TEXT NOT NULL
);

-- =========================================================
-- Table: T_No
-- =========================================================
CREATE TABLE "T_No" (
    "id"                BIGSERIAL PRIMARY KEY,
    "no"                VARCHAR(20),
    "nextNo"            BIGINT NOT NULL DEFAULT 0,
    "year"              INTEGER NOT NULL,
    "month"             INTEGER NOT NULL,
    "organizationId"    BIGINT NOT NULL
);

-- =========================================================
-- Table: T_RefreshTokens
-- =========================================================
CREATE TABLE "T_RefreshTokens" (
    "id"                VARCHAR(255),
    "token"             VARCHAR(255) NOT NULL UNIQUE,
    "userId"            BIGINT NOT NULL,
    "expiresAt"         TIMESTAMPTZ NOT NULL,
    "createdAt"         TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- =========================================================
-- Foreign Keys
-- =========================================================

-- M_Users
ALTER TABLE "M_Users"
    ADD CONSTRAINT "FK_M_Users_Organization"
        FOREIGN KEY ("organizationId") REFERENCES "M_Organizations" ("id"),
    ADD CONSTRAINT "FK_M_Users_Role"
        FOREIGN KEY ("roleId") REFERENCES "M_Roles" ("id"),
    ADD CONSTRAINT "FK_M_Users_Person"
        FOREIGN KEY ("personId") REFERENCES "M_Persons" ("id"),
    ADD CONSTRAINT "FK_M_Users_CreatedBy"
        FOREIGN KEY ("createdBy") REFERENCES "M_Users" ("id"),
    ADD CONSTRAINT "FK_M_Users_UpdatedBy"
        FOREIGN KEY ("updatedBy") REFERENCES "M_Users" ("id");

-- M_Organizations
ALTER TABLE "M_Organizations"
    ADD CONSTRAINT "FK_M_Organizations_CreatedBy"
        FOREIGN KEY ("createdBy") REFERENCES "M_Users" ("id"),
    ADD CONSTRAINT "FK_M_Organizations_UpdatedBy"
        FOREIGN KEY ("updatedBy") REFERENCES "M_Users" ("id");

-- M_Persons
ALTER TABLE "M_Persons"
    ADD CONSTRAINT "FK_M_Persons_CreatedBy"
        FOREIGN KEY ("createdBy") REFERENCES "M_Users" ("id"),
    ADD CONSTRAINT "FK_M_Persons_UpdatedBy"
        FOREIGN KEY ("updatedBy") REFERENCES "M_Users" ("id");

-- M_Roles
ALTER TABLE "M_Roles"
    ADD CONSTRAINT "FK_M_Roles_CreatedBy"
        FOREIGN KEY ("createdBy") REFERENCES "M_Users" ("id"),
    ADD CONSTRAINT "FK_M_Roles_UpdatedBy"
        FOREIGN KEY ("updatedBy") REFERENCES "M_Users" ("id");

-- T_No
ALTER TABLE "T_No"
    ADD CONSTRAINT "FK_T_No_Organization"
        FOREIGN KEY ("organizationId") REFERENCES "M_Organizations" ("id");

-- =========================================================
-- Indexes
-- =========================================================

-- M_Users
CREATE INDEX "IDX_M_Users_OrganizationId" ON "M_Users" ("organizationId");
CREATE INDEX "IDX_M_Users_RoleId"         ON "M_Users" ("roleId");
CREATE INDEX "IDX_M_Users_PersonId"       ON "M_Users" ("personId");
CREATE INDEX "IDX_M_Users_Status"         ON "M_Users" ("status");

-- M_Organizations
CREATE INDEX "IDX_M_Organizations_Status" ON "M_Organizations" ("status");

-- M_Persons
CREATE INDEX "IDX_M_Persons_BirthDate"    ON "M_Persons" ("birthDate");
CREATE INDEX "IDX_M_Persons_Email"        ON "M_Persons" ("email");
CREATE INDEX "IDX_M_Persons_PhoneNumber"  ON "M_Persons" ("phoneNumber");
CREATE INDEX "IDX_M_Persons_CitizenId"    ON "M_Persons" ("citizenIdentityCard");

-- =========================================================
-- Notes
-- =========================================================
-- 1. Database Name:
--      TrithenDec
--
-- 2. UUID is used as external/public identifier.
--
-- 3. BIGINT id is used for internal PK/FK joins.
--
-- 4. birthDate uses INTEGER format YYYYMMDD by business design.
--
-- 5. citizenIdentityCard is intentionally NOT UNIQUE by business rule.
--
-- 6. password stores hashed value only (bcrypt / argon2), never raw password.