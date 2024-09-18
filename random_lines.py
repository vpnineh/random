import random
import 'https://raw.githubusercontent.com/MrMohebi/xray-proxy-grabber-telegram/master/collected-proxies/row-url/actives.txt' = convert

# File names
input_file = 'convert'
output_file = 'random'

# Number of lines to select
num_lines_to_select = 100

def select_random_lines(input_file, output_file, num_lines):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    # Ensure we do not exceed the number of available lines
    num_lines = min(num_lines, len(lines))
    
    # Randomly sample lines without replacement
    selected_lines = random.sample(lines, num_lines)
    
    with open(output_file, 'w') as f:
        f.writelines(selected_lines)

if __name__ == "__main__":
    select_random_lines(input_file, output_file, num_lines_to_select)
