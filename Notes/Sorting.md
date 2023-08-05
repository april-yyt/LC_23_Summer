### bubble sort

适合数据量较小并且基本有序

排序稳定性：值相同元素排序后仍然保持原先的相对位置

​	不稳定：选择排序、堆排序

```py
def bubblesort(arr):
  for i in range(len(arr)):
    for j in range(len(arr)-i-1):
      if arr[j]>arr[j+1]:
        arr[j],arr[j+1] = arr[j+1],arr[j]
 	return arr
```

### selection sort

需要移动很多次元素，适用于数据量小的情况，优点在于原地操作

是一种不稳定排序， [6,5,2,6,1,8]

```py
def selectionsort(arr):
  for i in range(len(arr)-1):
    # 未排序部分中最小值位置
   	min_i = i
    for j in range(i+1,len(arr)):
      if arr[j] < arr[min_i]:
        min_i=j
    if i != min_i:
      arr[i],arr[min_i]=arr[min_i],arr[i]
 	return arr
```

### insertion sort

```py
def insertionsort(arr):
  for i in range(1,len(arr)):
    tmp = arr[i]
    j = i
    while j > 0 and arr[j-1]>tmp:
      arr[j]=arr[j-1]
      j -= 1
    arr[j]=tmp
 return arr
```

### shell sort



### merge sort

