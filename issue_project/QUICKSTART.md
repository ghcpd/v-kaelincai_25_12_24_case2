# Quick Start Guide - Safari Date Picker Bug Demo Project

## ⚡ One-Command Test Run

```powershell
# Install dependencies and run tests
pip install -r requirements.txt; pytest -v
```

## 📊 Expected Test Results

```
✅ 10 passed - All API functionality tests pass
❌ 2 failed  - CSS Safari Bug detection tests (intentional!)
```

### Failing Tests (indicating bug exists):

1. **test_safari_calendar_indicator_has_absolute_positioning** ❌
   - Detected: CSS uses `position: absolute` causing Safari calendar icon misalignment

2. **test_safari_display_none_on_calendar_indicator** ❌
   - Detected: Safari-specific media query uses `display: none` completely hiding calendar picker

## 🔍 View Issue Details

```powershell
# View detailed Bug description
pytest tests/test_css_safari_bug.py -v -s
```

## 🚀 Run Application

```powershell
python src/app.py
```

Then visit: http://localhost:5000

## 📁 Key File Locations

- **Bug Location:** `src/static/css/styles.css` (lines 95-119)
- **Bug Detection:** `tests/test_css_safari_bug.py`
- **API Tests:** `tests/test_api.py`
- **Issue Details:** `KNOWN_ISSUE.md`

## 🐛 Bug Description

### Bug #1: position: absolute
```css
.date-picker::-webkit-calendar-picker-indicator {
    position: absolute;  /* ⚠️ Not supported by Safari */
    /* ... */
}
```

### Bug #2: display: none
```css
@media not all and (min-resolution:.001dpcm) {
    @supports (-webkit-appearance:none) {
        .date-picker::-webkit-calendar-picker-indicator {
            display: none; /* ⚠️ Completely hides Safari calendar */
        }
    }
}
```

## 📚 Next Steps

Read `KNOWN_ISSUE.md` to learn about:
- Detailed problem analysis
- 4 fix approaches
- Cross-browser compatibility notes
- Prevention measures

---

**Note:** This is an educational project. The CSS bugs are intentionally planted to demonstrate cross-browser compatibility issues.
