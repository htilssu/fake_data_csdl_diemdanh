from pymongo import MongoClient

URL_CONNECTION = (
    "mongodb+srv://tolashuu:hieudz@cluster0.aw4wdjn.mongodb.net/?retryWrites=true&w=majority"
    "&appName=Cluster0")

client = MongoClient(URL_CONNECTION)

try:
    client.admin.command('ping')
    print("Kết nối đến mongodb thành công")
except Exception as e:
    print(e)

ql_DD = client.get_database("QL_DiemDanh")

studentCol = ql_DD.get_collection("student")
lecturerCol = ql_DD.get_collection("lecturer")
classCol = ql_DD.get_collection("class")
subjectCol = ql_DD.get_collection("subject")
majorCol = ql_DD.get_collection("major")
attendanceCol = ql_DD.get_collection("attendance")


