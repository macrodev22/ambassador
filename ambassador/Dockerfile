FROM python:3.12-alpine

# Install pkg-config and MariaDB client development libraries
RUN apk update && \
    apk add --no-cache gcc musl-dev pkgconfig mariadb-dev mariadb-connector-c-dev

# Show python logs in console
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

# Use a non root user
RUN addgroup -S appgroup && adduser -S appuser -G appgroup


COPY . .

# Change ownership and permissions
RUN chown -R appuser:appgroup /app

# switch user
USER appuser

CMD python manage.py wait_for_db && python manage.py runserver 0.0.0.0:8000