# test.py에서 생성한 test.json파일을
# mysql에 import하고
# 그 데이터를 뽑아옴

from flask import Flask
import pymysql.cursors

app = Flask(__name__)
app.debug = True
 
 
# MySQL connect
db = pymysql.connect(
        host="127.0.0.1", 
        user="root",
        passwd="whwnsgh99*", 
        db='Open_API',
        port=3306
        )

curs = db.cursor()
 
sql = "select * from test2;"
curs.execute(sql)

rows = curs.fetchall()

# db저장된 값 전체 출력
print(rows)


# # 한 행 출력
# for i in range(len(rows[0])):
#         print(rows[0][i], end=" ")


db.close()