from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninjas import Ninja



class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_ninjas').query_db(query)
        dojos = []
        for u in results:
            dojos.append( cls(u) )
        return dojos
    
    @classmethod
    def update(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        # result comes back as new row ID
        result = connectToMySQL('dojos_ninjas').query_db(query,data)
        return result
    
    @classmethod
    def add_ninjas_to_dojo(cls,data):
        query = "INSERT INTO dojos (first_name, last_name, age) VALUES (%(first_name)s, %(last_name)s, %(age)s);"
        return connectToMySQL('dojos_ninjas').query_db(query, data)
    
    @classmethod
    def get_dojo_w_ninjas(cls,data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        result = connectToMySQL('dojos_ninjas').query_db(query,data)
        dojo = cls(result[0])
        for row_from_db in result:
            if row_from_db['dojo_id'] == None:
                break
            ninja_data = {
                "id": row_from_db['ninjas.id'],
                "first_name": row_from_db['first_name'],
                "last_name": row_from_db['last_name'],
                "age": row_from_db['age'],
                "created_at": row_from_db['ninjas.created_at'],
                "updated_at": row_from_db['ninjas.updated_at'],
                "dojo_id": row_from_db['dojo_id']
            }
            dojo.ninjas.append(Ninja(ninja_data))
        
        return dojo
