import argparse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils import get_images_urls, download_images
import os

def readable_dir(prospective_dir):
    """Check if the provided path is a valid and readable directory."""
    if not os.path.isdir(prospective_dir):
        raise argparse.ArgumentTypeError(f"'{prospective_dir}' is not a valid directory.")
    if not os.access(prospective_dir, os.R_OK):
        raise argparse.ArgumentTypeError(f"'{prospective_dir}' is not a readable directory.")
    return prospective_dir

if __name__ == '__main__':
    # Determine the parent directory of the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)

    # Parse command-line arguments.
    parser = argparse.ArgumentParser(
        description="Google Image Search Downloader"
    )
    parser.add_argument(
        "query",
        type=str,
        help="Search query for images"
    )
    parser.add_argument(
        "-n", "--num_images",
        type=int,
        default=5,
        help="Total number of images to download (default: 5)"
    )
    parser.add_argument(
        "--output_dir",
        type=readable_dir,
        default=parent_dir,
        help=f"Directory to save images (default: parent directory of the script: '{parent_dir}')"
    )
    args = parser.parse_args()
    
    search_query = args.query
    num_images = args.num_images
    
    print(f"Searching for images of: {search_query}")
    # Set up Selenium 
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=chrome_options)

    # Get image URLs
    number_of_pages = 2    
    image_urls = get_images_urls(driver, search_query, number_of_pages)

    # Download images   
    data_dir = "../data/"
    download_images(image_urls, data_dir, search_query, number_of_images=20, check_size=(120,120))
