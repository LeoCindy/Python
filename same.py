numbers1 = ['WU','KA','WAI','Leo','Cindy']
numbers2 = ['Wu','ka','LAM','Cindy','leo']
same = []
notSame = []
while len(numbers1)>0 and len(numbers2)>0 :
    temp = numbers1.pop()
    if temp in numbers2:
        same.append(temp)
    else:
        notSame.append(temp)

print same
print notSame
