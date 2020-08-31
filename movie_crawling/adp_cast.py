import pymssql
from classes import CAST

# ip = {your ip}
# id = {your MSSQL ID}
# pw = {you MSSQL Password}
# db = {name of DB}}


# 리스트(class)를 반환하는 각각의 조회(select) 메서드 구현
def existsCast(m_code,s_code):
    
    conn = pymssql.connect(server=ip, user=id, password=pw, database=db)
    cursor = conn.cursor()
    query = 'SELECT COUNT(*) FROM CAST_LIST WHERE M_CODE = {0} AND S_CODE ={1}'
    cursor.execute(query.format(m_code,s_code))

    isExist = False
    row = cursor.fetchone()[0]

    if row != 0 :
        isExist = True

    return isExist

 

def CountCast(m_code):
    conn = pymssql.connect(server=ip, user=id, password=pw, database=db)
    cursor = conn.cursor()
    query = 'SELECT COUNT(*) FROM CAST_LIST WHERE M_CODE ={0}'
    cursor.execute(query.format(m_code))
    c = cursor.fetchone()[0]
    
    return c
   
def SelectCast():
    conn = pymssql.connect(server= ip, user =id, password =pw, database =db)
    cursor = conn.cursor()
    query = 'SELECT * FROM  CAST_LIST'
    cursor.execute(query)
    

    cast_list = []

    row = cursor.fetchone()
    while row :
        m_code,s_code,act_name,role_info = row
        new_cast = CAST(m_code,s_code,act_name,role_info)

        cast_list.append(new_cast)

        row = cursor.fetchone()

    return cast_list


def InsertCast(cast):
    
    conn = pymssql.connect(server=ip, user=id, password=pw, database=db)
    cursor = conn.cursor()
    query = 'INSERT INTO CAST_LIST(M_CODE,S_CODE,ACT_NAME,ROLE_INFO) VALUES(%s,%s,%s,%s)'
    cursor.execute(query,(cast.m_code, cast.s_code, cast.act_name, cast.role_info))

    conn.commit()


