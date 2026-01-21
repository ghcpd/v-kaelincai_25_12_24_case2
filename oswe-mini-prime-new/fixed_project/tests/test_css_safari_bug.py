"""
Browser-based tests to reproduce the Safari CSS bug.
These tests check for CSS issues that affect Safari browsers.
"""
import pytest
import re
import os


def read_css_file():
    """Read the CSS file content."""
    css_path = os.path.join(os.path.dirname(__file__), '..', 'src', 'static', 'css', 'styles.css')
    with open(css_path, 'r', encoding='utf-8') as f:
        return f.read()


def test_safari_calendar_indicator_has_absolute_positioning():
    """
    TEST FAILURE #1: This test verifies the problematic CSS rule exists.
    
    The bug: Using `position: absolute` on ::-webkit-calendar-picker-indicator
    causes layout issues in Safari. The indicator becomes misaligned or invisible,
    making the date picker unusable.
    
    Expected: The CSS should NOT use position: absolute on the calendar indicator.
    Actual: The CSS contains position: absolute, which breaks Safari's date picker.
    
    File: src/static/css/styles.css
    Lines: ~95-105 (calendar picker indicator styling)
    """
    css_content = read_css_file()
    
    # Check if the problematic absolute positioning exists
    indicator_section = re.search(
        r'\.date-picker::-webkit-calendar-picker-indicator\s*\{([^}]+)\}',
        css_content,
        re.DOTALL
    )
    
    assert indicator_section is not None, "Calendar picker indicator style not found"
    indicator_styles = indicator_section.group(1)
    
    # This assertion SHOULD FAIL because position: absolute is present (the bug)
    assert 'position: absolute' not in indicator_styles, (
        "BUG DETECTED: Safari doesn't properly support 'position: absolute' on "
        "::-webkit-calendar-picker-indicator. This causes the date picker to "
        "become invisible or misaligned in Safari browsers. The position property "
        "should be removed or set to 'relative' or 'static'."
    )


def test_safari_display_none_on_calendar_indicator():
    """
    TEST FAILURE #2: This test verifies the Safari-specific media query bug.
    
    The bug: Using `display: none` on ::-webkit-calendar-picker-indicator within
    a Safari-specific media query completely hides the native calendar picker,
    making it impossible for Safari users to select dates.
    
    Expected: The CSS should NOT hide the calendar indicator in Safari.
    Actual: The CSS contains display: none in a Safari-specific rule.
    
    File: src/static/css/styles.css
    Lines: ~113-119 (Safari-specific media query)
    """
    css_content = read_css_file()
    
    # Check for Safari-specific media query with display: none
    # This pattern looks for @media...@supports...display: none
    has_safari_display_none = re.search(
        r'@media\s+not\s+all.*?min-resolution.*?@supports.*?-webkit-appearance.*?'
        r'\.date-picker::-webkit-calendar-picker-indicator.*?display:\s*none',
        css_content,
        re.DOTALL
    )
    
    # This assertion SHOULD FAIL because display: none is present (the bug)
    assert has_safari_display_none is None, (
        "BUG DETECTED: Setting 'display: none' on the calendar picker indicator "
        "in Safari-specific media queries completely hides the native date picker. "
        "Safari users cannot open the calendar to select dates. This rule should "
        "be removed to allow Safari's native date picker to function properly."
    )


def test_webkit_calendar_indicator_has_custom_background():
    """
    TEST: Verify that custom background is applied to the calendar indicator.
    
    While custom backgrounds can work, when combined with absolute positioning
    and display: none in Safari-specific rules, they contribute to the bug.
    """
    css_content = read_css_file()
    
    indicator_section = re.search(
        r'\.date-picker::-webkit-calendar-picker-indicator\s*\{([^}]+)\}',
        css_content,
        re.DOTALL
    )
    
    assert indicator_section is not None, "Calendar picker indicator style not found"
    indicator_styles = indicator_section.group(1)
    
    # Verify custom background exists
    assert 'background:' in indicator_styles or 'background-image:' in indicator_styles, (
        "Custom background styling should be present on calendar indicator"
    )


def test_date_picker_has_basic_styling():
    """
    TEST: Verify basic date picker styling is present (this should pass).
    """
    css_content = read_css_file()
    
    # Check for .date-picker class
    assert '.date-picker' in css_content, "Date picker class not found in CSS"
    
    # Check for basic properties
    date_picker_section = re.search(
        r'\.date-picker\s*\{([^}]+)\}',
        css_content,
        re.DOTALL
    )
    
    assert date_picker_section is not None, "Date picker style block not found"
    styles = date_picker_section.group(1)
    
    # These should all be present
    assert 'padding:' in styles, "Date picker should have padding"
    assert 'border:' in styles, "Date picker should have border"
    assert 'border-radius:' in styles, "Date picker should have border-radius"


def test_css_file_exists():
    """
    TEST: Verify the CSS file exists and is readable.
    """
    css_path = os.path.join(os.path.dirname(__file__), '..', 'src', 'static', 'css', 'styles.css')
    assert os.path.exists(css_path), f"CSS file not found at {css_path}"
    assert os.path.isfile(css_path), f"CSS path is not a file: {css_path}"
    
    # Verify it has content
    css_content = read_css_file()
    assert len(css_content) > 0, "CSS file is empty"
    assert '.date-picker' in css_content, "CSS file doesn't contain date picker styles"