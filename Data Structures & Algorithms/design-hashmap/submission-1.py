class MyHashMap:

    def __init__(self):
        self.keys = []
        self.values = []

    def _contains(self, key: int) -> bool:
        return key in self.keys

    def _get_index(self, key) -> int:
        return self.keys.index(key)

    def put(self, key: int, value: int) -> None:
        if self._contains(key):
            self.values[self._get_index(key)] = value
        else:
            self.keys.append(key)
            self.values.append(value)


    def get(self, key: int) -> int:
        if self._contains(key):
            return self.values[self._get_index(key)]
        return -1

    def remove(self, key: int) -> None:
        if self._contains(key):
            self.values.remove(self.get(key))
            self.keys.remove(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)