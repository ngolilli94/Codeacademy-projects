def hotel_cost(nights):
    return 140 * nights

def plane_ride_cost(city):
    if city == "Hong Kong":
        return 450
    elif city == "Seoul":
        return 360
    elif city == "Tokyo":
        return 660
    elif city == "Los Angeles":
        return 475

def rental_car_cost(days):
    daily = 40 * days
    if days >= 7:
        daily -= 50
    elif days >= 3:
        daily -= 20
    return daily

def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days - 1) + plane_ride_cost(city) + spending_money
