import requests
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time


def STRtoDICT(string):
    toDICT= dict()
    items = string.replace(' ','').split('\n')
    for item in items :
        if item =='':
            return
        key, var = item.split(':',1)
        if var == '':
            toDICT[key] = None
        else:
            toDICT[key] = var
    return toDICT

def GETcity():

    cities = []
    driver = webdriver.Chrome('c:\python\chromedriver')         # chromedriver 위치 
    driver.get('http://www.opinet.co.kr/user/main/mainView.do#')
    time.sleep(3)

    driver.execute_script("goSubPage(0,0,99)")
    time.sleep(3)
    options = driver.find_elements_by_xpath('//*[@id="SIDO_NM0"]/option')
    for opt in options[1:] :
        city = opt.get_attribute('value')
        cities.append(city)
    return cities


    
def GETgu(city):  
    data_str = f'SIDO_NM: {city}'    
    headers_str = '''Accept: */*
                Accept-Encoding: gzip, deflate
                Accept-Language: ko,en;q=0.9,en-US;q=0.8
                Connection: keep-alive
                Content-Length: 53
                Content-Type: application/x-www-form-urlencoded; charset=UTF-8
                Cookie: WMONID=Me1s7WN-h4V; JSESSIONID=2Zcm5lKiJNtIA8SOoSPj5tNziunhMihxE1mloxjCUxcBmdyxVE1fM13aqeBBt6XA.opwas_1_servlet_engine2; NetFunnel_ID=
                Host: www.opinet.co.kr
                Origin: http://www.opinet.co.kr
                Referer: http://www.opinet.co.kr/searRgSelect.do
                User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36 Edg/84.0.522.63
                X-Requested-With: XMLHttpRequest
'''
    data = STRtoDICT(data_str)
    headers = STRtoDICT(headers_str)
    req = requests.post("http://www.opinet.co.kr/common/sigunguGisSelect.do", data=data, headers=headers)
    return req.json()['result']
    

def GETlist(city,gu):
    
    data_str = f'''
                BTN_DIV: os_btn
                BTN_DIV_STR: 
                POLL_ALL: all
                SIDO_NM: {city}
                SIGUNGU_NM: {gu}
                SIDO_CD: 02
                SIGUN_CD: 0209
                MAP_CENTER_X: 
                MAP_CENTER_Y: 
                MAP_ZOOM: 
                MAP_FIRST_X: 
                MAP_FIRST_Y: 
                LPG_YN: 
                SESSION_USER_ID: 
                SIDO_NM0: {city}
                SIGUNGU_NM0: {gu}
                DONG_NM: 
                GIS_X_COOR: 
                GIS_Y_COOR: 
                GIS_X_COOR_S: 
                GIS_X_COOR_E: 
                GIS_Y_COOR_S: 
                GIS_Y_COOR_E: 
                SEARCH_MOD: addr
                OS_NM: 
                OS_ADDR: 
                NORM_YN: on
                SELF_DIV_CD: on
                VLT_YN: on
                KPETRO_YN: on
                KPETRO_DP_YN: on
                POLL_DIV_CD: SKE
                POLL_DIV_CD: GSC
                POLL_DIV_CD: HDO
                POLL_DIV_CD: SOL
                POLL_DIV_CD: RTO
                POLL_DIV_CD: ETC
                '''

    headers_str = '''
            ccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
            Accept-Encoding: gzip, deflate
            Accept-Language: ko,en;q=0.9,en-US;q=0.8
            Cache-Control: max-age=0
            Connection: keep-alive
            Content-Length: 666
            Content-Type: application/x-www-form-urlencoded
            Cookie: WMONID=Me1s7WN-h4V; JSESSIONID=2Zcm5lKiJNtIA8SOoSPj5tNziunhMihxE1mloxjCUxcBmdyxVE1fM13aqeBBt6XA.opwas_1_servlet_engine2; NetFunnel_ID=5002%3A200%3Akey%3D66F831495F61E4889C8AA743ACEE3EF88B2B66F1AB982C710CC21D25225C0F9EAE99613091AF8EAD92E8D5773E9D83B45C135A6920387B774EFE75845EFC5E36EDA216B5A4016D80B04E5478C89AA3A7C05C4FB4A117B63488D854A91AD6BDF13A54157D356847B9D3C2AEE261A44BCD%26nwait%3D0%26nnext%3D0%26tps%3D0%26ttl%3D0%26ip%3Dnfl.opinet.co.kr%26port%3D443
            Host: www.opinet.co.kr
            Origin: http://www.opinet.co.kr
            Referer: http://www.opinet.co.kr/searRgSelect.do
            Upgrade-Insecure-Requests: 1
            User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36 Edg/84.0.522.63
            '''
    
    data = STRtoDICT(data_str)
    headers = STRtoDICT(headers_str)
    req = requests.post("http://www.opinet.co.kr/searRgSelect.do", data=data, headers=headers)
    return req.json()['result']




