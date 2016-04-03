# -*- coding: utf-8 -*-
import os
import multiprocessing
import threading
from PIL import Image
import sys

class ReducePNGFolder:
    #Author: Juan Pablo Toledo Gavagnin
    '''
    # How to use #
        python scriptName.py originalFolderURI destinationFolderURI

    # Dependencies #
        This scripts needs to have previously installed Pillow:
        
            pip install pillow
     
    '''

    # Attributes
    FOLDER_ORIGINALFILES = ""
    FOLDER_REDUCEDFILES = ""
    CORES = multiprocessing.cpu_count()

    # Global lists
    listOriginalFiles = []
    listReducedFiles = []
    listFilesToProcess = []

    def __init__(self):
        self.FOLDER_ORIGINALFILES = sys.argv[1]
        self.FOLDER_REDUCEDFILES = sys.argv[2]
        self.checkFolder(self.FOLDER_ORIGINALFILES)
        self.checkFolder(self.FOLDER_REDUCEDFILES)
        self.CORES = multiprocessing.cpu_count()
        print(self.FOLDER_ORIGINALFILES + self.FOLDER_REDUCEDFILES)
        

    def main(self):
        self.listOriginalFiles = self.listFolder(self.FOLDER_ORIGINALFILES)
        self.listReducedFiles = self.listFolder(self.FOLDER_REDUCEDFILES) 
        self.listFilesToProcess = self.compareLists()
        self.divide_jobs_multithreading(self.listFilesToProcess)

    def checkFolder(self, uri):
        if not(os.path.isdir(uri)):
            print("The folder '" + uri + "' doesn't exist")
            exit()

    def listFolder(self, ROUTE):
        listFiles = os.listdir(ROUTE)
        print("There are " + str(len(listFiles)) + " files in " + ROUTE)
        return listFiles

    # Manejo de listas
    def compareLists(self):
        lista = []
        for fileItem in self.listOriginalFiles:
            if fileItem not in self.listReducedFiles:
                print("The file " + fileItem + " is not reduced")
                lista.append(fileItem)
        return lista

    def divide_jobs_multithreading(self, lista):
        # 1 - Divide elements in differents lists to give each list to a new thread
        # 2 - This script divides the list depending of the cores
        listSize = len(lista)
        listOfList = []
        sliceSize = listSize / self.CORES
        remain = listSize % self.CORES
        iterator = iter(lista)
        elemento = 1
        for i in range(self.CORES):
            listOfList.append([])
            for j in range(sliceSize):
                listOfList[i].append(iterator.next())
                elemento+=1
            if remain:
                listOfList[i].append(iterator.next())
                elemento+=1
                remain -= 1

        # With each list, we have to create a new thread to process this problem more faster
        for listThread in listOfList:
            threading.Thread(target=self.reducePicture,args=(listThread,)).start()
        

    # Generar imagen reducida
    def reducePicture(self, listFiles):
        for item in listFiles:
            print("Reducing " + item)
            imagenOriginal = Image.open(self.FOLDER_ORIGINALFILES + os.path.sep + item)
            imagenOriginal.resize((400, 400), Image.ANTIALIAS) 
            imagenOriginal.save(self.FOLDER_REDUCEDFILES + os.path.sep + item,quality=20,optimize=True)

objeto = ReducePNGFolder()
objeto.main()