# A script to check the status of websites listed in a text file.
#
# To run this script:
# 1. Make sure you have the 'requests' library installed:
#    pip install requests
#
# 2. Save this script as 'check_websites.py'.
#
# 3. Create a text file (e.g., 'urls.txt') with one URL per line.
#    Example urls.txt content:
#    google.com
#    https://www.python.org
#    thissitedoesnotexist.xyz
#
# 4. Run the script from your terminal, passing the text file as an argument:
#    python check_websites.py urls.txt

import requests
import sys

def check_website(url):
    """
    Checks the status of a single website.
    Returns a string with the status (e.g., "ONLINE", "OFFLINE", "ERROR").
    """
    try:
        # Set headers to mimic a browser, as some sites block default python requests
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        # Make a GET request. We set a timeout of 10 seconds.
        # allow_redirects=True (which is the default) is good, as a redirect (3xx)
        # also means the site is "functional".
        response = requests.get(url, headers=headers, timeout=10)
        
        # A status code less than 400 (e.g., 200 OK, 301 Redirect)
        # generally means the site is accessible.
        if response.status_code < 400:
            return f"ONLINE (Status: {response.status_code})"
        else:
            # 4xx (e.g., 404 Not Found) or 5xx (Server Error)
            return f"OFFLINE (Status: {response.status_code})"
            
    except requests.exceptions.Timeout:
        return "ERROR: Request timed out"
    except requests.exceptions.ConnectionError:
        return "ERROR: Connection failed (e.g., DNS lookup failure, refused connection)"
    except requests.exceptions.InvalidURL:
        return "ERROR: Invalid URL format"
    except requests.exceptions.RequestException as e:
        # Catch any other request-related error
        return f"ERROR: {type(e).__name__}"

def main():
    # Check if a filename was provided as a command-line argument
    if len(sys.argv) < 2:
        print("Error: No file specified.")
        print("Usage: python check_websites.py <filename.txt>")
        sys.exit(1) # Exit the script with an error code

    filename = sys.argv[1]

    try:
        # Open and read the file
        with open(filename, 'r') as f:
            urls = f.readlines()

        if not urls:
            print(f"File '{filename}' is empty.")
            return

        print(f"Checking websites from '{filename}'...\n")

        # Process each URL
        for line in urls:
            # .strip() removes leading/trailing whitespace and newlines
            url = line.strip()
            
            if not url:
                continue  # Skip any empty lines
            
            # Simple check to add 'https://' if no scheme is present.
            # This is more reliable for the requests library.
            if not url.startswith(('http://', 'https://')):
                check_url = 'https://' + url
                print(f"[Info] No scheme found. Trying 'https://' for: {url}")
            else:
                check_url = url

            status = check_website(check_url)
            
            # Print the result in aligned columns
            # "{url:<60}" means "left-align 'url' in a 60-character wide column"
            print(f"{url:<60} | {status}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
