def RS(list):
    maxele=max(list)
    place=1
    while maxele//place>0:
        buckets=[[]for i in range(10)]
        for num in list:
            index=(num // place)%10
            buckets[index].append(num)
            list.clear() #The extend() method has added all the elements from the buckets to the list,
            #effectively "flattening" the list of buckets into a single list.
            for bucket in  buckets:
                list.extend(bucket)
        place*=10
    return list
list=[2, 45, 0, 11, 9, 88, 97, 202, 747]
res=RS(list)
print(res)
