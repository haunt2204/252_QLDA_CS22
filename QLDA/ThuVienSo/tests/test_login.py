import unittest
from ThuVienSo import dao


class TestLogin(unittest.TestCase):
    def test_case_1(self):
        self.assertTrue(dao.auth_user("user", 123))


if __name__ == '__main__':
    unittest.main()