def liters_100km_to_miles_gallon(liters):
#
    km = 100
    miles = km / 1.609344 
    gallons = liters / 3.785411784
    mpg = miles / gallons
    return mpg
#

def miles_gallon_to_liters_100km(miles):
#
    kms = miles * 1.609344
    liters_per_100km = 378.5411784 / kms
    return liters_per_100km
    
#

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
