Django User Management Project
A simple Django-based user management system with registration, mock email verification, profile management, and admin features.
Features

User Registration: Users can sign up with a username, email, and password.
User Verification: Mock email verification using a database token.
Profile Management: View/edit profile and change password.
Admin Panel: Admins can view/edit all user details.
Normal Users: Restricted to managing their own profile.
Tests: Unit tests for models and views.


Installation

Clone the repository:git clone <your-cloned-github-repo-url>


Create a virtual environment:python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install dependencies:pip install -r requirements.txt


Apply migrations:python manage.py migrate


Create a superuser:python manage.py createsuperuser


Run the development server:python manage.py runserver


Access the app at http://localhost:8000 and admin at http://localhost:8000/admin.

Running Tests
python manage.py test



Access at http://localhost:8000.

Git Commit History

Initial project setup: Created Django project and users app.
Added UserProfile model: Includes bio and verification fields.
Implemented user registration: Added form, view, and templates.
Added mock email verification: Token-based system.
Implemented profile management: View/edit profile and password change.
Configured admin panel: Enabled user management.
Added unit tests: For models and views.


Development Process
This project was built to create a user management system with Django, focusing on simplicity and functionality. Key steps included:

Setup: Initialized Django with a users app, using SQLite for simplicity.
Models: Created a UserProfile model to extend Django’s User model with bio and verification fields.
Registration: Used UserCreationForm with an email field, ensuring secure user creation.
Verification: Implemented a mock email verification system using database tokens, as real email integration was out of scope.
Profile Management: Added views for profile editing and password changes, restricted to authenticated users.
Admin Panel: Leveraged Django’s admin interface for user management.
Testing: Wrote unit tests to verify model creation and view accessibility.
Docker: Added containerization for consistent development environments.
Deployment: Deployed on Render for a live demo.
Challenges: Configuring Django’s authentication system and ensuring user restrictions were tricky but resolved using @login_required and form validation.
Lessons Learned: Django’s built-in auth system is powerful but requires careful configuration for custom user flows.
