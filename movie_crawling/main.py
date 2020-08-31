from selenium import webdriver
import pymssql
import time

from adp_movie import SelectMovie, ShowMovie
from adp_staff import SelectStaff, ShowStaff
from adp_cast import SelectCast
from crawling_movie import SeleniumMovie
from crawling_casting import SeleniumStaff
from moviehtml import Create_Mlist,Create_Slist,Create_Mpage,Create_Spage

driver = webdriver.Chrome('c:/python/chromedriver')
driver.get('http://naver.com')
time.sleep(10)


# ip = {your ip}
# id = {your MSSQL ID}
# pw = {you MSSQL Password}
# db = {name of DB}}
conn = pymssql.connect(server= ip, user =id, password =pw, database =db)


command = ''

while command.upper() != 'EXIT' :

    command = input('명령어를 입력해주세요 : ')

  
    if command == '1' :
        SeleniumMovie(driver)

        if command == input('결과를 보시겠습니까?') :
            ShowMovie()

    elif command == '2' :
        SeleniumStaff(driver)

        if command == input('결과를 보시겠습니까?') :
            ShowStaff()
    
    elif command == '3' :
        
        Create_Mlist(SelectMovie(conn))
        Create_Slist(SelectStaff(conn))

        for movie in movie_list:
            Create_Mpage(movie)
        for staff in staff_list:
            Create_Spage(staff)

        


          
    else :
        print('명령어는 0부터 3까지 가능합니다.')
    
