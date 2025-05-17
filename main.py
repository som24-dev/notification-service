from fastapi import FastAPI
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
from typing import List

app = FastAPI()

# Connect to MongoDB (replace the connection string with yours)
client = AsyncIOMotorClient("mongodb+srv://akash:<som@24>@som24.sctrevc.mongodb.net/notification_service?retryWrites=true&w=majority&appName=Som24")
db = client.notification_service  # Database name
collection = db.notifications     # Collection name

class Notification(BaseModel):
    user_id: int
    type: str
    message: str

@app.post("/notifications")
async def send_notification(notification: Notification):
    notification_dict = notification.dict()
    # Insert into MongoDB
    result = await collection.insert_one(notification_dict)
    return {"message": "Notification saved", "id": str(result.inserted_id)}

@app.get("/users/{user_id}/notifications")
async def get_user_notifications(user_id: int):
    # Fetch notifications from MongoDB for user_id
    cursor = collection.find({"user_id": user_id})
    notifications = await cursor.to_list(length=100)  # Get up to 100 notifications
    return {"user_id": user_id, "notifications": notifications}
