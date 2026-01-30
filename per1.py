f=open('perepis.txt', 'r+')
count=0
a=int(input())
b=int(input())
agnames=[]
for i in f:
    parts=i.split()
    surname=parts[0]
    date=parts[3].split('.')[2]
    if int(date)<1978:
        count+=1
        print(surname)
    if a<=int(date)<=b:
        agnames.append(surname)
print(count)
print(agnames)
f.close()
