import random
import urllib.request 
urllib.request.urlretrieve("https://raw.githubusercontent.com/MrMohebi/xray-proxy-grabber-telegram/master/collected-proxies/row-url/actives.txt", "actives.txt")
urllib.request.urlretrieve("https://raw.githubusercontent.com/Surfboardv2ray/Proxy-sorter/main/output/converted.txt", "actives2.txt")

# Open the source text files
file1 = open('actives.txt', 'r')
file2 = open('actives2.txt', 'r')

# Read the contents of the text files
content1 = file1.read()
content2 = file2.read()

# Close the source text files
file1.close()
file2.close()

# Open the destination file
destination_file = open('merged.txt', 'w')

# Write the concatenated content to the destination file
destination_file.write(content1 + content2)
# Close the destination file
destination_file.close()

# Search and Remark

def search_and_replace(file_path, search_word, replace_word):
   with open(file_path, 'r') as file:
      file_contents = file.read()

      updated_contents = file_contents.replace(search_word, replace_word)
      updated_contents = file_contents.replace(search_word2, replace_word)
      
   with open(file_path, 'w') as file:
      file.write(updated_contents)

file_path = 'merged.txt'
search_word = '@v2ray_configs_pool'
search_word2 = '@Surfboardv2ray'
replace_word = '@VPNineh'
search_and_replace(file_path, search_word, search_word2, replace_word)

# End Of Search and Remark

# File names
input_file = 'merged.txt'
output_file = 'random'

# Number of lines to select
num_lines_to_select = 50

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
