#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:CodeMonster
@file: 链表,单双链表,循环链表.py
@time: 2017/10/13 10:26
"""
class LNode:
    def __init__(self,elem,next_=None):
        self.elem = elem
        self.next = next_

# list1 = LNode(1)
# q = list1
# for i in range(2,11):
#     q.next = LNode(i)
#     q = q.next
#
# q = list1
# while q is not None:
#     print(q.elem)
#     q = q.next

class LinkekListUnderFlow(ValueError):
    pass
class LList:
    def __init__(self):
        self._head = None
    def is_empty(self):
        return self._head is None
    def prepend(self,elem):
        self._head = LNode(elem,self._head)
    def pop(self):
        if self._head is None:
            raise LinkekListUnderFlow("in pop")
        e = self._head.elem
        self._head = self._head.next
        return e
    def append(self,elem):
        if self._head is None:
            self._head = LNode(elem)
        p = self._head
        while p.next is not None:
            p = p.next
        p.next = LNode(elem)
    def pop_last(self,elem):
        if self._head is None:
            raise LinkekListUnderFlow("in pop_last")
        p = self._head
        if p.next is None:
            e = p.elem
            self._head = None
            return e
        if p.next.next is not None:
            p = p.next
        e = p.next.elem
        p.next = None
        return e
    def find(self, pred):
        p = self._head
        while p is not None:
            if pred(p.elem):
                return p.elem
            p = p.next
    def printall(self):
        p = self._head
        while p is not None:
            print(p.elem)
            if p.next is not None:
                print(",")
            p = p.next
        print('')
    #传统技术,优点是比较规范,缺点是不够灵活,不容易与其他编程机制配合
    def for_each(self,proc):
        p = self._head
        while p is not None:
            proc(p.elem)
            p = p.next
    #为了解决,人们经常使用lamda表达式顶指出在这里使用的操作函数
    def elements(self):
        p = self._head
        while p is not None:
            yield p.elem
            p = p.next
# for x in list1.element()
#     print(x)
    def filter(self,pred):
        p = self._head
        while p is not None:
            if pred(p.elem):
                yield p.elem
            p = p.next







































































































