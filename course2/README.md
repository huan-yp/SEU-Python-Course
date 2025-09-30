## 列表的删除


### 错误

```python
l = [1, 1, 4, 5, 1]
for x in l:
    if x == 1:
        l.remove(x)
print(l) # [4, 5, 1]
```

### 正确

```python
l = [1, 1, 4, 5, 1]
for x in l[:]: # 遍历 shallow copy 副本
    if x == 1:
        l.remove(x)
print(l) # [4, 5]
```

### 一些机制

- remove 删除第一个匹配项
- 用迭代器遍历时，相当于每次下标增大 1。
- 边遍历边删除时，后续元素会前移，导致跳过某些元素未被遍历到。

## 列表的切片

```python
l = [1, 2, 3, 4, 5]
print(l[1:4]) # [2, 3, 4]
print(l[:3]) # [1, 2, 3]
print(l[2:]) # [3, 4, 5]
print(l[-3:-1]) # [3, 4]
print(l[::2]) # [1, 3, 5]
print(l[::-1]) # [5, 4, 3, 2, 1]
print(l[4:1:-1]) # [5, 4, 3]
```

### 一些机制

- `l[start:end:step]`
- 切片返回的是一个新列表，是**浅拷贝**。
- 永远 **start 闭 end 开**。
