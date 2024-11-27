from pymongo import MongoClient, errors
from pymongo.server_api import ServerApi

try:
        #connecting db
        client = MongoClient("") #enter here your API

        #choosing the db
        db = client.cats_data_base

        #inserting data
        results_many = db.cats_book.insert_many(
        [   {
                "name": "barsik",
                "age": 3,
                "features": ["ходить в капці", "дає себе гладити", "рудий"],
                },
                {
                        "name": "Lama",
                        "age": 2,
                        "features": ["ходить в лоток", "не дає себе гладити", "сірий"],
                },
                {
                        "name": "Liza",
                        "age": 4,
                        "features": ["ходить в лоток", "дає себе гладити", "білий"],
                },
        ]
        )
        #in case input was completed successfully 
        print("Inserted document IDs:", results_many.inserted_ids)

except errors.ConnectionError as conn_err:
        print(f"Connection error occured: {conn_err}")

except errors.BulkWriteError as bwe:
        print(f"By inputting data an error occured: {bwe.details}")

except Exception as e:
        print(f"An error occured: {e}")