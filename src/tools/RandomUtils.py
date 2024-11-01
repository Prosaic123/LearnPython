import random

class RandomUtils:
    @staticmethod
    def random_integer(start, end):
        """生成指定范围内的随机整数"""
        return random.randint(start, end)

    @staticmethod
    def random_choice(sequence):
        """从序列中随机选择一个元素"""
        return random.choice(sequence)

    @staticmethod
    def random_sample(sequence, k):
        """从序列中随机选择 k 个元素"""
        return random.sample(sequence, k)
