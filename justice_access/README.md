# justice

#getting started
1.  **clone the repository**
     ```bash
     git clone
     cd repo-name


#create virtual environment
python -m venv env(environment name of your choice)
    source env/bin/activate #for mac or linux
    source env/scripts/activate for windows

#install dependencies
pip install -r requirements.txt

#set up environment variables
copy the `.env.example` file to `.env`
cp .env.example .env


#set up database
python manage.py migrate # for windows
python3 manage.py migrate # for linux

#collect static files(if there need be)
python manage.py collectstatic #for windows
python3 manage.py collectstatic # for linux

#run server
python manage.py runserver #for windows
python3 manage.py runserver #for linux


now you can access the app at 
http://127.0.0.1:8000 