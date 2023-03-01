import statistics

class Restaurant:
    all = []

    def __init__(self, name):
        if type(name) == str:
            self._name = name
            
            Restaurant.all.append(self)
        else:
            print("The restaurant name must be a string!")

            raise Exception("The restaurant name must be a string!")

        self.reviews = []
        self.customers = []

        

    # @property
    # def name(self):
    #     return self._name

    def get_name(self):
        return self._name

    name = property(get_name)

    def reviews(self):
        return self.reviews

    def get_average_rating(self):
        total = 0

        for review in self.reviews:
            total += review.rating

        average = total / len(self.reviews)   

    #METHOD ONE 
        # return average 

    #METHOD TWO
        # return sum([review.rating for review in self.reviews]) / len(self.reviews)
    
    #METHOD THREE
        return statistics.mean([review.rating for review in self.reviews])

    @classmethod
    def get_all_restaurants(cls):
        return cls.all



# class Restaurant:
#     all = []

#     def __init__(self, name, reviews = 0):
#         self._name = name
#         self.reviews = reviews
#         pass

#     def name(self):
#         return self._name
    
#     def set_name(self,name):
#         if isinstance(name,str):
#             self._name = name
#         else:
#             raise Exception("Name must be a string")

#     name = property(name,set_name)

#     def reviews(self):
#         return self.reviews

#     def get_average_rating(self):
#         statistics.mean(self.rating)
#         pass #relationship thing

#     @classmethod
#     def get_all_restaurants(cls):
#         pass