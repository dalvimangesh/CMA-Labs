import sys

# Function to check for any exception in inputFunction
def Check(inputFunction):

    # Function to handle the exception
    def newFunction(ref, *arg, **kwargs):
        try:
            return inputFunction(ref, *arg, **kwargs)
        except Exception as e:
            print(type(e))
            print(e)
            sys.exit(-1)

    return newFunction


class RowVectorFloat:

    @Check
    def __init__(self, v) -> None:

        # Input must be list and all elements must be either float or int
        if type(v) is not list or not all((type(i) is float or type(i) is int) for i in v):
            raise Exception('Input must be list and all elements must be either float or int')

        self.vector = v

    # string representation of row vector float
    @Check
    def __str__(self) -> str:
        res = " ".join("%.2f" % round(i, 2) if type(i) is float else str(i) for i in self.vector)
        return res

    # function to return the number of elements in the vector
    @Check
    def __len__(self):
        return len(self.vector)

    @Check
    def __getitem__(self, index):

        # Index Must be non negative integer and less than size of vector
        if index < 0 or index > len(self):
            raise Exception('Index out of bound')
        return self.vector[index]

    @Check    
    def __setitem__(self, index, value):

        if index is None or index < 0 or index > len(self): # Checking input index
            raise Exception('Index out of bound')
        
        if not ( type(value) is float or type(value) is int ):
            raise Exception('Value must be either float or int')

        self.vector[index] = value

    @Check
    def __add__(self, v):

        if type(v) is not RowVectorFloat: # Checking type of input vector
            raise Exception('RowVectorFloat can be added with RowVectorFloat only')

        if len(self) != len(v): # Both vectors should have same length
            raise Exception('length of vectors should be same')

        tempVector = []
        for i in range(len(v)):
            tempVector.append(self.vector[i] + v[i]) # Addition
        return RowVectorFloat(tempVector)

    @Check
    def __mul__(self, scalar):

        # can multiply scalar with rowvector only
        if type(scalar) is not float and type(scalar) is not int:
            raise Exception('Input must be scalar value') 

        # writing 0.00 to avoid floating point error
        tempVector = [(0.00 if round(i*scalar, 2) == 0 else (i*scalar))for i in self.vector]
        return RowVectorFloat(tempVector)

    # Reverse multiplication when the scalar is on the left
    @Check
    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    # Return the sum of all the elements in the vector
    def sum(self):
        return sum(self.vector)




if __name__ == '__main__':

    r1 = RowVectorFloat([1, 2 , 4])
    r2 = RowVectorFloat([1, 1 , 1])
    r3 = 2*r1 + (-3)*r2
    print(r2.sum())