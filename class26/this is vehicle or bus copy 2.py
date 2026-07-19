class bird:
    def __init__(self):
        print("ready bird")
    
    def who(self):
        print("Bird")
    
    def what(self):
        print("swimming")

class penguin(bird):
    def __init__(self):
        super().__init__()
        print("penguin is ready")
    def who(self):
        print("penguin")
    def what(self):
        print("Running")

p = penguin()

p.who()
p.what()

    



        






