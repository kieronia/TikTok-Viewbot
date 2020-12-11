import os,time

from selenium import webdriver, common

os.system('cls && title [TikTok Automated Viewbot]')
VIDEO_URL = input('[>] TikTok Video URL: ')

views_sent = 0
option = webdriver.ChromeOptions()
option.add_argument('lang=en')    
option.add_argument("--mute-audio")
option.add_experimental_option("excludeSwitches", ["enable-logging"])
option.add_argument("user-agent=Opera/9.80 (Android 4.1.2; Linux; Opera Mobi/ADR-1305251841) Presto/2.11.355 Version/12.10")    
def beautify(arg):
    return format(arg, ',d').replace(',', '.')


driver = webdriver.Chrome(options=option, executable_path=r"chromedriver.exe")
driver.set_window_size(800, 660)
driver.get('https://vipto.de/')
print('[!] Solve the captcha...')
captcha = True

while captcha:
    # Attempts to select the "Views" option.
    try:
        driver.find_element_by_xpath(
            '/html/body/div[4]/div[1]/div[3]/div/div[4]/div/button'
        ).click()
    except (
        common.exceptions.NoSuchElementException,
        common.exceptions.ElementClickInterceptedException
    ):
        continue
   # driver.set_window_position(-10000, 0) #remove the "#" and it'll move the window outa site. I personally like to see how it's doing
    print('[!] Running...')
    captcha = False
# Pastes the URL into the "Enter URL" textbox.
driver.find_element_by_xpath(
    '//*[@id="sid4"]/div/div/div/form/div/input'
).send_keys(VIDEO_URL)
time.sleep(0.5)

while True:
    os.system(
        f'title [TikTok Automated Viewbot] - Views Sent: {beautify(views_sent)} ^| Sending...'
    )
    waiting = True

    while waiting:
        # Clicks the "Search" button.
        time.sleep(0.5)
        driver.find_element_by_xpath(
            '//*[@id="sid4"]/div/div/div/form/div/div/button'
        ).click()
        os.system('TIMEOUT 2 >NUL')

        try:
            # Clicks the "Send Views" button.
            time.sleep(0.5)

            driver.find_element_by_xpath(
                '//*[@id="c2VuZC9mb2xsb3dlcnNfdGlrdG9V"]/div[1]/div/form/button'
            ).click()
        except (
            common.exceptions.NoSuchElementException,
            common.exceptions.ElementNotInteractableException
        ):
            continue
        else:
            views_sent += 1000
            os.system(f'title [TikTok Automated Viewbot] - Views Sent: {beautify(views_sent)}')
            waiting = False
