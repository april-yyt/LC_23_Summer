# Review 2 Ptrs & Sliding Window

## 双指针

时间复杂度降低一个数量级

## 对撞指针

- 有序数组里满足某些约束条件的元素问题：二分查找、数字之和

- 字符串反转问题：反转字符串、回文...

```python
left, right = 0, len(nums) - 1
while leftr < right:
  if 满足某种条件:
    return 符合条件的值
  elif xx条件1:
    left += 1
  elif xx条件2:
    right -= 1
    
 return 没找到 or 找到对应值

```

## 快慢指针

- 数组中移动、删除问题
- 链表中是否有环、长度问题

```python
slow = 0
fast = 1
while 没有遍历完:
  if 满足某种条件:
    slow += 1
  fast += 1
return 合适值
```

