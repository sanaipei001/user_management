##Introduction


Imagine a web app where a vibrant blue navbar sticks with you as you scroll, guiding you through registration, login, and profile updates with ease.
Prerequisites
Before cloning, ensure you have:

Python 3.13.2 

Git 

Virtualenv (optional but recommended) 

Clone and Set Up the Project
Ready to bring this app to life? Follow these steps to clone and run it locally! 

Clone the Repository:

git clone https://github.com/your-username/user_management.git
Create a Virtual Environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies: Ensure your requirements.txt includes:

django==5.2.4
gunicorn==22.0.0
django-widget-tweaks==1.5.0
Then run:

pip install -r requirements.txt
Apply Migrations: Set up the SQLite database:

python manage.py migrate
Create a Superuser: For admin access:

python manage.py createsuperuser

python manage.py collectstatic
Run the Development Server:

python manage.py runserver
Access the app at http://localhost:8000 and the admin panel at http://localhost:8000/admin.
