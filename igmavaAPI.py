from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Hello(Resource):
    def get(self):
        return "Hello World!!!"



api.add_resource(Hello, '/')


if __name__ == '__main__':
     app.run(port='8001')
        
        
#Ejemplos para tests:
#curl 127.0.0.1:5003/usuarios
#curl 127.0.0.1:5003/usuarios/9345872
#curl -X POST -d '{"id":"4", "nombre":"Juan"}' -H "Content-Type: application/json" 127.0.0.1:5003/usuarios
#curl -X DELETE 127.0.0.1:5003/usuarios/1
#curl -X PUT -d '{"nombre":"Iris"}' -H "Content-Type: application/json" 127.0.0.1:5003/usuarios/1

#curl 127.0.0.1:5003/cabanas
#curl -X PUT -d '{"estado":1}' -H "Content-Type: application/json" 127.0.0.1:5003/cabanas/1

#curl 127.0.0.1:5003/reservas

