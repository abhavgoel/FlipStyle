from pinscrape import pinscrape

def pinterest_images(query):

    details = pinscrape.scraper.scrape(query, "pins", {}, 10, 15)

    if details["isDownloaded"]:
        print("\nDownloading completed !!")
        print(f"\nTotal urls found: {len(details['extracted_urls'])}")
        print(f"\nTotal images downloaded (including duplicate images): {len(details['url_list'])}")
        # print(details)
        return True
    else:
        print("\nNothing to download !!")
        return False