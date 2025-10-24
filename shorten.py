import requests
import argparse

# TinyURL API endpoint does not require an API key
API_URL = "http://tinyurl.com/api-create.php"

def shorten_url(long_url):
    """
    Shortens a long URL using the TinyURL API.

    :param long_url: The original, long URL to be shortened.
    :return: The shortened URL as a string, or None if an error occurs.
    """
    try:
        # The API expects the URL to be passed as a 'url' query parameter
        response = requests.get(API_URL, params={'url': long_url})
        
        # Raise an exception for bad status codes (4xx or 5xx)
        response.raise_for_status()

        # The response text is the shortened URL
        return response.text

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def main():
    """Main function to parse arguments and shorten the URL."""
    parser = argparse.ArgumentParser(
        description="A simple command-line URL shortener using TinyURL."
    )
    parser.add_argument(
        "url",
        type=str,
        help="The long URL you want to shorten."
    )
    args = parser.parse_args()

    long_url = args.url
    print(f"Shortening URL: {long_url}")

    short_url = shorten_url(long_url)

    if short_url:
        print("\n" + "="*20)
        print(f"Shortened URL: {short_url}")
        print("="*20)

if __name__ == "__main__":
    main()
