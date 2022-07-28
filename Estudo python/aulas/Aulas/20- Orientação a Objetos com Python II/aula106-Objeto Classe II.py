"""

Continuação nos otros arquivos


"""


class MinhaClasse:
    membro_cls=50#---------------- membro CLS -------
    def __init__(self):
        self.membro_inst=-10



    def func(self):
        print(self.membro_inst)
        print(self.membro_cls)
        print(MinhaClasse.membro_cls)


i1=MinhaClasse()
i2=MinhaClasse()

print(MinhaClasse.membro_cls)
print(i1.membro_cls)
print(i2.membro_cls)

print(50*'-')
i1.membro_cls=1000
# MinhaClasse.membro_cls=1000
print(MinhaClasse.membro_cls)
print(i1.membro_cls)
print(i2.membro_cls)



# i1.membro_inst=10
# print("i1:"+str(i1.membro_inst))
# print("i2:"+str(i2.membro_inst))
#
# MinhaClasse.membro_cls=9
#
# print(50*'-')
# print("i1:"+str(i1.membro_cls))
# print("i2:"+str(i2.membro_cls))