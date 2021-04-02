class Graf(object):
    def __init__(self, size, dictgraf = None, dictTetangga = None):
        #atribut
        if dictgraf is None:
            dictgraf = {}
        self.dictgraf = dictgraf
        if dictTetangga is None:
            dictTetangga = {}
        self.dictTetangga = dictTetangga
        self.arraySimpul = []
        #adj matrix size
        self.size = size
        #array adj matrix            
        self.adj_matrix = []        
        for i in range(size):
            self.adj_matrix.append([0 for i in range(size)])
        self.distance_matrix  = []        
        for i in range(size):
            self.distance_matrix.append([0 for i in range(size)])
        self.real_distance_matrix  = []
        for i in range(size):
            self.real_distance_matrix.append([0 for i in range(size)])       
        
    #method (simpul)
    def addSimpul(self,simpul,target):
            if(target == "Simpul"):
                if simpul not in self.dictgraf:
                    self.dictgraf[simpul] = []
            elif(target == "Tetangga"):
                if simpul not in self.dictTetangga:
                    self.dictTetangga[simpul] = []
    # get simpul
    def getSimpul(self,target):
        if(target == "Simpul"):
            return list(self.dictgraf.keys())
        elif(target == "Tetangga"):
            return list(self.dictTetangga.keys())
    # printSimpul
    def printSimpul(self,target):
        if(target == "Simpul"):
            print(list(self.dictgraf.keys()))
        elif(target == "Tetangga"):
            print(list(self.dictTetangga.keys()))

    #method (sisi)
        #add sisi
    def addSisi(self, sisi,simpul,target):
        if(target == "Sisi"):
            if simpul in self.dictgraf:
                if len(self.dictgraf[simpul]) ==0:
                    self.dictgraf[simpul] = [sisi]
                else:
                    self.dictgraf[simpul].append(sisi)
        elif(target == "Tetangga"):
            simpul = self.arraySimpul[simpul]
            sisi = self.arraySimpul[sisi]
            if simpul in self.dictTetangga:
                if len(self.dictTetangga[simpul]) ==0:
                    self.dictTetangga[simpul] = [sisi]
                else:
                    self.dictTetangga[simpul].append(sisi)


        #print sisi
    def printSisi(self,target):
        if(target == "Sisi"):
            print(list(self.dictgraf.values()))
        elif(target == "Tetangga"):
            print(list(self.dictTetangga.values()))
        #get sisi
    def getSisi(self):
        if(target == "Simpul"):
            return list(self.dictgraf.values())
        elif(target == "Tetangga"):
            return list(self.dictTetangga.values())

    #method size
    def getSize(self):
        return self.size

    #method Matrix
        #print matrix
    def printMatrix(self,target):
        if(target == "Adj"):
            for i in range(self.size):
                for j in range(self.size):
                    print(self.adj_matrix[i][j], end=" ")
                print("")
        elif(target == "Euc"):
            for i in range(self.size):
                for j in range(self.size):
                    print(self.distance_matrix[i][j], end=" ")
                print("")
        elif(target == "Real"):
            for i in range(self.size):
                for j in range(self.size):
                    print(self.real_distance_matrix[i][j], end=" ")
                print("")

        #set  matrix
    def setMatrix(self,matrix,target):
        #set adj matrix sekalian dengan addSisi di dictTetangga
        if(target == "Adj"):
            for baris in range(self.size):
                counter = 0
                for kolom in matrix[baris]:
                    if(kolom == "1"):
                        self.adj_matrix[baris][counter] = 1
                        self.addSisi(counter,baris,"Tetangga")
                    counter += 1

        elif(target == "Euc"):
            for baris in range(self.size):
                counter = 0
                for kolom in matrix[baris]:
                    self.distance_matrix[baris][counter] = kolom
                    counter += 1
        
        elif(target == "Real"):
            for baris in range(self.size):
                counter = 0
                for kolom in matrix[baris]:
                    self.real_distance_matrix[baris][counter] = kolom
                    counter += 1
    
    #method array Tetangga
    def addArraySimpul(self,simpul):
        self.arraySimpul.append(simpul)

# INISIALISASI
# filename = input("Masukkan nama file kordinat (filename.txt): ")
# filematrix = input("Masukkan nama file matrix (filename.txt): ")
f = open("map.txt", "r")
fm = open("matrix.txt", "r")
fr = open("euclidean.txt", "r") #h(n)
fg = open("jarakreal.txt","r") #g(n)
tempArr = []
tempMatrix = []
tempEucledean = []
tempReal = []
for item in f:
    tempArr.append(item.rstrip("\n").rsplit(','))
for item in fm:
    tempMatrix.append(item.rstrip("\n"))
for item in fr:
    tempEucledean.append(item.rstrip("\n").rsplit(" "))
for item in fg:
    tempReal.append(item.rstrip("\n").rsplit(" "))

# MAIN DRIVER
graf = Graf(int(tempArr[0][0]))
del tempArr[0]
for item in tempArr:
    for i in range(3):
        if(i == 2):
            graf.addArraySimpul(item[i])
            graf.addSimpul(item[i],"Simpul")
            graf.addSimpul(item[i],"Tetangga")
            graf.addSisi(item[0],item[i],"Sisi")
            graf.addSisi(item[1],item[i],"Sisi")
        

graf.setMatrix(tempMatrix,"Adj")
graf.setMatrix(tempEucledean,"Euc")
graf.setMatrix(tempReal,"Real")
print("======= MATRIX REAL=======")
graf.printMatrix("Real")
print("====== INI SIMPUL========")
graf.printSimpul("Simpul")
print("====== KOORDINATNYA======")
graf.printSisi("Sisi")
