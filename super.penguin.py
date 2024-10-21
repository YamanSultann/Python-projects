class Bird:
    def __init__(self):
        print("Bird is ready")
    
    def whoIsThis(self):
        print("Bird")
    
    def swim(self):
        print("Swim faster")

class Penguin(Bird):
    def __init__(self):
        super().__init__()
        print("The penguin is ready")

    def 