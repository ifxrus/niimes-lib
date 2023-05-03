#Запускаем в режиме отладки
import subprocess
import shutil
from pathlib import Path
import os.path
print("Отладка библиотеки")
#Скопируем текущую билиотеку по пути в KLayout
HomeDir=Path.home()# пользовательская папка
print(HomeDir)
DestinationDir= str(HomeDir)+r"\KLayout\salt\SVR_pHEMT025D"
SourceDir=r"..\SVR_pHEMT025D"
KLayoutPath1=str(HomeDir)+r"\AppData\Roaming\KLayout\klayout_app.exe"
KLayoutPath2=r"c:\Program Files (x86)\KLayout\klayout_app.exe"
#проверим сущестование
if os.path.isfile(KLayoutPath1):
    KLayoutPath=KLayoutPath1
elif os.path.isfile(KLayoutPath2):
    KLayoutPath=KLayoutPath2  
shutil.copytree(SourceDir,DestinationDir,dirs_exist_ok=True)
print("Библиотека скопирована в "+ DestinationDir)
#Запустим KLayout
print("Запускаем KLayout...")
subprocess.run(KLayoutPath)
