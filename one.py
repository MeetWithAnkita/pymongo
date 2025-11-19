import pymongo
connectionstring = "mongodb+srv://ankitadas22156_db_user:ankitadas%4022156@cluster0.rqxjcm1.mongodb.net/"


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<INSERT>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def insert_document():
     # inserting a document 
    student_info = {
        "name": "Mamoni Bera",
        "Depertment": "MCA",
        "Year": "2nd year",
        "section": "C",
        "Mathematics": 89,
        "Science" : 85,
        "English": 90
    }
    student_id = collection.insert_one(student_info).inserted_id
    print(f"Student Id: {student_id} has been created. ")  #student_id no got in terminal is "Object_id"


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<READ>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#  two types of find() funtion : 
# a. collection.find() ==>> that gives output of value and attribute names , if give criteria [like {"section": "MCA1B"} ] then show all documents , not need to use mystudents.values()
# b. collection.find_one() ==>> that gives output of only attribute bcz using these function these become "ONE dictionary". then have to use mystudents.values() then show only value but only first document not all 
def read_documents(): 
    myStudents = collection.find({})
    for student in myStudents: 
        print(student)

    # myStudents = collection.find_one({"section" : "MCA1B"})
    # for student in myStudents.values():
    #     print(student)


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<UPDATE>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def update_documets():
    collection.update_one({"section":"MCA2B"},{'$set':{"section":"MCA2B[U]"}})  #$set for array, string 
    collection.update_one({"section":"MCA2B[U]"},{'$inc':{"Mathematics": -2}})  #$inc for numerical data  
    # 1st case: section modify 
    # 2nd case: using modify section name , increse -2 number of mathematics


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<DELETE>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def delete_document():
    # r = collection.delete_one({ "name": "Rai Singha"})
    # print(r.deleted_count) #delete object = r

    r = collection.delete_many({})
    print(r.deleted_count) #delete object = r




if __name__ == '__main__':
    client = pymongo.MongoClient(connectionstring)
    db = client['Rai_Academy']

    # creating collection 
    collection = db.class2 #class1 is a folder under "Rai_Academy", collection is just a attribute 
 
    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<CRUD : Create, Read, Update, Delete>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # 1. Create: 
    # insert_document()

    # 2.Read: 
    # read_documents()

    # 3.Update: 
    # update_documets()

    # 4.Delete: 
    # delete_document()