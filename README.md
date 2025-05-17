# Notification Service

This basic backend service is made using FastAPI. Allows users to send notifications (like email, SMS, or in-app) and fetch their notifications later. The data is stored in MongoDB.

---

## What it does

- Send notifications to users
- Get all notifications for a user
- Stores notifications in MongoDB
- Simple REST APIs using FastAPI

---

## How to set up

1. Clone this repo and go inside the folder

```bash
git clone <https://github.com/som24-dev/notification-service.git >
cd notification-service

2. Create and activate a virtual environment
python -m venv venv

to activate the virtual environment : venv\Scripts\activate

3. Install required packages
pip install -r requirements.txt

4. Edit the main.py file and update your MongoDB connection string
client = AsyncIOMotorClient("your-mongodb-connection-string")

5. Run the FastAPI app
uvicorn main:app --reload

6. Open your browser and go to http://127.0.0.1:8000/docs to see and test the API

API Endpoints:
POST /notifications — send/save a notification
GET /users/{user_id}/notifications — get notifications for a user

Notes:
This project doesn’t have user authentication yet.
Notifications only have user_id, type, and message.
MongoDB must be set up and accessible.

