class Philippines:
    def language(self):
        print("The language is tagalog")
    def capital(self):
        print("The capital is Manila")
    def continent(self):
        print("The continent is on asia")

class Burkina_Faso:
    def language(self):
        print("The language is Moore")
    def capital(self):
        print("The capital is Ouagadougou")
    def continent(self):
        print("The continent is on Africa")
burkinafasos = Burkina_Faso()
philippinnestop1 = Philippines()

for country in (burkinafasos,philippinnestop1):
    country.language()
    country.continent()
    country.capital()



   
