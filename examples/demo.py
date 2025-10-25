#!/usr/bin/env python3
"""
MazeSolver 包演示脚本

这个脚本展示了 maze_solver 包的基本用法。
"""

import sys
import os

# 添加父目录到路径，以便能够导入 maze_solver
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from maze_solver import MazeSolver, solve_maze, print_maze_with_path, showMaze


def demo_basic_usage():
    """演示基本使用方法"""
    print("=== 基本使用演示 ===")

    # 创建简单迷宫
    maze = [
        ["*", "0", "1", "0", "#"],
        ["1", "0", "1", "0", "1"],
        ["0", "0", "0", "0", "0"],
        ["1", "1", "1", "1", "0"],
        ["0", "0", "0", "0", "0"],
    ]

    print("迷宫:")
    print_maze_with_path(maze)

    # 方法1: 使用便捷函数
    print("\n方法1: 使用便捷函数")
    result = solve_maze(maze)
    if result["found"]:
        print(f"✓ 找到路径: {result['encoded_path']}")
        print(f"路径长度: {result['length']} 个位置")
        print(f"移动步数: {result['steps']} 步")

    # 方法2: 使用 MazeSolver 类
    print("\n方法2: 使用 MazeSolver 类")
    solver = MazeSolver()
    result2 = solver.bfs_solve(maze)
    if result2["found"]:
        print(f"✓ 找到路径: {result2['encoded_path']}")
        print("美化显示:")
        showMaze(maze, result2["movement"])

    print()


def demo_custom_encoding():
    """演示自定义编码"""
    print("=== 自定义编码演示 ===")

    maze = [
        ["*", "0", "0", "0", "#"],
        ["1", "1", "1", "0", "1"],
        ["0", "0", "0", "0", "1"],
        ["0", "1", "1", "1", "1"],
        ["0", "0", "0", "0", "0"],
    ]

    print("迷宫:")
    print_maze_with_path(maze)

    solver = MazeSolver()

    # 测试不同编码
    encodings = [
        ("默认编码", "U", "D", "L", "R"),
        ("箭头编码", "↑", "↓", "←", "→"),
        ("WASD编码", "W", "S", "A", "D"),
        ("中文编码", "上", "下", "左", "右"),
    ]

    print("\n不同编码的路径结果:")
    for name, up, down, left, right in encodings:
        solver.set_code(up, down, left, right)
        result = solver.bfs_solve(maze)
        if result["found"]:
            print(f"{name:12}: {result['encoded_path']}")

    print()


def demo_custom_symbols():
    """演示自定义符号"""
    print("=== 自定义符号演示 ===")

    # 使用自定义符号的迷宫
    custom_maze = [
        ["S", ".", "X", ".", "E"],
        ["X", ".", "X", ".", "X"],
        [".", ".", ".", ".", "."],
        ["X", "X", "X", ".", "X"],
        [".", ".", ".", ".", "."],
    ]

    print("自定义符号迷宫 (S=起点, E=终点, .=道路, X=墙壁):")
    print_maze_with_path(custom_maze)

    solver = MazeSolver()
    solver.set_symbols(".", "X", "S", "E")  # 道路、墙壁、起点、终点
    solver.set_code("↑", "↓", "←", "→")

    result = solver.bfs_solve(custom_maze)
    if result["found"]:
        print(f"\n✓ 找到路径: {result['encoded_path']}")
        print("美化显示:")
        showMaze(custom_maze, result["movement"], ".", "X", "S", "E")

        print(f"\n统计信息:")
        print(f"  访问了 {result['statistics']['visited_cells']} 个格子")
        print(f"  覆盖率: {result['statistics']['coverage_percentage']}%")
    else:
        print("✗ 未找到路径")

    print()


def demo_no_solution():
    """演示无解迷宫"""
    print("=== 无解迷宫演示 ===")

    # 创建无解迷宫
    impossible_maze = [
        ["*", "1", "1", "1"],
        ["1", "1", "1", "1"],
        ["1", "1", "1", "1"],
        ["1", "1", "1", "#"],
    ]

    print("无解迷宫:")
    print_maze_with_path(impossible_maze)

    solver = MazeSolver()
    result = solver.bfs_solve(impossible_maze)

    print(f"\n求解结果: {'找到路径' if result['found'] else '无解'}")
    print(f"访问了 {result['statistics']['visited_cells']} 个格子")
    print(f"覆盖率: {result['statistics']['coverage_percentage']}%")

    print()


def demo_convenience_methods():
    """演示便捷方法"""
    print("=== 便捷方法演示 ===")

    maze = [
        ["*", "0", "1", "0", "#"],
        ["1", "0", "1", "0", "1"],
        ["0", "0", "0", "0", "0"],
        ["1", "1", "1", "1", "0"],
        ["0", "0", "0", "0", "0"],
    ]

    solver = MazeSolver()
    solver.set_maze(maze)  # 预设迷宫
    solver.set_code("→", "←", "↑", "↓")  # 自定义编码

    print("使用预设迷宫和便捷方法:")
    print(f"求解器状态: {solver}")

    # 使用便捷方法求解
    result = solver.solve()
    if result["found"]:
        print(f"✓ 路径: {result['encoded_path']}")
        print("使用便捷显示方法:")
        solver.show(result["movement"])

    print()


def main():
    """主函数"""
    print("MazeSolver 包演示")
    print("=" * 60)

    demo_basic_usage()
    demo_custom_encoding()
    demo_custom_symbols()
    demo_no_solution()
    demo_convenience_methods()

    print("=" * 60)
    print("演示完成！")
    print("\n更多详细示例请参考:")
    print("- maze_solver.examples 模块")
    print("- README.md 文档")
    print("- 在线文档")


if __name__ == "__main__":
    main()
