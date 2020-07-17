from os import getenv

MONGODB_SETTINGS = {"url": getenv("MONGO_URL", "mongodb://localhost:27017")}
