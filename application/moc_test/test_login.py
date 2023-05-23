import unittest
from unittest import mock
from refactored_app import choose_login


class TestChooseLogin(unittest.TestCase):

    @mock.patch('builtins.input')
    @mock.patch('getpass.getpass')
    @mock.patch('refactored_app.db1.login_to_app')
    def test_choose_login(self, mock_login_to_app, mock_getpass, mock_input):

        mock_input.side_effect = ["test_username", "correct_password"]
        mock_getpass.return_value = "coreect_password"

        mock_login_to_app.return_value = True

        result = choose_login()

        mock_input.assert_called_once_with("Username: ")
        mock_getpass.assert_called_once_with(prompt="Password: ")
        mock_login_to_app.assert_called_once_with(
            "test_username", "correct_password")

        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
