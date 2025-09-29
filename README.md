Inventory Management System (IMS)
__________________________________

A full-stack CRUD Inventory Management System built with:
Backend: Python + Flask + PostgreSQL
Frontend: Angular
Infrastructure: Docker / Docker Compose
State Management: RxJS BehaviorSubject

FEATURES
_________
Full CRUD (Create, Read, Update, Delete) for Products.

Dashboard with metrics.
Angular Material UI with theming.
Efficient state management using BehaviorSubject.
Clean separation between frontend and backend.


TECH REQUIREMENTS
___________________
Docker & Docker Compose
Python 3.10+
Node.js 18+
Angular CLI

BACK-END SETUP
________________
(Flask + PostgreSQL)
STEP 1:
Start the database
docker-compose up -d

This runs a PostgreSQL container named "ims-postgres" with a persistent volume.

STEP 2: 
Install backend dependencies
cd IMS_backend
python -m venv venv
venv\Scripts\activate 
pip install -r reqs.txt

STEP 3: 
Run the Flask API
flask run 

API:
http://127.0.0.1:5000/api/products

____________________________________________________________
