# Overview:

Link shortening REST service

# Stack:

- Python 3.10
- Django
- Rest framework
- PostgreSQL (Redis for 'redis' branch)

*Redis branch in development*

# Endpoints

URL: **/**
| Method        | Request       | Response        |
| ------------- | ------------- |---------------- |
| POST          | link          | 200: short_link |
|               |               | 400: error      |
|               |               | 404: error      |

URL: **/{encoded_id}**
| Method        | Request       | Response        |
| ------------- | ------------- |---------------- |
| GET           | -             | 200: source     |
|               |               | 400: error      |
|               |               | 404: error      |

# Examples

**1. POST http://<area>0.0.0.0:8000/**

Body:
```
link: "https://github.com/Danil-Tolmachov/ShortUrl/"
```

Response:
```json
{
    "link": "http://0.0.0.0:8000/Mw"
}
```

**2. GET http://<area>0.0.0.0:8000/Mw**

Response:
```json
{
    "source": "https://github.com/Danil-Tolmachov/ShortUrl/"
}
```

# Instalation and setup

**1. Clone repository**
```sh
git clone https://github.com/Danil-Tolmachov/ShortUrl/
cd ShortUrl/
```

**2. Create and activate virtual enviroment (optional)**
```sh
python -m venv venv
```

Activation for Windows:
```sh
./venv/Sctipts/activate
```

Activation for Linux:
```sh
source venv/bin/activate
```

**3. Install requirements.txt**
```sh
pip install -r requirements.txt
```

**4. Setup enviroment variables**

**Example:**
```env
SECRET_KEY=somekey
ALLOWED_HOSTS=*
DATABASE_URL=postgres://user:password@db:5432/short_db

POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=short_db
```
Note: Use 'db' as the host in DATABASE_URL to estabilish a connection between the database and the api containers. Also you can change database container name in the docker-compose.

**5. Build and run docker-compose file**
```sh
docker-compose -f docker-compose.yml up
```
