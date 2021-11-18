import random
from base.const import RANDON_RANGES

def loadPersonalBest(eventId,eType):
    rRange = RANDON_RANGES[eventId]
    rand = random.uniform(rRange[0],rRange[1])
    if eType == 1 or eType == 2: 
        PB = convertTime(rand)
        return PB
    else:
        PB ="{0:.2f}".format(random.uniform(rRange[0],rRange[1])) 
        return PB
    
def convertTime(data):
    time = data
    if time > 60:
        minutes = int(time/60)
        seconds = time%60
        if seconds<10:
            stringTime = "{0}:0{1:.2f}".format(minutes,seconds)
        else:
            stringTime = "{0}:{1:.2f}".format(minutes,seconds)
    else:
        stringTime = "{0:.2f}".format(data)
    return stringTime
