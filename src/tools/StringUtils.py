class StringUtils:
    @staticmethod
    def is_palindrome(s):
        """检查一个字符串是否是回文"""
        cleaned = ''.join(c.lower() for c in s if c.isalnum())
        return cleaned == cleaned[::-1]

    @staticmethod
    def count_vowels(s):
        """统计字符串中的元音字母数量"""
        vowels = 'aeiouAEIOU'
        return sum(1 for char in s if char in vowels)

    @staticmethod
    def to_snake_case(s):
        """将字符串转换为蛇形命名法"""
        return '_'.join(word.lower() for word in s.split())
