#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:CodeMonster
@file: 类和ADT.py
@time: 2017/9/21 9:48
"""

class Rational:
    def __init__(self,num,den=1):
        self.num = num
        self.den = den

    def plus(self,another):
        den = self.den * another.den
        num = (self.num * another.den +
               self.den * another.num)
        return Rational(num,den)

    def print1(self):
        print (str(self.num)+"/"+str(self.den))

class Rational_Pro:
    @staticmethod
    def _gcd(m,n):
        if n == 0:
            m,n = n,m
        while m != 0:
            m,n = n % m , m
        return n
    def __init__(self,num,den=1):
        if not isinstance(num,int) or not isinstance(den,int):
            raise TypeError
        if den==0:
            raise ZeroDivisionError
        sign =1
        if num < 0:
            num,sign = -num,-sign
        if den < 0:
            den,sign = -den,-sign
        g = Rational_Pro._gcd(num,den)
        self._num = sign * (num//g)
        self._den = (den//g)
    def num(self):
        return self._num
    def den(self):
        return self._den
    def __add__(self,another):
        if isinstance(another,Rational_Pro):
            raise TypeError
        den = self._den * another.den()
        num = (self._num * another.den()+
               self._den * another.num())
        return (Rational_Pro(num,den))
    def __mul__(self, another):
        if isinstance(another,Rational_Pro):
            raise TypeError
        den = self._den * another.den()
        num = self._num * another.num()
        return (Rational_Pro(num,den))
    def __floordiv__(self, another):
        if isinstance(another,Rational_Pro):
            raise TypeError
        if another.num() == 0:
            raise ZeroDivisionError
        return Rational_Pro(self._num * another.den()
                            ,self._den * another.num())
    def __eq__(self,another):
        return self._num * another.den() == self._den * another.num()
    def __lt__(self, another):
        return self._num * another.den() < self._den * another.num()

    def __str__(self):
        return str(self.num()) + "/" + str(self.den())
    def print1(self):
        print(self._num,"/",self._den)

class LNode:
    def __init__(self,elem,next_=None):
        self.elem = elem
        self.next = next_

list1 = LNode(1)
p = list1
for i in range(2,11):
    p.next = LNode(i)
    p = p.next
p = list1
while p is not None:
    print(p.elem)
    p = p.next

class LinkedListUnderflow(ValueError):
    pass
class LList:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None
    def prepend(self,elem):
        self._head = LNode(elem, self._head)
    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop")
        e = self._head.elem
        self._head = self._head.next
        return e
    def append(self,elem):
        if self._head is None:
            return None







