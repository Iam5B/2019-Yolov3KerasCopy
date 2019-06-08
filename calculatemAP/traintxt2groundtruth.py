classnamedic = {}

print("using default class names.")

for i in range(200):
	# for certain name, you can define the dic below
	classnamedic[str(i)] = str(i)

trainfilename = input("traintxt name:")

trainfilename = trainfilename.strip("\n")

trainfile = open(trainfilename)

for line in trainfile:

	line = line.strip('\n')

	linearr = line.split(' ')

	imagefullfilename = linearr[0]

	imagefilename = imagefullfilename.split('/')[-1]

	groundtruthfilename = imagefilename.replace('.jpg','.txt')

	groundtruthfile = open("./input/ground-truth/" + groundtruthfilename, 'w')

	for i in range(len(linearr)):

		if i == 0:
			
			continue
		
		else:

			boxmessage = linearr[i]

			boxmessagearr = boxmessage.split(",")

			x1, y1, x2, y2, cls = boxmessagearr[0:5]

			groundtruthfile.write(classnamedic[cls] + " " + x1 + " " + y1 + " " + x2 + " " + y2 + "\n")

	groundtruthfile.close()

trainfile.close()