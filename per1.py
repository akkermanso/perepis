f=open('perepis.txt', 'r+')
count=0
for i in f:
    parts=i.split()
    surname=parts[0]
    date=parts[3].split('.')[2]
    if int(date)<1978:
        count+=1
        print(surname)
print(count)
f.close()
