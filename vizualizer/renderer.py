
def algorithm_explained(Paragraph, font, max_width):
    words = Paragraph.split(" ")
    lines = []
    current_line = ""
    for word in words:
        test = current_line + word + " "
        #print (word, end = ' ')
        if font.size(test)[0] <= max_width:
            current_line = test
        else:
            lines.append(current_line)
            current_line = word + " "
    lines.append(current_line)
    return lines
    