import random

# File names
input_url = 'https://raw.githubusercontent.com/MrMohebi/xray-proxy-grabber-telegram/master/collected-proxies/row-url/actives.txt'
output_file = 'random'

# Number of lines to select
num_lines_to_select = 100

def select_random_lines(input_url, output_file, num_lines):
    with open(input_url, 'r') as f:
        lines = f.readlines()

    # Ensure we do not exceed the number of available lines
    num_lines = min(num_lines, len(lines))
    
    # Randomly sample lines without replacement
    selected_lines = random.sample(lines, num_lines)
    
    with open(output_file, 'w') as f:
        f.writelines(selected_lines)

if __name__ == "__main__":
    select_random_lines(input_url, output_file, num_lines_to_select)
