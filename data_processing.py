import sys
import csv

def read_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 3:
                name, age, score = parts
                try:
                    data.append((name.strip(), int(age.strip()), float(score.strip())))
                except ValueError:
                    continue  # Skip invalid lines
    return data

def calculate_statistics(data):
    if not data:
        return 0, 0.0
    total_score = sum(entry[2] for entry in data)
    average_score = total_score / len(data)
    return total_score, average_score

def write_to_csv(output_path, data, total, average):
    with open(output_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Age", "Score"])
        writer.writerows(data)
        writer.writerow([])
        writer.writerow(["Total Score", total])
        writer.writerow(["Average Score", average])

def main(input_file, output_file):
    data = read_data(input_file)
    total, average = calculate_statistics(data)
    write_to_csv(output_file, data, total, average)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python data_processing.py <input_file> <output_csv_file>")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
