from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import getpass
driver = webdriver.Chrome(executable_path='C:\\BrowserDriver\\chromedriver.exe')
# directing to the twitter login page
driver.get('https://twitter.com/login')
driver.implicitly_wait(50)

# driver.find_element_by_name('text').send_keys('@Nchii206')
# driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]').click()
# driver.find_element_by_name('password').send_keys('nguyenchi2006')
# driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div').click()

driver.find_element_by_name('text').send_keys('tranphuongnhi1009@gmail.com')
driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]').click()
driver.find_element_by_name('text').send_keys('nhi_cybergirl')
driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div').click()   
driver.find_element_by_name('password').send_keys('100903nh!')
driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div').click()

time.sleep(10)

cmt=driver.find_element('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div[1]')
cmt.send_keys('@sontungmtp777 #SonTungMTP #TheresNoOneAtAll #STANWORLD #WeStanEarth')

c=300
while(1):
    rt = driver.find_elements_by_css_selector('.css-18t94o4[data-testid ="retweet"]')
    for r in rt:
        try:
            r.click()
            driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div[2]/div[3]/div/div/div/div').click()

    # rt = driver.find_elements('#id__9680ulqze9w > div:nth-child(1) > div')
    # for r in rt:
    #     try:
    #         r.click()
    #         cmt=driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
    #         cmt.send_keys('love #SonTungMTP#TheresNoOneAtAll')
    #         cmt.send_keys(Keys.ENTER)

            c -= 1
            if(c==0):
                break
        except (ElementClickInterceptedException, StaleElementReferenceException):
            pass
           
     # scrolling to the bottom of the page
    # driver.execute_script("window.scrollTo(0,document.body.scrollHeight)") 
     # max number of retweets are achieved
    if(c==0):
        break # breaking from the retweet loop