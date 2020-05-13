### python3中关于队列（FIFO：先进先出）
- collections是python内建的一个集合模块，里面封装了许多集合类，
其中队列相关的集合只有一个：deque。
- deque 是双边队列（double-ended queue），具有队列和栈的性质，在 list 的基础上增加了移动、旋转和增删等。

```python
from collections import deque

d = deque() # 或deque([])   # 创建一个队列
d.append('a')               # 在最右边添加一个元素, return：d=deque('a')
d.appendleft('b')           # 在最左边添加一个元素, return：d=deque(['b','a'])
d.extend(['c', 'd'])        # 在最右边依次添加所有元素, return：d=deque(['b','a'，'c', 'd'])
d.extendleft(['e', 'f'])    # 在最左边依次添加所有元素, return：d=deque(['f', 'e'，'b','a'，'c', 'd'])
d.pop()                     # 在最右边删除一个元素, return：d=deque(['f', 'e'，'b','a'，'c'])
d.popleft()                 # 在最左边删除一个元素, return：d=deque(['e'，'b','a'，'c'])
d.rotate(-2)                # 向左旋转2个位置（正数则向右旋转）, return：d=deque(['a', 'c', 'e', 'b'])
d.reverse()                 # 队列倒序(或者反转), return：d=deque(['b', 'e', 'c', 'a'])
d.count('a')                # 队列'a'的个数, return 1
d.remove('c')               # 从左边删除一个元素'c', return：d=deque(['b', 'e', 'a'])
```