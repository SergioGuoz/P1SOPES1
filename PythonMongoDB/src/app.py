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


@app.route('/informacion', methods = ['GET'])
def informacion():
	try:
		with open('/usr/src/ramsopes.txt') as ramContent:
			resultado=json.loads(ramContent)
			usedRam=str(resultado['used'])

		with open('/usr/src/cpusopes.txt') as cpuContent:
			resultado=json.loads(cpuContent)
			usedCPU=str(resultado['used'])

		info={
			'ram_used':usedRam,
			'cpu_used':usedCPU,
			'cantidad':client.db.machine.count_documents({})
		}
		return(info) 
		pass
	except Exception as e:
		print('Error')


	id=client.db.machine.insert(
		{'RAM':'23%','PROCESSOR':'24%'}	
	)
	respuesta={
		'mirespuesta':1,
		'id_mongo':id
		}
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
