import pymongo

connectionstring = "mongodb+srv://ankitadas22156_db_user:ankitadas%4022156@cluster0.rqxjcm1.mongodb.net/"
#mongodb atlas password: ankitadas@22156    # "@" ==after decode==>> "%40"
# mongodb username: ankitadas22156@gmail.com [ankitadas22156_db_user]


if __name__ == '__main__':
    # making connection with mongoclient
    client = pymongo.MongoClient(connectionstring)
    # getting database 

    db = client['test-database'] #"test-database" is a database ==> Folder
    # A collection is a group of documents stored in MongoDB,
    #  and can be thought of as roughly the equivalent of a table
    #  in a relational database. Getting a collection in PyMongo works
    #  the same as getting a database:

    #    collection = db['test-collection']
    posts = db.posts  #posts ==> folder under db[test-database]
    
    post_id = posts.insert_one({"p":1}).inserted_id  #document store in .json file 
    print(post_id)

    # one data may have multiple collection ,also one collection may have multiple documents
    #  in MONGO Db , each and every document may create in different schema , the can add ed in 


