f=open('perepis.txt', 'r+')
count=0
a=int(input())
b=int(input())
answA=[]
answB=''
for i in f:
    parts=i.split()
    surname=parts[0]
    name=parts[1]
    name2=parts[2]
    dateall=parts[3]
    date=dateall.split('.')[2]
    if int(date)<1978:
        count+=1
        print('<1978: ',surname)
    if a<=int(date)<=b:
        print('В заданном диапозоне: ',surname,name,name2)
print(count)
f.close()
