# simple python program to test GitHub
# combines items from both lists and creates a new list of tuples
# iterating over two lists simultaniously

first_list = [1, 2, 3, 4]
second_list = ["one", "two", "three", "four"]
combined_list = []

for number, word in zip(first_list, second_list):
    combined_list.append((number, word))

print(combined_list)
