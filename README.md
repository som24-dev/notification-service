# Notification Service

This basic backend service is made using FastAPI. Allows users to send notifications (like email, SMS, or in-app) and fetch their notifications later. The data is stored in MongoDB.

---

## What it does

- **Send notifications** to users
- **Get all notifications** for a user
- **Stores notifications** in MongoDB
- Simple REST APIs using FastAPI

---
## How to set up: 
1. Clone this repo and go inside the folder
   - git clone <https://github.com/som24-dev/notification-service.git >
   - cd notification-service
2. Create and activate a virtual environment
   - python -m venv venv
3. to activate the virtual environment: 
   - venv\Scripts\activate (windows)
   - source venv/bin/activate (linux/mac)
4. Install required packages
   - pip install -r requirements.txt
5. Edit the main.py file and update your MongoDB connection string
   - client = AsyncIOMotorClient("your-mongodb-connection-string")
6. Run the FastAPI app:
   - uvicorn main:app --reload   
7. Open your browser and go to http://127.0.0.1:8000/docs to see and test the API

---
## API Endpoints:

- POST /notifications — send/save a notification

  ### send a notification:
 - Request body:

   json:

   {
    "user_id": 1,
    "type": "email",
    "message": "Hello there!"
    }

- GET /users/{user_id}/notifications — get notifications for a user

---

## Notes:

- This project doesn’t have user authentication yet.
- Notifications only have user_id, type, and message.
- Notifications are just stored — not actually sent.
- user_id can be either integer or string.
- MongoDB must be set up and accessible.

---

## Bonus Functionality (Queue & Retry)

This project includes the bonus features mentioned in the assignment:

- **Background Task (Queue Simulation):**  
  Notification sending is handled using FastAPI’s `BackgroundTasks`, which allows it to run in the background after the API request is completed. This simulates a task queue like Celery or RabbitMQ.

- **Retry Mechanism:**  
  If sending a notification fails (simulated using randomness), the system automatically retries up to 3 times with a short delay between each attempt. This adds fault tolerance to the notification system.

These features demonstrate how background processing and retry logic can be integrated into a backend system without external dependencies.

