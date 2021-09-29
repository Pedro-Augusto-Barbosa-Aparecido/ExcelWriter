class Array(list):
    __array = None

    def __init__(self, _list=None) -> None:
        if _list and type(_list) is list:
            self.array = _list
    
    def __init_subclass__(cls) -> None:
        return super().__init_subclass__()

    @property
    def array(self) -> property:
        return self.__array

    @array.setter
    def array(self, value) -> None:
        if type(value) is list:
            self.__array = value
        else:
            raise TypeError("Array class property only receive values of type list")

    @property
    def length(self) -> int:
        if self.__array:
            return len(self.__array)
        
        return -1

if __name__ == "__main__":
    print("Array class is a type with one goal, has Array.length")
    print("-----------------------------------------------------------------------") 
    print("var = Array() # instance of Array")
    print("var.array = [] # set a value")
    print("print(var.length) # -1 | when is a empty array. The property returns -1")
    print("-----------------------------------------------------------------------") 
    print("Working")

    var = Array()

    var.array = []
    print(var.array)
    print(var.length)

    var = Array(["one", "two"])

    print(var.array)
    print(var.length)
