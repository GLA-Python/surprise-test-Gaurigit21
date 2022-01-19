def Look_and_Say(s):
     lst = []
     i = 0
     while i < len(s):
         j= 1
         while i+1 < len(s) and s[i]==s[i+1]:
             i+= 1 
             j+= 1 
         lst.append(str(j)+s[i])
         i+= 1 
     return ''.join(lst)
    
rows = int(input())
number = 1
for i in range (rows):
    print(number)
    number = Look_and_Say(str(number))
