# Hash Table

## hash function

一个key只能对应一个value

- if hash(key1)!=hash(key2), then key1 != key2

## data structure

数组、集合、映射

快速判断一个元素是否出现在集合里，“判断一个元素是否出现过”类型题目



## examples

- LC242
  - 数组
  - 字母相对位置对应索引

## Operations

- ```ord(c)-ord('a')``` is usually used as the hash function for lower case letters

- store occurrences in a dict:

- ```py
  my_dict = {}
  for s in string:
    my_dict[c]=my_dict.get(c,0)+1
  ```