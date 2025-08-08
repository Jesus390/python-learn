class Switch:
    _case = []
    _default = None

    def __init__(self):
        self.value = None

    def case(self, value, func, *args):
        self._case.append((value, func(*args)))
        return self
    
    def default(self, func, *args):
        self._default = func(*args)
        return self
    
    def switch(self, value):
        self.value = value
        for value, func in self._case:
            if self.value == value:
                return func
    
if __name__ == "__main__":
    r = None
    s = Switch()
    s.case(1, r:=lambda x: x * 2, 2)
    s.case(2, r:=lambda x: x * 3, 2)
    s.default(r:=lambda x: x * 4, 2)
    s.switch(1)
    print(r)