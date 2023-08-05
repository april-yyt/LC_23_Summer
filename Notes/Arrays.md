## arrays



#### insert

尾部插入：append， O(1)

某个位置插入：arr.insert(i, val)

​	检查下标是否合法

​	该位置是否有数据

#### modify

Change(arr, i , val)

#### delete

删除尾部 arr.pop()

删除某个位置 arr.pop(i)

arr.remove(x)





## binary search

前提条件：有序数组、

注意：

1. 左闭右闭
2. 中间元素mid = left + (right - left + 1) // 2
3. Left <= right
4. while循环里left = mid + 1, right = mid - 1



排除法：while left < right，一定会剩下left=right仅有一个元素的情况



LC 27

