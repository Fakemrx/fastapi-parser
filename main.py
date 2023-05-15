"""Main file of all project"""
from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo import MongoClient

config = dotenv_values(".env")

app = FastAPI()


@app.on_event("startup")
def startup_db_client():
    """Launches MongoDB after an app was started"""
    app.mongodb_client = MongoClient(config["DATABASE_URL"])
    app.database = app.mongodb_client[config["MONGO_INITDB_DATABASE"]]
    print("Connected to the MongoDB database!")


@app.on_event("shutdown")
def shutdown_db_client():
    """Shuts down DB after an app was stopped."""
    app.mongodb_client.close()
    print("MongoDB database connection were closed.")


@app.get("/ping")
def ping():
    """Check availability of server"""
    coll_example = str(app.database.list_collections().next())
    return {"Collection example": coll_example}
