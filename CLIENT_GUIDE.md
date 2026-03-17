# Client Guide: Expert Marketplace Automation

This document explains how your automated expert data system works and what items are needed for setup.

## 1. How the System Works (Simplified)

Your system is fully automated and ensures fresh data without needing scheduled tasks. It uses a "Trigger-on-Read" structure.

```mermaid
graph LR
    A[Intro.co Website] -->|Auto-Fetch| B(Smart Scraper)
    B -->|Calculate +20% Price| C[Secure Database]
    C -->|Feed Data| D[Your API Service]
    D -->|Ready for use| E[Client Frontend/App]
```

1.  **Instant Content**: When your app or website calls the "Get Experts" link, it instantly gets the saved experts.
2.  **Automatic Data Sync**: At the exact same time, the server silently starts visiting the marketplace in the background to fetch new data for the *next* visitor.
3.  **Price Adjustment**: It automatically adds **20%** to the expert's original price.
4.  **Secure Storage**: The updated data (names, descriptions, and new prices) is stored safely in your database.

---

## 2. Requirements for Setup (Credentials)

To keep this system running, you will need to provide the following two services:

### A. Database (MongoDB Atlas)
This is where the expert information is stored.
- **What we need**: A **MongoDB Connection String**.
- **Example**: `mongodb+srv://user:password@cluster.mongodb.net/`
- **Purpose**: Allows the system to save and retrieve the experts.

### B. Hosting Account (Vercel)
This is where the code "lives". 
- **Requirement**: A Vercel account.
- **Purpose**: Runs the API and handles the background scraping process whenever data is requested.

---

## 3. Data Points Provided

For every expert, the system provides:
- **Name**: The expert's full name.
- **Biography**: Their professional description.
- **Original Price**: The price shown on the source website.
- **Your Price**: The price with your **20% markup** applied.
- **Profile Link**: A direct link to their page.

---

*This system is designed for high reliability and zero manual intervention.*
