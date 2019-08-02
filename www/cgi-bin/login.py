import psycopg2
import cgi

#データベース 接続
conn = psycopg2.connect("dbname=postgres user=postgres password=password")

#カーソル取得
cur = conn.cursor()

#select文の実行
cur.execute("SELECT * FROM priorites;")

#結果の出力
#for row in cur:
#    print(str(row[0]) + row[1])


form = cgi.FieldStorage()
user_id = form.getvalue('user_id','')

print("""
<!DOCTYPE html>
<html lang="ja">
<head>
	<meta charset="UTF-8" />
	<title>ログイン</title>
	<link rel="stylesheet" href="../css/login.css" />
</head>

<body>
    <form action="/cgi-bin/todo.py" method="post">
        <h1>ToDo</h1>
        <input type="text" placeholder="ユーザーID" name="user_id"
        value={user_id}>
        <input type="password" placeholder="パスワード" name="password"/>
        <button type="submit">ログイン</button>
        <a href="register.py">新規登録</a>
    </form>""".format(user_id=user_id))

print(user_id)


print("""    
</body>
</html>
"""
)