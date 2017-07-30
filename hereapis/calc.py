from math import sin, cos, sqrt, atan2, radians

# approximate radius of earth in km
#R = 6373.0
R = 3956 # in miles

def getDistance(latt1, lonn1, latt2, lonn2):
    
    #lat1 = radians(52.2296756)
    #lon1 = radians(21.0122287)
    #lat2 = radians(52.406374)
    #lon2 = radians(16.9251681)
    lat1 = radians(latt1)
    lon1 = radians(lonn1)
    lat2 = radians(latt2)
    lon2 = radians(lonn2)
    
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = (sin(dlat/2))**2 + cos(lat1) * cos(lat2) * (sin(dlon/2))**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    distance = R * c
    
    #print("Result:", distance)
   
    return distance

def getLatLong(data):
    return""