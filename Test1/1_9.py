dataset = [3,5,1,2,4]
size = len(dataset)
for i in range(size-1):
    for j in range(i+1,size):
        if dataset[i] > dataset[j]:
            temp = dataset[i]
            dataset[i] = dataset[j]
            dataset[j] = temp
    print('%d Round: %s ' % (i,dataset))
print()
print('result: ', dataset)