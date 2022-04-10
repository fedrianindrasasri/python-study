# exception = events yang terdeteksi selama exsekusi yang mengganggu alur program

try:
    numerator = int(input("Enter a number to devide : "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
    # print(result)
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero! idiot")
except ValueError as e:
    print(e)
    print("Enter only number please")
except Exception as e:
    print(e)
    print("something went wrong :(")
else:
    print(result)
finally:
    print("Thank you")  # akan selalu dieksekusi
