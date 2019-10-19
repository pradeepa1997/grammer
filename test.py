import rule

# name=dict()
# name["noun"]=("pradeepa sandaruwa","hello")
# print(name)
# name["age"]=(rule.Rule("h","k"),)
# print(name)
# name["age"]=name["age"]+rule.Rule("1","c")
# print(name)
# if "a" in name:
#     print("aaaaa")
# else:
#     print("bbbbbb")
name=rule.Rule("left",("right",))
temp=name.__repr__()
print(temp)