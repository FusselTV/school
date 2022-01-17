def convertFile(filename, length):
    with open(filename, 'r') as file:
        data = file.read().replace('\n', '') # add "," if not already present
        data = data.split(",")
    output =[]
    for x in data:
        if len(x) <= length:
            output.append(x)
    return output
print(convertFile("mutelist.txt", 5)) #file name and item length to be added
