# Install

## Activate virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

## Install requirements

```bash
pip install -r requirements.txt
```

## Launch dev project

```bash
uvicorn app:app --reload
```

## Launch prod project with docker

```bash
docker build -t sales_predict .
docker run --rm -ti -p 8484:8484 sales_predict
```

## Authentification

### Create application with auth0

You need to create an Regular Web Application into auth0.
Setting and Environnement variable with .env file

```python
# .env

AUTH0_DOMAIN = your.domain.auth0.com
AUTH0_API_AUDIENCE = https://your.api.audience
AUTH0_ISSUER = https://your.domain.auth0.com/
AUTH0_ALGORITHMS = RS256
```

If you forget information about the audiance, check this video.
[https://community.auth0.com/t/what-is-the-audience/71414](https://community.auth0.com/t/what-is-the-audience/71414)

Get a token with this curl command

```curl
curl -X 'POST' \
--url 'https://qfp.eu.auth0.com/oauth/token' \
 --header 'content-type: application/x-www-form-urlencoded' \
 --data 'grant_type=client_credentials' \
 --data 'client_id=<CLIENT_ID>' \
 --data 'client_secret=<CLIENT_SECRET>' \
 --data 'audience=audience.api'
 ```

Test a private access with this

```curl
curl -X 'GET'   'http://localhost:8000/private'   -H 'accept: application/json'
  -H 'Authorization: Bearer <TOKEN>
```
