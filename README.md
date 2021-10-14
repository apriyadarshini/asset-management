Steps to run the server:

clone this repo:
git clone https://github.com/apriyadarshini/asset-management.git

create a virtual env
python3 -m venv assetenv

Actvate the virtual env
source ./assetenv/bin/activate

Install the requirements
pip install -r requirements.txt

Make migrations and migrate:
python manage.py makemigrations
python manage.py migrate

Run the server:
python manage.py runserver

Usecase:

1) Open http://127.0.0.1:8000/ in a web browser
2) The links to view analysts and assets when clicked should ask for authentication
3) create a new user using http://127.0.0.1:8000/signup/
4) Login using the email and password provided in the previous step: http://127.0.0.1:8000/login/
5) Try the analysts and assets APIs : http://localhost:8000/analysts/ and http://localhost:8000/assets/ . It should now display the details.
6) logout: http://localhost:8000/logout/ and then try to access  http://localhost:8000/analysts/ and http://localhost:8000/assets/. This will now fail with authentiaiton required error. 

Analysts and Assets API accept both GET and POST requests.


