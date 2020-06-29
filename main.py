from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time,os,requests
import random
driver=None
play_time=0 # 이벤트를 참여하고 몇분후에 컴퓨터를 종료할것인지 설정한다.
def open_site():
    global driver
    options = Options()
    options.add_argument('headless')
    options.add_argument('--start-fullscreen')
    options.add_argument("disable-gpu")
    url="http://fifaonline4.nexon.com/main/index"
    driver = webdriver.Chrome(executable_path='', chrome_options=options) #크롬드라이버의 위치를 저장해야한다.
    driver.get(url)
    time.sleep(random.random()+2)
    driver.execute_script("top.PS.nxlogin.showLoginLayer(); return false;")

def log_in():
    id='' #id 와 pw 입력.
    pw=''

    driver.find_element_by_xpath('//*[@id="txtNexonID"]').send_keys(id)
    driver.find_element_by_xpath('//*[@id="txtPWD"]').send_keys(pw)
    # 로그인 버튼을 눌러주자.
    time.sleep(random.random()+5)
    driver.find_element_by_xpath('//*[@id="btnLogin"]').click()

def play_yoot():
    time.sleep(play_time-900)
    time.sleep(random.random()+3)
    driver.get('https://events.fifaonline4.nexon.com/200123/sticknori?utm_source=pc&utm_medium=mainMiddle&utm_campaign=200123_yutnori')
    driver.execute_script("$f.cookie.set('lessonLayerPopupCheck', true, 7); layerPopupClose('lesson'); return false;")
    chance=driver.find_element_by_xpath('//*[@id="divPlayInfo"]/button/p[2]').text
    time.sleep(random.random()+3)
    while chance != '0회 가능' :
        driver.find_element_by_xpath('//*[@id="divPlayInfo"]/button').click()
        time.sleep(random.random()+3)
        driver.refresh()
        time.sleep(random.random()+3)
    driver.quit()

def shutdown():
    global play_time
    time.sleep(random.random()+3)
    driver.get('https://events.fifaonline4.nexon.com/200123/pointshop?utm_source=pc&utm_medium=mainMiddle&utm_campaign=200123_pointshop')
    time.sleep(random.random()+2)
    driver.execute_script("PointShop.GetTodayPoint(this, 0, 0); return false;") #내포인트 조회하기 눌러줌.
    time.sleep(random.random()+5)
    time_text=driver.find_element_by_xpath('//*[@id="userTodayPoint"]').text
    play_time=(18-int(time_text))*10*60
    os.system('shutdown -s -t '+str(play_time))

open_site()
log_in()
shutdown()
play_yoot()
