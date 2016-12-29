class SplitIntoPairs:
	def makepairs(self, A, X):
		elementNum = len(A);
		result = elementNum / 2 - 1;
		templist = sorted(A);
		for i in range(elementNum):
			if(templist[i] >=0):
				break;

		if(i % 2 == 0):
			return result+1 == correct;
		elif(templist[i] * templist[i-1] >= X):
			return result+1;
		else:
			return result;
