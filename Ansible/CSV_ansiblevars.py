import csv

def create_ansible_vars(csv_file, ansible_vars_file):
    # Ensure the output file has a .yml extension
    if not ansible_vars_file.endswith('.yml'):
        ansible_vars_file += '.yml'
        
    try:
        with open(csv_file, mode='r') as infile, open(ansible_vars_file, mode='w') as outfile:
            reader = csv.reader(infile)
            outfile.write('---\n')  # YAML start marker
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
                elif data_type == "boolean":
                    variable_value = variable_value.lower() in ['true', 'yes', '1']
                elif data_type == "null":
                    variable_value = "null"
                elif data_type == "string":
                    variable_value = f'"{variable_value}"'  # Enclose string in quotes
                else:
                    print(f'Skipping row: {row} (unsupported data type)')  # Debug output
                    continue  # Skip rows with unsupported data types
                
                print(f'Processing: data_type="{data_type}", description="{description}", variable_name="{variable_name}", variable_value="{variable_value}"')  # Debug output
                
                # Write to Ansible vars file
                if description:
                    outfile.write(f'{variable_name}: {variable_value}  # {description}\n')
                else:
                    outfile.write(f'{variable_name}: {variable_value}\n')
                    
        print(f'Successfully created {ansible_vars_file}')
    except Exception as e:
        print(f'Error: {e}')

if __name__ == "__main__":
    csv_file = input("Enter the path to the CSV file: ")
    ansible_vars_file = input("Enter the desired output Ansible vars file name (without extension): ")
    create_ansible_vars(csv_file, ansible_vars_file)
