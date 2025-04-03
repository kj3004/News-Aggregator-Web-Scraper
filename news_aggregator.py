import requests
import pandas as pd

# Your NewsAPI key (you provided it, so I've included it here)
api_key = '1717b73408de44e88e43a05c7a8c6934'

# Function to fetch news headlines using NewsAPI
def fetch_news_headlines():
    url = f"https://newsapi.org/v2/top-headlines?apiKey={api_key}&country=us"
    response = requests.get(url)
    
    if response.status_code == 200:
        news_data = response.json()
        headlines = []
        urls = []
        
        for article in news_data['articles']:
            headlines.append(article['title'])
            urls.append(article['url'])
        
        return headlines, urls
    else:
        print(f"Failed to fetch news: {response.status_code}")
        return [], []

# Function to save the aggregated news to a CSV file
def save_to_csv(headlines, urls):
    data = {
        "Headlines": headlines,
        "URLs": urls
    }
    df = pd.DataFrame(data)

    # Save the DataFrame to a CSV file
    df.to_csv("newsapi_headlines.csv", index=False)
    print("News saved to newsapi_headlines.csv")

# Main function to aggregate the news and save it to a CSV file
def main():
    headlines, urls = fetch_news_headlines()
    save_to_csv(headlines, urls)

# Run the scraper
if __name__ == "__main__":
    main()
