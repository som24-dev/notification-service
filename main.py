from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Union
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import PyMongoError
from fastapi import BackgroundTasks
import asyncio


app = FastAPI()

# MongoDB connection
try:
    client = AsyncIOMotorClient(
        "mongodb+srv://akash:som%4024@som24.sctrevc.mongodb.net/notification_service?retryWrites=true&w=majority&appName=Som24"
    )
    db = client.notification_service
    collection = db.notifications
except PyMongoError as e:
    print(" Failed to connect to MongoDB:", str(e))
    raise

# Notification schema
class Notification(BaseModel):
    user_id: Union[int, str]
    type: str
    message: str

    class Config:
        schema_extra = {
            "example": {
                "user_id": "user1",
                "type": "email",
                "message": "Hello, this is a test notification."
            }
        }

# POST: Create a notification
@app.post("/notifications")
async def send_notification(notification: Notification, background_tasks: BackgroundTasks):
    try:
        notification_dict = notification.dict()
        result = await collection.insert_one(notification_dict)

        # Add to background queue with retry logic
        background_tasks.add_task(send_with_retries, notification_dict)

        return {"message": "Notification saved", "id": str(result.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to save notification: {str(e)}")

# GET: Retrieve notifications for a user
@app.get("/users/{user_id}/notifications")
async def get_user_notifications(user_id: str):
    try:
        # to cast to int if applicable
        try:
            user_id_query = int(user_id)
        except ValueError:
            user_id_query = user_id

        cursor = collection.find({"user_id": user_id_query})
        notifications = await cursor.to_list(length=100)

        # Convert ObjectId to string
        for n in notifications:
            n["_id"] = str(n["_id"])

        return {
            "user_id": user_id_query,
            "notifications": notifications
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch notifications: {str(e)}")

async def send_with_retries(notification: dict, max_attempts: int = 3, delay: int = 2):
    for attempt in range(1, max_attempts + 1):
        try:
            # Simulate random failure
            print(f"Attempt {attempt}: Sending notification to user_id={notification['user_id']}")
            if attempt < max_attempts:
                raise Exception("Simulated failure")  # Force retry for demo
            print(" Notification sent successfully !!")
            break
        except Exception as e:
            print(f" Attempt {attempt} failed: {str(e)}")
            await asyncio.sleep(delay)
