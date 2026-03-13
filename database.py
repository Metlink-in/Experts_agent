import os
import asyncio
import certifi
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()

class Database:
    def __init__(self):
        self.uri = os.getenv("MONGODB_URI")
        self.db_name = os.getenv("DB_NAME", "intro_scraper")
        self.collection_name = os.getenv("COLLECTION_NAME", "experts")
        
        if self.uri:
            self.client = AsyncIOMotorClient(self.uri, tlsCAFile=certifi.where())
            self.db = self.client[self.db_name]
            self.collection = self.db[self.collection_name]
            self.is_connected = True
            print("MongoDB Atlas connection initialized with SSL certs.")
        else:
            self.is_connected = False
            print("WARNING: MONGODB_URI not found in .env. Falling back to memory/local storage.")

    async def save_experts(self, experts):
        """
        Deletes all existing records and inserts new ones.
        """
        if not self.is_connected:
            # Fallback for local testing without DB
            print("Local Fallback: Saving experts to experts.json")
            import json
            with open("experts.json", "w") as f:
                json.dump(experts, f)
            return

        try:
            # Delete old data
            delete_result = await self.collection.delete_many({})
            print(f"Deleted {delete_result.deleted_count} old experts.")
            
            # Insert new data
            if experts:
                insert_result = await self.collection.insert_many(experts)
                print(f"Inserted {len(insert_result.inserted_ids)} new experts.")
        except Exception as e:
            print(f"Error saving to MongoDB: {e}")

    async def get_experts(self):
        if not self.is_connected:
            # Fallback for local testing
            import json
            if os.path.exists("experts.json"):
                with open("experts.json", "r") as f:
                    return json.load(f)
                return []
            return []

        try:
            cursor = self.collection.find({}, {"_id": 0})
            experts = await cursor.to_list(length=1000)
            return experts
        except Exception as e:
            print(f"Error fetching from MongoDB: {e}")
            return []

db = Database()
