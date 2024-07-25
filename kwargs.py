# **kwargs = parameter that will pack all arguments into a dictionary
# useful so that a function can accept a varying amount of keyword arguments

def hello(**name):
    print("Hello ",end= " ")
    for key,value in name.items():
        print(value,end=" ")

hello(title="Mr.",first="Kiev",middle="Dev",last="Ops")
