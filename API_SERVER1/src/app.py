from flask import Flask, request, jsonify
import json
import logging
import os
import requests
import simplejson

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

url='http://34.71.104.245:3000/informacion'

@app.route('/nuevo', methods = ['POST'])
def nuevo():

	datos={
		"autor":request.json['autor'],
		"nota":request.json['nota']
	}

	print(datos)
	respuesta=""
	url_infoa='http://34.72.179.225:3000/informacion'
	url_infob='http://34.72.179.225:3000/informacion'
	
	url_posta='http://34.72.179.225:3000/nuevo'
	url_postb='http://34.72.179.225:3000/nuevo'

	server1a=requests.get(url_infoa)
	infoA=json.loads(server1a.text)
	
	server1b=requests.get(url_infob)
	infoB=json.loads(server1b.text)
	
	if infoA['cantidad']>infoB['cantidad']:
		#make post to server1b
		respuesta=requests.post(url_postb,json=datos,headers={"Content-Type":"application/json"})
		print('sending server1b')
	elif infoA['cantidad']<infoB['cantidad']:
		#make post to server1a
		print('sending server1a')
		respuesta=requests.post(url_posta,json=datos,headers={"Content-Type":"application/json"})		
	else:
		if float(infoA['ram_used'])>float(infoB['ram_used']):
			#make post to server1b
			respuesta=requests.post(url_postb,json=datos,headers={"Content-Type":"application/json"})
			print('sending server1b')
		elif float(infoA['ram_used'])<float(infoB['ram_used']):
			#make post to server1a
			print('sending server1a')
			respuesta=requests.post(url_posta,json=datos,headers={"Content-Type":"application/json"})
			
		else:
			if float(infoA['cpu_used'])>float(infoB['cpu_used']):
				#make post to server1b
				respuesta=requests.post(url_postb,json=datos,headers={"Content-Type":"application/json"})
				print('sending server1b')
			elif float(infoA['cpu_used'])<float(infoB['cpu_used']):
				#make post to server1a
				print('sending server1a')
				respuesta=requests.post(url_posta,json=datos,headers={"Content-Type":"application/json"})
				
			else:
				#make post to server1a
				print('sending server1a')
				respuesta=requests.post(url_posta,json=datos,headers={"Content-Type":"application/json"})
				
	print(infoA)
	print(infoB)
	print("Esta es la respuesta ",respuesta.text)

	return (respuesta.text)

@app.route("/")
def hello():
    return "Sistemas Operativos 1"

	
if __name__ == "__main__":
    app.run(debug=1, port=3000, host='0.0.0.0')
