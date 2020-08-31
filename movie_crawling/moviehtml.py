import pymssql
from classes import MOVIE, STAFF, CAST
from adp_staff import SelectStaff
from adp_movie import SelectMovie

# ip = {your ip}
# id = {your MSSQL ID}
# pw = {you MSSQL Password}
# db = {name of DB}}


def Create_Mpage(movie) :
    
    m_link ='m{}.html'.format(movie.code)

    head_movie = '''
    <div>
        <h2 >{0}</h2>  
        <div>네티즌 평점: {1}</div>
        <div>재개봉 횟수: {2}</div>
    </div>'''.format(movie.title,movie.score,movie.n_reopen)
    
    li_text = ''
    cursor = conn.cursor()
    q = '''
    SELECT C.ACT_NAME
	, C.ROLE_INFO
    , S.CODE
    , S.K_NAME
    , S.E_NAME
    , S.BIRTH
    , S.NATION
    FROM CAST_LIST C
    INNER JOIN STAFF_LIST S ON S.CODE = C.S_CODE
    WHERE C.M_CODE = {0}'''.format(movie.code)
    cursor.execute(q)
    row = cursor.fetchone()
    while row :   # 그 movie 찍은 배우 loop. list 만들어서 li_text 꾸밈과 동시에 spage 만들기.
        act_name, role_info, s_code, k_name, e_name, birth, nation = row
        staff = STAFF(s_code,k_name, e_name, birth, nation)

        s_link = 's{}.html'.format(s_code)

        li_text +='''<li>
        <a href ='{0}' title='{1}'>{2}</a>
        <div>{3}</div>
        <div>{4}</div>
        <div>{5}</div> 
        </li>'''.format(s_link,s_code,k_name,e_name,role_info,act_name)

        row = cursor.fetchone()
    
    body_movie = '''    
    <div>
        <ul>
        {0}
        </ul>
    </div>
'''.format(li_text)

    html_text_movie = """
<html>
	<head>
    <title>{0}</title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	</head>
	<body>{1}

        <table>
            <tr>
                <th> {3}</th>
            </tr>
        {2}
        </table>
	
	</body>
</html>
""".format(movie.code,head_movie,body_movie,movie.title)

    with open(m_link, 'w', encoding='UTF-8', newline='') as f:
        f.write(html_text_movie)
    
    
    


def Create_Spage(staff) :

    s_link = 's{}.html'.format(staff.code)

    head_staff = '''
    <div> 
        <h2>{0}</h2>  
        <div>{1}</div>
        <div>{2}년 출생</div>
        <div>{3} 출신</div>
    </div>'''.format(staff.k_name,staff.e_name,staff.birth,staff.nation)

    cursor = conn.cursor()
    q = '''
    SELECT C.ACT_NAME
    , C.ROLE_INFO
    , M.CODE
    , M.TITLE                       
    FROM CAST_LIST C
    INNER JOIN MOVIE_LIST M ON M.CODE = C.M_CODE
    WHERE C.S_CODE = {0}'''.format(staff.code)
    cursor.execute(q)
    div_text = ''
    row = cursor.fetchone()
    while row :   # 그 배우가 찍은 movie list 만들기! title 누르면 m 상세페이지로 가도록!
        act_name, role_info, m_code, title = row
        m_link = 'm{}.html'.format(m_code)

        div_text +='''<li>
            <a href="{0}">{1}</a>
            <div>{2}</div>
            <div>{3}</div>
        </li>'''.format(m_link,title, role_info, act_name)

        row = cursor.fetchone()
    
    body_staff = '''    
    <div>
        <ul>
        {0}
        </ul>
    </div>
'''.format(div_text)
    
    html_text_staff = """
<html>
	<head>
    <title>{0}</title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	</head>
	<body>{1}

        <table>
            <tr>
                <th> {3}</th>
            </tr>
        {2}
        </table>
	</body>
</html>
""".format(staff.code,head_staff,body_staff,staff.k_name)

    with open(s_link, 'w', encoding='UTF-8', newline='') as f:
        f.write(html_text_staff)
  
    



## main page 만들기 시작!
def Create_Mlist(movie_list):

    li_text =''

    
    for movie in movie_list :

        m_link = 'm{}.html'.format(m_code)

        li_text += """
            <li> 
                <a href ='{1}' title ='{2}'>{3}</a>
            </li>
    """.format(m_link, movie.title, movie.title)

        

    html_text_main = """
                        <html>
                            <head>
                            <title> Movie List</title>
                            <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
                            </head>
                            <body>
                                <div>
                                    <h1> Movie List</h1>
                                </div>
                                <ol>
                                {0}
                                </ol>
                            
                            </body>
                        </html>
""".format(li_text)


    with open('MOVIE_LIST.html', 'w', encoding='UTF-8', newline='') as f:
        f.write(html_text_main)


def Create_Slist(staff_list):
    
    
    li_text =''

    
    for staff in staff_list :

        s_link = 's{}.html'.format(s_code)

        li_text += """
            <li> 
                <a href ='{1}' title ='{2}'>{3}</a>
            </li>
    """.format(s_link, staff.code, staff.k_name)

        



    html_text_main = """
                        <html>
                            <head>
                            <title> Staff List</title>
                            <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
                            </head>
                            <body>
                                <div>
                                    <h1> Staff List</h1>
                                </div>
                                <ol>
                                {0}
                                </ol>
                            
                            </body>
                        </html>
""".format(li_text)


    with open('STAFF_LIST.html', 'w', encoding='UTF-8', newline='') as f:
        f.write(html_text_main)
  







