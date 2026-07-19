class Toyota:
    def origin(self):
        print("The country of origin is Japan")
    def bestcar(self):
        print("The best car is the Hiace")
    def continent(self):
        print("The continent is on asia")

class BYD:
    def origin(self):
        print("The country of origin is china")
    def bestcar(self):
        print("The best car is the Seal")
    def continent(self):
        print("The continent is on asia")
byd = Toyota()
toyota = BYD()

for carsinnnfop in (toyota,byd):
    carsinnnfop.origin()
    carsinnnfop.bestcar()
    carsinnnfop.continent()
