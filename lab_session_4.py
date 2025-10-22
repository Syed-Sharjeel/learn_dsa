# Copyright 2025 Hafiz Syed Sharjeel Najam
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#  Lab Session 04 — Codelab Notebook
#  Repository: Syed-Sharjeel/learn_dsa
#  Author: Hafiz Syed Sharjeel Najam
#  Year: 2025

# Lab Session 04
# To develop and apply the recursive divide and conquer approach in sorting 
# (using debugging tools in Python)

# Debugging is the process of studying the workflow of program and identifying if there is an error in it.

def merge(a,b):
    n1 = len(a)
    n2 = len(b)
    a = a + [float('inf')]
    b = b + [float('inf')]
    i = 0
    j = 0
    m = []
    for k in range(n1+n2):
        if a[i] < b[j]:
            m.append(a[i])
            i += 1
        else:
            m.append(b[j])
            j += 1
    return m

def merge_sort(a):
    n = len(a)
    s = []
    if n==1:
        s = a
    else:
        mid = n//2
        s1 = merge_sort(a[0:mid])
        s2 = merge_sort(a[mid:n])
        s = merge(s1, s2)
    return s

print(merge_sort([5,4,3,2,1]))