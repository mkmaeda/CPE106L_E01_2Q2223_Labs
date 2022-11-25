inputFile = input('Enter the file name: ')

OpenFile = open(inputFile, "r")

textList = list()

for line in OpenFile:
    line = line.strip('\n')
    textList.append(line)

i = True
while i:
    print('The file has',len(textList),'lines.')
    lineNum = int(input('Enter a line number or press 0 to quit: '))
    if lineNum == 0:
        i = False
    else:
        print(str(lineNum)+': '+textList[lineNum-1]+'\n')


OpenFile.close()