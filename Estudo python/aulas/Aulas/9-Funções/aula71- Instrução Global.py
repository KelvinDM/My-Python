"""

ESCOPO GLOBAL

É o escopo dos módulos
"""

# num=10 #ESCOPO GLOBAL
#
# print(num)

def func(): #ESCOPO LOCAL
    global num
    num=50
    print(num)

func()

print(num)