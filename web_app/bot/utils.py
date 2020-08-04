import os
import time
from random import randint
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image


def screen_by_url(message, **kwargs):
    bot = kwargs.get('bot')
    url = message.text
    tok = randint(10, 10**4)
    png_name = f"sqreen-{tok}.png"
    pdf_name = f"sqreen-{tok}.pdf"

    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver', 
    						  chrome_options=chrome_options)
    driver.get(url)
    time.sleep(2)

    height = driver.execute_script("return document.documentElement.scrollHeight")
    driver.set_window_size(1920, height)
    time.sleep(2)

    driver.save_screenshot(png_name)
    driver.quit()

    photo = open(png_name, 'rb')
    bot.send_photo(message.chat.id, photo)
    photo.close()

    img_png = Image.open(png_name)
    img_pdf = img_png.convert('RGB')
    img_pdf.save(pdf_name)

    with open(pdf_name, 'rb') as doc_pdf:
    	bot.send_document(message.chat.id, doc_pdf)

    try:
    	os.remove(png_name)
    	os.remove(pdf_name)
    except:
        pass
