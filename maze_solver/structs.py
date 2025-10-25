"""
结构体类定义模块
包含Code和Symbols两个数据结构类
"""


class Code:
    """
    方向代码结构体
    存储上下左右四个方向的字符串代码
    """

    def __init__(self, up: str, down: str, left: str, right: str):
        """
        初始化Code结构体

        Args:
            up (str): 向上的代码
            down (str): 向下的代码
            left (str): 向左的代码
            right (str): 向右的代码
        """
        self.up = up
        self.down = down
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Code(up='{self.up}', down='{self.down}', left='{self.left}', right='{self.right}')"

    def __str__(self):
        return f"Code(↑:{self.up}, ↓:{self.down}, ←:{self.left}, →:{self.right})"

    def __iter__(self):
        """
        支持解包操作，返回 (up, down, left, right) 的迭代器
        使用方式: up, down, left, right = code
        """
        return iter((self.up, self.down, self.left, self.right))

    def to_tuple(self):
        """
        返回 (up, down, left, right) 元组
        """
        return (self.up, self.down, self.left, self.right)


class Symbols:
    """
    迷宫符号结构体
    存储道路、墙壁、起点、终点的符号
    """

    def __init__(self, road: str, wall: str, start: str, end: str):
        """
        初始化Symbols结构体

        Args:
            road (str): 道路符号
            wall (str): 墙壁符号
            start (str): 起点符号
            end (str): 终点符号
        """
        self.road = road
        self.wall = wall
        self.start = start
        self.end = end

    def __repr__(self):
        return f"Symbols(road='{self.road}', wall='{self.wall}', start='{self.start}', end='{self.end}')"

    def __str__(self):
        return (
            f"Symbols(路:{self.road}, 墙:{self.wall}, 起:{self.start}, 终:{self.end})"
        )

    def __iter__(self):
        """
        支持解包操作，返回 (road, wall, start, end) 的迭代器
        使用方式: road, wall, start, end = symbols
        """
        return iter((self.road, self.wall, self.start, self.end))

    def to_tuple(self):
        """
        返回 (road, wall, start, end) 元组
        """
        return (self.road, self.wall, self.start, self.end)


# 使用示例
if __name__ == "__main__":
    # 创建Code实例
    code = Code(up="w", down="s", left="a", right="d")
    print(code)

    # 创建Symbols实例
    symbols = Symbols(road=" ", wall="█", start="S", end="E")
    print(symbols)

    # 测试解包功能
    print("\n=== 解包测试 ===")
    up, down, left, right = code
    print(f"解包Code: up={up}, down={down}, left={left}, right={right}")

    road, wall, start, end = symbols
    print(f"解包Symbols: road='{road}', wall='{wall}', start='{start}', end='{end}'")
