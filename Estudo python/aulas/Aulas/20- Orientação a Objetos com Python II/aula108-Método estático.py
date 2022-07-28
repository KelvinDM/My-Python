"""

MÉTODO ESTÁTICO

É qualquer método declarado na classe
contendo quaisquer parâmetros



"""

class MEstaticos:
    @staticmethod
    def func1():
        print("func1()")
    @staticmethod
    def func2(x,y):
        print("Função {} invocada.\nParams=({},{})".format("func2",x,y))
    @staticmethod
    def func3(a,b,c):
        info="""
        Nome da Função: {nome}
        Quantidade de Args: {quantidade}
        Args: {args}
        """
        info=info.format(
            nome=MEstaticos.func3.__name__,
            quantidade=MEstaticos.func3.__code__.co_argcount,
            args=MEstaticos.func3.__code__.co_varnames



        )
        print(info)

    # func1=staticmethod(func1)
    # func2=staticmethod(func2)
    # func3=staticmethod(func3)


me=MEstaticos()
me.func1()
me.func2(100,200)
me.func3(5,10,15)
