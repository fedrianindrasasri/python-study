# **kwargs = parameter yang akan mempacking semua argumen ke dalam dictionary

def hello(**kwargs):
    print("Hello " + kwargs['first'])
    print("Hello", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")


hello(title="Mr.", first="Fedrian", middle="Indra", last="Sasri")
