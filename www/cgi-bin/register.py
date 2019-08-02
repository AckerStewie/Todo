import psycopg2

#データベース 接続
conn = psycopg2.connect("dbname=postgres user=postgres password=password")

#カーソル取得
cur = conn.cursor()

#select文の実行
cur.execute("SELECT * FROM priorites;")

ERA = []
#for row in cur:
#    ERA.append((row[1].***,row[0))

print("""
<!DOCTYPE html>
<html lang="ja">
<head>
	<meta charset="UTF-8" />
	<title>新規登録</title>
	<link rel="stylesheet" href="../css/register.css" />
</head>
<body>
	<form action="login.py" method="post">
	<h1>新規登録</h1>
		<p>ユーザーID</p>
		<input type="text" placeholder="ユーザーIDを入力してください。" name="user_id"/>
		<p>パスワード</p>
		<input type="text" placeholder="パスワードを入力してください。" name="password"/>
		<p>パスワード再入力</p>
		<input type="text" placeholder="再度パスワードを入力してください。" name="re_password"/>
		<button>決定</button>
	</form>
</body>
</html>
""")
#try:
#except:
