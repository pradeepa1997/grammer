import grammer
import rule

# this is main file.
# using this method u can test your code


if __name__ == "__main__":
    print("===========Testing Rules============")
    a=rule.Rule('Noun',   ('cat',))
    print(a)
    a=rule.Rule('Noun',   ('boy',))
    print(a)
    a=rule.Rule('Noun',   ('dog',))
    print(a)
    a=rule.Rule('Noun',   ('girl',))
    print(a)
    a=rule.Rule('Verb',   ('bit',))
    print(a)
    a=rule.Rule('Verb',   ('chased',)) 
    print(a)
    a=rule.Rule('Verb',   ('kissed',))
    print(a)
    a=rule.Rule('Phrase', ('the', 'Noun', 'Verb', 'the', 'Noun'))
    print(a)
    a=rule.Rule('Story',  ('Phrase',)) 
    print(a)
    a=rule.Rule('Story',  ('Phrase', 'and', 'Story'))    
    print(a)
    a=rule.Rule('Story',  ('Phrase', 'but', 'Story'))  
    print(a)
    a=rule.Rule('Start',  ('Story', '.'))
    print(a)
    print("======================================")
    print("\n\n\n")

     
    G = grammer.Grammar(101) 
    G.rule('Noun',   ('cat',))                                #  01 
    G.rule('Noun',   ('boy',))                                #  02 
    G.rule('Noun',   ('dog',))                                #  03 
    G.rule('Noun',   ('girl',))                               #  04 
    G.rule('Verb',   ('bit',))                                #  05 
    G.rule('Verb',   ('chased',))                             #  06 
    G.rule('Verb',   ('kissed',))                             #  07 
    G.rule('Phrase', ('the', 'Noun', 'Verb', 'the', 'Noun'))  #  08 
    G.rule('Story',  ('Phrase',))                             #  09 
    G.rule('Story',  ('Phrase', 'and', 'Story'))              #  10 
    G.rule('Story',  ('Phrase', 'but', 'Story'))              #  11 
    G.rule('Start',  ('Story', '.'))                          #  12
    print("===========Testing Grammer============")
    print(G.generate())
    print(G.generate())
    print(G.generate())
    print(G.generate())
    print(G.generate())
    print(G.generate())
    print(G.generate())
    print(G.generate())
    print("======================================")
