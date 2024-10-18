class President:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(President, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        # 隐藏构造函数的逻辑可以放在这里
        pass

    def __copy__(self):
        # 禁用复制
        raise NotImplementedError("Cloning of this object is not allowed.")

    def __deepcopy__(self, memo):
        # 禁用深度复制
        raise NotImplementedError("Deep cloning of this object is not allowed.")

    def __setstate__(self, state):
        # 禁用反序列化
        raise NotImplementedError("Unserializing of this object is not allowed.")

# 使用示例
president1 = President()
president2 = President()

print(president1 is president2)  # 输出: True

