class Rule:

    def __init__(self,left,right):
        self.left=left
        self.right=right
        self.count=1
    
    
    def __repr__(self):
        returnstrin=str(self.count) +" "+self.left+" ->"
        for i in self.right:
            returnstrin+=(" "+i)
        return returnstrin



