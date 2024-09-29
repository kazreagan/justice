# justice

#getting started
1.  **clone the repository**
     ```bash
     git clone
     cd repo-name


2.  **create virtual environment**
     ```bash
     python -m venv env(environment name of your choice)
     source env/bin/activate #for mac or linux
     source env/scripts/activate for windows

3.  **install dependencies**
     ```bash
     pip install -r requirements.txt

4.  **create superuser for django admin access**
     ```bash
     python manage.py createsuperuser # for windows
     python3 manage.py createsuperuser # for linux

5.  **set up environment variables**
    copy the `.env.example` file to `.env`
     ```bash
     cp .env.example .env


6.  **set up database**
     ```bash
     python manage.py migrate # for windows
     python3 manage.py migrate # for linux

7.  **collect static files(if there need be)**
     ```bash
     python manage.py collectstatic #for windows
     python3 manage.py collectstatic # for linux

8.  **run server**
     ```bash
     python manage.py runserver #for windows
     python3 manage.py runserver #for linux


now you can access the app at 
http://127.0.0.1:8000 
