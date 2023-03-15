class Array:
    def __int__(self, capacity):
        self.data = [-1] * capacity
        # 记录存储数据量
        self.count = 0
        # 数组容量
        self.n = capacity

    def insert(self, location, value):
        # 数据已经存储满，无法继续插入
        if self.n == self.count:
            return False
        # 插入位置越界
        if location < 0 or location > self.count:
            return False
        # 后移其他value，空出location位置
        for i in range(self.count, location, -1):
            self.data[i] = self.data[i-1]
        # 数据插入location位置
        self.data[location] = value
        # 插入数据后array长度+1
        self.count += 1
        return True

    def find(self, location):
        if location < 0 or location > self.count:
            return -1
        return self.data[location]

    def delete(self, location):
        if location < 0 or location > self.count:
            return False
        # 从location位置向前移数据
        for i in range(location+1, self.count):
            self.data[i - 1] = self.data[i]

        self.count -= 1
        return True


def test_demo():
    array = Array(5)
    array.insert(0, 1)
    array.insert(0, 2)
    array.insert(1, 2)
    array.insert(2, 4)
    array.insert(4, 5)
    # 判断插入是否成功
    assert not array.insert(0, 100)
    assert array.find(0) == 2
    assert array.find(4) == 5
    assert array.find(10) == -1
    removed = array.delete(4)
    assert removed
    assert array.find(4) == -1
    removed = array.delete(10)
    assert not removed
