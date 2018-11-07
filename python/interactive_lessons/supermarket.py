# Python Lesson 5.2 - Lists & Dictionaries

prices = {
    "strawberry": 3,
    "dragonfruit": 6,
    "mango": 4,
    "pear": 3
}

stock = {
    "strawberry": 6,
    "dragonfruit": 0,
    "mango": 32,
    "pear": 15
}

# If two dictionaries have the same keys, can loop through one dictionary & print values from both
for key in prices:
    print key
    print "Price: $%s" % prices[key]
    print "Stock: %s" % stock[key]
    print 

# Looping through both dictionaries to obtain values of each fruit key to figure out total inventory value
total = 0
for key in prices:
    print key + ": $" + str(prices[key] * stock[key])
    total = total + prices[key] * stock[key]
print "Inventory Value: $" + str(total)


# Customer-side
groceries = ["strawberry", "mango", "dragonfruit"]

def compute_bill(food):
    total = 0
    for item in food:
        if stock[item] > 0:
            stock[item] -= 1
            total += prices[item]
            # print stock[item]
    return total

print compute_bill(groceries)