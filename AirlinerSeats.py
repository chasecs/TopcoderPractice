
class AirlinerSeats:
    def mostAisleSeats(self, width, seats):
        dotsNum = width-seats;
        groups = seats/2; # 'group' represents the string "S.S"

        if( 2*width >= 3*seats):
            if(seats % 2 == 0):
                result = ("." * (dotsNum - groups))+("S.S" * groups);
            else:
                result = ("." * (dotsNum - groups))+"S"+("S.S" * groups);
        else:
            result = ("S.S" * dotsNum) + ("S"*(seats - 2*dotsNum));

        if(width <= 50):
            aTuple = (result);
        elif(width >50 and width <= 100):
            aTuple = (result[0:51], result[51:]);
        else:
            aTuple = (result[0:51], result[ width-51: width ]);

        return aTuple;
