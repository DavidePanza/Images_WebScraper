import requests
from bs4 import BeautifulSoup
import os
import urllib.parse
import time

def google_image_search(query, num_images=5):
    # Prepare the query URL for Google Images
    query_encoded = urllib.parse.quote_plus(query)
    url = f"https://www.google.com/search?q={query_encoded}&tbm=isch"
    
    # Set a User-Agent header to mimic a regular browser request.
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/102.0.0.0 Safari/537.36"
        )
    }
    
    # Make the HTTP request to get the search results page.
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Failed to retrieve search results.")
        return []
    
    # Parse the HTML with BeautifulSoup.
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Attempt to find image tags.
    # Note: Google often uses complex structures and JavaScript, so this may not capture all images.
    img_tags = soup.find_all("img")
    
    image_urls = []
    for img in img_tags:
        # The first image is typically a Google logo or similar.
        src = img.get("src")
        if src and src.startswith("http"):
            image_urls.append(src)
        if len(image_urls) >= num_images:
            break
    
    return image_urls

def download_images(image_urls, folder="downloaded_images"):
    # Create a folder to store the downloaded images if it doesn't exist.
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    for i, url in enumerate(image_urls):
        try:
            # Delay between downloads to be polite.
            time.sleep(1)
            image_data = requests.get(url).content
            image_path = os.path.join(folder, f"image_{i}.jpg")
            with open(image_path, "wb") as f:
                f.write(image_data)
            print(f"Downloaded image_{i}.jpg")
        except Exception as e:
            print(f"Error downloading {url}: {e}")

if __name__ == '__main__':
    search_query = "cute cats"
    print(f"Searching for images of: {search_query}")
    urls = google_image_search(search_query, num_images=5)
    if urls:
        print("Found image URLs:")
        for url in urls:
            print(url)
        download_images(urls)
    else:
        print("No images found.")
