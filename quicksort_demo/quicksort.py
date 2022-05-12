#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  8 17:33:54 2022

@author: Mingzhe Wang
"""


def quicksort(arr):
  quicksort_rec(arr, 0, len(arr) - 1)

def quicksort_rec(arr, lo, hi):
  if (lo >= hi):
    return
  
  else:
    pi = partition(arr, lo, hi)
    quicksort_rec(arr, lo, pi - 1)
    quicksort_rec(arr, pi + 1, hi)

def partition(arr, lo, hi):  
  pivot = arr[hi]
  i = lo - 1

  for j in range(lo, hi):
    if (arr[j] <= pivot):
      i = i + 1
      arr[i], arr[j] = arr[j], arr[i]

  arr[i+1], arr[hi] = arr[hi], arr[i+1]

  return i+1

# test part
arr = [8,7,6,1,0,9,2]
print("original array: ", arr)
quicksort(arr)
print("sorted array: ", arr)
