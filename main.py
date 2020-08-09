
import settings,os,pathlib,requests,shutil,json

from zipfile import ZipFile
__version__="0.0.1"
print(f"Bienvenidos a Cobra {__version__}")
print("Asistente de configuracion de frameworks")
frameworks={

    "jsee":"https://gitlab.com/jesbram/jsee/-/archive/master/jsee-master.zip"
}
exclude=["cobra",
         "node_modules"
        ]
cobrapath=str(pathlib.Path(__file__).parent.absolute())
def hacer_backup():
    pass
def actualizar_framework(path=os.getcwd()):
    if settings.framework in frameworks:
        r=requests.get(frameworks[settings.framework],stream=True)
        print(cobrapath)
        with open(cobrapath+"/backups/jsee.zip", 'wb') as fd:
            for chunk in r.iter_content(chunk_size=128):
                fd.write(chunk)
        with  ZipFile(cobrapath+"/backups/backup.zip", 'w') as fd:
            for dirname, subdirs, files in os.walk(path):
                for filename in files:
                    filepath=os.path.join(dirname, filename)
                    
                    if dirname[len(os.getcwd()+"/"):].split("/")[0] not in exclude:
       
                        fd.write(filepath[len(os.getcwd()+"/"):])
            fd.close()

        

        with ZipFile(cobrapath+"/backups/jsee.zip", 'r') as zipObj:
            zipObj.extractall(cobrapath+"/backups/")

        for elem in os.listdir(cobrapath+"/backups/"+settings.framework+"-master"):
            if elem not in ["package.json",
                            "settings.json",
                            "index.js",
                            "package-lock.json",
                            ]:
                if os.path.exists(path+"/"+elem): 
                    if os.path.isfile(path+"/"+elem):
                        os.remove(path+"/"+elem)

                shutil.move(cobrapath+"/backups/"+settings.framework+"-master/"+elem,path)
            elif elem=="package.json":
                with open(path+"/package.json","r") as f:
       
                    data2=json.loads(f.read())
                with open(cobrapath+"/backups/"+settings.framework+"-master/package.json","r") as f:
                    data=json.loads(f.read())
                data3=data2
                for elem2 in data2["dependencies"]: 
                    for elem in data["dependencies"]:
                        if elem2==elem:
                            break
                    else:
                        data3["dependencies"][elem2]=data2["dependencies"][elem2]
                with open(cobrapath+"/backups/"+settings.framework+"-master/package.json","w") as f:
                    f.write(json.dumps(data3, indent=4, sort_keys=True))
        print("Sistema actualizado")

exclude=["cobra",
		 "node_modules"
		]
cobrapath=str(pathlib.Path(__file__).parent.absolute())
def hacer_backup():
	pass
def actualizar_framework(path=os.getcwd()):
	if settings.framework in frameworks:
		r=requests.get(frameworks[settings.framework],stream=True)
		print(cobrapath)
		with open(cobrapath+"/backups/jsee.zip", 'wb') as fd:
			for chunk in r.iter_content(chunk_size=128):
				fd.write(chunk)
		with  ZipFile(cobrapath+"/backups/backup.zip", 'w') as fd:
			for dirname, subdirs, files in os.walk(path):
			    for filename in files:
			    	filepath=os.path.join(dirname, filename)
			    	
			    	if dirname[len(os.getcwd()+"/"):].split("/")[0] not in exclude:
	   
	        			fd.write(filepath[len(os.getcwd()+"/"):])
			fd.close()

		

		with ZipFile(cobrapath+"/backups/jsee.zip", 'r') as zipObj:
			zipObj.extractall(cobrapath+"/backups/")
		for elem in os.listdir(cobrapath+"/backups/"+settings.framework+"-master"):
			if elem not in ["package.json",
	            				"settings.json",
	            				"index.js",
	            				"package-lock.json",
	            				]:
	            if os.path.exists(path+elem):
	            	if os.path.isdir(path+elem):
	            		shutil.rmtree(path+elem)
	            	elif os.path.isfile(path+elem):
	            		os.remove(path+elem)

				shutil.move(cobrapath+"/backups/"+settings.framework+"-master/"+elem,path)
			else:
			
				if fileName=="package.json":
					with open(path+"/package.json","r") as f:
						data2=json.loads(f.read())
					data=zip.read(path+"/package.json")
					data3=data2
					for elem2 in data2["dependencies"]: 
						for elem in data["dependencies"]:
							if elem2==elem3:
								break
						else:
							data3["dependencies"][elem2]=data2["dependencies"][elem2]
		print("Sistema actualizado")


print("Selecciona las acciones que desea realizar")
print("1)Actualizar framework")
print("2)Salir")
option=input("[opcion]:")
if option.strip()=="1":

	print("Actualizando framework...")
	if str(pathlib.Path(__file__).parent.absolute())!=os.getcwd():
		actualizar_framework()

	else:
		print("No se ha determinado la ubicacion de su framework respecto a cobra")
		print("Por favor indique la ruta absoluta de su framework")
		path=input("[path]:")

		if path: actualizar_framework(path=path)
		else: actualizar_framework()

