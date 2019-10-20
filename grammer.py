import random
import rule

class Grammar:
    def __init__(self,seed):
        self.dictionary=dict()
        self.rand_nm_gen=random.Random(seed)

    def rule(self,left,right):
        if left in self.dictionary:
            self.dictionary[left]=self.dictionary[left]+(rule.Rule(left,right),)
        else:
            self.dictionary[left]=(rule.Rule(left,right),)

    def generate(self):
        if "Start" in self.dictionary:
            return self.generating(self.dictionary["Start"][0].right)
        else:
            print("There is no rule start")

    def generating(self,strings):
        result=""
        for element in strings:
            if element not in self.dictionary:
                result=result+" "+element
            else:
                temp=self.select(element)
                result=result+" "+self.generating(temp)
        
        return result


    def select(self,left):
        
        rules=self.dictionary[left]
        total=0
        choose=None
        
        for rule in rules:
            total=total+rule.count
            
        index=self.rand_nm_gen.choose(total)
        
        for rule in rules:
            index=index-rule.count
            if index <=0:
                chosen=rule
                break
            
        for rule in rules:
            if chosen!=rule:
                rule.count=rule.count+1
        
        return chosen.right




    
