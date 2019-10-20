import math

class Random:

    def __init__(self, seed):

        self.m_min= seed
        self.m_max= 2147483648
        self.no =seed

        if(seed<1 or seed>self.m_max-2):
              print("out of range")


    def  next(self):
        a = self.m_min
        m= self.m_max
        self.no = (16807*self.no)%(2147483648-1)
        return self.no

    def choose(self, limit):
        new_no=self.next()
        new_no = new_no%limit
        # print(new_no)
        return new_no
















