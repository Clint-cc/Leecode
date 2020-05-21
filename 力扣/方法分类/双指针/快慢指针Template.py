# !D:/Code/python
# -*- coding:utf-8 -*-
# @Author : Clint
# @Question : 
# @Thinking :

# 主要解决链表中的问题；如，判断链表是否包含环
''''''
# 1、判断链表是否包含环
'''
boolean hasCycle(ListNode head) {
    while (head != null)
        head = head.next;
    return false;
}
'''

# 2、经典解法就是⽤两个指针，⼀个跑得快，⼀个跑得慢。如果不含有环，跑得快的那个指针最终会遇到 null，
# 说明链表不含环；如果含有环，快指针最终会超慢指针⼀圈，和慢指针相遇，说明链表含有环;
'''
boolean hasCycle(ListNode head) { 
    ListNode fast, slow; 
    fast = slow = head; 
    while (fast != null && fast.next != null) { 
        fast = fast.next.next; 
        slow = slow.next; 
        if (fast == slow) 
        return true; 
    }
    return false; 
}
'''

# 3、已知链表中含有环，返回这个环的起始位置
'''
ListNode detectCycle(ListNode head) { 
    ListNode fast, slow; 
    fast = slow = head; 
    while (fast != null && fast.next != null) { 
        fast = fast.next.next; 
        slow = slow.next; 
        if (fast == slow) 
            break; 
    }
    // 上⾯的代码类似hasCycle函数
    slow = head; 
    while (slow != fast) { 
        fast = fast.next; 
        slow = slow.next;
    }
    return slow; 
}
'''

# 4、寻找链表的中点
'''
while (fast != null && fast.next != null) { 
    fast = fast.next.next; 
    slow = slow.next; 
}
// slow 就在中间位置 
return slow;
'''

# 5、寻找链表的倒数第k个元素
'''
ListNode slow, fast; 
slow = fast = head; 

while (k-- > 0) 
    fast = fast.next; 
    
while (fast != null) { 
    slow = slow.next; 
    fast = fast.next; 
}
return slow;
'''
