def hotel_cost(nights):
    return 140*nights
print("Hotel cost:",hotel_cost(nights))

def plane_cost(city):
    if "Charlotte" == city:
        return 180
    elif "Tampa" == city:
        return 200
    elif "Pittsburg" == city:
        return 220
    elif "Los Angeles" == city:
        return 475
print("Plane cost:",plane_cost(city))
    
def car_rent_cost(days):
    if days < 7:
        return days*40 - 50
    elif days > 7:
        return days*40 - 20
print("Rented car cost:",car_rent_cost(days))
    
def trip_cost(nights,days,city,spending_money):