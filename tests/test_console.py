# tests/test_console.py

import unittest
from console import AirBnBConsole


class TestConsole(unittest.TestCase):
    def test_quit_command(self):
        console = AirBnBConsole()
        self.assertTrue(console.onecmd("quit"))

    def test_EOF_command(self):
        console = AirBnBConsole()
        self.assertTrue(console.onecmd("EOF"))


if __name__ == '__main__':
    unittest.main()
