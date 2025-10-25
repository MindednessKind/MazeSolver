from collections import deque
import math
from typing import List, Dict, Tuple, Optional, Union


class MazeSolver:
    """
    迷宫求解器类，提供方向编码和路径寻找功能

    支持功能：
    - BFS最短路径寻找
    - 自定义方向编码
    - 多种迷宫格式支持
    - 路径可视化
    - 详细的路径分析
    """

    def __init__(self):
        """
        初始化迷宫求解器，使用默认编码 (U/D/L/R)
        """

        self.maze = None  # 保存当前迷宫
        self.last_result = None  # 保存最后一次求解结果
        self.codes = {"up": "U", "down": "D", "left": "L", "right": "R"}
        self.symbols = {"road": "0", "wall": "1", "start": "*", "end": "#"}
        self.decode = {
            (0, -1) : "←",
            (0, 1) : "→",
            (1, 0) : "↓",
            (-1, 0) : "↑",
        }

    def set_code(self, up: str, down: str, left: str, right: str) -> None:
        """
        设置方向编码

        参数:
        up (str): 向上移动的编码
        down (str): 向下移动的编码
        left (str): 向左移动的编码
        right (str): 向右移动的编码

        异常:
        ValueError: 如果编码参数不是字符串或为空
        """
        if not all(isinstance(code, str) and code for code in [up, down, left, right]):
            raise ValueError("所有方向编码必须是非空字符串")

        # 检查是否有重复编码
        codes = [up, down, left, right]
        if len(set(codes)) != len(codes):
            raise ValueError("方向编码不能重复")

        self.codes = {"up": up, "down": down, "left": left, "right": right}

    def set_symbols(self, road: str, wall: str, start: str, end: str) -> None:
        """
        设置迷宫符号

        参数:
        road (str): 道路符号
        wall (str): 墙壁符号
        start (str): 起点符号
        end (str): 终点符号

        异常:
        ValueError: 如果符号参数不是字符串或为空
        """
        if not all(
            isinstance(symbol, str) and symbol for symbol in [road, wall, start, end]
        ):
            raise ValueError("所有符号必须是非空字符串")

        # 检查是否有重复符号
        symbols = [road, wall, start, end]
        if len(set(symbols)) != len(symbols):
            raise ValueError("迷宫符号不能重复")

        self.symbols = {"road": road, "wall": wall, "start": start, "end": end}

    def get_symbols(self) -> Dict[str, str]:
        """
        返回当前迷宫符号字典

        返回:
        Dict[str, str]: 迷宫符号字典
        """
        return self.symbols.copy()

    def set_maze(self, maze: List[List[str]]) -> None:
        """
        设置当前迷宫

        参数:
        maze (List[List[str]]): 二维迷宫数组

        异常:
        各种迷宫验证相关的异常
        """
        self.validate_maze(maze)
        self.maze = [row[:] for row in maze]  # 深拷贝迷宫

    def get_maze(self) -> Optional[List[List[str]]]:
        """
        获取当前迷宫

        返回:
        Optional[List[List[str]]]: 当前迷宫副本，如果未设置则返回None
        """
        return [row[:] for row in self.maze] if self.maze else None

    def get_codes(self) -> Dict[str, str]:
        """
        返回当前方向编码字典

        返回:
        Dict[str, str]: 方向编码字典
        """
        return self.codes.copy()

    def validate_maze(self, maze: List[List[str]]) -> bool:
        """
        验证迷宫格式是否正确

        参数:
        maze (List[List[str]]): 二维迷宫数组

        返回:
        bool: 迷宫格式是否有效

        异常:
        TypeError: 如果迷宫不是正确的二维列表
        ValueError: 如果迷宫为空或行长度不一致
        """
        if not isinstance(maze, list):
            raise TypeError("迷宫必须是二维列表")

        if not maze:
            raise ValueError("迷宫不能为空")

        if not all(isinstance(row, list) for row in maze):
            raise TypeError("迷宫的每一行必须是列表")

        if not maze[0]:
            raise ValueError("迷宫的行不能为空")

        row_length = len(maze[0])
        if not all(len(row) == row_length for row in maze):
            raise ValueError("迷宫的所有行必须具有相同的长度")

        # 检查所有元素是否为字符串
        for i, row in enumerate(maze):
            for j, cell in enumerate(row):
                if not isinstance(cell, str):
                    raise TypeError(f"迷宫位置 ({i}, {j}) 的值必须是字符串")

        return True

    def find_positions(
        self, maze: List[List[str]], start_symbol: str, end_symbol: str
    ) -> Tuple[Optional[Tuple[int, int]], Optional[Tuple[int, int]]]:
        """
        寻找起点和终点位置

        参数:
        maze (List[List[str]]): 二维迷宫数组
        start_symbol (str): 起点符号
        end_symbol (str): 终点符号

        返回:
        Tuple: (起点坐标, 终点坐标)，如果未找到则为None

        异常:
        ValueError: 如果找到多个起点或终点
        """
        start_positions = []
        end_positions = []

        for i in range(len(maze)):
            for j in range(len(maze[0])):
                if maze[i][j] == start_symbol:
                    start_positions.append((i, j))
                elif maze[i][j] == end_symbol:
                    end_positions.append((i, j))

        # 检查起点和终点的数量
        if len(start_positions) > 1:
            raise ValueError(f"找到多个起点 '{start_symbol}': {start_positions}")
        if len(end_positions) > 1:
            raise ValueError(f"找到多个终点 '{end_symbol}': {end_positions}")

        start_pos = start_positions[0] if start_positions else None
        end_pos = end_positions[0] if end_positions else None

        return start_pos, end_pos

    def bfs_solve(
        self,
        maze: Optional[List[List[str]]] = None,
        road_symbol: Optional[str] = None,
        wall_symbol: Optional[str] = None,
        start_symbol: Optional[str] = None,
        end_symbol: Optional[str] = None,
    ) -> Dict[str, Union[bool, List[Tuple[int, int]], int, str, Dict]]:
        """
        使用BFS算法寻找迷宫中的最短路径

        参数:
        maze (Optional[List[List[str]]]): 二维数组表示的迷宫 (默认使用set_maze设置的迷宫)
        road_symbol (Optional[str]): 道路符号 (默认使用set_symbols设置的符号)
        wall_symbol (Optional[str]): 墙壁符号 (默认使用set_symbols设置的符号)
        start_symbol (Optional[str]): 入口符号 (默认使用set_symbols设置的符号)
        end_symbol (Optional[str]): 出口符号 (默认使用set_symbols设置的符号)

        返回:
        Dict: 包含以下键值的字典
            - 'found': bool, 是否找到路径
            - 'movement': List[Tuple[int, int]], 最短路径的坐标列表
            - 'path': List[Tuple[int, int]], 未编码的方向指示列表 [(-1,0), (0,1), ...]
            - 'length': int, 路径长度
            - 'steps': int, 移动步数 (路径长度-1)
            - 'encoded_path': str, 用编码表示的路径字符串
            - 'statistics': Dict, 路径统计信息

        异常:
        各种验证相关的异常
        """
        # 使用默认迷宫或提供的迷宫
        if maze is None:
            if self.maze is None:
                raise ValueError("未设置迷宫，请先调用set_maze()或传入maze参数")
            maze = self.maze
        else:
            # 验证输入
            self.validate_maze(maze)

        # 使用默认符号或提供的符号
        road_symbol = road_symbol if road_symbol is not None else self.symbols["road"]
        wall_symbol = wall_symbol if wall_symbol is not None else self.symbols["wall"]
        start_symbol = (
            start_symbol if start_symbol is not None else self.symbols["start"]
        )
        end_symbol = end_symbol if end_symbol is not None else self.symbols["end"]

        if not all(
            isinstance(symbol, str)
            for symbol in [road_symbol, wall_symbol, start_symbol, end_symbol]
        ):
            raise TypeError("所有符号参数必须是字符串")

        rows, cols = len(maze), len(maze[0])

        # 寻找起点和终点
        start_pos, end_pos = self.find_positions(maze, start_symbol, end_symbol)

        # 初始化返回结果
        result = {
            "found": False,
            "movement": [],
            "path": [],
            "length": 0,
            "steps": 0,
            "encoded_path": "",
            "statistics": {
                "maze_size": f"{rows}x{cols}",
                "total_cells": rows * cols,
                "start_position": start_pos,
                "end_position": end_pos,
                "visited_cells": 0,
                "direction_counts": {"up": 0, "down": 0, "left": 0, "right": 0},
            },
        }

        if start_pos is None:
            result["statistics"]["error"] = f"未找到起点符号 '{start_symbol}'"
            return result

        if end_pos is None:
            result["statistics"]["error"] = f"未找到终点符号 '{end_symbol}'"
            return result

        # BFS算法
        queue = deque(
            [(start_pos, [start_pos], [], [])]
        )  # (当前位置, 移动坐标, 方向序列, 方向向量)
        visited = set([start_pos])

        # 四个方向：上下左右，对应的方向名称
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        direction_names = ["up", "down", "left", "right"]

        while queue:
            (x, y), movement, move_sequence, direction_vectors = queue.popleft()

            # 如果到达终点
            if (x, y) == end_pos:
                # 生成编码路径
                encoded_path = "".join([self.codes[move] for move in move_sequence])

                # 统计方向使用次数
                direction_counts = {
                    direction: move_sequence.count(direction)
                    for direction in direction_names
                }

                result.update(
                    {
                        "found": True,
                        "movement": movement,
                        "path": direction_vectors,
                        "length": len(movement),
                        "steps": len(movement) - 1,
                        "encoded_path": encoded_path,
                    }
                )
                result["statistics"].update(
                    {
                        "visited_cells": len(visited),
                        "direction_counts": direction_counts,
                    }
                )

                self.last_result = result
                return result

            # 探索四个方向
            for i, (dx, dy) in enumerate(directions):
                nx, ny = x + dx, y + dy

                # 检查边界
                if 0 <= nx < rows and 0 <= ny < cols:
                    # 检查是否可以通行（道路、起点或终点，且未访问过）
                    if (nx, ny) not in visited and maze[nx][ny] in [
                        road_symbol,
                        start_symbol,
                        end_symbol,
                    ]:
                        visited.add((nx, ny))
                        new_movement = movement + [(nx, ny)]
                        new_move_sequence = move_sequence + [direction_names[i]]
                        new_direction_vectors = direction_vectors + [(dx, dy)]
                        queue.append(
                            (
                                (nx, ny),
                                new_movement,
                                new_move_sequence,
                                new_direction_vectors,
                            )
                        )

        # 没有找到路径
        result["statistics"]["visited_cells"] = len(visited)
        result["statistics"]["error"] = "无法从起点到达终点"
        self.last_result = result
        return result

    def encode_path(
        self,
        maze: Optional[List[List[str]]] = None,
        road_symbol: Optional[str] = None,
        wall_symbol: Optional[str] = None,
        start_symbol: Optional[str] = None,
        end_symbol: Optional[str] = None,
    ) -> str:
        """
        使用当前编码方案寻找路径并返回编码结果

        参数:
        maze (Optional[List[List[str]]]): 二维数组表示的迷宫 (默认使用set_maze设置的迷宫)
        road_symbol (Optional[str]): 道路符号 (默认使用set_symbols设置的符号)
        wall_symbol (Optional[str]): 墙壁符号 (默认使用set_symbols设置的符号)
        start_symbol (Optional[str]): 入口符号 (默认使用set_symbols设置的符号)
        end_symbol (Optional[str]): 出口符号 (默认使用set_symbols设置的符号)

        返回:
        str: 编码后的路径字符串，如果没有路径则返回空字符串
        """
        result = self.bfs_solve(
            maze, road_symbol, wall_symbol, start_symbol, end_symbol
        )
        return result["encoded_path"]

    def get_last_result(self) -> Optional[Dict]:
        """
        获取最后一次求解的详细结果

        返回:
        Optional[Dict]: 最后一次求解结果，如果没有则返回None
        """
        return self.last_result

    def print_statistics(self) -> None:
        """
        打印最后一次求解的统计信息
        """
        if not self.last_result:
            print("尚未进行任何求解")
            return

        stats = self.last_result["statistics"]
        print("=== 求解统计信息 ===")
        print(f"迷宫大小: {stats['maze_size']}")
        print(f"总格子数: {stats['total_cells']}")
        print(f"起点位置: {stats['start_position']}")
        print(f"终点位置: {stats['end_position']}")
        print(f"访问格子数: {stats['visited_cells']}")

        if self.last_result["found"]:
            print(f"路径长度: {self.last_result['length']}")
            print(f"移动步数: {self.last_result['steps']}")
            print(f"编码路径: {self.last_result['encoded_path']}")
            print("方向统计:")
            for direction, count in stats["direction_counts"].items():
                if count > 0:
                    print(f"  {direction} ({self.codes[direction]}): {count}次")
        else:
            print(f"求解失败: {stats.get('error', '未知错误')}")

    def show_maze(
        self,
        maze: Optional[List[List[str]]] = None,
        path: Optional[List[Tuple[int, int]]] = None,
        road_symbol: Optional[str] = None,
        wall_symbol: Optional[str] = None,
        start_symbol: Optional[str] = None,
        end_symbol: Optional[str] = None,
    ) -> None:
        """
        美化显示迷宫，使用MazeSolver的方法

        参数:
        maze (Optional[List[List[str]]]): 二维迷宫数组 (默认使用set_maze设置的迷宫)
        path (Optional[List[Tuple[int, int]]]): 路径坐标列表
        road_symbol (Optional[str]): 道路符号 (默认使用set_symbols设置的符号)
        wall_symbol (Optional[str]): 墙壁符号 (默认使用set_symbols设置的符号)
        start_symbol (Optional[str]): 起点符号 (默认使用set_symbols设置的符号)
        end_symbol (Optional[str]): 终点符号 (默认使用set_symbols设置的符号)
        """
        # 使用默认迷宫或提供的迷宫
        if maze is None:
            if self.maze is None:
                raise ValueError("未设置迷宫，请先调用set_maze()或传入maze参数")
            maze = self.maze

        # 使用默认符号或提供的符号
        road_symbol = road_symbol if road_symbol is not None else self.symbols["road"]
        wall_symbol = wall_symbol if wall_symbol is not None else self.symbols["wall"]
        start_symbol = (
            start_symbol if start_symbol is not None else self.symbols["start"]
        )
        end_symbol = end_symbol if end_symbol is not None else self.symbols["end"]

        showMaze(maze, path, road_symbol, wall_symbol, start_symbol, end_symbol)

    def solve_and_show(
        self,
        maze: Optional[List[List[str]]] = None,
        road_symbol: Optional[str] = None,
        wall_symbol: Optional[str] = None,
        start_symbol: Optional[str] = None,
        end_symbol: Optional[str] = None,
    ) -> Dict:
        """
        求解迷宫并美化显示结果

        参数:
        maze (Optional[List[List[str]]]): 二维迷宫数组 (默认使用set_maze设置的迷宫)
        road_symbol (Optional[str]): 道路符号 (默认使用set_symbols设置的符号)
        wall_symbol (Optional[str]): 墙壁符号 (默认使用set_symbols设置的符号)
        start_symbol (Optional[str]): 起点符号 (默认使用set_symbols设置的符号)
        end_symbol (Optional[str]): 终点符号 (默认使用set_symbols设置的符号)

        返回:
        Dict: 求解结果
        """
        # 使用默认迷宫或提供的迷宫
        if maze is None:
            if self.maze is None:
                raise ValueError("未设置迷宫，请先调用set_maze()或传入maze参数")
            maze = self.maze

        result = self.bfs_solve(
            maze, road_symbol, wall_symbol, start_symbol, end_symbol
        )

        print("原始迷宫:")
        # 使用默认符号或提供的符号
        road_symbol = road_symbol if road_symbol is not None else self.symbols["road"]
        wall_symbol = wall_symbol if wall_symbol is not None else self.symbols["wall"]
        start_symbol = (
            start_symbol if start_symbol is not None else self.symbols["start"]
        )
        end_symbol = end_symbol if end_symbol is not None else self.symbols["end"]

        showMaze(maze, None, road_symbol, wall_symbol, start_symbol, end_symbol)

        if result["found"]:
            print( "\n✓ 找到路径! ")
            tmp = "".join( [self.decode[move] for move in result['path'] ] )
            print(f"未编码路线: { tmp }")
            print(f"编码后路线: {result['encoded_path']}")
            print("解决方案:")
            showMaze(
                maze,
                result["movement"],
                road_symbol,
                wall_symbol,
                start_symbol,
                end_symbol,
            )
            print()
            self.print_statistics()
        else:
            print("\n✗ 未找到路径")
            self.print_statistics()

        return result

    def solve(
        self,
        road_symbol: Optional[str] = None,
        wall_symbol: Optional[str] = None,
        start_symbol: Optional[str] = None,
        end_symbol: Optional[str] = None,
    ) -> Dict:
        """
        求解当前设置的迷宫（便捷方法）

        参数:
        road_symbol (Optional[str]): 道路符号 (默认使用set_symbols设置的符号)
        wall_symbol (Optional[str]): 墙壁符号 (默认使用set_symbols设置的符号)
        start_symbol (Optional[str]): 入口符号 (默认使用set_symbols设置的符号)
        end_symbol (Optional[str]): 出口符号 (默认使用set_symbols设置的符号)

        返回:
        Dict: 求解结果

        异常:
        ValueError: 如果未设置迷宫
        """
        if self.maze is None:
            raise ValueError("未设置迷宫，请先调用set_maze()")

        return self.bfs_solve(
            self.maze, road_symbol, wall_symbol, start_symbol, end_symbol
        )

    def show(
        self,
        path: Optional[List[Tuple[int, int]]] = None,
        road_symbol: Optional[str] = None,
        wall_symbol: Optional[str] = None,
        start_symbol: Optional[str] = None,
        end_symbol: Optional[str] = None,
    ) -> None:
        """
        显示当前设置的迷宫（便捷方法）

        参数:
        path (Optional[List[Tuple[int, int]]]): 路径坐标列表
        road_symbol (Optional[str]): 道路符号 (默认使用set_symbols设置的符号)
        wall_symbol (Optional[str]): 墙壁符号 (默认使用set_symbols设置的符号)
        start_symbol (Optional[str]): 起点符号 (默认使用set_symbols设置的符号)
        end_symbol (Optional[str]): 终点符号 (默认使用set_symbols设置的符号)

        异常:
        ValueError: 如果未设置迷宫
        """
        if self.maze is None:
            raise ValueError("未设置迷宫，请先调用set_maze()")

        self.show_maze(
            self.maze, path, road_symbol, wall_symbol, start_symbol, end_symbol
        )

    def __str__(self) -> str:
        """字符串表示"""
        maze_info = f"{len(self.maze)}x{len(self.maze[0])}" if self.maze else "未设置"
        return (
            f"MazeSolver(maze={maze_info}, symbols={self.symbols}, codes={self.codes})"
        )

    def __repr__(self) -> str:
        """调试表示"""
        return self.__str__()


def print_maze_with_path(
    maze: List[List[str]],
    path: Optional[List[Tuple[int, int]]] = None,
    path_symbol: str = "·",
) -> None:
    """
    打印迷宫，如果提供路径则高亮显示路径

    参数:
    maze (List[List[str]]): 二维迷宫数组
    path (Optional[List[Tuple[int, int]]]): 路径坐标列表
    path_symbol (str): 用于标记路径的符号 (默认为 '·')
    """
    if not path:
        for row in maze:
            print("".join(row))
        return

    # 创建迷宫副本用于显示路径
    display_maze = [row[:] for row in maze]

    # 标记路径（除了起点和终点）
    for i, (x, y) in enumerate(path):
        if i != 0 and i != len(path) - 1:  # 不覆盖起点和终点
            display_maze[x][y] = path_symbol

    for row in display_maze:
        print("".join(row))


def showMaze(
    maze: List[List[str]],
    path: Optional[List[Tuple[int, int]]] = None,
    road_symbol: str = "0",
    wall_symbol: str = "1",
    start_symbol: str = "*",
    end_symbol: str = "#",
) -> None:
    """
    美化显示迷宫，墙显示为🧱，路径根据行走方向显示为箭头

    参数:
    maze (List[List[str]]): 二维迷宫数组
    path (Optional[List[Tuple[int, int]]]): 路径坐标列表
    road_symbol (str): 道路符号
    wall_symbol (str): 墙壁符号
    start_symbol (str): 起点符号
    end_symbol (str): 终点符号
    """
    if not maze or not maze[0]:
        return

    # 创建显示用的迷宫副本
    display_maze = [row[:] for row in maze]

    # 符号映射
    symbol_map = {
        wall_symbol: " # ",
        road_symbol: "   ",  # 两个空格让格子更宽
        start_symbol: " S ",  # 绿色圆圈表示起点
        end_symbol: " E ",  # 红色圆圈表示终点
    }

    # 如果有路径，计算每个位置的移动方向
    if path and len(path) > 1:
        # 方向箭头映射
        direction_arrows = {
            (-1, 0): " ↑ ",  # 向上
            (1, 0): " ↓ ",  # 向下
            (0, -1): " ← ",  # 向左
            (0, 1): " → ",  # 向右
        }

        # 为路径中的每个点（除了起点和终点）设置方向箭头
        for i in range(len(path) - 1):
            current_pos = path[i]
            next_pos = path[i + 1]

            # 计算移动方向
            direction = (next_pos[0] - current_pos[0], next_pos[1] - current_pos[1])

            # 只为中间的路径点设置箭头（不覆盖起点和终点）
            if i > 0:  # 不是起点
                x, y = current_pos
                if direction in direction_arrows:
                    display_maze[x][y] = direction_arrows[direction]

        # 为最后一个位置（终点前一步）也设置箭头
        if len(path) > 2:
            second_last = path[-2]
            last = path[-1]
            direction = (last[0] - second_last[0], last[1] - second_last[1])
            x, y = second_last
            if direction in direction_arrows:
                display_maze[x][y] = direction_arrows[direction]

    # 应用符号映射并打印
    for row in display_maze:
        display_row = []
        for cell in row:
            display_row.append(symbol_map.get(cell, cell))
        print("".join(display_row))


def create_maze_from_string(input_string: str) -> List[List[str]]:
    """
    将字符串转换为正方形迷宫

    参数:
    input_string (str): 输入字符串

    返回:
    List[List[str]]: 二维迷宫数组

    异常:
    ValueError: 如果字符串长度不是完全平方数
    """
    if not isinstance(input_string, str):
        raise TypeError("输入必须是字符串")

    if not input_string:
        raise ValueError("输入字符串不能为空")

    length = int(math.sqrt(len(input_string)))
    if length * length != len(input_string):
        raise ValueError(
            f"字符串长度 {len(input_string)} 不是完全平方数，无法形成正方形迷宫"
        )

    maze = []
    for i in range(length):
        row = []
        for j in range(length):
            index = i * length + j
            row.append(input_string[index])
        maze.append(row)

    return maze


# 示例和测试
if __name__ == "__main__":
    # 示例1: 从字符串创建迷宫
    print("=== 示例1: 从字符串创建的迷宫 ===")
    input_str = "*11110100001010000101111#"
    try:
        maze = create_maze_from_string(input_str)
        print("原始迷宫:")
        print_maze_with_path(maze)

        solver = MazeSolver()
        result = solver.bfs_solve(maze, "0", "1", "*", "#")

        if result["found"]:
            print( "\n✓ 找到最短路径!")
            print(f"编码路径: {result['encoded_path']}")
            print("\n带路径的迷宫 (·表示路径):")
            print_maze_with_path(maze, result["movement"])
            solver.print_statistics()
        else:
            print("\n✗ 未找到从入口到出口的路径")
            solver.print_statistics()

    except Exception as e:
        print(f"错误: {e}")

    print("\n" + "=" * 50)

    # 示例2: 使用MazeSolver类
    print("示例2: 使用MazeSolver类")

    solver = MazeSolver()

    print("使用不同编码获取路径:")
    print(f"默认编码 (U/D/L/R): {solver.encode_path(maze)}")

    solver.set_code("W", "S", "A", "D")
    print(f"WASD编码: {solver.encode_path(maze)}")

    solver.set_code("↑", "↓", "←", "→")
    print(f"箭头编码: {solver.encode_path(maze)}")

    solver.set_code("上", "下", "左", "右")
    print(f"中文编码: {solver.encode_path(maze)}")

    solver.set_code("F", "B", "L", "R")
    print(f"机器人编码: {solver.encode_path(maze)}")

    print("\n" + "=" * 50)

    # 示例3: 手动创建的迷宫
    maze2 = [
        ["S", "0", "1", "0", "E"],
        ["1", "0", "1", "0", "1"],
        ["0", "0", "0", "0", "0"],
        ["1", "1", "1", "1", "0"],
        ["0", "0", "0", "0", "0"],
    ]

    print("示例3: 手动创建的迷宫")
    print("原始迷宫:")
    print_maze_with_path(maze2)

    solver.set_code("W", "S", "A", "D")
    result2 = solver.bfs_solve(maze2, "0", "1", "S", "E")

    if result2["found"]:
        print(f"\nWASD路径: {result2['encoded_path']}")
        print("\n带路径的迷宫 (·表示路径):")
        print_maze_with_path(maze2, result2["movement"])
        solver.print_statistics()

    print("\n" + "=" * 50)

    # 示例4: 错误处理
    print("示例4: 错误处理测试")

    try:
        # 测试重复编码
        solver.set_code("A", "A", "B", "C")
    except ValueError as e:
        print(f"捕获到预期错误: {e}")

    try:
        # 测试无效迷宫
        invalid_maze = [["*", "1"], ["0"]]  # 行长度不一致
        solver.bfs_solve(invalid_maze)
    except ValueError as e:
        print(f"捕获到预期错误: {e}")

    print("\n" + "=" * 60)
    print("MazeSolver使用说明:")
    print("1. 创建求解器: solver = MazeSolver()")
    print("2. 设置编码: solver.set_code(up, down, left, right)")
    print("3. 求解迷宫: result = solver.bfs_solve(maze, road, wall, start, end)")
    print("4. 快速获取编码路径: solver.encode_path(maze, road, wall, start, end)")
    print("5. 查看统计信息: solver.print_statistics()")
    print("6. 支持任意字符编码：字母、数字、符号、表情、中文等")
    print("7. 应用场景：游戏控制、机器人导航、路径压缩存储等")
