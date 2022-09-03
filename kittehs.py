from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

url = 'https://google.com/'


def kitteh():
    ffox_options = Options()
    ffox_options.headless = False
    sel = webdriver.Firefox(options=ffox_options)
    sel.maximize_window()
    sel.implicitly_wait(5)
    sel.get(url)
    sel.find_element(By.CSS_SELECTOR, '.gLFyf').send_keys('милые кошки')
    sel.find_element(By.CSS_SELECTOR, '.FPdoLc > center:nth-child(1) > input:nth-child(1)').click()
    sel.find_element(By.CSS_SELECTOR, 'div.hdtb-mitem:nth-child(2) > a:nth-child(1)').click()


if __name__ == '__main__':
    print(kitteh())
