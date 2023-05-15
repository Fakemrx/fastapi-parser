"""Main file of all project"""
from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo import MongoClient

from parsing_scripts.lamoda_parser import parse_page

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


@app.get("/clothes")
def clothes_retrieve(url_to_parse: str):
    """Page that parses lamoda's page"""
    return parse_page(url_to_parse)
