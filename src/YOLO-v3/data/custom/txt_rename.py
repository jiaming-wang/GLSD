#!/usr/bin/env python
# coding=utf-8
'''
@Author: wjm
@Date: 2020-03-21 23:05:29
@LastEditTime: 2020-03-21 23:15:18
@Description: file content
'''


def main():
    sets=['train', 'val', 'test']
    for name in sets:
        for line in open('%s.txt'%(name),'r', encoding='UTF-8'): 
            print(line)

if __name__ == '__main__':
    main()
