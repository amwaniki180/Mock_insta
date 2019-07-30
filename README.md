# [mock_insta][(https://still-gorge-91310.herokuapp.com//)]
### This is a clone of the image sharing network, Instagram. Users can sign up login, view and post photos and follow other users.

 
### July 22, 2019
#### By **[ANTONY MWANIKI](https://github.com/amwaniki180)**
## Description
[MOCK-INSTA]((https://still-gorge-91310.herokuapp.com//))This is a clone of the image sharing network, Instagram. Users can sign up login, view and post photos and follow other users.



## USER STORIES
1.Register and Sign in to the application.
2.Upload my pictures to the application.
3.See my profile with all my pictures.
4.Follow other users and see their pictures on my timeline.
5.Like or Save a picture and leave a comment on it.

### Prerequisites
1. Ubuntu Software
2. Python3.6
3. [Postgres](https://www.postgresql.org/download/)
4. [python virtualenv](https://gist.github.com/Geoyi/d9fab4f609e9f75941946be45000632b)
### Clone the Repo
Run the following command on the terminal:
`git clone https://github.com/amwaniki180/photogallery`
### Activate virtual environment
Activate virtual environment using python3.6 as default handler
```bash
virtualenv -p /usr/bin/python3.6 venv && source venv/bin/activate
```
### Install dependancies
Install dependancies that will create an environment for the app to run
`pip3 install -r requirements.txt`
### Create the Database
```bash
psql
CREATE DATABASE photos;
```
### .env file
Create .env file and paste paste the following filling where appropriate:
```python
SECRET_KEY = '<Secret_key>'
DBNAME = 'instagram'
USER = '<Username>'
PASSWORD = '<password>'
DEBUG = True
```
### Run initial Migration
```bash
python3.6 manage.py makemigrations photos
python3.6 manage.py migrate
```
### Run the app
```bash
python3.6 manage.py runserver
```
Open terminal on `localhost:8000`
## Known bugs
Copy functionality does not work
## Technologies used
    - Python 3.6
    - HTML
    - Bootstrap 4
    - Bootstrap 3
    - JavaScript
    - Heroku
    - Postgresql
## Support and contact details
Contact me on developer on amwaniki180@gmail.com for any comments, reviews or advice.
## License
This project is licensed under the MIT License - see the LICENSE file for details

