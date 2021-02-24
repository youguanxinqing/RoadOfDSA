from enum import Enum, auto
from typing import Any

import mmh3
from bitarray import bitarray


class Status(Enum):
    NONE = auto()
    MAYBE = auto()


class BloomFilter(object):
    def __init__(self, size, hash_num):
        self.size = size
        self.hash_num = hash_num
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)

    def add(self, s: Any):
        for seed in range(self.hash_num):
            result = mmh3.hash(s, seed) % self.size
            self.bit_array[result] = 1

    def lookup(self, s: Any) -> Status:
        for seed in range(self.hash_num):
            result = mmh3.hash(s, seed) % self.size
            if self.bit_array[result] == 0:
                return Status.NONE
        return Status.MAYBE


def test_bloom_filter():
    bf = BloomFilter(100000, 10)
    bf.add("zhong")
    
    print(bf.lookup("zhong") == Status.MAYBE)
    print(bf.lookup("zhang") == Status.NONE)


if __name__ == "__main__":
    test_bloom_filter()

