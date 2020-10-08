from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
import json
import logging
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['MONGO_URI']='mongodb://datastore:27017/pythonmongodb'

client = PyMongo(app)

@app.route('/nuevo',methods=['POST'])
def nuevo():
	info=request.data
	try:
		id=client.db.machine.insert(
			{'autor':info['autor'],'nota':info['nota']}	
		)
		return({'exito':1})
	except:
		return({'exito':0})
	

@app.route('/informacion', methods = ['GET'])
def informacion():
	file=open('/app/ramsopes.txt','r')
	contenidoRam=file.read()
	resultado=json.loads(contenidoRam)
	usedRam=str(resultado['used'])
        
	file=open('/app/cpusopes.txt','r')
	contenidoCPU=file.read()
	resultado=json.loads(contenidoCPU)
	usedCPU=str(resultado['used'])
        
	info={
		'ram_used':usedRam,
		'cpu_used':usedCPU,
		'cantidad':client.db.machine.count_documents({})
	}
	
	return (info)

	_items =client.db.machine.find()
	items=[item for item in _items]
	
	return ({'funciona:':respuesta})

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/api', methods = ['GET','POST'])
def registro():

	return (estado)

	
if __name__ == "__main__":
    app.run(debug=1, port=3000, host='0.0.0.0')
