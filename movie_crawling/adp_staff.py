import pymssql
from classes import STAFF


# ip = {your ip}
# id = {your MSSQL ID}
# pw = {you MSSQL Password}
# db = {name of DB}}


# 리스트(class)를 반환하는 각각의 조회(select) 메서드 구현
def ShowStaff() :
    staffs = SelectStaff(conn)
    count = 1
    for s in staffs:
        s.show(count)
        count += 1

def SelectStaff(conn):
    cursor = conn.cursor()
    query = 'SELECT * FROM STAFF_LIST'
    cursor.execute(query)
    

    staff_list = []

    row = cursor.fetchone()
    while row :
        code, k_name, e_name, birth, nation, img = row
        new_staff = STAFF(code, k_name, e_name, birth, nation, img)

        staff_list.append(new_staff)

        row = cursor.fetchone()

    return staff_list


def existsStaff(code):
    
    conn = pymssql.connect(server=ip, user=id, password=pw, database=db)
    cursor = conn.cursor()
    query = 'SELECT CODE FROM STAFF_LIST WHERE CODE = {0}'
    cursor.execute(query.format(code))

    isExist = False
    row = cursor.fetchone()

    while row :
        isExist = True
        break
    
    return isExist


def InsertStaff(code,k_name,e_name,birth,nation, img):

    conn = pymssql.connect(server=ip, user=id, password=pw, database=db)
    cursor = conn.cursor()
    query = 'INSERT INTO STAFF_LIST(CODE,K_NAME,E_NAME,BIRTH,NATION, IMG) VALUES(%s,%s,%s,%s,%s)'
    cursor.execute(query,(code,k_name,e_name,birth,nation, img))

    conn.commit()

