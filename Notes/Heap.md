# Heap

在Python中，有一个模块叫做`heapq`，它提供了堆数据结构（Heap）的实现.

1. `heapq.heapify(iterable)`：此函数用于将可迭代的对象转换成堆数据结构。这个堆满足堆的特性，即每个父节点的值都小于或等于其子节点的值。

   将可迭代的对象（例如列表）转换为最小堆。

2. `heapq.heappush(heap, ele)`：此函数用于在已有的堆中添加一个元素。

   向堆中添加元素。

3. `heapq.heappop(heap)`：此函数用于从堆中删除并返回最小的元素。

   从堆中删除并返回最小元素。

4. `heapq.heappushpop(heap, ele)`：此函数先向堆中添加元素，然后从堆中删除并返回最小的元素。

   向堆中添加元素，然后弹出并返回堆中最小的元素。

5. `heapq.heapreplace(heap, ele)`：此函数先从堆中删除并返回最小的元素，然后向堆中添加元素。

   弹出并返回堆中最小的元素，然后将新元素添加到堆中。

6. `heapq.nlargest(n, iterable[, key])`：此函数用于返回可迭代对象中的n个最大元素。

   返回可迭代对象中的n个最大元素。

7. `heapq.nsmallest(n, iterable[, key])`：此函数用于返回可迭代对象中的n个最小元素。

   返回可迭代对象中的n个最小元素。