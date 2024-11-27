from bson.objectid import ObjectId
from pymongo import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient('') #enter your client API
db = client.cats_data_base

def full_database_info(db):
    res_lst = []
    result = db.cats_book.find({})
    for element in result:
        res_lst.append(element)
    return res_lst

def cat_info(db, cat_name):
    if db.cats_book.count_documents({"name": cat_name}):
        output = db.cats_book.find_one({"name": cat_name})
        print(f"Information about {cat_name}: ")
        return output
    else:
        return f"There is no cat with the {cat_name} name"

def renew_cats_info(db, cat_name, age):
    if db.cats_book.count_documents({"name": cat_name}):
        db.cats_book.update_one({"name": cat_name},{"$set": {"age":int(age)}})
        return cat_info(db, cat_name)
    else:
        return f"There is no cat with the {cat_name} name"
    
def add_to_features(db, cat_name, new_feature):
    if db.cats_book.count_documents({"name": cat_name}):
        db.cats_book.update_one({"name": cat_name}, {"$push": {"features": new_feature}})
        return cat_info(db, cat_name)
    else:
        return f"There is no cat with the {cat_name} name"
    
def delete_cat_document(db, cat_name):
    if db.cats_book.count_documents({"name": cat_name}):
        db.cats_book.delete_one({"name": cat_name})
        for i, element in enumerate(full_database_info(db)):
            print(f"{i+1}. {element}")
    else:
        return f"There is no cat with the {cat_name} name"

def delete_all_from_database(db):
    count = db.cats_book.count_documents({})
    if count > 0:
        db.cats_book.delete_many({})
        return full_database_info(db)
    else:
        return f"There is nothing to delete. The data base is empty"



if __name__ == "__main__":
    if len(full_database_info(db)):
         print("Complete information from data base: ")
         for i, element in enumerate(full_database_info(db)):
            print(f"{i+1}. {element}")
    else:
        print("There is no data in data base")

    cat_name = input("Enter a cat name for getting the information:")
    print(cat_info(db, cat_name))

    #enter a name of a cat and his correct age to put changes into data base
    cat_name, new_age = input("Enter a name of a cat and age you want to input separated by a white space to put changes into data base: ").split()
    print(renew_cats_info(db, cat_name, new_age))

    #enter a name of a cat and a new characteristic to add it to the data base
    input_line = input("Enter a name of a cat and new feature separated by a white space to put changes into data base: ").split()
    cat_name = input_line[0]
    new_feature = " ".join(input_line[1:])
    print(add_to_features(db, cat_name, new_feature))

    #call delete_cat_document to delete document by cat's name 
    cat_name = input("Enter a cat name for deleting all information from data base:")
    print(delete_cat_document(db, cat_name))

    #delete all documents
    print(delete_all_from_database(db))