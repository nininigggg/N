"""
简单列表排序
[20,50,20,30,70]
['ee','bb','dd','aa','cc']
原列表排序或不改变原列表
升序或降序
"""

l1 = [20, 50, 20, 30, 70]
l2 = ['ee', 'bb', 'dd', 'aa', 'cc']
l1.sort(reverse=True)
print(f"sort list: {l1}")
l22 = sorted(l2, reverse=True)
print(f"source list:{l2} ,sort list: {l22}")