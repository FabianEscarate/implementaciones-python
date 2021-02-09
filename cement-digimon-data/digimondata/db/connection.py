from pymongo import MongoClient
from .tinymongo_extension import TinyMongoConnection

class ConnectionManager:
    Base = None
    myclient = None
    database = None

    def __init__(self, config_dict):
        _is_mongo = config_dict['is_mongo'] if 'is_mongo' in config_dict else False
        _hostname = config_dict['HOSTNAME'] if 'HOSTNAME' in config_dict else None
        _port = config_dict['PORT'] if 'PORT' in config_dict else None
        _dbname = config_dict['DBNAME'] if 'DBNAME' in config_dict else None
        _user = config_dict['USER'] if 'USER' in config_dict else None
        _pass = config_dict['PASS'] if 'PASS' in config_dict else None

        if _is_mongo:
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
                if not 'digimon-collection' in self.collections_names:
                    self.database['digimon-collection']
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
                if not 'digimon-collection' in self.collections_names:
                    self.database['digimon-collection']
                    self.database.tinydb.close()


    def insert_data_in_collection(self, collection_name, data):
        # se realiza insercion a la base de datos
        # validar si existe collecion
        result = False
        collection = None
        data_inserted = None
        try:
            collection = self.database[collection_name]
            
            data_inserted = collection.insert(data)
            self.database.tinydb.close()
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