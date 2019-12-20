#!/usr/bin/python3
"""test for db_storage"""
import unittest
import pep8


class Testdbstorage(unittest.TestCase):
    '''this will test the FileStorage'''

    def test_pep8_FileStorage(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")


if __name__ == "__main__":
    unittest.main()
