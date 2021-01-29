#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/1/23 6:03 PM
# @Author: wisdom
# @File:deleteRepetitionNum.py


def identifyPalindromic(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


if __name__ == '__main__':
    print('identify the number is Palindromic')
    s = input()
    left = 0
    right = len(s) - 1
    maxLen = 1
    begin = 0
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            if j - i + 1 > maxLen and identifyPalindromic(s, i, j):
                maxLen = j - i + 1
                begin = i
                j += 1
        i += 1
    print(s[begin:begin + maxLen])
