# To successfully test this project in your local system, please follow the steps below:

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/prakashtaz0091/Techforing.git
cd project
```

### Step 2: Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Apply Migrations

```bash
python manage.py migrate
```

### Step 5: Create a Superuser

```bash
python manage.py createsuperuser
```

### Step 6: Run the Development Server

```bash
python manage.py runserver
```

Access the app at [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## Usage

- Access the admin panel: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

---

## API Documentation

- Swagger UI: [http://127.0.0.1:8000/api/docs/swagger/](http://127.0.0.1:8000/api/docs/swagger/)
- ReDoc: [http://127.0.0.1:8000/api/docs/redoc/](http://127.0.0.1:8000/api/docs/redoc/)
- OpenAPI Schema: [http://127.0.0.1:8000/api/schema/](http://127.0.0.1:8000/api/schema/)

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to modify this template based on your specific project requirements! Let me know if you'd like help adding more details or customizing this further.
