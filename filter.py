import csv
import sys
from urllib.parse import urlparse

def filter_domains(input_csv, output_csv):
    with open(input_csv, 'r') as infile, open(output_csv, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            domain = row[0]
            
            # Parse the domain using urlparse to extract the subdomain
            parsed_url = urlparse(f"http://{domain}")
            subdomain = parsed_url.netloc.split('.')[0].lower() if parsed_url.netloc.count('.') > 1 else None

            # Keep only main domains and 'www' subdomains
            if subdomain in [None, 'www']:
                writer.writerow([domain])

if __name__ == "__main__":
    # Check if the correct number of command-line arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python filter.py input_csv output_csv")
        sys.exit(1)

    input_csv_file = sys.argv[1]
    output_csv_file = sys.argv[2]

    filter_domains(input_csv_file, output_csv_file)
