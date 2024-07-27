import csv

def create_tfvars(csv_file, tfvars_file):
    try:
        with open(csv_file, mode='r') as infile:
            reader = csv.reader(infile)
            for row in reader:
                print(f'Read row: {row}')  # Debug output to inspect row contents
                if len(row) < 4:
                    print(f'Skipping row: {row} (less than 4 columns)')  # Debug output
                    continue  # Skip rows that don't have enough columns
                
                data_type = row[0].strip()
                description = row[1].strip()
                variable_name = row[2].strip()
                variable_value = row[3].strip()

                # Convert variable value based on data type
                if data_type == "int":
                    variable_value = int(variable_value)
                elif data_type == "float":
                    variable_value = float(variable_value)
                elif data_type == "string":
                    variable_value = f'"{variable_value}"'  # Enclose string in quotes
                else:
                    print(f'Skipping row: {row} (unsupported data type)')  # Debug output
                    continue  # Skip rows with unsupported data types
                
                print(f'Processing: data_type="{data_type}", description="{description}", variable_name="{variable_name}", variable_value="{variable_value}"')  # Debug output
                
                with open(tfvars_file, mode='a') as outfile:  # Open in append mode to write each variable
                    if description:
                        outfile.write(f'# {description}\n')
                    outfile.write(f'{variable_name} = {variable_value}\n\n')
                    
        print(f'Successfully created {tfvars_file}')
    except Exception as e:
        print(f'Error: {e}')

if __name__ == "__main__":
    csv_file = input("Enter the path to the CSV file: ")
    tfvars_file = input("Enter the desired output .tfvars file name: ")
    create_tfvars(csv_file, tfvars_file)
