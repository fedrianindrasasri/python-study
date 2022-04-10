# list =  digunakan untuk menyimpan multiple items didalam single variable
# menggunakna []

food = ["pizza", "hamburger", "hotdog", "spaghetti", "pudding"]

food[0] = "sushi"

# method di list yang berguna
food.append("ice cream")  # menambahkan list
food.remove("hotdog")  # menghapus bagian dari list
food.pop()  # menghapus index terakhir dari list
food.insert(0, "cake") # menambahkan di index 0
food.sort() # mengurutkan list
# food.clear()

print(food[0])

for x in food:
    print(x)
