import os
import pymongo
from pymongo import MongoClient
from bson import ObjectId
from contextlib import contextmanager

@contextmanager
def connect_mongo():
    client = MongoClient(os.getenv("MONGO_URI"))
    try:
        yield client
    finally:
        client.close()

def get_nex_account_by_pid(pid):
    with connect_mongo() as client:
        db = client.pretendo
        collection = db.nexaccounts
        result = collection.find_one({"pid": pid})
        if result is None:
            return None
        return result

# Example usage
if __name__ == "__main__":
    pid = 12345
    account = get_nex_account_by_pid(pid)
    print(account)
