# Data Access Object
import cx_Oracle as db

# conn() DB 접속!! 이 함수를 쓰고나면 꼭 닫아주자

def conn():
    db_id = 'hr'
    db_pw = 'hr'
    url = '192.168.21.136:1521/xe'
    con = db.connect(db_id, db_pw, url)
    return con

# insert() 회원가입
def insert(join_id, join_pw, join_name):
    con = conn()
    curs = con.cursor()
    sql = "insert into member(id, pw, name) values(:1, :2, :3)"
    curs.execute(sql, (join_id, join_pw, join_name))
    con.commit()
    curs.close()
    con.close()

# select() 전체 회원 조회
def select():
    con = conn()
    curs = con.cursor()
    sql = 'select * from member'
    rs = curs.execute(sql) # rs : result set
    result = rs.fetchall()
    r = '</br>'.join(map(str, result))
    curs.close()
    con.close()
    return r

# login() id, pw -> 로그인 성공/실패 여부
def login(login_id, login_pw):
    con = conn()
    curs = con.cursor()
    sql = f"select pw from member where id = '{login_id}'"
    rs = curs.execute(sql)
    result = rs.fetchall()
    check = False
    try:
        if result[0][0] == login_pw:
            check = True
    except:
        print("로그인 실패")
    curs.close()
    con.close()
    return check