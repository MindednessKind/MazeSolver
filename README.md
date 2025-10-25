# MazeSolver

一个功能完整的迷宫求解器 Python 包，支持 BFS 算法、自定义编码和路径可视化。

## 特性

- 🔍 **BFS 最短路径算法** - 保证找到最短路径
- 🎨 **自定义方向编码** - 支持多种编码方案（UDLR、WASD、箭头、中文等）
- 📊 **路径可视化** - 美化的迷宫显示和路径标记
- 🛠️ **灵活的符号设置** - 自定义迷宫符号（道路、墙壁、起点、终点）
- 📈 **详细统计信息** - 路径长度、访问格子数、覆盖率等
- 🔧 **便捷的API** - 多种使用方式，从简单到高级
- ✅ **完善的错误处理** - 友好的错误提示和验证

## 安装

### 方式1: 从源码安装 (推荐)

```bash 
git clone https://github.com/MindednessKind/MazeSolver.git
cd MazeSolver
pip install -e .
```

### 方式2: setuptools 安装

```bash
git clone https://github.com/MindednessKind/MazeSolver.git
cd MazeSolver
python ./setup.py
```

## 快速开始

### 基本使用

```python
from maze_solver import MazeSolver

# 创建迷宫
maze = [
    ["*", "0", "1", "0", "#"],
    ["1", "0", "1", "0", "1"],
    ["0", "0", "0", "0", "0"],
    ["1", "1", "1", "1", "0"],
    ["0", "0", "0", "0", "0"],
]

# 创建求解器并求解
solver = MazeSolver()
result = solver.solve_and_show(maze)

```

### 便捷函数

```python
from maze_solver import quick_solve

# 一行代码求解迷宫
quick_solve(maze)
```

## 详细功能

### 1. 自定义方向编码

```python
from maze_solver import MazeSolver
solver = MazeSolver()

# 设置不同的编码方案
solver.set_code("↑", "↓", "←", "→")  # 箭头
solver.set_code("W", "S", "A", "D")  # WASD游戏
solver.set_code("上", "下", "左", "右")  # 中文
solver.set_code("N", "S", "W", "E")  # 罗盘方向


```

### 2. 自定义迷宫符号

```python
# 使用自定义符号
solver.set_symbols(".", "X", "S", "E")  # 道路、墙壁、起点、终点

custom_maze = [
    ["S", ".", "X", ".", "E"],
    ["X", ".", "X", ".", "X"],
    [".", ".", ".", ".", "."],
]

result = solver.bfs_solve(custom_maze)
```

### 3. 预设迷宫和便捷方法

```python
solver = MazeSolver()
solver.set_maze(maze)  # 预设迷宫
solver.set_symbols("0", "1", "*", "#")
solver.set_code("↑", "↓", "←", "→")

# 使用便捷方法
result = solver.solve()  # 求解预设迷宫
solver.show(result["movement"])  # 显示结果
```

### 4. 从字符串创建迷宫

```python
from maze_solver import create_square_maze_from_string, solve_maze

# 从字符串创建正方形迷宫
maze_string = "*000100001000010000#"  # 5x5迷宫
maze = create_square_maze_from_string(maze_string)
maze_string2 = "*0010011100110100#"  # 3x6迷宫
maze2 = create_rectangle_maze_from_string(maze_string2)
result = solve_maze(maze)
```

## API 参考

### MazeSolver 类

#### 主要方法

- `bfs_solve(maze, road_symbol, wall_symbol, start_symbol, end_symbol)` - BFS求解迷宫
- `set_code(up, down, left, right)` - 设置方向编码
- `set_symbols(road, wall, start, end)` - 设置迷宫符号
- `set_maze(maze)` - 设置预设迷宫
- `solve()` - 求解预设迷宫
- `show(path)` - 显示预设迷宫和路径
- `solve_and_show(maze)` - 一体化求解和显示

#### 便捷方法

- `get_codes()` - 获取当前编码设置
- `get_symbols()` - 获取当前符号设置
- `get_maze()` - 获取预设迷宫
- `get_last_result()` - 获取上次求解结果
- `print_statistics()` - 打印统计信息

### 工具函数

- `solve_maze(maze, ...)` - 便捷求解函数
- `print_maze_with_path(maze, path)` - 打印迷宫和路径
- `showMaze(maze, path)` - 美化显示迷宫
- `create_maze_from_string(string)` - 从字符串创建正方形迷宫
- `create_rectangle_maze_from_string(string, width, height, padding_char)` - 创建矩形迷宫
- `create_rectangle_maze_from_dimensions(string, width, height, fill_mode, padding_char)` - 多种填充模式的矩形迷宫

### 返回结果格式

```python
{
    "found": bool,           # 是否找到路径
    "path": List[Tuple],     # 路径坐标列表
    "movement": List[str],   # 移动序列
    "encoded_path": str,     # 编码后的路径字符串
    "length": int,           # 路径长度（位置数）
    "steps": int,            # 移动步数
    "statistics": {          # 统计信息
        "visited_cells": int,
        "total_cells": int,
        "coverage_percentage": float,
        "explored_positions": List[Tuple]
    }
}
```

## 高级用法

### 矩形迷宫应用场景

```python
from maze_solver import create_rectangle_maze_from_string, solve_maze, MazeSolver

# 游戏关卡设计
level_data = "*00100100100#"
maze = create_rectangle_maze_from_string(level_data, 4, 3)
solver = MazeSolver()
solver.set_code("W", "S", "A", "D")  # WASD 控制
result = solver.bfs_solve(maze)
print(f"游戏控制序列: {result['encoded_path']}")

# 训练数据生成
base_pattern = "*010101#"
sizes = [(3, 3), (4, 2), (6, 2)]
for width, height in sizes:
    maze = create_rectangle_maze_from_string(base_pattern, width, height, "0")
    result = solve_maze(maze)
    print(f"{width}x{height}: {result['encoded_path'] if result['found'] else '无解'}")
```

## 更多高级用法

### 批量处理多个迷宫

```python
mazes = [maze1, maze2, maze3]
solver = MazeSolver()
solver.set_symbols("0", "1", "*", "#")
solver.set_code("↑", "↓", "←", "→")

for i, maze in enumerate(mazes):
    solver.set_maze(maze)
    result = solver.solve()
    print(f"迷宫 {i+1}: {result['encoded_path'] if result['found'] else '无解'}")
```

### 多种编码格式输出

```python
encodings = [
    ("默认", "U", "D", "L", "R"),
    ("箭头", "↑", "↓", "←", "→"),
    ("WASD", "W", "S", "A", "D"),
    ("中文", "上", "下", "左", "右"),
]

for name, up, down, left, right in encodings:
    solver.set_code(up, down, left, right)
    path = solver.encode_path(maze)
    print(f"{name}: {path}")
```

### 错误处理

```python
try:
    result = solver.bfs_solve(maze)
    if not result["found"]:
        print("迷宫无解")
except ValueError as e:
    print(f"迷宫格式错误: {e}")
except Exception as e:
    print(f"其他错误: {e}")
```

## 命令行使用

安装后可以直接运行演示：

```bash
maze-solver-demo
```

## 开发和测试

### 运行测试

```bash
pytest
```

### 代码格式化

```bash
black maze_solver/
```

### 类型检查

```bash
mypy maze_solver/
```

## 示例

查看 `maze_solver.examples` 模块获取更多详细示例：

```python
from maze_solver.examples import main
main()  # 运行所有演示
```

## 贡献

欢迎贡献代码！请：

1. Fork 项目
2. 创建功能分支
3. 提交更改
4. 推送到分支
5. 创建 Pull Request

## 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

## 更新日志

### v1.0.0
- 初始版本发布
- 支持 BFS 迷宫求解
- 自定义编码和符号
- 路径可视化功能
- 完整的 API 文档
- **新增**: 矩形迷宫创建功能
  - `create_rectangle_maze_from_string()` - 创建任意尺寸矩形迷宫
  - `create_rectangle_maze_from_dimensions()` - 多种填充模式
  - 支持自动高度计算
  - 智能字符串处理（填充、重复、截断）

## 联系方式

- 作者：Mindedness
- 邮箱：FallenMind1020@outlook.com
- 项目主页：https://github.com/yourusername/maze-solver
- 问题报告：https://github.com/yourusername/maze-solver/issues