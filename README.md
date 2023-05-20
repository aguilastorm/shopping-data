# File Generator

The File Generator is a Python script that processes a CSV file containing data related to different categories and generates two output files. The first file contains the average values for each category, and the second file contains the most popular brand for each category.

## Usage

1. Ensure you have Python installed (version 3.6 or higher).

2. Install the required dependencies by running the following command:

pip install -r requirements.txt


3. Prepare your input CSV file. The file should have the following format:

ID,Location,Category,Quantity,Brand
ID1,Minneapolis,shoes,2,Air
ID2,Chicago,shoes,1,Air
ID3,Central Department Store,shoes,5,BonPied
ID4,Quail Hollow,forks,3,Pfitzcraft


4. Modify the `input_example.csv` file with your own data or create a new CSV file with the same structure.

5. Run the script by executing the following command:

python file_generator.py

6. Two output files will be generated:
- `0_input_example.csv` - Contains the average values for each category.
- `1_input_example.csv` - Contains the most popular brand for each category.

## License

This project is licensed under the [MIT License](LICENSE.txt).
