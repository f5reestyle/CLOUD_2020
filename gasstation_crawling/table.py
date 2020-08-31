import pymysql



def CREATE():
    db = pymysql.connect(host='localhost',port=3303, user='study',passwd='studymysql',
                        db='oil',charset='utf8',autocommit=True)
    cursor = db.cursor()
    sql1= """
        CREATE TABLE oil.ADDRESS (
                    CITY VARCHAR(10),
                    GU VARCHAR(10)
        );
        """
    sql2="""
        CREATE TABLE oil.TANK (
                    NAME VARCHAR(10),
                    GU VARCHAR(10),
                    PRICE FLOAT,
                    SELF CHAR(1),
                    REG_DATE DATETIME DEFAULT NOW()
        );
        """
    cursor.execute(sql1)
    cursor.execute(sql2)

def TRUNCATE():
    db = pymysql.connect(host='localhost',port=3303, user='study',passwd='studymysql',
                        db='oil',charset='utf8',autocommit=True)
    cursor = db.cursor()
    sql = 'trucate table oil.ADDRESS, oil.TANK;'
    cursor.execute(sql)


def INSERT_TANK(name, gu, price, self):
    db = pymysql.connect(host='localhost',port=3303, user='study',passwd='studymysql',
                        db='oil',charset='utf8',autocommit=True)
    cursor = db.cursor()
        
    sql = f"""
        INSERT INTO oil.TANK
        VALUES(0,'{name}','{gu}',{price},'{self}',current_timestamp())"""
    
    cursor.execute(sql)

def INSERT_ADDR(city, gu):

    db = pymysql.connect(host='localhost',port=3303, user='study',passwd='studymysql',
                        db='oil',charset='utf8',autocommit=True)
    cursor = db.cursor()
        
    sql = f"""
        INSERT INTO oil.ADDRESS
        VALUES('{city}','{gu}')"""
    
    cursor.execute(sql)


def SEARCH_ADDR(gu) :
    db = pymysql.connect(host='localhost',port=3303, user='study',passwd='studymysql',
                        db='oil',charset='utf8',autocommit=True)
    cursor = db.cursor()
    sql = f"""
            SELECT COUNT(*) FROM oil.ADDRESS
            WHERE GU = '{gu}'"""
    cursor.execute(sql)
    rows = cursor.fetchone()
    return rows[0]



