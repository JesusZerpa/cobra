
import settings,os,pathlib,requests,shutil,json,time

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
        with open(cobrapath+"/backups/"+settings.framework+".zip", 'wb') as fd:
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
        updatepath=cobrapath+"/backups/"+settings.framework+"-master/"
        with ZipFile(cobrapath+"/backups/jsee.zip", 'r') as zipObj:
            zipObj.extractall(cobrapath+"/backups/")
        for dirname, subdirs, files in os.walk(updatepath):
            for filename in files:
                elem=os.path.join(dirname, filename)[len(updatepath):]
                if elem not in ["package.json",
                                "settings.js",
                                "index.js",
                                "package-lock.json",
                                ]:

                    if os.path.exists(path+"/"+elem):

                        if os.path.isfile(path+"/"+elem):
                            os.remove(path+"/"+elem)
                            while os.path.exists(path+"/"+elem):
                                time.sleep(0.5)
                            shutil.move(updatepath+elem,path+"/"+elem)
                    else:
                     
                        try:
                            shutil.copy2(updatepath+elem,path+"/"+elem)
                        except:
                            #Si la ruta de carpetas no existe, la creara y repetira la accion de copiar el archivo                           
                            os.makedirs(path+"/"+"/".join(elem.split("/")[:-1]))
                            shutil.copy2(updatepath+elem,path+"/"+elem)

                elif elem=="package.json":
                        with open(path+"/package.json","r") as f:
                            data2=json.loads(f.read())
                        with open(updatepath+"package.json","r") as f:
                            data=json.loads(f.read())
                        data3=data2
                        for elem2 in data2["dependencies"]: 
                            for elem in data["dependencies"]:
                                if elem2==elem:
                                    break
                            else:
                                data3["dependencies"][elem]=data["dependencies"][elem]
                        with open(path+"/package.json","w") as f:
                            f.write(json.dumps(data3,indent=4, sort_keys=True))


        print("Sistema actualizado")

if not os.path.exists(cobrapath+"/settings.py"):
    print("Generando archivo de configuracion settings.py")
    shutil.copy2(cobrapath+"/settings.example.py",cobrapath+"/settings.py")

print("Selecciona las acciones que desea realizar:")
print("1) Actualizar framework")
print("2) Ver configuracion")
print("3) Editar configuracion")
print("4) Construir documentación")
print("5) Salir")
option=input("[opcion]:")
if option.strip()=="1":

    print("Actualizando framework...")
    if cobrapath!=os.getcwd():
        actualizar_framework()

    else:
        print("No se ha determinado la ubicacion de su framework respecto a cobra")
        print("Por favor indique la ruta absoluta de su framework")
        path=input("[path]:")

        if path: actualizar_framework(path=path)
        else: actualizar_framework()
elif option.strip()=="2":
    print("\nSETTINGS:\n")
    for elem in dir(settings):
        
        if (type(getattr(settings,elem))==list 
            or type(getattr(settings,elem))==str 
            or type(getattr(settings,elem))==float 
            or type(getattr(settings,elem))==int 
            or type(getattr(settings,elem))==bool 
            or type(getattr(settings,elem))==dict 
            or type(getattr(settings,elem))==tuple) and elem not in ["__builtins__"]:
            print(elem,"=",getattr(settings,elem))

elif option.strip()=="3":
    os.system("nano "+cobrapath+"/settings.py")
elif option.strip()=="4":
    
    if os.path.exists("doc/source/apps"):
        os.system("rm doc/source/apps")
    time.sleep(1)
    os.system("cd doc/source && ln -s ../../apps")
    
    with open("doc/source/index.rst") as f:
        doc=f.read()
    order=[]
    with open("doc/source/index.txt") as f:
        order=f.readlines()
    with open("doc/source/index.rst","w") as f:
        
        ini=doc.find(".. toctree::")+len(".. toctree::")
        fin=doc.find(":maxdepth:",ini)
        start=doc[:ini]+"\n"
        data=os.popen('node info.js action=get_apps').read()
        start+="   "+"   ".join(order)+"\n"
        apps=json.loads(data)
        for app in apps:
            if os.path.exists("apps/"+app+"/doc/index.rst"):
                start+="   ../../apps/"+app+"/doc/index\n"
        """
        for elem in os.listdir("doc/source/"):
            if elem.endswith(".rst") and not elem.startswith("_") and elem!="index.rst":
                start+="   "+elem+"\n"
        """
        

        start+="   "+doc[fin:]
        f.write(start)


    os.system("cd doc && make html && make latexpdf")
elif option.strip()=="5":
    print("Adios!")
