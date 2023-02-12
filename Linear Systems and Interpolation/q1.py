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

    def __getitem__(self,index):
        return self.vector[index]

    def __add__(self,v):
        tempVector = []
        for i,_ in enumerate(v):
            tempVector.append( self.vector[i] + v[i] )
        return RowVectorFloat(tempVector)
    
    def __mul__(self,scalar):
        tempVector = [ i*scalar for i in self.vector ]
        return RowVectorFloat(tempVector)
    def __rmul__(self,scalar):
        tempVector = [ i*scalar for i in self.vector ]
        return RowVectorFloat(tempVector)

r1 = RowVectorFloat([1, 2 , 4])
r2 = RowVectorFloat([1, 1 , 1])
r3 = 2*r1 + (-3)*r2
print(r3)
