# loop control statement = mengubah cara eksekusi sebuah loop dari cara yang biasanya menjadi berbeda
# break =       digunakan untuk menghentikan loop
# continue =    menlanjutkan ke iterasi selanjutnya dari loop
# pass =        betindak seperti placeholder


## BREAK
# while True:
#     name = input("Enter your name : ")
#     if name != "":
#         break

## CONTINUE
# phone_number = "123-456-789-0"
# for i in phone_number:
#     if i == "-":
#         continue
#     print(i, end="")

## PASS
for i in range(1, 21):
    if i == 13:
        pass
    else:
        print(i)
