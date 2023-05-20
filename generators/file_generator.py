import csv

class FileGenerator:
    def __init__(self, input_file):
        self.input_file = input_file
        self.data = self.import_csv()  # Import CSV data upon initialization

    def import_csv(self):
        data = {}
        with open(self.input_file, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                category = row[2]
                brand = row[4]
                quantity = int(row[3])
                if category not in data:
                    data[category] = []
                data[category].append((brand, quantity))
        return data

    def calculate_averages(self):
        averages = {}
        total_orders = sum(len(items) for items in self.data.values())
        for category, items in self.data.items():
            total_quantity = sum(quantity for _, quantity in items)
            num_items = len(items)
            if num_items > 0:
                average = total_quantity / total_orders
                averages[category] = round(average, 2)  # Round the average to 2 decimal places
        return averages

    def calculate_most_popular_brands(self):
        brands = {}
        for category, items in self.data.items():
            brand_count = {}
            for brand, _ in items:
                if brand not in brand_count:
                    brand_count[brand] = 0
                brand_count[brand] += 1
            if brand_count:
                popular_brand = max(brand_count, key=brand_count.get)
                brands[category] = popular_brand
        return brands

    def generate_files(self):
        averages = self.calculate_averages()
        most_popular_brands = self.calculate_most_popular_brands()

        # Generate the first file with category averages
        with open("0_" + self.input_file, "w", newline="") as file:
            writer = csv.writer(file)
            for category, average in averages.items():
                writer.writerow([category, round(average, 2)])

        # Generate the second file with most popular brands
        with open("1_" + self.input_file, "w", newline="") as file:
            writer = csv.writer(file)
            for category, brand in most_popular_brands.items():
                writer.writerow([category, brand])

        return averages, most_popular_brands

if __name__ == '__main__':
    # Create an instance of FileGenerator with the input file name
    generator = FileGenerator('input_example.csv')

    # Generate the files and retrieve the averages and most popular brands
    generator.generate_files()
