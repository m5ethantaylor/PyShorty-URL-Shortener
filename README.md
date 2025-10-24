# PyShorty - A Simple URL Shortener

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)

**PyShorty** is a command-line tool that shortens long URLs using the TinyURL API. It's a lightweight and fast way to make your links more manageable directly from your terminal.

## Features

-   **Simple Interface**: Just provide a long URL and get a short one back.
-   **Reliable**: Powered by the free and public TinyURL API.
-   **Error Handling**: Provides clear feedback if the network request fails.
-   **No API Key Needed**: The TinyURL API used in this project is public and does not require registration or an API key.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/pyshorty-url-shortener.git
    cd pyshorty-url-shortener
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required dependencies:**
    The only dependency is the `requests` library.
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To shorten a URL, run the `shorten.py` script from your terminal and pass the long URL as an argument.

**Important:** Make sure to wrap your URL in quotes (`"`) if it contains special characters like `&` or `?`.

```bash
python shorten.py "YOUR_LONG_URL"
```

### Example

```bash
python shorten.py "https://www.amazon.com/dp/B08C76W233/ref=sspa_dk_detail_0?psc=1&pd_rd_i=B08C76W233&pd_rd_w=lUu7F"
```

**Output:**
```
Shortening URL: https://www.amazon.com/dp/B08C76W233/ref=sspa_dk_detail_0?psc=1&pd_rd_i=B08C76W233&pd_rd_w=lUu7F

====================
Shortened URL: https://tinyurl.com/2p8a9y3z
====================
```

## How It Works

This script sends an HTTP GET request to the `tinyurl.com/api-create.php` endpoint. The long URL is passed as a query parameter. If the request is successful, the API returns a plain text response containing only the shortened URL, which the script then prints to the console.

## License
This project is licensed under the MIT License.
