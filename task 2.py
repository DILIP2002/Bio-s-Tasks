i = int(input("number= ")
        )
reverse = 0
x = i
while(i>0):
    reverse = reverse*10+i%10
    i=i//10
if (x==reverse):
    print("true")
else:
    print("false")
if(x>0):
    print("true")
else:
    print("false")
    
