# Wall Street Football 
The purpose of this task is to design and implement a web page that displays some data pulled from an API, allows users to make modifications and finally displays the results of said modifications in real time.

## About
The backend is written in Django, django-restframework, which consists of an API which can retrive, create, update or delete contents.


## Quickstart

```
bash setup.sh
bash runapi.sh
```

Browse http://localhost:8080/

## Setup
Clone this repo and cd:

```
git clone https://github.com/anshku/wsf.git
cd wsf
```

Run `setup.sh` or setup manually:
```
bash setup.sh
```

Create environment:

```
python3 -m venv venv
source venv/bin/activate
```

Install Dependencies

```
pip install -r requirements.txt
```

Setup DB

```
python manage.py makemigrations
python manage.py migrate

```

Create user (optional)

```

python manage.py createsuperuser

```

  
## Run

Run `runapi.sh`

```
bash runapi.sh
```

Or

```

python manage.py runserver

```

## Players API

You can browse the API through

http://127.0.0.1:8000/players/

Or by commandline

Create a player.

```
curl --location --request POST 'http://127.0.0.1:8000/players/' --header 'Content-Type: application/json' --data-raw '{
    "id": "3",
    "name": "axvd",
    "position": "Midfielder",
    "odds": 0.5,
    "margin": 0.1
}'
```

Get a list of all availabe players and their attributes.

```
curl --location --request GET 'http://127.0.0.1:8000 players/'
```

Get instance of a player.

```
curl --location --request GET 'http://127.0.0.1:8000/players/3'
```

Edit a player.

```
curl --location --request PATCH 'http://127.0.0.1:8000/players/3/' --header 'Content-Type: application/json' --data-raw '{
    "margin": 0.5
}'
```

Delete a player.

```
curl --location --request DELETE 'http://127.0.0.1:8000/players/3/'
```

## Frontend

Goto http://localhost:8080/