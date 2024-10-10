# Link Manager API

Link Manager is a Django-based API for storing and managing user links and collections. This document provides instructions on how to set up and run the project locally using Docker.

## Prerequisites

- Docker (version 27.1.1 or later)
- Docker Compose (version 2.29.1 or later)
- Python (version 3.12.7 or later)
- Django (version 5.1.2 or later)
- PostgreSQL (version 14 or later)

## Getting Started

Follow these steps to get a copy of the project running on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/LvYegor/drf-link-manager-api
cd link_manager
```

### 2. Configure Environment Variables

Create a `.env` file in the root directory of the project to set your environment variables:

```bash
POSTGRES_DB=linkmanagerdb
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_password
PG_HOST=db
PG_PORT=5432
```

### 3. Build and Run the Containers
Use Docker Compose to build and run the application:

```bash
docker-compose up --build
```

### 4. Run Migrations
After the containers are running, you need to apply database migrations:

```bash
docker-compose exec web python manage.py migrate
```

### 6. Access the API
The API will be available at http://localhost:8000/api/. You can also access the Swagger documentation at http://localhost:8000/swagger/.