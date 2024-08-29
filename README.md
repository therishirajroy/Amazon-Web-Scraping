# Amazon-Web-Scraping
This project is a web scraper built using Python and BeautifulSoup to extract product information from Amazon. The scraper can collect data such as product titles, prices, ratings, reviews, and more, directly from Amazon's product pages.

## Features
- Extracts product titles, prices, ratings, and reviews.
- Handles pagination to scrape multiple pages.
- Stores scraped data in CSV format for easy analysis.
- Includes error handling and user-agent rotation to minimize blocking.

## Requirements
- Python 3.x
- BeautifulSoup4
- Requests
- Pandas (for data storage)

## Usage
1. Clone the repository.
2. Install the required packages using pip install -r requirements.txt.
3. Run the script and specify the product search keyword and the number of pages to scrape.
4. The scraped data will be saved in a CSV file.
