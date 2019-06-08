classnamedic = {}

print("using default class names.")

for i in range(200):
	# for certain name, you can define the dic below
	classnamedic[str(i)] = str(i)

outputfilename = input("outputtxt name:")

outputfilename = trainfilename.strip("\n")

outputfile = open(outputfilename)

for line in outputfile:

	line = line.strip('\n')

	linearr = line.split(' ')

	imagefullfilename = linearr[0]

	imagefilename = imagefullfilename.split('/')[-1]

	detectionresultsfilename = imagefilename.replace('.jpg','.txt')

	detectionresultsfile = open("./input/detection-results/" + detectionresultsfilename, 'w')

	for i in range(len(linearr)):

		if i == 0:
			
			continue
		
		else:

			boxmessage = linearr[i]

			boxmessagearr = boxmessage.split(",")

			cls, score, x1, y1, x2, y2 = boxmessagearr[0:6]

			detectionresultsfile.write(classnamedic[cls], + " " + score + " " + x1 + " " + y1 + " " + x2 + " " + y2 + "\n")

	detectionresultsfile.close()

outputfile.close()