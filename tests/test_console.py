#!/usr/bin/python3
import unittest
from unittest.mock import patch
from console import AirBnBConsole

class TestAirBnBConsole(unittest.TestCase):
    def setUp(self):
        self.console = AirBnBConsole()

    @patch('builtins.print')
    def test_do_help(self, mock_print):
        self.console.onecmd("help")
        mock_print.assert_any_call("Documented commands (type help <topic>):")
        mock_print.assert_any_call("========================================")
        mock_print.assert_any_call("EOF help quit")
        mock_print.assert_any_call("create")
        mock_print.assert_any_call("show")
        mock_print.assert_any_call("update")
        mock_print.assert_any_call("destroy")
        mock_print.assert_any_call("all")

    def test_do_EOF(self):
        result = self.console.onecmd("EOF")
        self.assertTrue(result)

    @patch('builtins.print')
    def test_do_quit(self, mock_print):
        result = self.console.onecmd("quit")
        mock_print.assert_called_with("Exiting the AirBnB Console....")
        self.assertTrue(result)

    @patch('builtins.print')
    def test_default(self, mock_print):
        self.console.onecmd("unknowncommand")
        mock_print.assert_called_with("Uknown commnd: unknowncommand")

    @patch('builtins.print')
    def test_do_create(self, mock_print):
        self.console.onecmd("create")
        mock_print.assert_called_with("Create Object...")

    @patch('builtins.print')
    def test_do_show(self, mock_print):
        self.console.onecmd("show")
        mock_print.assert_called_with("Objects List...")

    @patch('builtins.print')
    def test_do_destroy(self, mock_print):
        self.console.onecmd("destroy")
        mock_print.assert_called_with("Delete Object...")

    @patch('builtins.print')
    def test_do_all(self, mock_print):
        self.console.onecmd("all")
        mock_print.assert_called_with("List of classes...")

    @patch('builtins.print')
    def test_do_update(self, mock_print):
        self.console.onecmd("update")
        mock_print.assert_called_with("Update Object....")

if __name__ == '__main__':
    unittest.main()
