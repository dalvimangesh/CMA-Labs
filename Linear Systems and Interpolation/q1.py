

class RowVectorFloat:


    def __init__(self,v) -> None:

        if type(v) is not list:
            raise Exception('Something went wrong\n')
        self.vector = v
        
    def __str__(self) -> str:
        res = " ".join( str(i) for i in self.vector )
        return res

    def __len__(self):
        return len(self.vector)

    def __mangesh__(self):
        return "mangesh dalvi"

obj = RowVectorFloat([1,2,3,5,6,7])
print(obj)
print(len(obj))

