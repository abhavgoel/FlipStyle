from pinscrape import pinscrape
import os
def pinterest_images(query):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    folder_path = os.path.join(current_directory,"pins")
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