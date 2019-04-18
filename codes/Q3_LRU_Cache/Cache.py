from datetime import datetime
from time import sleep


class LRUCache:
    def __init__(self, capacity):
        self.cache = {}
        self.data_list = []
        self.capacity = capacity

    def get(self, key):
        if key in self.cache:
            if key != self.data_list[-1]:
                self.data_list.remove(key)
                self.data_list.append(key)
            return self.cache[key]
        else:
            return -1

    def set(self, key, data):
        if key in self.cache:
            self.data_list.remove(key)
        else:
            if len(self.cache) == self.capacity:
                temp = self.data_list.pop(0)
                self.cache.pop(temp)
        self.data_list.append(key)
        value = {"data": data, "time": str(datetime.now())}
        self.cache[key] = value

    def display(self):
        print("cache : " + str(self.cache))
        print("list  : " + str(self.data_list))
        print()


if __name__ == '__main__':
    cache = LRUCache(5)

    for k in range(0, 5):
        cache.set(k, "data" + str(k))
        # print(cache.get(k))
        cache.display()
        sleep(2)

    cache.set(2, "data" + str(2) + "_second")
    cache.display()


