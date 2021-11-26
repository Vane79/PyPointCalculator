from creds import login, pwd
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

url = 'https://admin.keywording.pro/'


def selenium():
    ffox_options = Options()
    ffox_options.headless = True
    sel = webdriver.Firefox(options=ffox_options)
    sel.implicitly_wait(5)
    sel.get(url)
    sel.find_element_by_id('loginform-email').send_keys(login)
    sel.find_element_by_id('loginform-password').send_keys(pwd)
    sel.find_element_by_name('login-button').click()
    sleep(1)
    sel.find_element_by_css_selector('li.treeview:nth-child(3)').click()
    sel.find_element_by_css_selector('li.treeview:nth-child(3)').click()
    sel.find_element_by_css_selector('.fa-line-chart').click()
    photos = sel.find_element_by_xpath(
        '/html/body/div[1]/div/section[2]/div/div/div[2]/div[3]/table/tfoot/tr/td[3]').text
    videos = sel.find_element_by_xpath(
        '/html/body/div[1]/div/section[2]/div/div/div[2]/div[3]/table/tfoot/tr/td[4]').text
    sel.quit()
    return photos, videos


if __name__ == '__main__':
    print(selenium())
