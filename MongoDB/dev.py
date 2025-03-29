from pymongo import MongoClient

# MongoDBに接続
client = MongoClient("mongodb://admin:password@mongo:27017/")  # 接続先を適宜変更
db = client["app"]  # データベース名
collection = db["mycollection"]  # コレクション名

# 挿入するドキュメント
document = {"name": "John Doe", "age": 30, "email": "johndoe@example.com"}

# ドキュメントを挿入
result = collection.insert_one(document)

# 挿入結果を表示
print(f"ドキュメントが挿入されました。ID: {result.inserted_id}")


def find_document_by_name(name):
    """
    指定された名前でドキュメントを検索する関数
    """
    result = collection.find_one({"name": name})
    return result


# テスト: 名前でドキュメントを検索
search_name = "John Doeff"
found_document = find_document_by_name(search_name)
if found_document:
    print(f"ドキュメントが見つかりました: {found_document}")
else:
    print(f"名前 '{search_name}' のドキュメントは見つかりませんでした。")
