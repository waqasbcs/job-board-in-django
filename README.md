# Job Board Project

This is a Django-based web application for posting and applying to jobs.

## Features

- User registration and authentication
- Job posting
- Job application
- Profile management
- Resume upload

## Installation

### Prerequisites

- Python 3.x
- pip

### Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/waqasbcs/job-board-in-django.git
    cd job-board-in-django
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    # For Windows
    venv\Scripts\activate
    # For macOS/Linux
    source venv/bin/activate
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run migrations:
    ```bash
    python manage.py migrate
    ```

5. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```

6. Start the development server:
    ```bash
    python manage.py runserver
    ```

## Usage

- Access the application at `http://127.0.0.1:8000`
- Admin interface at `http://127.0.0.1:8000/admin`

## License

This project is licensed under the MIT License.

## Contact

- GitHub: [waqasbcs](https://github.com/waqasbcs)
