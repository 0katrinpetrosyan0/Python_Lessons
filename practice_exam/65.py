# 2 tveri amenamec yndhanur bajanarary
def gcd(a,b):
    while b!=0:
        a,b = b,a%b
    return a

## or recursive

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)