from pymongo import MongoClient
from config import Config

class MongoDBConnector:
    def __init__(self):
        self.client = MongoClient(Config.MONGO_URI)
        self.db = self.client[Config.DATABASE_NAME]

    def fetch_results(self, transformer_id=None):
        query = {}
        if transformer_id:
            query["transformer_identification.transformer_id"] = transformer_id
        return list(self.db[Config.COLLECTION_NAME].find(query))
