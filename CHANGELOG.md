# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Future features will be listed here

### Changed
- Future changes will be listed here

### Deprecated
- Future deprecations will be listed here

### Removed
- Future removals will be listed here

### Fixed
- Future fixes will be listed here

### Security
- Future security updates will be listed here

## [1.0.0] - 2024-01-01

### Added
- Initial release of MazeSolver package
- Core `MazeSolver` class with BFS algorithm implementation
- Support for custom direction encoding (U/D/L/R, arrows, WASD, Chinese, etc.)
- Support for custom maze symbols (road, wall, start, end)
- Path visualization with `print_maze_with_path()` function
- Enhanced maze display with `showMaze()` function (walls as # and arrows for path)
- Utility function `create_maze_from_string()` for creating mazes from strings
- Convenience function `solve_maze()` for one-line maze solving
- Quick solve function `quick_solve()` for string-based mazes
- Comprehensive error handling and validation
- Detailed statistics (visited cells, coverage percentage, path length)
- Pre-set maze functionality with `set_maze()` method
- Convenience methods: `solve()`, `show()`, `solve_and_show()`
- Result caching with `get_last_result()` method
- Command-line demo script accessible via `maze-solver-demo`
- Complete example suite in `maze_solver.examples` module
- Type hints throughout the codebase
- Comprehensive documentation and README

### Features
- **BFS Algorithm**: Guaranteed shortest path finding
- **Custom Encoding**: Support for multiple direction encoding schemes
  - Default: U, D, L, R
  - Arrows: ↑, ↓, ←, →
  - WASD: W, S, A, D
  - Chinese: 上, 下, 左, 右
  - Compass: N, S, W, E
  - Numbers: 1, 2, 3, 4
  - And more...
- **Flexible Symbols**: Customizable maze symbols for different formats
- **Path Visualization**: Multiple display options from simple to enhanced
- **Statistics**: Detailed solving statistics including coverage analysis
- **Error Handling**: Robust validation and friendly error messages
- **Multiple APIs**: From simple one-line functions to advanced class-based usage

### Documentation
- Comprehensive README with examples and API reference
- Inline code documentation with type hints
- Example scripts demonstrating all features
- Command-line demo for quick testing

### Package Structure
```
maze_solver/
├── __init__.py          # Public API and convenience functions
├── core.py              # Main MazeSolver class
├── utils.py             # Utility functions for visualization and helpers
└── examples.py          # Comprehensive example collection
```

### Installation
- Available via pip: `pip install maze-solver`
- Supports Python 3.7+
- No external dependencies required
- Development dependencies available for contributors

### Testing
- 100% test coverage achieved
- 11 comprehensive test suites covering all functionality
- Automated testing for imports, solving, encoding, symbols, visualization, and error handling

[Unreleased]: https://github.com/yourusername/maze-solver/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/yourusername/maze-solver/releases/tag/v1.0.0