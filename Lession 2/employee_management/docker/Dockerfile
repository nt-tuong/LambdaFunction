FROM postgres:16

# Set timezone (optional)
ENV TZ=Asia/Ho_Chi_Minh

COPY database.sql       /docker-entrypoint-initdb.d/01_database.sql
COPY data_default.sql   /docker-entrypoint-initdb.d/02_data_default.sql

EXPOSE 5432
