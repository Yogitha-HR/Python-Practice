class Calculator:
    def calc(self,a=None,b=None):
        if a is not None and b is not None:
            print(a+b)
        elif a is not None and b is None:
            print(a**2)
        else:
            print("bye")
c=Calculator()
c.calc()
c.calc(5)
c.calc(6,7)
  

