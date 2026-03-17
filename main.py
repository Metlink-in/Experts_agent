from fastapi import FastAPI, BackgroundTasks
from scraper import scrape_marketplace
from database import db
import uvicorn
import asyncio

app = FastAPI(title="Intro.co Expert Scraper API")

# Define the scrape task to be used by both endpoint and scheduler
async def run_scrape_task():
    print("Starting scheduled scrape...")
    data = await scrape_marketplace()
    
    # Apply 20% price increase before saving to DB
    for expert in data:
        base_price = expert.get("base_price", 0)
        expert["increased_price"] = round(base_price * 1.20, 2)
        
    await db.save_experts(data)
    print(f"Successfully scraped {len(data)} experts with increased pricing.")



@app.get("/")
async def root():
    return {"message": "Welcome to the Intro.co Expert Scraper API. Go to /experts to see data."}

@app.get("/experts")
async def get_experts(background_tasks: BackgroundTasks):
    """
    Returns current experts and simultaneously triggers a background scrape 
    so the next request has fresh data.
    """
    experts = await db.get_experts()
    background_tasks.add_task(run_scrape_task)
    return {
        "count": len(experts),
        "experts": experts
    }

@app.get("/scrape")
async def trigger_scrape(background_tasks: BackgroundTasks):
    """
    Manual trigger for the scraper.
    """
    background_tasks.add_task(run_scrape_task)
    return {"status": "Scrape task initiated in background"}

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
