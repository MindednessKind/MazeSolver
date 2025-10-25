"""
MazeSolver - 迷宫求解器包

一个功能完整的迷宫求解器，支持BFS算法、自定义编码和路径可视化。

主要功能：
- BFS最短路径寻找
- 自定义方向编码
- 多种迷宫格式支持
- 路径可视化
- 详细的路径分析

基本使用方法：
    from maze_solver import MazeSolver

    # 创建求解器
    solver = MazeSolver()

    # 定义迷宫
    maze = [
        ["*", "0", "1", "0", "#"],
        ["1", "0", "1", "0", "1"],
        ["0", "0", "0", "0", "0"],
        ["1", "1", "1", "1", "0"],
        ["0", "0", "0", "0", "0"],
    ]

    # 求解迷宫
    result = solver.bfs_solve(maze)
    if result["found"]:
        print(f"路径: {result['encoded_path']}")
"""

from .core import MazeSolver
from .utils import (
    print_maze_with_path,
    showMaze,
    create_square_maze_from_string,
    create_rectangle_maze_from_string,
    create_rectangle_maze_from_dimensions,
    solve_maze,
)

# 定义包的公共API
__all__ = [
    "MazeSolver",
    "print_maze_with_path",
    "showMaze",
    "create_maze_from_string",
    "create_rectangle_maze_from_string",
    "create_rectangle_maze_from_dimensions",
    "solve_maze",
]

# 版本信息
__version__ = "1.0.0"
__author__ = "MazeSolver Developer"
__email__ = "developer@example.com"
__description__ = (
    "A comprehensive maze solving package with BFS algorithm and path visualization"
)


# 包级别的便捷函数
def quick_solve(maze_string, symbols=None, code=None, size=None):
    """
    快速求解字符串迷宫的便捷函数

    参数:
    maze_string (str): 迷宫字符串
    size (int, optional): 迷宫边长，如果不提供则自动计算

    返回:
    dict: 求解结果

    示例:
    >>> result = quick_solve("*00100001000010000#")
    >>> print(result["encoded_path"])
    """

    if size is None:
        maze = create_square_maze_from_string(maze_string)
    else:
        maze = []
        for i in range(size):
            row = []
            for j in range(size):
                index = i * size + j
                if index < len(maze_string):
                    row.append(maze_string[index])
                else:
                    row.append("0")  # 默认填充道路
            maze.append(row)

    solver = MazeSolver()
    solver.set_maze(maze)
    if symbols is not None:
        solver.set_symbols(symbols)
    if code is not None:
        solver.set_code(code)

    solver.solve_and_show()
    return solver


def demo():
    """
    运行包的演示程序
    """
    print("MazeSolver 包演示")
    print("=" * 50)

    # 创建简单迷宫
    maze = [
        ["*", "0", "1", "0", "#"],
        ["1", "0", "1", "0", "1"],
        ["0", "0", "0", "0", "0"],
        ["1", "1", "1", "1", "0"],
        ["0", "0", "0", "0", "0"],
    ]

    print("演示迷宫:")
    print_maze_with_path(maze)

    print("\n求解结果:")
    result = solve_maze(maze)

    if result["found"]:
        print(f"✓ 找到路径: {result['encoded_path']}")
        print(f"路径长度: {result['length']} 位置")
        print(f"移动步数: {result['steps']} 步")

        print("\n美化显示:")
        showMaze(maze, result["movement"])
    else:
        print("✗ 未找到路径")

    print("\n使用自定义编码:")
    solver = MazeSolver()
    solver.set_code("↑", "↓", "←", "→")
    custom_result = solver.bfs_solve(maze)
    print(f"箭头编码: {custom_result['encoded_path']}")

    print("\n演示完成!")
