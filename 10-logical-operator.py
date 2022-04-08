# logical operator (and, or, not) = digunakan untuk mengecek jika dua atau lebih pernyataan kondisi adalah benar

temp = int(input("what is the temperature outside? : "))

if not (temp >= 0 and temp <= 30):
    print("the temperature is bad today!")
    print("stay inside")
elif not (temp < 0 or temp > 30):
    print("the temperature is good today!")
    print("go outside!")
