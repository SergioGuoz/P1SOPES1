import os
import random 
import requests 

pathFile=""
direccion=""
contenido=""
usuarios=['Juan Guzman','Jose Perez','Maria Salazar','Alejandra Gonzales','Pedro Fernandez','Manual Villa','Maria Fernanda','Mynor Poc','Sandra Gomez','Felix Ramirez','Samuel Alonzo']
objetos=[]
arregloOraciones=[]
def menu():
	os.system('clear') 
	print ("=================================================")
	print ("                    Menu                        ")
	print ("=================================================")
	print ("\t1. - Ingresar ruta archivo")
	print ("\t2. - Ingresar direccion (url)")
	print ("\t3. - Ver datos")
	print ("\t4. - Enviar datos")
	print ("\t5. - Salir")

def getRandomAutor():
	posicion=random.randrange(0, 9,1)
	return usuarios[posicion]

while True:
	menu()
	opcionMenu = str(raw_input("Selecciona una opcion: "))
	print ("-------------------------------------------------")
 	
	if opcionMenu=="1":
		try:
			pathFile=raw_input("Ingresa la ruta del archivo:")
			print("La direccion es: ",pathFile)
			objetos=[]
			f = open(pathFile,"r")
			contenido=f.read()
			f.close()
			contenido=contenido.replace('\n','')
			arregloOraciones=contenido.split('.')
			for oracion in arregloOraciones:
				if oracion!='':
					autor=getRandomAutor()
					dato={
						"autor":autor,
						"nota":oracion
					}
					objetos.insert(1,dato)
			pass
		except Exception as e:
			print(e);
			raw_input("Existe un error al leer archivo")
		

	elif opcionMenu=="2":
		print("")
		pathFile=raw_input("Ingresa la direccion url:")
		print("La url es:",pathFile)
		raw_input("Presiona enter para continar. ")

	elif opcionMenu=="3":
		print(objetos)
		print ("-------------------------------------------------")
		raw_input("Presiona enter para continuar")
	
	elif opcionMenu=="4":
		try:
			for nota in objetos:
				print("sending... ",nota);
				respuesta=requests.post(direccion,json=nota,headers={"Content-Type":"application/json"})
				print('Respuesta: ',respuesta.text)
			pass
		except Exception as e:
			print('Ocurrio un error al enviar datos')
		
		raw_input("Presione enter para continuar")
		
	elif opcionMenu=="5":
		break
	else:
		#/home/sergio/Escritorio/SOPES1/P1SOPES1/prueba.txt
		#C:\Users\sergi\Desktop\SOPES1_P1\prueba.txt
		print ("")
		raw_input("Opcion Incorrecta")
		print("")