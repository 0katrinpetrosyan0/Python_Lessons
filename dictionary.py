# how to create dictionaries
Dict = {
    "1" : "hi",
    "2" : "hi2"
}

Dict2 = dict(hi = 7,
            hi2 = 5)

list_tuple = [("hi" , 7), ("hi2", 6)]

# how access to items

Dict["1"]
Dict.get("1")
Dict.keys()
Dict.values()
Dict.items()
Dict.setdefault("1", "hiii")

#how to change and add items 
Dict.update({"5": 555})
Dict["1"] = "hii"


#how to remove 

Dict.pop("1")
del Dict["1"]
del Dict
Dict.clear()

#how to copy

mydict = Dict.copy()
mydict = dict(Dict)