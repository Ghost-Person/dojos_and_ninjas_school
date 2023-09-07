from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']


    @classmethod
    def get_ninjas(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL('dojos_ninjas').query_db(query)
        ninjas = []
        for u in results:
            ninjas.append( cls(u) )
        return ninjas
    
    @classmethod
    def add_ninja(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"
        # result comes back as new row ID
        result = connectToMySQL('dojos_ninjas').query_db(query,data)
        return result
    
    @classmethod
    def ninjas_in_dojo(cls,dojo_id):
        query = "SELECT * FROM ninjas WHERE dojo_id = %(dojo_id)s";
        data = {'dojo_id': dojo_id }
        result = connectToMySQL('dojos_ninjas').query_db(query,data)
        return cls(result[0])
    

