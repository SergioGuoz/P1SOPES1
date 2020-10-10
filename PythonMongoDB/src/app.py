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
		autor=request.json['autor']
		nota=request.json['nota']
		try:
			id=client.db.notas.insert(
				{'autor':autor,'nota':nota}
			)
			return({'exito':1})
        except:
			return({'exito':0})
	

@app.route('/elementos',methods=['GET'])
def getElementos():
		items=client.db.notas.find()
		respuesta=[]
		contador=0
		for item in items:
			registro={
				"indice":contador,
				"autor":item['autor'],
				"nota":item['nota']
			}
			contador=contador+1
			respuesta.insert(1,registro)
		return (json.dumps(respuesta))

@app.route('/ram',methods=['GET'])
def getRam():
	file=open('/app/ramsopes.txt','r')
	contenidoRam=file.read()
	resultado=json.loads(contenidoRam)
	usedRam=str(resultado['used'])
	return({'ram':usedRam})

@app.route('/cpu',methods=['GET'])
def getCPU():
		file=open('/app/cpusopes.txt','r')
		contenidoCPU=file.read()
		resultado=json.loads(contenidoCPU)
		usedCPU=str(resultado['used'])
		return({'cpu':usedCPU})

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
		'cantidad':client.db.notas.count_documents({})
	}
	return (info)
        

@app.route("/")
def hello():
	return "Hello World!"

@app.route('/api', methods = ['GET','POST'])
def registro():
	return (estado)

	
if __name__ == "__main__":
	app.run(debug=1, port=3000, host='0.0.0.0')
