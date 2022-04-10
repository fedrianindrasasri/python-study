import time

# for loop = statement perulangan yang mengeksekusi block kode yang mempunyai batas perulangan nya
# for loop = linited
# while loop = unlimited if the condition true

# for i in range(10):
#     print(i + 1)

# for i in range(50, 100 + 1, 2):
#     print(i)

# for i in "Fedrian":
#     print(i)

for seconds in range(10, 0, -1):
    print(seconds)
    time.sleep(1)
print("Selesai")
