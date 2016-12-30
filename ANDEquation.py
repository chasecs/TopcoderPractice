class ANDEquation:
    def restoreY(self, A):
        alist = list(A);
        #caculate the bitwise and of all the elements in A
        temp = alist[0];
        for i in range(len(alist)-1):
            temp &= alist[i+1];

        #if the Y exists, it's necessary temp is in A
        if(temp not in alist):
            return -1;

        #remove that potential element, caculate the bitwise and of all the elements left in A
        alist.remove(temp);
        right = alist[0];
        for i in range(len(alist)-1):
            right &= alist[i+1];
        #if the result is still the same, then we found it
        if(right == temp):
            return right;
        else:
            return -1;
