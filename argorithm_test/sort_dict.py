"""
指定字段排序

"""

var = [
    {"sno": 101, "sname": "小张", "sgrade": 88},
    {"sno": 102, "sname": "小王", "sgrade": 99},
    {"sno": 103, "sname": "小李", "sgrade": 77},
    {"sno": 104, "sname": "小赵", "sgrade": 66},
]

var_sort = sorted(var, key=lambda x: x["sgrade"])
print(f"source {var}, sort result: {var_sort}")
