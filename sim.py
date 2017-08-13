from ailookahead import AiLookahead
from aibasic import AiRand, AiLeft
from aiquality import AiQuality
from aiapi import AiRequest, AiResponse
from board import Board
import sys

if __name__ == "__main__":
	aireq = AiRequest({'board':"2,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0", 'gid':1, 'prior':""})
	moveNum = 0
	lines = []
	while (True):
		moveNum += 1
		airesp = AiQuality(aireq)
		aireq.b = aireq.b.move(airesp.dir)
		lines.append(str(moveNum) + "," + str(aireq.b) + "," + str(airesp.dir))
		aireq.b = aireq.b.drop()
		if (aireq.b.canMove() == False):
			break
	for i in range(0, len(lines)):
		lines[i] = lines[i] + "," + str(len(lines)-(i+1)) + "," + str(aireq.b.score) + "\n"
		sys.stdout.write(lines[i])
