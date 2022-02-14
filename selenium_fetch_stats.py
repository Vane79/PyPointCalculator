from creds import login, paswd
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

url = 'https://admin.keywording.pro/'


def selenium():
    ffox_options = Options()
    ffox_options.headless = True
    sel = webdriver.Firefox(options=ffox_options)
    sel.implicitly_wait(5)
    sel.get(url)
    sel.find_element(By.CSS_SELECTOR, '#loginform-email').send_keys(login)
    sel.find_element(By.CSS_SELECTOR, '#loginform-password').send_keys(paswd)
    sel.find_element(By.CSS_SELECTOR, '.col-xs-4').click()
    sleep(1)
    sel.find_element(By.CSS_SELECTOR, 'li.treeview:nth-child(3)').click()
    sel.find_element(By.CSS_SELECTOR, 'li.treeview:nth-child(3)').click()
    sel.find_element(By.CSS_SELECTOR, '.fa-line-chart').click()
    # sel.find_element(By.CSS_SELECTOR, '.fa-line-chart').click()
    photos = sel.find_element(By.CSS_SELECTOR,
                              '.kv-table-footer > td:nth-child(3)').text
    videos = sel.find_element(By.CSS_SELECTOR,
                              '.kv-table-footer > td:nth-child(4)').text
    sel.quit()
    return photos, videos


if __name__ == '__main__':
    print(selenium())
