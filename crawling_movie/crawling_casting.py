from adp_staff import existsStaff, InsertStaff
from adp_cast import existsCast, CountCast, InsertCast
from adp_movie import AddCount
import pymssql
from selenium import webdriver
from classes import CAST
from try_except import TrygetAttribute, TrygetStep5, TrygetText_xpath

# ip = {your ip}
# id = {your MSSQL ID}
# pw = {you MSSQL Password}
# db = {name of DB}}

def SeleniumStaff(driver):  # DB에서 MOVIE LIST 받아와서 M_CODE로 그 영화 해당 STAFF들 불러오고 저장하기! 이미 insert 완료됏으면
    #CAST_LIST의 M_CODE = CODE 인거 COUNT했을 때 C_COUNT와 같겠지??!

    conn = pymssql.connect(server=ip, user=id, password=pw, database=db)
    cursor = conn.cursor()
    cursor.execute('SELECT CODE, CASTING_COUNT FROM MOVIE_LIST')
    
    # cast 까지 다 insert 완료된 거 빼고 m_code list 얻기! 이거 가지고 제작진 디테일 홈페이지 들어갈것!
    movie_list = list()

    row = cursor.fetchone()
    while row :
        m_code = row[0]
        c_count = row[1]
        
        if CountCast(m_code) != c_count :             # 해당 영화 모든 staff가 다 입력된 건 아닐 경우. ->cast_list 마지막 
            movie_list.append(m_code)                # 한 명만 입력 안 된 걸수도 있음!
            
        row = cursor.fetchone()


    for m_code in movie_list:
        driver.get('https://movie.naver.com/movie/bi/mi/detail.nhn?code={0}'.format(m_code))
        
        GetMoviestaff(driver,m_code)   # 그 영화 페이지에서 배우/제작진 들어가서 배우 하나씩 정보 모으기
        

 # 이 driver 안에는 이미 movie code가 받아져서 그 상세페이지로 가있음!
def GetMoviestaff(driver,m_code):

    
    lis = driver.find_elements_by_xpath('//*[@id="content"]/div[1]/div[4]/div[1]/div/div[2]/ul/li')
    cast_list = list()

    for li in lis :
        try:
            s_code = li.find_element_by_xpath('.//p[1]/a').get_attribute('href').split('=')[1]
        except:
            continue
        

        if existsCast(m_code,s_code) == True :                 # CAST_LIST까지 안 들어간 영화만 모으기! STAFF 들어가잇을수도
           continue
        
        act_name = TrygetText_xpath(li, './/div/div/p[2]/span', 'Null')
        role_info = TrygetText_xpath(li, './/div/div/p/em', 'Null')
        

        new_cast = CAST(m_code,s_code,act_name,role_info)
        cast_list.append(new_cast)
    
    for cast in cast_list :
        s_code = cast.s_code
                    
        if existsStaff(s_code) == False :                 # staff_list 없을 경우 넣기
        
        # 배우 클릭!
            driver.get('https://movie.naver.com/movie/bi/pi/basic.nhn?code={0}'.format(s_code))
        #class step5 가 있으면 됨 -그게 바로 출생과 나라
            k_name = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[2]/div[1]/h3/a').text
            e_name = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[2]/div[1]/strong').text
            
            
            img = TrygetAttribute(driver, '//*[@id="content"]/div[1]/div[2]/div[2]/img', 'src', 'Null')
            birth, nation = TrygetStep5(driver, '//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[1]', 'Null')
            
            InsertStaff(s_code,k_name,e_name,birth,nation)
            InsertCast(cast)
        
        else:
            InsertCast(cast)
            print('staff에는 있고 cast 엔 없구만! s_code : {}'.format(s_code))
        

      
  


