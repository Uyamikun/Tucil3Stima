class Graf(object):
    def __init__(self, size, dictgraf = None):
        #atribut
        if dictgraf is None:
            dictgraf = {}
        self.dictgraf = dictgraf
        #adj matrix size
        self.size = size
        #array adj matrix            
        self.adj_matrix = []        
        for i in range(size):
            self.adj_matrix.append([0 for i in range(size)])
    
    #method (simpul)
    def addSimpul(self,simpul):
        if simpul not in self.dictgraf:
            self.dictgraf[simpul] = []

    # delete simpul
    def delSimpul(self,simpul):
        if simpul in self.dictgraf:
            del self.dictgraf[simpul]
    
    # get jumlah simpul
    def getSimpul(self):
        return len(self.dictgraf.keys())
    

    #method (sisi)
    #add sisi
    def addSisi(self, sisi,simpul):
        if simpul in self.dictgraf:
            if len(self.dictgraf[simpul]) ==0:
                self.dictgraf[simpul] = [sisi]
            else:
                self.dictgraf[simpul].append(sisi)
    
    #delete sisi
    def delSisi(self,sisi):
        tempval = sisi
        list2 ={simpul: [a for a in sisina if a not in tempval] for simpul,sisina in self.dictgraf.items()}
        self.dictgraf = list2

    #print sisi
    def printSisi(self):
        print(list(self.dictgraf.values()))

    #method size
    def getSize(self):
        return self.size

    #method adj matridx
    def printMatrix(self):
        for i in range(self.size):
            for j in range(self.size):
                print(self.adj_matrix[i][j], end=" ")
            print("")

    def setMatrix(self,matrix):
        for baris in range(self.size):
                counter = 0
                for kolom in matrix[baris]:
                    if(kolom == "1"):
                        self.adj_matrix[baris][counter] = 1
                    counter += 1

# INISIALISASI
filename = input("Masukkan nama file kordinat (filename.txt): ")
filematrix = input("Masukkan nama file matrix (filename.txt): ")
f = open(filename, "r")
fm = open(filematrix, "r")
tempArr = []
tempMatrix = []
for item in f:
    tempArr.append(item.rstrip("\n").rsplit(','))
for item in fm:
    tempMatrix.append(item.rstrip("\n"))
# MAIN DRIVER
graf = Graf(int(tempArr[0][0]))
del tempArr[0]
graf.setMatrix(tempMatrix)