class Otobus:
    
    def __init__(self) -> None:
        self.no = 0
        self.hici = []
        self.ctesi = []
        self.pazar = [] 
        self.duraklar = {} # isimler -> []    numaralar -> []    adresler -> []

    def read(self, file_path:str) -> None:

        print(f"Creating a bus from file path: {file_path}\n")
        
        file = open(file_path, "r")
        self.no = file.readline().strip()


        hici_count = int(file.readline().strip())
        self.hici = []
        for i in range(hici_count):
            self.hici.append(file.readline().strip())
        


        ctesi_count = int(file.readline().strip())
        self.ctesi = []
        for i in range(ctesi_count):
            self.ctesi.append(file.readline().strip())
        


        pazar_count = int(file.readline().strip())
        self.pazar = []
        for i in range(pazar_count):
            self.pazar.append(file.readline().strip())
        
        


        durak_count = int(file.readline().strip())
        self.duraklar = {}
        self.duraklar["isimler"] = []
        self.duraklar["numaralar"] = []
        self.duraklar["adresler"] = []


        for i in range(durak_count):
            self.duraklar["isimler"].append(file.readline().strip().lower())
            self.duraklar["numaralar"].append(file.readline().strip().lower()) 
            self.duraklar["adresler"].append(file.readline().strip().lower())



    def Save(self, filepath:str):
        file = open(filepath, "w")
        file.write(self.no+"\n")
        
        file.write(str(len(self.hici))+ "\n")
        for i in range(len(self.hici)):
            file.write(self.hici[i] + "\n")

        file.write(str(len(self.ctesi))+ "\n")
        for i in range(len(self.ctesi)):
            file.write(self.ctesi[i] + "\n")

        file.write(str(len(self.pazar))+ "\n")
        for i in range(len(self.pazar)):
            file.write(self.pazar[i] + "\n")
        

        file.write(str(len(self.duraklar["isimler"]))+ "\n")
        for i in range(len(self.duraklar["isimler"])):
            file.write(self.duraklar["isimler"][i] + "\n")
            file.write(self.duraklar["numaralar"][i] + "\n")
            file.write(self.duraklar["adresler"][i] + "\n")

    def update(self, no ,hici, ctesi, pazar, duraklar):
        self.ctesi = ctesi
        self.no = no
        self.duraklar = duraklar
        self.pazar = pazar
        self.hici = hici
