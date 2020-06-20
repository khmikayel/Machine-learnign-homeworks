import csv


class Persistor:

    def __init__(self, filename):
        self.filename = filename

    def read_raw_data(self):
        file = open(self.filename, encoding='utf8', mode="r")
        return file.read()

    def save_raw_data(self, data):
        encoded_unicode = data.encode('utf8')
        file = open(self.filename, 'wb')
        file.write(encoded_unicode)
        file.close()

    def save_csv(self, data, output_filename):
        with open(output_filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for item in data:
                writer.writerow(item)