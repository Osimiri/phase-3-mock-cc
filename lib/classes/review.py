from classes.customer import Customer
from classes.restaurant import Restaurant

class Review:
    
    def __init__(self, customer, restaurant, rating):
        self.customer = customer 
        self.restaurant = restaurant
        self.rating = rating

        self.add_customer_to_restaurant()
        self.add_review_to_restaurant()
        self.add_restaurant_to_customer()
        self.add_review_to_customer()

    @property
    def customer(self):
        return self._customer 

    @customer.setter   
    def customer(self,customer):
        if isinstance(customer, Customer):
            self._customer = customer
        else:
            print("Customer is not an instance of customer")
            raise Exception("Customer is not an instance of customer")



    def get_restaurant(self):
        return self._restaurant 
    
    def set_restaurant(self, restaurant):
        if isinstance(restaurant, Restaurant):
            self._restaurant = restaurant
        else: 
            print("Restaurant is not an instance of customer")

            raise Exception("Restaurant is not an instance of customer")
    
    restaurant = property(get_restaurant, set_restaurant)

    @property   
    def rating(self):
        return self._rating 

    @rating.setter
    def rating(self, rating):
        if rating > 0 and rating <6:
            self._rating = rating
        else:
            print("Your rating must be a number between 1 and 5, inclusive")
            
            raise Exception("Rating must be a number between 1 and 5")


    def add_customer_to_restaurant(self):
        if self._customer not in self._restaurant.customers:
            self._restaurant.customers.append(self._customer)

    def add_review_to_restaurant(self):
        self._restaurant.reviews.append(self)

    def add_restaurant_to_customer(self): #has constraint cuz its UNIQUE list
        if self.restaurant not in self._customer.restaurants:
            self._customer.restaurants.append(self.restaurant)

    def add_review_to_customer(self):
        self._customer.reviews.append(self)



# from classes.customer import Customer
# from classes.restaurant import Restaurant

# class Review:
    
#     def __init__(self, customer, restaurant, rating):
#         self.customer = customer 
#         self.restaurant = restaurant
#         self.rating = rating

#     def customer(self):
#         return self.customer
        
    
 
#     def restaurant(self):
#         return self.restaurant
        
        
#     def rating(self):
#         # rating property goes here!
#         return self._rating 

#     def set_rating(self, rating = 5):
#         if isinstance(rating, int) and 1 <= rating <= 5:
#             self._rating = rating
#         else:
#             raise ValueError("Rating must be a number between 1 and 5")




#     def add_customer_to_restaurant(self):
#         pass

#     def add_review_to_restaurant(self):
#         pass

#     def add_restaurant_to_customer(self):
#         pass

#     def add_review_to_customer(self):
#         pass
