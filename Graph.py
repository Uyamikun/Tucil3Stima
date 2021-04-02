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

#Kelas untuk menyimpan nama dan nilai g,h,f
class Simpul():
    def __init__(self, parent=None, name=None):
        #nilai parent dan position
        self.parent = parent
        self.name = name
        
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self,other):
        return self.name == other.name
    
    def __lt__(self,other):
        return float(self.f) < float(other.f)

# take f for sort
def takeF(elem):
    return float(elem.f)

#Algoritma A* untuk mencari rute
def astar(graf,start,end):
    
    #Buat simpul awal dan akhir
    start_node = Simpul(None,start)
    start_node.g = start_node.h = start_node.f =0
    end_node = Simpul(None,end)
    end_node.g = end_node.h = end_node.f =0
    
    #inisialisasi open dan closed list
    #open: live node, closed: expanded node
    open_list = []
    closed_list = []
    
    #tambahkan start node
    open_list.append(start_node)
    
    #buat list of simpul
    list_simpul = graf.getSimpul("Simpul")
    
    #indeks untuk start dan elnd
    start_index = list_simpul.index(start)
    end_index = list_simpul.index(end)
    
    #debug
    counter=1
    
    #loop sampai mencapai end
    while len(open_list) > 0:
        
        #debug
        print("Iterasi ke-"+str(counter))
        counter+=1
        
        print("OpenList:")
        for x in open_list:
            print(x.name+":"+str(x.f),end=" ")
        print("")

        print("ClosedList:")
        for x in closed_list:
            print(x.name,end=" ")
        print("")
        
        #Ambil curr node dengan f terkecil
        current_node = open_list[0]
        current_index = 0
        for item in open_list:
            if (item < current_node):
                current_node = item
                current_index = index
                
        #debug
        print ("Index:"+ str(current_index))
        print("Current node:"+current_node.name)
        
        #Pop dan masukkan ke closed list
        open_list.pop(current_index)
        closed_list.append(current_node)
        
        #Menemukan goal, catat pathnya
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                #Debug
                #print("Muncul")
                path.append(current.name)
                current = current.parent
            return path[::-1] #path adalah array yang direversed
        
        #Generate children
        list_children = graf.dictTetangga[current_node.name]
        
        children = []
        for child_element in list_children:
            #Buat simpul baru
            new_node = Simpul(current_node,child_element)
            #Append
            children.append(new_node)
        
        print("List Children:")
        for child in children:
            print(child.name,end=" ")
        print("")
        
        #Loop untuk setiap children
        for child in children:
            skip = False
            #debug
            #print("Nama child" + child.name)
            
            #Cek child apakah ada di closed list (sudah expanded)
            for closed_child in closed_list:
                if child == closed_child:
                    #debug
                    #print ("SKIP1")
                    skip = True
                    continue
            if(skip):
                continue
            
            #Mengkalkulasikan nilai f dari nilai g dan h
            child_index = list_simpul.index(child.name)
            
            #dari matrix real
            child.g = float(graf.real_distance_matrix[child_index][start_index]) 
            #dari matrix euclidean distance
            child.h = float(graf.distance_matrix[child_index][end_index])
            #f didapat dari g dan h
            child.f = child.g + child.h
            
            #Cek child apakah ada di open list (di live node) dan g lebih besar
            for open_node in open_list:
                if child == open_node and child.g >= open_node.g:
                    #debug
                    #print ("SKIP2")
                    skip = True
                    continue
            if(skip):
                continue
            
            #Tambahkan child ke open list (live node)
            open_list.append(child)
            open_list.sort(key=takeF)

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

#Print
# print("======= MATRIX REAL=======")
# graf.printMatrix("Real")
# print("====== INI SIMPUL========")
# graf.printSimpul("Simpul")
# print("====== KOORDINATNYA======")
# graf.printSisi("Sisi")

#menerima masukan astar(graf,start,end)
print(astar(graf,"Tirta Anugrah", "Depan ITB"))
print(astar(graf,"Tirta Anugrah", "MCD Dago"))


