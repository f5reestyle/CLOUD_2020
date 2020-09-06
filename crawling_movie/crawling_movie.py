from adp_movie import InsertMovie, existsMovie
from try_except import TrygetAttribute, TrygetStep5, TrygetText_xpath, TrygetText_id, TrygetReopen
from classes import MOVIE


def SeleniumMovie(driver):
    
    old_html = ''
    current_html = ''
    page = 1
    
    url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200804&page={0}'
    driver.get(url.format(page))

    
    trs = driver.find_elements_by_xpath('//*[@id="old_content"]/table/tbody/tr')
    current_html = driver.find_element_by_xpath('//*[@id="old_content"]/table/tbody').text

    while current_html != old_html :

        code_list = list()

        for tr in trs :      #각 페이지별 movie들!
            
            tds = tr.find_elements_by_xpath('.//td')
            if len(tds) == 1 :
                continue

            div = tds[1].find_element_by_xpath('.//div/a')
            code = div.get_attribute('href').split('=')[1]

            code_list.append(code)

        
        for code in code_list:

            if existsMovie(code) == True:        # DB 중복체크! 
                continue

            new_movie = SeleniumMovieDetail(driver,code)

            InsertMovie(new_movie)     # DB에 넣기! 


        page += 1
        old_html = current_html
        url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200804&page={0}'
        driver.get(url.format(page))
        
        
        current_html = driver.find_element_by_xpath('//*[@id="old_content"]/table/tbody').text
        trs = driver.find_elements_by_xpath('//*[@id="old_content"]/table/tbody/tr')




def SeleniumMovieDetail(driver, code):

    driver.get('https://movie.naver.com/movie/bi/mi/detail.nhn?code={0}'.format(code))
            
    title = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[2]/div[1]/h3/a').text
    c_count = len(driver.find_elements_by_xpath('//*[@class="lst_people"]/li'))
    img = TrygetText_xpath(driver, '//*[@id="content"]/div[1]/div[2]/div[2]/a/img', 'Null')
    score = TrygetText_id(driver,"pointNetizenPersentBasic",'0.00')
    span = driver.find_elements_by_xpath('//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[1]/p/span')
    n_reopen = TrygetReopen(span, title)


    new_movie = MOVIE(code, title,score,n_reopen,c_count,img)
    return new_movie

