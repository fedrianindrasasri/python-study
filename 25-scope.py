# scope = wilayah tempat variable dikenali
# sebuah variable hanya dikenali dimana dia dibuat
# ada dua versi scope yaitu global dan local

name = "Indra"  # Global scope variable


def display_name():
    name = "Fedrian"  # variable local scope
    print(name)


print(name)
display_name()
