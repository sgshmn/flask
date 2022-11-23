# Server - DB 연동
# Server란?
# 요청(request)하면 응답(respond)하는 돌고있는 모듈. 이때 요청하는 입장을 Client라 한다. server와 client는 상대적인 개념이다

# Flask Server
# Python 언어를 활용한 Micro Web FrameWork

# Web FrameWork?
# 웹을 편리하게 개발하기 위해 만든 일정한 툴

# Flask Server 설치!
# pip install flask
# from flask import Flask
# flask 패키지 안에 여러가지 라이브러리가 있다
# Flask lib : 서버 구동!!, 웹 경로 설정
# render_template : 동일 경로에 있는 template dir에 있는 html문서를 가져온다
# request : 요청 객체!! 요청한 정보를 담고있다
# Data 전송방식 : GET, POST
# GET(Query String) : URL 뒤에 ?key1=value1&key2=value2...
# 장점 : URL을 통한 방식이기 때문에 같은 page를 볼 수 있다 
# 단점 : 보안, data길이 제한(URL은 최대 길이가 있는데 그만큼만 전송할 수 있다)
# POST : <body>태그 안에 data를 Key, Value형식으로 저장해서 전송
# 장점 : 보안
# 단점 : 같은 page를 볼수 없다.
# ('/longin') 경로에서 request를 받고 싶으면
# methods = ['GET', 'POST']
# request에서 data 꺼내기
# GET : request.args[key값]
# POST : request.form[key값]
# POST인데 file : request.file[key값]
# 하나의 경로(route)에는 함수가 하나만 정의돼야 한다
# 이 때 return에 오는 자료형은 html문서!!
# redirect : 페이지를 이동
# redirect('http://www.naver.com')
# redirect('/login') '/'로 시작하면 내 플라스크 서버에서 출발한다
# app.run(host='IPv4', port=정수형 포트번호)
# flask port number : 5000 ~ 5099
# IPv4 : 32bit (8bit x 4)

# DB연동!!
# Linux에서는 Oracle 실행 안 됨
# DBMS : DataBase Management System
# MariaDB, MySQL, MSSQL 등 다른 DB를 쓰고 싶다면?
# import cs_Oracle as db 대신
# import pymysql as db 등으로 바꾸면 된다.
# 각 DBMS가 Interface를 통해 드라이버를 개발한다
# 변수, 함수 일므이 동일해진다

# DB연동 4단계
# 1. 드라이버 로딩
# pip install cx_Oracle
# Oracle 홈페이지에서 드라이버 설치 instant-client
# 우리 오라클 버전 : 11.g xe(Express Edition) 에 맞게 설치, 아는 방법 select * from v$version
# 경로!! (환경변수 추가, 1번만 하면 된다)

# 2. 커넥션 생성
# DataBase 연결 (DB_ID, DB_PW, DB_URL)

# 3. Cursor 생성
# SQL문을 전달하고 결과를 받는다

# 4. 연결종료
# cursor 인스턴스 이름.close()
# connect() 인스턴스 이름.close()








from flask import Flask, render_template, request, redirect
import DAO


app = Flask(__name__)
@app.route('/')
def home():
    return render_template('login.html')

@app.route('/join', methods=['POST'])
def sign_up_member():
    join_id = request.form['id']
    join_pw = request.form['pw']
    join_name = request.form['name']

    DAO.insert(join_id, join_pw, join_name)

    return redirect('/') # http://192.168.21.136:5091가 / 앞에 생략되어 있다. 알아서 내 Flask 서버로 간다

@app.route('/login', methods=['POST'])
def login_member():
    login_id = request.form['id']
    login_pw = request.form['pw']
    if DAO.login(login_id, login_pw):
        return "로그인 성공"
    else:
        return "로그인 실패"

@app.route('/select')
def select_member():
    result = DAO.select()
    return result

if __name__ == "__main__":
    app.run(host='192.168.21.136', port=5091)