# E-Commerce Order Filter - Safari Date Picker Bug

## Project Overview

This is a demonstration project that simulates a Safari browser date picker display issue in an e-commerce website's order filtering functionality. The project includes a simple Flask backend and frontend pages, with an **intentionally planted** CSS bug that causes Safari's date picker to malfunction.

## Problem Scenario

**Scenario Description:** The order filtering functionality of an e-commerce website uses HTML5 date input controls (`<input type="date">`). It works normally in Chrome and Firefox, but in Safari browsers (especially Safari on macOS), the date picker styles are broken and the calendar cannot be displayed correctly.

**Impact:** Safari users (approximately 15% of traffic) cannot use the date filtering functionality, resulting in degraded user experience.

## Tech Stack

- **Backend:** Python 3.x + Flask 3.0.0
- **Frontend:** HTML5, CSS3, Vanilla JavaScript
- **Testing:** pytest 7.4.3
- **Environment:** Windows 11

## Project Structure

```
issue_project/
├── src/
│   ├── app.py                          # Main Flask application file
│   ├── static/
│   │   ├── css/
│   │   │   └── styles.css              # CSS file with bug ⚠️
│   │   └── js/
│   │       └── main.js                 # Frontend JavaScript logic
│   └── templates/
│       └── index.html                  # Main page template
├── tests/
│   ├── __init__.py
│   ├── conftest.py                     # pytest configuration
│   ├── test_api.py                     # API unit tests
│   └── test_css_safari_bug.py          # CSS bug detection tests ⚠️
├── requirements.txt                    # Python dependencies
├── README.md                           # This file
├── KNOWN_ISSUE.md                      # Detailed issue description and fix ideas
└── .gitignore
```

## Quick Start

### 1. Install Dependencies

```powershell
# Create virtual environment (recommended)
python -m venv venv
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

### 2. Run Tests (See the Bug)

```powershell
# Run all tests
pytest -v

# Run only CSS bug tests
pytest tests/test_css_safari_bug.py -v

# View detailed output
pytest tests/test_css_safari_bug.py -v -s
```

**Expected Result:** 2 tests will **fail**, and these failing tests identify the problematic CSS code.

### 3. Run the Application

```powershell
# Start Flask server
python src/app.py
```

Visit http://localhost:5000 to view the application interface.

### 4. Verify the Bug (Optional)

If you have Safari browser (macOS):
1. Open http://localhost:5000 in Safari
2. Try clicking the date picker
3. Observe whether the calendar icon displays correctly
4. Try selecting a date and check if the date picker popup works

Compare with normal behavior in Chrome/Firefox.

## 已知问题说明

### 问题类型
**CSS兼容性问题 - Safari不正确处理`::-webkit-calendar-picker-indicator`伪元素样式**

### 问题位置
- **文件：** `src/static/css/styles.css`
- **行号：** 约95-119行
- **涉及选择器：**
  - `.date-picker::-webkit-calendar-picker-indicator`
  - Safari特定的媒体查询 `@media not all and (min-resolution:.001dpcm)`

### 触发条件
1. 用户使用Safari浏览器访问页面
2. 页面包含 `<input type="date" class="date-picker">` 元素
3. CSS中对 `::-webkit-calendar-picker-indicator` 应用了以下有问题的样式：
   - `position: absolute`（导致指示器位置错乱）
   - `display: none`（在Safari特定媒体查询中，完全隐藏日历图标）

### 预期 vs. 实际行为

| 浏览器 | 预期行为 | 实际行为 |
|--------|---------|---------|
| Chrome | ✅ 日历图标正常显示，点击可选择日期 | ✅ 正常工作 |
| Firefox | ✅ 日历图标正常显示，点击可选择日期 | ✅ 正常工作 |
| Safari | ✅ 日历图标正常显示，点击可选择日期 | ❌ 日历图标不可见或位置错乱，无法选择日期 |

### 复现步骤
1. 运行 `pytest tests/test_css_safari_bug.py -v`
2. 观察以下测试失败：
   - `test_safari_calendar_indicator_has_absolute_positioning` ❌
   - `test_safari_display_none_on_calendar_indicator` ❌

详细修复思路请参阅 [KNOWN_ISSUE.md](KNOWN_ISSUE.md)

## Test Description

The project contains two types of tests:

1. **API Functionality Tests** (`test_api.py`) - 8 tests, all should pass ✅
   - Validates Flask backend API correctness
   - Tests date filtering functionality

2. **CSS Bug Detection Tests** (`test_css_safari_bug.py`) - 5 tests
   - ✅ 3 tests should pass (basic CSS detection)
   - ❌ 2 tests should fail (detecting Safari bug)
   
The failing tests will clearly indicate the problem location and reason.

## Sample Data

The application contains 5 sample order records (hardcoded in `src/app.py`):

```python
Orders from Dec 1, 5, 8, 10, 11 (2025)
- Total: 5 orders
- Date range: 2025-12-01 to 2025-12-11
```

## API Endpoints

- `GET /` - Main page
- `GET /api/orders` - Get all orders
- `GET /api/orders?start_date=YYYY-MM-DD` - Filter by start date
- `GET /api/orders?end_date=YYYY-MM-DD` - Filter by end date
- `GET /api/orders?start_date=YYYY-MM-DD&end_date=YYYY-MM-DD` - Filter by date range
- `GET /api/health` - Health check

## License

This project is for educational and demonstration purposes only.

## Important Notice

⚠️ **This is a project demonstrating a bug, and the CSS issues are intentionally planted.** Do not use this code in production unless you have fixed the known issues.

---

**Next Step:** See [KNOWN_ISSUE.md](KNOWN_ISSUE.md) for detailed problem analysis and fix recommendations.
