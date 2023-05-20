import unittest
import csv
import os
from unittest.mock import Mock, call, patch
from generators.file_generator import FileGenerator

class TestFileGenerator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up a sample input file for testing
        cls.input_file = "input_example.csv"
        data = [
            ["ID1", "Minneapolis", "shoes", "2", "Air"],
            ["ID2", "Chicago", "shoes", "1", "Air"],
            ["ID3", "Central Department Store", "shoes", "5", "BonPied"],
            ["ID4", "Quail Hollow", "forks", "3", "Pfitzcraft"]
        ]

        # Write the sample data to the input file
        with open(cls.input_file, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(data)

        # Create an instance of the FileGenerator class for testing
        cls.generator = FileGenerator(cls.input_file)

    @classmethod
    def tearDownClass(cls):
        # Remove the sample input file after testing
        if os.path.exists("input_example.csv"):
            os.remove("input_example.csv")

    def test_import_csv(self):
        # Define the expected data after importing the CSV file
        expected_data = {
            "shoes": [("Air", 2), ("Air", 1), ("BonPied", 5)],
            "forks": [("Pfitzcraft", 3)]
        }

        # Call the import_csv method and compare the result with the expected data
        data = self.generator.import_csv()
        self.assertEqual(data, expected_data)

    def test_calculate_most_popular_brands(self):
        # Create a test data dictionary
        data = {
            "shoes": [("Air", 2), ("Air", 1), ("BonPied", 5)],
            "forks": [("Pfitzcraft", 3)]
        }

        # Create a new instance of the FileGenerator class for testing
        generator = FileGenerator("input_example.csv")
        generator.data = data

        # Call the calculate_most_popular_brands method and compare the result with the expected result
        result = generator.calculate_most_popular_brands()
        expected_result = {"shoes": "Air", "forks": "Pfitzcraft"}
        self.assertEqual(result, expected_result)

    def test_calculate_averages(self):
        # Generate the output files and retrieve the averages and most popular brands
        averages, most_popular_brands = self.generator.generate_files()

        # Test the content of the first generated file
        with open("0_" + self.generator.input_file, "r") as file:
            reader = csv.reader(file)

            # Define the expected averages
            expected_averages = {"shoes": 2.0, "forks": 0.75}

            # Compare each row in the file with the expected average values
            for row, (category, average) in zip(reader, expected_averages.items()):
                self.assertEqual(row, [category, str(round(average, 2))])

        # Test the content of the second generated file
        with open("1_" + self.generator.input_file, "r") as file:
            reader = csv.reader(file)

            # Define the expected most popular brands
            expected_brands = {"shoes": "Air", "forks": "Pfitzcraft"}

            # Compare each row in the file with the expected brand values
            for row, (category, brand) in zip(reader, expected_brands.items()):
                self.assertEqual(row, [category, brand])

        # Compare the calculated averages and most popular brands with the expected values
        expected_averages = {"shoes": 2.0, "forks": 0.75}
        expected_brands = {"shoes": "Air", "forks": "Pfitzcraft"}
        self.assertEqual(averages, expected_averages)
        self.assertEqual(most_popular_brands, expected_brands)


if __name__ == '__main__':
    unittest.main()
