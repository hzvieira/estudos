# BumpsInTheRoad

#Your car is old, it breaks easily. The shock absorbers are gone and you think it 
# can handle about 15 more bumps before it dies totally.

#Unfortunately for you, your drive is very bumpy! Given a string showing either 
# flat road ("_") or bumps ("n"), work out if you make it home safely. 
# 15 bumps or under, return "Woohoo!", over 15 bumps return "Car Dead".

def bumps(road):
    if (road.count("n") > 15):
        return "Car Dead"
    return "Woohoo!"


#Boas prátcas que gostei
#@ituxka
def bumps(road):
    MAX_BUMPS = 15
    SUCCESS_MESSAGE = 'Woohoo!'
    ERROR_MESSAGE = 'Car Dead'
    
    return SUCCESS_MESSAGE if road.count('n') <= MAX_BUMPS else ERROR_MESSAGE


#@falek-marcin
def bumps(road: str) -> str:
    """ Check if the car can handle the given number of bumps on the road. """
    return ["Woohoo!", "Car Dead"][road.count("n") > 15]