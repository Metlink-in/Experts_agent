import os
import json
from upstash_redis import Redis
from dotenv import load_dotenv

load_dotenv()

class Database:
    def __init__(self):
        # Use Upstash Redis for Vercel, fallback to local JSON for dev
        redis_url = os.getenv("UPSTASH_REDIS_REST_URL")
        redis_token = os.getenv("UPSTASH_REDIS_REST_TOKEN")
        
        if redis_url and redis_token:
            self.client = Redis(url=redis_url, token=redis_token)
            self.is_redis = True
        else:
            self.db_file = "experts.json"
            self.is_redis = False

    async def save_experts(self, experts):
        if self.is_redis:
            self.client.set("experts", json.dumps(experts))
        else:
            with open(self.db_file, "w") as f:
                json.dump(experts, f)

    async def get_experts(self):
        if self.is_redis:
            data = self.client.get("experts")
            return json.loads(data) if data else []
        else:
            if os.path.exists(self.db_file):
                with open(self.db_file, "r") as f:
                    return json.load(f)
            return []

db = Database()
