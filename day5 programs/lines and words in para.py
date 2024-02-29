paragraph = """Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Pellentesque euismod ultricies ex, nec malesuada nunc convallis nec.
Suspendisse potenti. Duis ut justo ut magna scelerisque vestibulum. 
Vivamus tincidunt massa et neque ultricies, a lacinia erat scelerisque. 
Nunc tincidunt purus sit amet varius malesuada."""

def count_lines(paragraph):
    lines = paragraph.split("\n")
    return len(lines)
def count_words(line):
    words = line.split()
    return len(words)

print("number of lines in the paragraph: ", count_lines(paragraph))

lines = paragraph.split("\n")
print("word count in each line: ")
for line in lines:
      print(count_words(line))
