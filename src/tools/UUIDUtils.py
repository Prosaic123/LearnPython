import uuid

class UUIDUtils:
    @staticmethod
    def generate_uuid4():
        """生成一个随机 UUID (UUID4)"""
        return str(uuid.uuid4())

    @staticmethod
    def generate_uuid1():
        """生成一个基于时间的 UUID (UUID1)"""
        return str(uuid.uuid1())

    @staticmethod
    def generate_uuid3(namespace, name):
        """生成一个基于名字的 UUID (UUID3)"""
        return str(uuid.uuid3(namespace, name))

    @staticmethod
    def generate_uuid5(namespace, name):
        """生成一个基于名字的 UUID (UUID5)"""
        return str(uuid.uuid5(namespace, name))