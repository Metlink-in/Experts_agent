# Intro.co Marketplace Scraper & API

A FastAPI project that scrapes expert details from Intro.co every 15 minutes and serves the data through an API with a 20% price increase.

## Features
- **Scraper**: Periodically crawls `https://intro.co/marketplace`.
- **FastAPI**: Serves the scraped data.
- **Price logic**: Increases expert prices by 20% in the API output.
- **Scheduled**: Runs every 15 minutes using Vercel Cron Jobs.

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

1. **Vercel KV (Redis)**:
   - Go to your Vercel Dashboard.
   - Storage -> Create Database -> Redis (KV).
   - Go to Settings -> Environment Variables.
   - Copy `UPSTASH_REDIS_REST_URL` and `UPSTASH_REDIS_REST_TOKEN` to your project's Environment Variables.

2. **Deploy**:
   ```bash
   vercel
   ```

The Cron job is configured in `vercel.json` to run every 15 minutes.
