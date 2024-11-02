class Bangladesh():
    def capital(self):
        print("The capital of Bangladesh is Dhaka")

    def language(self):
        print("The most common language in Bangladesh is Bangla")

    def type(self):
        print("Bangladesh is a developing country")

class England():
    def capital(self):
        print("The capital of England is London")

    def language(self):
        print("The most common language in England is English")

    def type(self):
        print("England is a developed country")

obj_bangladesh = Bangladesh()
obj_england = England()

for country in (obj_bangladesh,obj_england):
    country.capital()
    country.language()
    country.type()