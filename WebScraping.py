import os
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

url = "https://tr.pinterest.com/search/pins/?rs=ac&len=2&q=shark&eq=shar&etslf=8726"

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get(url)

image_urls = set()
scroll_pause_time = 2
max_scroll_time = 60
start_time = time.time()

while time.time() - start_time < max_scroll_time:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(scroll_pause_time)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    for img in soup.find_all('img'):
        img_url = img.get('src') or img.get('data-src')
        if img_url and img_url.startswith("http"):
            image_urls.add(img_url)

    print(f"Top Pictures: {len(image_urls)}")

    if len(image_urls) >= 200:
        break

driver.quit()

if not os.path.exists('downloaded_images'):
    os.makedirs('downloaded_images')

downloaded_count = len([name for name in os.listdir('downloaded_images') if os.path.isfile(os.path.join('downloaded_images', name))])
max_images_to_download = 200
downloaded_in_session = 0

# This part of the code was written with the help of GPT.
for img_url in image_urls:
    try:
        file_path = os.path.join('downloaded_images', f'image_{downloaded_count + downloaded_in_session}.jpg')
        img_data = requests.get(img_url).content
        with open(file_path, 'wb') as img_file:
            img_file.write(img_data)

        print(f"Image {downloaded_count + downloaded_in_session} downloaded: {img_url}")
        downloaded_in_session += 1

        if downloaded_in_session >= max_images_to_download:
            break
    except Exception as e:
        print(f"Failed to download image: {e}")
