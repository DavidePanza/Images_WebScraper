import argparse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils import get_images_urls, download_images
from parser import parse_arguments
import os

if __name__ == '__main__':
    """
    Main function to execute the Google Image Search Downloader.

    This function parses command-line arguments to determine the search query,
    number of images to download, page range, output directory, and minimum image size.
    It then sets up a headless Chrome browser using Selenium, retrieves image URLs
    based on the search query, and downloads the specified number of images
    to the designated output directory.

    Example command-line usage:
        python your_script.py "puppies" -n 10 --max_number_of_pages 5 --page_range 1 3 --min_image_size 800 600 --output_dir /path/to/output 
    """

    # Determine the parent directory of the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)

    # Parse the arguments
    args = parse_arguments()
    search_query = args.query
    num_images = args.num_images
    page_range = tuple(args.page_range) if args.page_range else None
    max_number_of_pages = args.max_number_of_pages
    min_image_size = tuple(args.min_image_size) if args.min_image_size else (120, 120)
    output_dir = args.output_dir
    
    print(f"Searching for images of: {search_query}")
    # Set up Selenium 
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=chrome_options)

    # Get image URLs 
    image_urls = get_images_urls(driver, search_query, max_number_of_pages)

    # Download images   
    download_images(image_urls, output_dir, search_query, number_of_images=num_images, check_size=min_image_size)
