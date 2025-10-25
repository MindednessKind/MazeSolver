from maze_solver import (
    MazeSolver,
    print_maze_with_path,
    create_square_maze_from_string,
    quick_solve,
    showMaze,
)


def demo_basic_usage():
    """演示基本使用方法"""
    print("=== 演示1: 基本使用方法 ===")

    # 创建简单迷宫
    maze = [
        ["*", "0", "1", "0", "0"],
        ["1", "0", "1", "0", "1"],
        ["0", "0", "0", "0", "0"],
        ["1", "1", "1", "1", "0"],
        ["0", "0", "0", "0", "#"],
    ]

    print("迷宫:")
    print_maze_with_path(maze)

    # 创建求解器
    solver = MazeSolver()

    # 使用默认编码求解
    result = solver.bfs_solve(maze)

    if result["found"]:
        print( "\n✓ 找到路径!")
        print(f"默认编码路径: {result['encoded_path']}")
        print("\n路径可视化:")
        print_maze_with_path(maze, result["movement"])

        print("\n美化显示:")
        showMaze(maze, result["movement"])
        print()
        solver.print_statistics()
    else:
        print("✗ 未找到路径")

    print()


def demo_set_symbols():
    """演示set_symbols功能"""
    print("=== 演示2: set_symbols符号设置 ===")

    # 创建求解器
    solver = MazeSolver()

    print("默认符号设置:")
    print(f"符号配置: {solver.get_symbols()}")
    print(f"编码配置: {solver.get_codes()}")

    # 使用默认符号的迷宫
    default_maze = [
        ["*", "0", "1", "0", "#"],
        ["1", "0", "1", "0", "1"],
        ["0", "0", "0", "0", "0"],
        ["1", "1", "1", "1", "0"],
        ["0", "0", "0", "0", "0"],
    ]

    print("\n使用默认符号的迷宫:")
    print_maze_with_path(default_maze)

    # 不需要传入符号参数
    result = solver.bfs_solve(default_maze)
    if result["found"]:
        print(f"路径: {result['encoded_path']}")

    # 设置自定义符号
    solver.set_symbols(".", "X", "S", "E")
    solver.set_code("↑", "↓", "←", "→")

    print( "\n更改符号设置:")
    print(f"符号配置: {solver.get_symbols()}")
    print(f"编码配置: {solver.get_codes()}")

    # 使用自定义符号的迷宫
    custom_maze = [
        ["S", ".", "X", ".", "E"],
        ["X", ".", "X", ".", "X"],
        [".", ".", ".", ".", "."],
        ["X", "X", "X", ".", "X"],
        [".", ".", ".", ".", "."],
    ]

    print("\n自定义符号迷宫:")
    print_maze_with_path(custom_maze)

    # 现在可以直接求解，不需要传入符号参数
    result2 = solver.bfs_solve(custom_maze)
    if result2["found"]:
        print(f"路径: {result2['encoded_path']}")
        print("美化显示:")
        solver.show_maze(custom_maze, result2["path"])

    print()


def demo_set_maze():
    """演示set_maze功能"""
    print("=== 演示3: set_maze迷宫预设 ===")

    solver = MazeSolver()
    solver.set_symbols(".", "X", "S", "E")
    solver.set_code("↑", "↓", "←", "→")

    # 创建迷宫
    maze = [
        ["S", ".", "X", ".", "E"],
        ["X", ".", "X", ".", "X"],
        [".", ".", ".", ".", "."],
        ["X", "X", "X", ".", "X"],
        [".", ".", ".", ".", "."],
    ]

    print("设置迷宫:")
    solver.set_maze(maze)
    print_maze_with_path(solver.get_maze())

    print(f"\n求解器状态: {solver}")

    # 使用便捷方法
    print("\n使用便捷方法求解:")
    result = solver.solve()  # 不需要传入任何参数

    if result["found"]:
        print(f"路径编码: {result['encoded_path']}")
        print("美化显示:")
        solver.show(result["movement"])  # 便捷显示方法

    # 演示处理多个相同格式的迷宫
    print("\n处理多个相同格式的迷宫:")
    mazes = [
        [["S", ".", "E"], [".", "X", "."], [".", ".", "."]],
        [["S", "X", "E"], [".", ".", "."], ["X", "X", "."]],
    ]

    for i, test_maze in enumerate(mazes, 1):
        print(f"\n迷宫 {i}:")
        solver.set_maze(test_maze)
        result = solver.solve()
        print(f"路径: {result['encoded_path'] if result['found'] else '无解'}")

    print()


def demo_different_encodings():
    """演示不同编码方案"""
    print("=== 演示4: 不同编码方案 ===")

    maze = [
        ["S", "0", "1", "0", "E"],
        ["1", "0", "1", "0", "1"],
        ["0", "0", "0", "0", "0"],
        ["1", "1", "1", "1", "0"],
        ["0", "0", "0", "0", "0"],
    ]

    print("迷宫:")
    print_maze_with_path(maze)

    solver = MazeSolver()
    # 预设符号，避免每次传入
    solver.set_symbols("0", "1", "S", "E")

    # 测试多种编码方案
    encoding_schemes = [
        ("默认编码", "U", "D", "L", "R"),
        ("WASD游戏", "W", "S", "A", "D"),
        ("箭头符号", "↑", "↓", "←", "→"),
        ("数字编码", "1", "2", "3", "4"),
        ("中文方向", "上", "下", "左", "右"),
        ("机器人指令", "F", "B", "L", "R"),
        ("罗盘方向", "N", "S", "W", "E"),
        ("表情符号", "🔼", "🔽", "◀️", "▶️"),
    ]

    print("\n不同编码方案的路径结果:")
    for name, up, down, left, right in encoding_schemes:
        solver.set_code(up, down, left, right)
        # 不需要传入符号参数了
        path = solver.encode_path(maze)
        print(f"{name:12}: {path}")

    print()


def demo_string_maze():
    """演示从字符串创建迷宫"""
    print("=== 演示5: 从字符串创建迷宫 ===")

    # 测试有效的字符串迷宫
    input_string = "*000010000100001000010000#"  # 5x5 迷宫

    try:
        maze = create_square_maze_from_string(input_string)
        print("从字符串创建的迷宫:")
        print_maze_with_path(maze)

        solver = MazeSolver()
        solver.set_code("↑", "↓", "←", "→")

        result = solver.bfs_solve(maze, "0", "1", "*", "#")

        if result["found"]:
            print(f"\n箭头编码路径: {result['encoded_path']}")
            print("解决方案:")
            print_maze_with_path(maze, result["movement"])
            solver.print_statistics()
        else:
            print("未找到路径")
            solver.print_statistics()

    except Exception as e:
        print(f"错误: {e}")

    print()


def demo_complex_maze():
    """演示复杂迷宫求解"""
    print("=== 演示6: 复杂迷宫求解 ===")

    complex_maze = [
        ["#", "1", "1", "1", "1", "1", "1", "1"],
        ["0", "0", "0", "1", "0", "0", "0", "1"],
        ["1", "1", "0", "1", "0", "1", "0", "1"],
        ["1", "0", "0", "0", "0", "1", "0", "1"],
        ["1", "0", "1", "1", "1", "1", "0", "1"],
        ["1", "0", "0", "0", "0", "0", "0", "1"],
        ["1", "1", "1", "1", "1", "1", "0", "0"],
        ["1", "1", "1", "1", "1", "1", "1", "*"],
    ]

    print("复杂迷宫 (从#到*):")
    print_maze_with_path(complex_maze)

    solver = MazeSolver()
    solver.set_symbols("0", "1", "*", "#")
    solver.set_code("U", "D", "L", "R")

    result = solver.bfs_solve(complex_maze)

    if result["found"]:
        print( "\n✓ 找到解决方案!")
        print(f"路径编码: {result['encoded_path']}")
        print(f"路径长度: {result['length']} 个位置")
        print(f"移动步数: {result['steps']} 步")

        print("\n解决方案可视化:")
        print_maze_with_path(complex_maze, result["movement"])

        print()
        solver.print_statistics()

        # 显示多种编码格式
        print("\n其他编码格式:")
        solver.set_code("W", "S", "A", "D")
        print(f"WASD: {solver.encode_path(complex_maze)}")

        solver.set_code("上", "下", "左", "右")
        print(f"中文: {solver.encode_path(complex_maze)}")

    else:
        print("未找到路径")
        solver.print_statistics()

    print()


def demo_error_handling():
    """演示错误处理"""
    print("=== 演示7: 错误处理 ===")

    solver = MazeSolver()

    print("编码错误测试:")
    print("测试1: 重复编码错误")
    try:
        solver.set_code("A", "A", "B", "C")  # 重复编码
    except ValueError as e:
        print(f"✓ 捕获预期错误: {e}")

    print("\n测试2: 空编码错误")
    try:
        solver.set_code("", "D", "L", "R")  # 空编码
    except ValueError as e:
        print(f"✓ 捕获预期错误: {e}")

    print("\n符号错误测试:")
    print("测试3: 重复符号错误")
    try:
        solver.set_symbols("A", "A", "B", "C")  # 重复符号
    except ValueError as e:
        print(f"✓ 捕获预期错误: {e}")

    print("\n测试4: 空符号错误")
    try:
        solver.set_symbols("", "1", "*", "#")  # 空符号
    except ValueError as e:
        print(f"✓ 捕获预期错误: {e}")

    print("\n测试3: 无效迷宫格式")
    try:
        invalid_maze = [["*", "0"], ["1"]]  # 行长度不一致
        solver.bfs_solve(invalid_maze)
    except ValueError as e:
        print(f"✓ 捕获预期错误: {e}")

    print("\n测试4: 无效字符串迷宫")
    try:
        create_square_maze_from_string("*00100#")  # 长度不是完全平方数
    except ValueError as e:
        print(f"✓ 捕获预期错误: {e}")

    print("\n测试5: 无解迷宫")
    impossible_maze = [["*", "1", "1"], ["1", "1", "1"], ["1", "1", "#"]]

    print("无解迷宫:")
    print_maze_with_path(impossible_maze)

    result = solver.bfs_solve(impossible_maze)
    print(f"求解结果: {'找到路径' if result['found'] else '无解'}")
    solver.print_statistics()

    print()


def demo_convenience_functions():
    """演示便捷函数"""
    print("=== 演示8: 便捷函数 ===")

    maze = [
        ["*", "0", "0", "0", "#"],
        ["1", "1", "1", "0", "1"],
        ["0", "0", "0", "0", "1"],
        ["0", "1", "1", "1", "1"],
        ["0", "0", "0", "0", "0"],
    ]

    print("测试迷宫:")
    print_maze_with_path(maze)

    # 使用便捷函数
    result = quick_solve(maze)

    if result["found"]:
        print( "\n使用便捷函数求解:")
        print(f"自定义编码路径: {result['encoded_path']}")
        print("路径可视化:")
        print_maze_with_path(maze, result["movement"])

    print()


def demo_advanced_features():
    """演示高级功能"""
    print("=== 演示9: 高级功能 ===")

    # 创建一个较大的迷宫
    large_input = "*" + "0" * 8 + "1" * 8 + "0" * 7 + "#"  # 5x5
    maze = create_square_maze_from_string(large_input)

    print("大型迷宫:")
    print_maze_with_path(maze)

    solver = MazeSolver()
    solver.set_symbols("0", "1", "*", "#")

    # 第一次求解
    solver.set_code("N", "S", "W", "E")
    result1 = solver.bfs_solve(maze)

    print(f"\n第一次求解 (N/S/W/E): {result1['encoded_path']}")

    # 获取最后结果
    last_result = solver.get_last_result()
    if last_result:
        print(f"从缓存获取: 访问了 {last_result['statistics']['visited_cells']} 个格子")

    # 第二次求解使用不同编码
    solver.set_code("🌟", "⭐", "💫", "✨")
    result2 = solver.bfs_solve(maze)

    print(f"第二次求解 (星星编码): {result2['encoded_path']}")

    # 打印详细统计
    solver.print_statistics()

    print()


def demo_show_maze():
    """演示美化显示功能"""
    print("=== 演示10: 美化迷宫显示 ===")

    # 创建测试迷宫
    maze = [
        ["*", "0", "1", "0", "0", "1", "0"],
        ["1", "0", "1", "0", "1", "0", "0"],
        ["0", "0", "0", "0", "1", "1", "0"],
        ["0", "1", "1", "0", "0", "0", "0"],
        ["0", "0", "0", "1", "1", "1", "0"],
        ["1", "1", "0", "0", "0", "0", "0"],
        ["1", "1", "1", "1", "1", "1", "#"],
    ]

    print("原始迷宫 (普通显示):")
    print_maze_with_path(maze)

    print("\n原始迷宫 (美化显示):")
    showMaze(maze)

    # 求解迷宫
    solver = MazeSolver()
    solver.set_code("↑", "↓", "←", "→")
    result = solver.bfs_solve(maze)

    if result["found"]:
        print(f"\n✓ 找到路径! 编码: {result['encoded_path']}")

        print("\n解决方案 (普通显示):")
        print_maze_with_path(maze, result["movement"])

        print("\n解决方案 (美化显示 - 方向箭头):")
        showMaze(maze, result["movement"])

        print()
        solver.print_statistics()
    else:
        print("✗ 未找到路径")

    print("\n使用solve_and_show一体化方法:")
    solver2 = MazeSolver()
    solver2.set_code("W", "S", "A", "D")

    # 创建另一个测试迷宫
    simple_maze = [
        ["*", "0", "0", "1"],
        ["1", "1", "0", "1"],
        ["0", "0", "0", "0"],
        ["1", "1", "1", "#"],
    ]

    solver2.solve_and_show(simple_maze)

    print()


def main():
    """主函数，运行所有演示"""
    print("MazeSolver 完整功能演示")
    print("=" * 60)

    demo_basic_usage()
    demo_set_symbols()
    demo_set_maze()
    demo_different_encodings()
    demo_string_maze()
    demo_complex_maze()
    demo_error_handling()
    demo_convenience_functions()
    demo_advanced_features()
    demo_show_maze()

    print("=" * 60)
    print("功能总结:")
    print("✓ 基本迷宫求解 (BFS最短路径)")
    print("✓ 自定义方向编码")
    print("✓ 多种迷宫输入格式")
    print("✓ 路径可视化")
    print("✓ 美化迷宫显示 (🧱墙 + ➡️箭头)")
    print("✓ 详细统计信息")
    print("✓ 错误处理和验证")
    print("✓ 便捷函数接口")
    print("✓ 高级功能 (结果缓存等)")
    print()
    print("使用方法:")
    print("1. 创建求解器: solver = MazeSolver()")
    print("2. 设置迷宫: solver.set_maze(maze)")
    print("3. 设置符号: solver.set_symbols(road, wall, start, end)")
    print("4. 设置编码: solver.set_code(up, down, left, right)")
    print("5. 求解迷宫: result = solver.solve() 或 solver.bfs_solve(maze)")
    print("6. 美化显示: solver.show(path) 或 showMaze(maze, path)")
    print("7. 查看结果: solver.print_statistics()")


if __name__ == "__main__":
    main()
