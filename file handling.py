#File Handling

# Create and write to the file
with open('data.txt', 'w') as file:
    for i in range(1, 11):
        file.write(f"{i}\n")

# Read and print the contents of the file
with open('data.txt', 'r') as file:
    content = file.read()
    print(content)

# Read the file and count the words
def count_words_in_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            words = content.split()  # Split the content into words
            word_count = len(words)
            print(f"Total number of words in {filename}: {word_count}")
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")

# Example usage
count_words_in_file('sample.txt')