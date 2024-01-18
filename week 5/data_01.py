# Chukwuemka Nwachukwu
# W211379501
# Cosc - Intro to Python 2

from fractions import Fraction


class RationalNumberProcessor:
    def __init__(self, input_filename, output_filename):
        # Sets up the rational number handler object
        self.input_filename = input_filename
        self.output_filename = output_filename

    def construct_rational_number(self, numerator, denominator):
        try:
            # Builds a rational number from the given parts
            return Fraction(numerator, denominator)
        except ZeroDivisionError:
            # Handles divizzy by zero fam
            return "Cannot divide by zero."

    def handle_rational_number_errors(self, error):
        if "ZeroDivisionError" in str(error):
            # Handles divi by zero issue
            return "Cannot divide by zero."
        else:
            # Handles any unknown error making a rational number
            return "An unknown error occurred."

    def handle_input_file_errors(self, error):
        if "FileNotFoundError" in str(error):
            # Handles file not found sitch when reading the input
            return "Input file not found."
        else:
            # Handles any unknown error reading the input
            return "An unknown error occurred."

    def read_lines_from_input_file(self):
        try:
            # Reads lines from the input file
            with open(self.input_filename, 'r') as file:
                return file.readlines()
        except Exception as e:
            # Handles any error reading the input
            return self.handle_input_file_errors(e)

    def process_input_data(self, lines):
        results = []
        for line in lines:
            try:
                # Process each line individually and convert to rational num
                numerator, denominator = map(int, line.strip().split(','))
                results.append(self.construct_rational_number(
                    numerator, denominator))
            except ValueError:
                # Handles invalid input data
                results.append("Invalid input data.")
            except Exception as e:
                # Handles any unknown error converting to rational num
                results.append(self.handle_rational_number_errors(e))
        return results

    def write_results_to_output_file(self, results):
        with open(self.output_filename, 'w') as file:
            # Writes the results to the output file
            file.writelines(str(result) + '\n' for result in results)

    def main(self):
        lines = self.read_lines_from_input_file()

        if isinstance(lines, str) and lines.startswith("Error"):
            # Handles error messages reading the file
            print(lines)
            return

        results = self.process_input_data(lines)

        self.write_results_to_output_file(results)


if __name__ == '__main__':
    input_file = 'data_01.txt'
    output_file = 'output.txt'
    processor = RationalNumberProcessor(input_file, output_file)
    processor.main()
