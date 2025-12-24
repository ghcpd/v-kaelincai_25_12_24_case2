# Project Fix Task Prompt

## Task Overview

You need to fix an e-commerce order filtering project that has a **Safari browser date picker CSS compatibility issue**. The project works normally in Chrome and Firefox, but the date picker functionality is completely broken in Safari browsers.

**Important Requirements:**
1. Create the fixed project in a new directory `fixed_project/`
2. Do not modify any files in the original `issue_project/` directory
3. After fixing, ensure all pytest tests pass
4. Maintain complete project structure and functionality

---

## Problem Analysis

### Core Issues

The CSS file (`src/static/css/styles.css`) contains two critical bugs that cause Safari date picker to fail:

**Bug #1: Using `position: absolute` on `::-webkit-calendar-picker-indicator` pseudo-element**
- Location: Approximately lines 95-109
- Problem: Safari cannot properly handle absolute positioning on pseudo-elements, causing the calendar icon to be misaligned or completely invisible
- Impact: Users cannot see the calendar icon and don't know they can select a date

**Bug #2: Using `display: none` in Safari-specific media query**
- Location: Approximately lines 113-119
- Problem: A Safari-detection media query completely hides the calendar picker trigger element
- Impact: Safari users completely lose date selection functionality and can only manually type dates

### Test Verification

The project includes two failing test cases (`tests/test_css_safari_bug.py`):
1. `test_safari_calendar_indicator_has_absolute_positioning` - Detects absolute positioning issue
2. `test_safari_display_none_on_calendar_indicator` - Detects display: none issue

These tests currently fail and should all pass after the fix.

---

## Project Structure

### Current Problem Project Structure (Reference only, do not modify)

```
issue_project/
├── src/
│   ├── app.py                          # Flask main application (no modification needed)
│   ├── static/
│   │   ├── css/
│   │   │   └── styles.css              # ⚠️ CSS file with bugs
│   │   └── js/
│   │       └── main.js                 # Frontend JavaScript (no modification needed)
│   └── templates/
│       └── index.html                  # HTML template (no modification needed)
├── tests/
│   ├── __init__.py
│   ├── conftest.py                     # pytest configuration (no modification needed)
│   ├── test_api.py                     # API tests (no modification needed)
│   └── test_css_safari_bug.py          # CSS bug detection tests (no modification needed)
├── requirements.txt                    # Python dependencies (no modification needed)
├── README.md                           # Project documentation
├── KNOWN_ISSUE.md                      # Detailed issue description
└── .gitignore
```

### Required Fixed Project Structure

Please create the following complete directory structure and ensure all files are properly copied and fixed:

```
fixed_project/
├── src/
│   ├── app.py                          # Copy from issue_project (no modification needed)
│   ├── static/
│   │   ├── css/
│   │   │   └── styles.css              # ✅ Fix Safari CSS bugs
│   │   └── js/
│   │       └── main.js                 # Copy from issue_project (no modification needed)
│   └── templates/
│       └── index.html                  # Copy from issue_project (no modification needed)
├── tests/
│   ├── __init__.py                     # Copy from issue_project
│   ├── conftest.py                     # Copy from issue_project
│   ├── test_api.py                     # Copy from issue_project
│   └── test_css_safari_bug.py          # Copy from issue_project (no modification needed)
├── requirements.txt                    # Copy from issue_project
├── README.md                           # Copy from issue_project or update with fix notes
├── FIX_SUMMARY.md                      # ✅ Create new: Document fix details
└── .gitignore                          # Copy from issue_project
```

---

## Fix Task Checklist

### 1. Create New Directory Structure
Create `fixed_project/` and all subdirectories under `v-kaelincai_25_12_24_case2/`

### 2. Copy All Files
Copy all files from `issue_project/` to corresponding locations in `fixed_project/`

### 3. Fix CSS Bugs
Modify `fixed_project/src/static/css/styles.css` to resolve the following issues:


**Fix Principles:**
- Maintain the date picker's visual style and functionality
- Ensure compatibility with Chrome, Firefox, and Safari browsers
- Keep the calendar icon visible and clickable
- Don't break existing CSS styles

### 4. Verify the Fix
Ensure all tests pass:
```bash
cd fixed_project
pytest tests/test_css_safari_bug.py -v
pytest -v
```

### 5. Create Fix Documentation
Document the following in `fixed_project/FIX_SUMMARY.md`:
- Specific code changes made
- Before/after comparison
- Test results
- Technical rationale for the fix

---

## Validation Criteria

After completing the fix, the following standards must be met:

1. ✅ All pytest tests pass (especially the two tests in `test_css_safari_bug.py`)
2. ✅ Date picker displays and functions normally in Safari browser
3. ✅ Date picker continues to work normally in Chrome/Firefox
4. ✅ Original visual design and user experience are maintained
5. ✅ CSS code follows browser compatibility best practices

---

## Technical Hints

- `::-webkit-calendar-picker-indicator` pseudo-element behaves differently across WebKit engines
- Safari handles `position` and `display` properties on pseudo-elements more strictly
- Consider using simpler style override methods to avoid complex positioning and hiding operations
- Custom styling can be retained, but ensure it doesn't break native functionality
- Removing Safari-specific hiding rules is critical

---

## Important Notes

1. **Do not modify issue_project directory** - All work should be done in fixed_project
2. **Do not change project functionality** - Only fix CSS bugs, don't add new features
3. **Keep test files unchanged** - Files in tests directory should only be copied, not modified
4. **Ensure cross-browser compatibility** - Fix should work with all major browsers
5. **Preserve existing comments** - Other comments in CSS file can be retained or updated

---

## Completion Indicators

The task is complete when you have finished all the following steps:

- [x] Create `fixed_project/` directory structure
- [x] Copy all necessary files
- [x] Fix Safari CSS bugs in `styles.css`
- [x] Run tests and ensure all pass
- [x] Create `FIX_SUMMARY.md` documenting fix details

Begin the fix task! Remember: work only in the `fixed_project/` directory, do not modify `issue_project/`.
