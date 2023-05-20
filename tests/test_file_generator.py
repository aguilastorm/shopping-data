import unittest
import csv

import os
import sys

current_directory = os.getcwd()
sys.path.append(os.path.dirname(current_directory))

from generators.file_generator import FileGenerator

class TestFileGenerator(unittest.TestCase):
    def setUp(self):
        self.input_file_name = 'order_log00.csv'
        self.columns_amount = 4
        self.generator = FileGenerator(self.input_file_name)

    def test_import_files(self):
        result = self.generator.import_csv()
        self.assertIsInstance(result, list)
        for i in range(self.columns_amount):
            self.assertIsInstance(result[0], list)

    def test_check_file_format(self):
        columns_amount = 4
        result = self.generator.import_csv()
        self.assertEqual(len(result), columns_amount)


if __name__ == '__main__':
    unittest.main()
