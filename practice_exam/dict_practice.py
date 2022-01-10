d = {}
while True:
    k=input("Please input a key: ") 
    if k == "Stop":
        break
    v=input("Plesse input a value: ") 
    d.update({k:v})

def func(country):
    
    print(d.get(country, "No such country"))
  
func("armenia")