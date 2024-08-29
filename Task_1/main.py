from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://lianalotarets:19980228@cluster0.yi2v1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi("1"))

# Send a ping to confirm a successful connection
try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client.cats


# Читання (Read)


def show_all():
    """
    Функція для виведення всіх записів із колекції.
    """
    result = db.cats.find({})
    for el in result:
        print(el)


def show_cat():
    """
    Функція, яка дозволяє користувачеві ввести ім'я кота та виводить інформацію про цього кота.
    """
    name = input("Enter cat's name: ")
    result = db.cats.find_one({"name": name})
    if result:
        print(result)
    else:
        print("No cat.")


# Оновлення (Update)


def new_cat_age(name: str, new_age: int):
    """
    Функція, яка дозволяє користувачеві оновити вік кота за ім'ям.
    """
    db.cats.update_one({"name": name}, {"$set": {"age": new_age}})
    result = db.cats.find_one({"name": name})
    if result:
        print("Age updated.")
    else:
        print("No cat.")


def new_cat_feature(name: str, new_feature: str):
    """
    Функцію, яка дозволяє додати нову характеристику до списку features кота за ім'ям.
    """
    result = db.cats.find_one({"name": name})
    if result:
        result["features"].append(new_feature)
        db.cats.update_one({"name": name}, {"$set": {"features": list(set(result["features"]))}})
        print('Feature added.')
    else:
        print("No cat.")


# Видалення (Delete)

def delete_cat(name: str):
    """
    Функція для видалення запису з колекції за ім'ям тварини.
    """
    db.cats.delete_one({"name": name})
    print("Record deleted.")

def delete_all():
    """
    Функція для видалення всіх записів із колекції.
    """
    db.cats.delete_many({})
    print("Records deleted.")

if __name__ == "__main__":
    show_all()
