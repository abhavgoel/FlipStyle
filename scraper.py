from pinscrape import pinscrape

def pinterest_scraper(query):

    details = pinscrape.scraper.scrape(query, "output", {}, 10, 15)

    if details["isDownloaded"]:
        print("\nDownloading completed !!")
        print(f"\nTotal urls found: {len(details['extracted_urls'])}")
        print(f"\nTotal images downloaded (including duplicate images): {len(details['url_list'])}")
        print(details)
    else:
        print("\nNothing to download !!")