import time

class Opener():

    def __init__(self):
        self.blnDoorOpen = False
        self.blnDoorClosed = False
        self.strDoorMotion = 'Not moving'
        self.blnEncoderState = False
        self.intEncoderCount = 0

    def runEncoder(self, intRPS, fltDuration):

        print 'starting the encoder...'
        self.intEncoderCount = 0
        while self.intEncoderCount < (fltDuration * intRPS):
            #print self.intEncoderCount
            time.sleep(1.0/float(intRPS))
            self.blnEncoderState = not self.blnEncoderState
            self.intEncoderCount += 1
        print 'stopping the encoder...'

def main():

    o = Opener()
    #Opener.runEncoder(o)
    o.runEncoder(1000,2.0)
    print o.intEncoderCount

if __name__ == '__main__':
    main()
