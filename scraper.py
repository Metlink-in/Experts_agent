import httpx
from bs4 import BeautifulSoup
import re

async def scrape_marketplace():
    url = "https://intro.co/marketplace"
    async with httpx.AsyncClient(headers={"User-Agent": "Mozilla/5.0"}) as client:
        response = await client.get(url)
        response.raise_for_status()

    soup = BeautifulSoup(response.content, "html.parser")
    experts = []
    
    # Based on the HTML structure analyzed earlier
    cards = soup.find_all("div", class_="expert-card")
    for card in cards:
        try:
            name_el = card.find("div", class_="expert-name")
            price_el = card.find("div", class_="expert-price")
            desc_el = card.find("p", class_="expert-short-description")
            link_el = card.find("a")
            
            name = name_el.get_text(strip=True) if name_el else "N/A"
            price_text = price_el.get_text(strip=True) if price_el else "0"
            description = desc_el.get_text(strip=True) if desc_el else ""
            link = "https://intro.co" + link_el['href'] if link_el and link_el['href'].startswith('/') else (link_el['href'] if link_el else "")
            
            # Extract profile image url
            img_el = card.find("div", class_="marketplace-avatar").find("img", class_="object-center")
            image_url = img_el['src'] if img_el and img_el.has_attr('src') else ""


            # Extract price number
            # Example: "$2,000 • Session" -> 2000
            price_match = re.search(r'\$(\d+(?:,\d+)?)', price_text)
            price_val = 0.0
            if price_match:
                price_val = float(price_match.group(1).replace(',', ''))

            if "astrologer" in description.lower():
                continue

            experts.append({
                "name": name,
                "base_price": price_val,
                "description": description,
                "link": link,
                "image_url": image_url
            })
        except Exception as e:
            print(f"Error parsing expert card: {e}")
            
    return experts

if __name__ == "__main__":
    import asyncio
    data = asyncio.run(scrape_marketplace())
    print(f"Scraped {len(data)} experts")
    for e in data[:5]:
        print(e)
