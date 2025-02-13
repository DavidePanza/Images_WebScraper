# 🖼️ Google Image Search Downloader

A Python-based command-line tool that downloads images from **Google Image Search** based on a given query.  
It utilizes **Selenium** to automate the search, extract image URLs, and save images to a specified directory.

## 📌 Arguments
The following command-line arguments can be passed to the script:

- **`query`** (Positional Argument):  
  The keyword or phrase to search for images.  
  Example: `"cats"` or `"sunset landscape"`.

- **`-n` or `--number_of_images`**:  
  Specify the number of images to download.  
  Example: `-n 10` to download 10 images.

- **`--max_number_of_pages`**:  
  (Optional) Set the maximum number of pages to scrape.  
  Example: `--max_number_of_pages 5` to limit scraping to 5 pages.

- **`--page_range`**:  
  (Optional) Define a custom range of pages to scrape (start and end). Useful to avoid starting from page 0 every time.  
  Example: `--page_range 1 3` to scrape pages 1 to 3.

- **`--min_image_size`**:  
  (Optional) Filter images by minimum dimensions (width and height).  
  Example: `--min_image_size 800 600` to exclude images smaller than 800x600 pixels.

- **`--output_dir`**:  
  Specify the directory where downloaded images will be saved.  
  Example: `--output_dir /path/to/output`.
  
---

## 🔧 Installation & Requirements

### **Prerequisites**
- **Python 3.9**
- **Google Chrome Browser**
- **ChromeDriver** (matching your Chrome version)
- Required Python libraries:
  ```bash
  pip install -r requirements.txt

---

## 🚀 Usage  
Run the script using the command line with your desired parameters:  
```bash  
python your_script.py "images class" -n 10 --max_number_of_pages 5 --page_range 1 3 --min_image_size 800 600 --output_dir /path/to/output


