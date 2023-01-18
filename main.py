list1= [9,14,3,27,1]
print("unsorted list: ",list1)
for j in range(len(list1)-1):
  for i in range(len(list1)-1):
    if list1[i]<list1[i+1]:
      list1[i],list1[i+1] = list1[i+1],list1[i] 
      print(list1) #This will print the steps where number will swap
    else:
      print(list1) #This will print all whether it swap or not

  
print("sorted list: ",list1)