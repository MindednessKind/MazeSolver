import math
from typing import List, Dict, Optional, Tuple


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
    path: Optional[List[str]] = None,
    road_symbol: str = "0",
    wall_symbol: str = "1",
    start_symbol: str = "*",
    end_symbol: str = "#",
) -> None:
    """
    美化显示迷宫，墙显示为 #，路径根据行走方向显示为箭头

    参数:
    maze (List[List[str]]): 二维迷宫数组
    path (Optional[List[str]]): 路径移动序列（字符串列表）
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
        road_symbol: "   ",  # 三个空格让格子更宽
        start_symbol: " S ",  # S表示起点
        end_symbol: " E ",  # E表示终点
    }

    # 如果有路径，需要先找到起点，然后根据移动序列计算路径坐标
    if path and len(path) > 0:
        # 找到起点
        start_pos = None
        for i in range(len(maze)):
            for j in range(len(maze[0])):
                if maze[i][j] == start_symbol:
                    start_pos = (i, j)
                    break
            if start_pos:
                break

        if start_pos:
            # 根据移动序列计算路径坐标
            path_positions = [start_pos]
            current_pos = start_pos

            # 移动方向映射
            move_map = {
                "U": (-1, 0),
                "D": (1, 0),
                "L": (0, -1),
                "R": (0, 1),
                "u": (-1, 0),
                "d": (1, 0),
                "l": (0, -1),
                "r": (0, 1),
                "W": (-1, 0),
                "S": (1, 0),
                "A": (0, -1),
                "D": (0, 1),
                "w": (-1, 0),
                "s": (1, 0),
                "a": (0, -1),
                "d": (0, 1),
                "↑": (-1, 0),
                "↓": (1, 0),
                "←": (0, -1),
                "→": (0, 1),
                "上": (-1, 0),
                "下": (1, 0),
                "左": (0, -1),
                "右": (0, 1),
                "N": (-1, 0),
                "S": (1, 0),
                "W": (0, -1),
                "E": (0, 1),
                "n": (-1, 0),
                "s": (1, 0),
                "w": (0, -1),
                "e": (0, 1),
                "1": (-1, 0),
                "2": (1, 0),
                "3": (0, -1),
                "4": (0, 1),
                "F": (-1, 0),
                "B": (1, 0),
                "L": (0, -1),
                "R": (0, 1),
                "f": (-1, 0),
                "b": (1, 0),
                "l": (0, -1),
                "r": (0, 1),
            }

            # 方向箭头映射
            direction_arrows = {
                (-1, 0): " ↑ ",  # 向上
                (1, 0): " ↓ ",  # 向下
                (0, -1): " ← ",  # 向左
                (0, 1): " → ",  # 向右
            }

            # 计算每个移动的位置
            for move in path:
                if move in move_map:
                    dr, dc = move_map[move]
                    new_pos = (current_pos[0] + dr, current_pos[1] + dc)
                    path_positions.append(new_pos)
                    current_pos = new_pos

            # 为路径中的每个点（除了起点和终点）设置方向箭头
            for i in range(len(path_positions) - 1):
                current_pos = path_positions[i]
                next_pos = path_positions[i + 1]

                # 计算移动方向
                direction = (next_pos[0] - current_pos[0], next_pos[1] - current_pos[1])

                # 只为中间的路径点设置箭头（不覆盖起点和终点）
                if i > 0:  # 不是起点
                    x, y = current_pos
                    if 0 <= x < len(maze) and 0 <= y < len(maze[0]):
                        if direction in direction_arrows:
                            display_maze[x][y] = direction_arrows[direction]

    # 应用符号映射并打印
    for row in display_maze:
        display_row = []
        for cell in row:
            display_row.append(symbol_map.get(cell, f" {cell} "))
        print("".join(display_row))


def create_square_maze_from_string(input_string: str) -> List[List[str]]:
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


def create_rectangle_maze_from_string(
    input_string: str, width: int, height: Optional[int] = None, padding_char: str = "0"
) -> List[List[str]]:
    """
    将字符串转换为矩形迷宫

    参数:
    input_string (str): 输入字符串
    width (int): 迷宫宽度（列数）
    height (Optional[int]): 迷宫高度（行数），如果不提供则自动计算
    padding_char (str): 填充字符，当字符串长度不足时使用

    返回:
    List[List[str]]: 二维迷宫数组

    异常:
    ValueError: 如果参数无效
    TypeError: 如果输入类型错误

    示例:
    >>> create_rectangle_maze_from_string("*0110#", 3, 2)
    [['*', '0', '1'], ['1', '0', '#']]

    >>> create_rectangle_maze_from_string("*01#", 2)  # 自动计算高度为2
    [['*', '0'], ['1', '#']]
    """
    # 输入验证
    if not isinstance(input_string, str):
        raise TypeError("输入必须是字符串")

    if not isinstance(width, int) or width <= 0:
        raise ValueError("宽度必须是正整数")

    if height is not None:
        if not isinstance(height, int) or height <= 0:
            raise ValueError("高度必须是正整数")

    if not isinstance(padding_char, str) or len(padding_char) != 1:
        raise ValueError("填充字符必须是单个字符")

    if not input_string:
        raise ValueError("输入字符串不能为空")

    # 计算高度
    if height is None:
        # 自动计算高度
        height = len(input_string) // width
        if len(input_string) % width != 0:
            height += 1  # 向上取整

    total_cells = width * height

    # 处理字符串长度
    if len(input_string) < total_cells:
        # 用填充字符补齐
        input_string += padding_char * (total_cells - len(input_string))
    elif len(input_string) > total_cells:
        # 截断字符串
        input_string = input_string[:total_cells]

    # 创建迷宫
    maze = []
    for i in range(height):
        row = []
        for j in range(width):
            index = i * width + j
            row.append(input_string[index])
        maze.append(row)

    return maze


def create_rectangle_maze_from_dimensions(
    input_string: str,
    width: int,
    height: int,
    fill_mode: str = "pad",
    padding_char: str = "0",
) -> List[List[str]]:
    """
    根据指定的宽度和高度创建矩形迷宫，提供多种填充模式

    参数:
    input_string (str): 输入字符串
    width (int): 迷宫宽度
    height (int): 迷宫高度
    fill_mode (str): 填充模式 ("pad", "repeat", "truncate")
        - "pad": 不足时用padding_char填充，超出时截断
        - "repeat": 不足时重复字符串，超出时截断
        - "truncate": 仅截断，不足时保持原样
    padding_char (str): 填充字符

    返回:
    List[List[str]]: 二维迷宫数组

    异常:
    ValueError: 如果参数无效

    示例:
    >>> create_rectangle_maze_from_dimensions("*01#", 3, 2, "pad", "0")
    [['*', '0', '1'], ['#', '0', '0']]

    >>> create_rectangle_maze_from_dimensions("*01#", 3, 2, "repeat")
    [['*', '0', '1'], ['#', '*', '0']]
    """
    # 输入验证
    if not isinstance(input_string, str):
        raise TypeError("输入必须是字符串")

    if not isinstance(width, int) or width <= 0:
        raise ValueError("宽度必须是正整数")

    if not isinstance(height, int) or height <= 0:
        raise ValueError("高度必须是正整数")

    if fill_mode not in ["pad", "repeat", "truncate"]:
        raise ValueError("填充模式必须是 'pad', 'repeat' 或 'truncate'")

    if not isinstance(padding_char, str) or len(padding_char) != 1:
        raise ValueError("填充字符必须是单个字符")

    if not input_string:
        raise ValueError("输入字符串不能为空")

    total_cells = width * height

    # 根据填充模式处理字符串
    if fill_mode == "pad":
        if len(input_string) < total_cells:
            input_string += padding_char * (total_cells - len(input_string))
        elif len(input_string) > total_cells:
            input_string = input_string[:total_cells]
    elif fill_mode == "repeat":
        if len(input_string) < total_cells:
            # 重复字符串直到满足长度要求
            repeat_count = (total_cells // len(input_string)) + 1
            input_string = (input_string * repeat_count)[:total_cells]
        elif len(input_string) > total_cells:
            input_string = input_string[:total_cells]
    elif fill_mode == "truncate":
        if len(input_string) > total_cells:
            input_string = input_string[:total_cells]
        # 对于长度不足的情况，保持原字符串不变

    # 创建迷宫
    maze = []
    for i in range(height):
        row = []
        for j in range(width):
            index = i * width + j
            if index < len(input_string):
                row.append(input_string[index])
            else:
                row.append(padding_char)  # 对于truncate模式，不足时用填充字符
        maze.append(row)

    return maze


# 便捷函数
def solve_maze(
    maze: List[List[str]],
    road_symbol: str = "0",
    wall_symbol: str = "1",
    start_symbol: str = "*",
    end_symbol: str = "#",
    direction_codes: Optional[Dict[str, str]] = None,
) -> Dict:
    """
    便捷函数：一次性求解迷宫

    参数:
    maze: 迷宫数组
    road_symbol: 道路符号
    wall_symbol: 墙壁符号
    start_symbol: 起点符号
    end_symbol: 终点符号
    direction_codes: 方向编码字典

    返回:
    Dict: 求解结果
    """
    from .core import MazeSolver

    solver = MazeSolver()
    if direction_codes:
        solver.codes = direction_codes
    return solver.bfs_solve(maze, road_symbol, wall_symbol, start_symbol, end_symbol)
