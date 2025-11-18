import pymongo
connectionstring = "mongodb+srv://ankitadas22156_db_user:ankitadas%4022156@cluster0.rqxjcm1.mongodb.net/"


def insert_document():
     # inserting a document 
    student_info = {
        "name": "Raka Mandal",
        "section": "MCA1B",
        "Mathematics": 69.6,
        "Science" : 90,
        "English": 89
    }
    student_id = collection.insert_one(student_info).inserted_id
    print(f"Student Id: {student_id} has been created. ")

if __name__ == '__main__':
    client = pymongo.MongoClient(connectionstring)
    db = client['Rai_Academy']

    # creating collection 
    collection = db.class1

    # CRUD : Create, Read, Update, Delete 

    # 1. Create: 
    # inserting a document 
    # insert_document()

    # 2.Read: 
    # Reading a collection 
    # myStudents = collection.find({})
    myStudents = collection.find({"section": "MCA1B", "name":"Raka Mandal"})
    for student in myStudents:
        print(student)
    
    