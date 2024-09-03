# ✨ OneStopShop ✨
## _Multivendor Ecommerce App_

OneStopShop backend is a multivendor platform.
## Installation Instructions

### Prerequisites
Before you begin, ensure you have the following installed on your system:

- [Python](https://www.python.org/) - version 3.8 or higher.
- [PIP](https://pypi.org/project/pip/) - awesome web-based text editor.
- [Virtualenv](https://pypi.org/project/virtualenv/) - for creating isolated Python environments.
- [Git](https://git-scm.com/) - for cloning the repository.
- [PostgreSQL](https://www.postgresql.org/download/) - or any other database specified in the project settings.

## Installation

### Clone the Repository
First, clone the repository to your local machine using Git.

```sh
git clone git@github.com:samikaran/onestopshop_backend.git
cd onestopshop_backend
```

### Set Up a Virtual Environment
> Note: You should run `pip install virtualenv` if virtual environment package is not installed previously.
```sh
python -m venv venv
```

### Activate the virtual environment:

#### On macOS/Linux:
```sh
source venv/bin/activate
```
#### On Windows:
```sh
.\venv\Scripts\activate
```
### Install the Required Packages
```sh
pip install -r requirements.txt
```

### Set Up the Database
> Note: Create a new PostgreSQL or MySQL database and user, then update the `DATABASES` setting in `settings.py` with your database credentials.
Apply the database migrations:
```sh
python manage.py migrate
```

### Collect Static Files
If your project uses static files, collect them using the following command:
```sh
python manage.py collectstatic
```
### Run the Development Server
Start the Django development server:
```sh
python manage.py runserver
```

The project should now be running at http://127.0.0.1:8000/.

### Create Super User
Create super user and login to admin panel http://127.0.0.1:8000/admin/
```sh
python manage.py createsuperuser
```
**Hurray it's done!!!**