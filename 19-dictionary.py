# dictionary = tipe data yang bisa diubah, unordered collection of unique key:value pairs
# cepat karena menggunakan hashing, mengizinkan kita mengakses value dengan cepat

capitals = {'USA': 'Washington DC',
            'India': 'New Delhi',
            'China': 'Beijing',
            'Russia': 'Moscow'
            }

print(capitals['Russia'])
print(capitals.get('Indonesia'))
print(capitals.keys())
print(capitals.values())
print(capitals.items())

capitals.update({'Indonesia': 'Jakarta'})
capitals.pop('China')
capitals.clear()

for key, value in capitals.items():
    print(key, value)
