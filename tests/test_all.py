"""
Запуск: python -m pytest tests/ -v   или  python tests/test_all.py
"""

import os
import sys
import tempfile
import unittest
from io import StringIO
from unittest.mock import patch

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestTask01(unittest.TestCase):
    def test_integer(self):
        import task01
        self.assertEqual(task01.get_param_type("42"), "целое число")
        self.assertEqual(task01.get_param_type("-10"), "целое число")

    def test_float(self):
        import task01
        self.assertEqual(task01.get_param_type("3.14"), "дробное число")
        self.assertEqual(task01.get_param_type("0.5"), "дробное число")

    def test_string(self):
        import task01
        self.assertEqual(task01.get_param_type("hello"), "строка")
        self.assertEqual(task01.get_param_type(""), "строка")


class TestTask02(unittest.TestCase):
    def test_table_has_rows(self):
        import task02
        with patch("sys.argv", ["task02.py", "5"]):
            out = StringIO()
            with patch("sys.stdout", out):
                task02.main()
        html = out.getvalue()
        self.assertIn("<table", html)
        self.assertIn("<td>1</td>", html)
        self.assertIn("<td>5</td>", html)


class TestTask03(unittest.TestCase):
    def test_color_for_level(self):
        import task03
        self.assertEqual(task03.color_for_level(1), "red")
        self.assertEqual(task03.color_for_level(2), "blue")
        self.assertEqual(task03.color_for_level(4), "purple")
        self.assertEqual(task03.color_for_level(5), "yellow")

    def test_render_dict(self):
        import task03
        html = task03.render({"a": 1}, level=1)
        self.assertIn("<ul>", html)
        self.assertIn("color:red", html)
        self.assertIn("[a]", html)

    def test_render_scalar(self):
        import task03
        html = task03.render("hello", level=1)
        self.assertIn("hello", html)
        self.assertIn("color:red", html)


class TestTask04(unittest.TestCase):
    def test_sum_digits(self):
        import task04
        with patch("sys.argv", ["task04.py", "123"]):
            out = StringIO()
            with patch("sys.stdout", out):
                task04.main()
        self.assertEqual(out.getvalue().strip(), "6")

    def test_sum_digits_negative(self):
        import task04
        with patch("sys.argv", ["task04.py", "-99"]):
            out = StringIO()
            with patch("sys.stdout", out):
                task04.main()
        self.assertEqual(out.getvalue().strip(), "18")


class TestTask05(unittest.TestCase):
    def test_longest_word(self):
        import task05
        with patch("sys.argv", ["task05.py", "a", "bb", "ccc", "dd"]):
            out = StringIO()
            with patch("sys.stdout", out):
                task05.main()
        self.assertEqual(out.getvalue().strip(), "ccc")


class TestTaskAdditional01(unittest.TestCase):
    def test_detect_type_integer(self):
        import importlib.util
        path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "cgi-bin", "task_additional01.py")
        spec = importlib.util.spec_from_file_location("cgi_task01", path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        self.assertEqual(mod.detect_type("42"), "integer")

    def test_detect_type_float(self):
        import importlib.util
        path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "cgi-bin", "task_additional01.py")
        spec = importlib.util.spec_from_file_location("cgi_task01", path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        self.assertEqual(mod.detect_type("3.14"), "float")

    def test_detect_type_string(self):
        import importlib.util
        path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "cgi-bin", "task_additional01.py")
        spec = importlib.util.spec_from_file_location("cgi_task01", path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        self.assertEqual(mod.detect_type("hello"), "string")


class TestTaskAdditional02(unittest.TestCase):
    def test_generates_file_with_rows(self):
        import task_additional02
        with tempfile.NamedTemporaryFile(suffix=".html", delete=False) as f:
            out_path = f.name
        try:
            with patch("sys.argv", ["task_additional02.py", "5", out_path]):
                with patch("sys.stderr", StringIO()):
                    task_additional02.main()
            with open(out_path, encoding="utf-8") as f:
                html = f.read()
            self.assertIn("<table", html)
            self.assertIn("Строка 1", html)
            self.assertIn("Строка 5", html)
            self.assertEqual(html.count("<tr "), 5)
        finally:
            if os.path.exists(out_path):
                os.unlink(out_path)


if __name__ == "__main__":
    unittest.main()
