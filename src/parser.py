import argparse
import os

def readable_dir(prospective_dir):
    """Check if the provided path is a valid and readable directory."""
    if not os.path.isdir(prospective_dir):
        raise argparse.ArgumentTypeError(f"'{prospective_dir}' is not a valid directory.")
    if not os.access(prospective_dir, os.R_OK):
        raise argparse.ArgumentTypeError(f"'{prospective_dir}' is not a readable directory.")
    return prospective_dir

def parse_arguments():
    """
    Parses command-line arguments for the Google Image Search Downloader.

    Returns:
        argparse.Namespace: An object containing all parsed arguments.

    Arguments:
        query (str): The search query for retrieving images.
        -n, --num_images (int): Number of images to download (default: 5).
        --max_number_of_pages (int): Maximum pages to scrape (default: 2).
        --page_range (int, int): Start and end page numbers to scrape (optional).
        --min_image_size (int, int): Minimum width and height for images (optional).
        --output_dir (str): Directory to save downloaded images (default: parent directory of the script).
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)

    parser = argparse.ArgumentParser(description="Google Image Search Downloader")
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
        "--max_number_of_pages",
        type=int,
        default=2,
        help="Maximum number of Google Images result pages to parse (default: %(default)s)"
    )
    parser.add_argument(
        "--page_range",
        type=int,
        nargs=2,
        metavar=('START', 'END'),
        help="Range of pages to parse, specified as two integers: start and end (e.g., --page_range 0 2)"
    )
    parser.add_argument(
        "--min_image_size",
        type=int,
        nargs=2,
        metavar=('WIDTH', 'HEIGHT'),
        help="Minimum image dimensions to download, specified as two integers: WIDTH and HEIGHT (e.g., --min_image_size 800 600)"
    )
    parser.add_argument(
        "--output_dir",
        type=readable_dir,
        default=parent_dir,
        help=f"Directory to save images (default: parent directory of the script: '{parent_dir}')"
    )
    return parser.parse_args()