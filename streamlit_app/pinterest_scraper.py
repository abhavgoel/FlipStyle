from pinscrape import pinscrape
from pathlib import Path

def pinterest_images(query):
    current_directory = Path(__file__).resolve().parent
    folder_path = current_directory / "pins"
    folder_path.mkdir(exist_ok=True)  # Create the "pins" directory if it doesn't exist
    
    details = pinscrape.scraper.scrape(query, folder_path, {}, 10, 15)

    if details["isDownloaded"]:
        print("\nDownloading completed !!")
        print(f"\nTotal urls found: {len(details['extracted_urls'])}")
        print(f"\nTotal images downloaded (including duplicate images): {len(details['url_list'])}")
        # print(details)
        return True
    else:
        print("\nNothing to download !!")
        return False
