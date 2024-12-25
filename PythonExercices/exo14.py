                                        #Framed word
word = input("Word: ")
frame_width = 30

padding = (frame_width - len(word) - 2) // 2  
width = "*" * frame_width
middle = "*" + " " * padding + word + " " * (frame_width - len(word) - 2 - padding) + "*"

print(width)
print(middle)
print(width)