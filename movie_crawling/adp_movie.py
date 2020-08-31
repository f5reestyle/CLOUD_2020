import pymssql
from classes import MOVIE




# 리스트(class)를 반환하는 각각의 조회(select) 메서드 구현
def ShowMovie() :
    movies = SelectMovie(conn)
    count = 1
    for m in movies:
        m.show(count)
        count += 1

def SelectMovie(conn) :
    cursor = conn.cursor()
    
    query = 'SELECT * FROM MOVIE_LIST'
    cursor.execute(query)
    

    movie_list = []

    row = cursor.fetchone()
    while row :
        code, title, score, n_reopen, c_count, img = row
        new_movie = MOVIE(code, title, score, n_reopen, c_count, img)

        movie_list.append(new_movie)

        row = cursor.fetchone()

    return movie_list




def existsMovie(code):
    
    conn = pymssql.connect(server=ip, user=id, password=pw, database=db)
    cursor = conn.cursor()
    query = 'SELECT CODE FROM MOVIE_LIST WHERE CODE = {0}'
    cursor.execute(query.format(code))

    isExist = False
    row = cursor.fetchone()

    while row :
        isExist = True
        break
    
    return isExist


def InsertMovie(movie):
    code = movie.code
    title = movie.title
    score = movie.score
    n_reopen = movie.n_reopen
    c_count = movie.c_count
    img = movie.img

    conn = pymssql.connect(server=ip, user=id, password=pw, database=db)
    cursor = conn.cursor()
    query = 'INSERT INTO MOVIE_LIST(CODE,TITLE,SCORE,N_REOPEN,CASTING_COUNT, IMG) VALUES(%s,%s,%s,%s,%s)'    
    cursor.execute(query,(code,title,score,n_reopen,c_count, img))

    conn.commit()


def AddCount(count,code):

    conn = pymssql.connect(server=ip, user=id, password=pw, database=db)
    cursor = conn.cursor()
    query = 'UPDATE MOVIE_LIST SET _COUNT = {0} WHERE CODE = {1}'.format(count,code)
    cursor.execute(query)
    
    conn.commit()
