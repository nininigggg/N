
def select_sort(li):
    li_new = []
    for i in range(len(li)):
        min_value = min(li)
        # li_new.append(min_value)
        # li.remove(min_value)
        li_new.append(li.pop(li.index(min_value)))
    return li_new


li = [8, 7, 9, 5, 4, 2, 6, 1, 3]
print(select_sort(li))


def select_sort_new(li):
    for i in range(len(li) - 1):
        min_loc = i
        for j in range(i + 1, len(li)):
            if li[j] < li[min_loc]:
                min_loc = j
        li[i], li[min_loc] = li[min_loc], li[i]


li = [8, 7, 9, 5, 4, 2, 6, 1, 3]
select_sort_new(li)
print(li)
