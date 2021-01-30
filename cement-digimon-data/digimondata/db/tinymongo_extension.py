from tinymongo import TinyMongoClient, TinyMongoDatabase
from tinydb.storages import JSONStorage
from tinydb.middlewares import CachingMiddleware
import os

class TinyMongoConnection(TinyMongoClient):
    """This client has cache"""
    @property
    def _storage(self):
        return CachingMiddleware(JSONStorage)
    
    def list_database_names(self):
        databases = list(map(lambda archivo_name: archivo_name.replace('.json',''), os.listdir(self._foldername)))
        return databases

    def __getattr__(self, name):
       return customTinyMongoDatabase(name, self._foldername, self._storage) 
       
    def __getitem__(self, name):
       return customTinyMongoDatabase(name, self._foldername, self._storage) 
    
class customTinyMongoDatabase(TinyMongoDatabase):

    def list_collection_names(self):
        return self.tinydb.tables()
