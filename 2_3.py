#整数Nを受け取り、N以下の偶数を出力する

#func1(N)
#前から順番にコードは理解していくのでerrorとなる。

class plac:
    x = 'test'

    def f(self):
        print(self.x)

    def func1(self,n):
        for i in reversed(range(n)):
            if i%2==0 :
                print(i)
        return True

    




N = int(input('input integer number : '))
cl = plac()
cl.func1(N)
cl.f()
