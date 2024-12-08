# pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup
import os

# URL of the webpage containing the images
url = "https://bcomik.com/893-2/"  # Replace with the actual URL

# Folder to save the downloaded images
output_folder = "bengla"
os.makedirs(output_folder, exist_ok=True)

# Fetch the webpage content
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all <img> tags within the <noscript> section
    noscript = soup.find("noscript")
    if noscript:
        images = noscript.find_all("img")

        # Loop through the images and download them
        for img in images:
            img_url = img.get("src")
            if img_url:
                # Get the image filename
                img_filename = os.path.join(output_folder, img_url.split("/")[-1])

                # Download the image
                img_data = requests.get(img_url).content
                with open(img_filename, "wb") as f:
                    f.write(img_data)

                print(f"Downloaded: {img_filename}")
    else:
        print(f"No no script")
else:
    print(f"Failed to fetch the page. Status code: {response.status_code}")
