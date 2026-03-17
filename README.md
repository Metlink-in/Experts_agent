# Intro.co Marketplace Scraper & API

A FastAPI project that scrapes expert details from Intro.co. It serves the data through an API with a 20% price increase and triggers a background scrape on every read request.

## Features
- **Scraper**: Crawls `https://intro.co/marketplace`.
- **FastAPI**: Serves the scraped data.
- **Price logic**: Increases expert prices by 20% in the API output.
- **Trigger-on-Read**: Hitting `/experts` returns the current data immediately and queues a background scrape to update the database for the next user.

## Local Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   python main.py
   ```

3. Trigger a scrape:
   Go to `http://localhost:8000/scrape`

4. View experts:
   Go to `http://localhost:8000/experts`

## Deployment on Vercel

1. **Connect Repository**:
   - Go to [Vercel Dashboard](https://vercel.com).
   - Click **Add New** -> **Project**.
   - Select this project repository.

2. **Environment Variables**:
   - Go to your Vercel project's **Environment Variables** tab.
   - Add your `MONGODB_URI` connection string.

3. **Deploy**:
   - Click **Deploy**. Vercel will host the FastAPI application seamlessly.
   - Note: Because scraping is triggered on an HTTP Request to `/experts`, no manual Cron setup is required!
