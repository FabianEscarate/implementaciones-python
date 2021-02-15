from pymongo import MongoClient
from .tinymongo_extension import TinyMongoConnection

class ConnectionManager:
    Base = None
    myclient = None
    database = None
    __private_collectionName = 'digimon-collection'

    def __init__(self, config_dict):
        self._is_mongo = config_dict['is_mongo'] if 'is_mongo' in config_dict else False
        _hostname = config_dict['HOSTNAME'] if 'HOSTNAME' in config_dict else None
        _port = config_dict['PORT'] if 'PORT' in config_dict else None
        _dbname = config_dict['DBNAME'] if 'DBNAME' in config_dict else None
        _user = config_dict['USER'] if 'USER' in config_dict else None
        _pass = config_dict['PASS'] if 'PASS' in config_dict else None

        if self._is_mongo:
            # configuracion con mongoDB
            self.myclient = MongoClient('mongodb://{hostname}:{port}'.format(hostname=_hostname, port=_port))
            database_list = self.myclient.list_database_names()
            if _dbname in database_list:
                self.database = self.myclient[_dbname]
                self.collections_names = self.database.list_collection_names()
            else:
                # creacion de db
                self.database = self.myclient[_dbname]
                # creacion de collection
                self.collections_names = self.database.list_collection_names()
                if not self.__private_collectionName in self.collections_names:
                    self.database[self.__private_collectionName]
        else:
            # configuracion de manera 'localFile' con tinymongo
            self.myclient = TinyMongoConnection('database')
            # base de datos creada
            database_list = self.myclient.list_database_names()
            if _dbname in database_list:
                self.database = self.myclient[_dbname]
                self.collections_names = self.database.list_collection_names()
            else:
                # creacion de db
                self.database = self.myclient[_dbname]
                # creacion de collection
                self.collections_names = self.database.list_collection_names()
                if not self.__private_collectionName in self.collections_names:
                    self.database[self.__private_collectionName]
                    self.database.tinydb.close()

    def open(self):
        if self._is_mongo is False:
            if self.database.tinydb._opened is False:
                self.database = self.myclient[self.database.dbName]

    def close(self):
        if self._is_mongo is False:
            if self.database.tinydb._opened:
                self.database.tinydb.close() 

    def insert_data_in_collection(self, collection_name, data):
        # se realiza insercion a la base de datos
        # validar si existe collecion
        result = False
        collection = None
        data_inserted = None
        try:
            self.open()
            collection = self.database[collection_name]
            current_data_name = list(map(lambda x : x['name'], collection.find()))
            data_to_insert = list(filter(lambda x: not x["name"] in current_data_name, data))
            collection.insert(data_to_insert)
            data_inserted = list(data_to_insert)
            self.close()
            result = {
                "success": True,
                "data": data_inserted
            }
        except Exception as _ex:
            result = {
                "success" : False,
                "message" : _ex
            }

        return result

    def Buscar(self, id=None, name=None, level=None):
        query = {}
        result_data = None
        result = {
            "success" : False,
            "message" : ''           
        }
        collection = self.database[self.__private_collectionName]

        if id is not None:
            # obtener digimon por id
            query["_id"] = id
            result_data = list(collection.find(query))
        elif name is not None:
            # obtener digimon por nombre
            query["name"] = name
            result_data = list(collection.find(query))
        elif level is not None:
            # obtener digimon por level
            query["level"] = level
            result_data = list(collection.find(query))
        else:
            # mostrar todos 
            result_data = list(collection.find())

        if len(result_data) == 0:
            result["message"] = """no data finded or database it's empty"""
        else:
            result["success"] = True
            result["data"] = result_data

        return result