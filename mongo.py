from pymongo import MongoClient

URL_CONNECTION = ("mongodb+srv://tolashuu:shuu2004@cluster0.kv1ih7e.mongodb.net/?retryWrites=true&w"
                  "=majority&appName=Cluster0")

client = MongoClient(URL_CONNECTION)


try:
    client.admin.command('ping')
    print("Kết nối đến mongodb thành công")
except Exception as e:
    print(e)
