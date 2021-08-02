from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from getpass import getpass
from time import sleep

# this block of code takes user creds
print('')
print('Step 1/10: Getting Credentials....')
username = input('enter your username: ")
password = getpass('enter your password: ')
print('')
print('Step 2/10: Validating Credentials...')

# This block of code launches the browser and URL
print('')
print('Step 3/10: Launching Browser...')
browser = webdriver.Firefox()
browser.maximize_window()
browser.get('https://www.bwin.be')
print('')
print("Step 4/10: Authenticating User Credentials...")
logIn = browser.find_element_by_link_text("LOG IN")
logIn.click()

# first identify the element ID(for signing-in) in the source code of the website and store that in the variable 'signIn'
# then call the username variable  to enable signing in with the credentials that were giving
signIn = browser.find_element_by_id('userId')
signIn.send_keys(username)

# The cookies pop-up came at unpredictable intervals but needed to be accepted before proceeding
# this block here waits for 10 seconds to accept the cookies pop-up before going on to validating the password
print('')
print("Step 5/10: Accepting Relevant Cookies...")
button = browser.find_elements_by_id("onetrust-accept-btn-handler")
WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.ID,"onetrust-accept-btn-handler"))).click()  

# proceed with the validating of the password
print('')
print("Step 6/10: Validation in progress...")
passW = browser.find_elements_by_css_selector('.form-control-pw')
passW[0].send_keys(password)

#identify/locate and click on the Log in button
loginButton = browser.find_elements_by_css_selector('.login')
loginButton[0].click()

# To prevent the programme from moving on too early before page is properly loaded, the sleep function is employed here to buy time
sleep(5)

# Once logged in , my favorite menu is loaded
print('')
print('Step 7/10: Getting your favorite Menu...')
linkElem = browser.find_elements_by_css_selector('vn-menu-item.active > a:nth-child(1) > span:nth-child(1)')
sleep(5)
WebDriverWait(browser,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"vn-menu-item.active > a:nth-child(1) > span:nth-child(1)"))).click()
soccer = browser.find_elements_by_css_selector('vn-menu-item.ng-star-inserted:nth-child(3) > a:nth-child(1) > span:nth-child(2)')
WebDriverWait(browser,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"vn-menu-item.ng-star-inserted:nth-child(3) > a:nth-child(1) > span:nth-child(2)"))).click()

print('')
print('Step 8/10: Opening new tab....launching Flashscore for fixtures and H2H check!')
print('')
browser.execute_script("window.open('about:blank','tab2');")
browser.switch_to.window("tab2")
browser.get("https://www.flashscore.com/football/belgium/jupiler-league/")
sleep(5)
print('Step 9/10: Accepting Relevant cookies...')
print('')
print('Step 10/10: Opening final tab....launching Forebet for possible tips!')
browser.find_element_by_css_selector("#onetrust-accept-btn-handler").click()
browser.execute_script("window.open('about:blank','tab3');")
browser.switch_to.window("tab3")
browser.get("https://www.forebet.com/en/football-tips-and-predictions-for-belgium/jupiler-pro-league")

print('')
print("All tabs opened- GOODLUCK !!")
print('')
print('EXITING !!')
print('')
