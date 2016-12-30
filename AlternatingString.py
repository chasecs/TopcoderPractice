# this approach make things more complicated, and not functioning well, deprecated!

# class AlternatingString:
# 	def maxLength(self, s):
# 		int_value = int(s,2);
# 		maxLength = temp = 1;

# 		while(int_value >1 ):
# 			if((int_value ^ (int_value>>1)) & 1):
# 				temp+=1;
# 			else:
# 				temp=1;
# 			if(temp > maxLength):
# 				maxLength = temp;
# 			int_value >>= 1;
#
# 		if(s[0] == '0' and int(s)>0 and maxLength <= 1):
# 			maxLength += 1;
# 		return maxLength;


class AlternatingString:
	def maxLength(self, s):
		i = 0;
		maxLength = temp = 1;
		# just compare each charater with the following one
		while( i <= len(s)-2):
			if(s[i] != s[i+1]):
				temp += 1;
			else:
				if(temp > maxLength):
					maxLength = temp;
				temp = 1;
			i +=1;
		if(temp > maxLength):
			return temp;
		else:
			return maxLength;
