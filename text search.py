#
#
text = " hey i am chandan Mallik and i am here for the AI development. id number is 234 . here is my number for the Project work 6370780590 nm "

i = 0
for m in text:
    if m.isnumeric() and text[i: i+10].isnumeric():
        chunk = text[i:i+11]
        print(chunk)


    i = i+1




