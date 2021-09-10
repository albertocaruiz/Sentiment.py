file = open("mayo2020.txt", "r",encoding='utf-8')

number_of_lines = 0
number_of_words = 0
number_of_characters = 0
for line in file:
  line = line.strip("\n")
##won't count \n as character

  words = line.split()
  number_of_lines += 1
  number_of_words += len(words)
  number_of_characters += len(line)

file.close()

print("number of tweets:", number_of_lines, "number of words:", number_of_words, "number of characters:", number_of_characters)