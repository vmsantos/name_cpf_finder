def remove_bad_cpfs(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            cpf, *rest = line.split()  # Split each line by whitespace
            if "BAD" not in rest:  # Check if "BAD" is not in the rest of the line
                outfile.write(cpf + '\n')  # Write the CPF to the output file

# Usage example
input_file = 'cpf_results.txt'
output_file = 'good_cpf_results.txt'
remove_bad_cpfs(input_file, output_file)
print("Non-BAD CPFs have been written to", output_file)
