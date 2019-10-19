
class rule:
    def __init__(self, left, *right):
        self.left=left
        self.right =right

        self.count=1
        self.string= self.__repr__()
        print(self.string)


    def __repr__(self):
        str1=""

        for var in self.right:
            for var1 in var:
                str1= str1+ " " +var1

        str2 = str(self.count)+ " "+self.left+" ->"+str1
        return str2




n=rule("left",("right",))

