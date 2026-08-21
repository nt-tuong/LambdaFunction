FROM postgres:16

# Set timezone (optional)
ENV TZ=Asia/Ho_Chi_Minh

COPY database.sql /docker-entrypoint-initdb.d/

EXPOSE 5432
