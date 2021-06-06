class base1(object):
    def __init__(self):
        self.str1 = "geek1"
        print("base1")

class base2(object):
    def __init__(self):
        self.str2 = "geek2"
        print("base2")

class derived(base1, base2):
    def _init__(self):

        #calling constructors of basel
        #and base2 clasees
        base1.__init__(self)
        base2.__init__(self)
        print("derived")

    def printstrs(self):
        print(self.str1, self.str2)

ob = derived()
ob.printstrs()