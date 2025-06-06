mile_to_metres = 1_609.344
gallon_to_liters = 3.785411784

def liters_100km_to_miles_gallon(liters):
    return (100 * 1_000 / mile_to_metres) / (liters / gallon_to_liters)

def miles_gallon_to_liters_100km(miles):
    return gallon_to_liters / (miles * mile_to_metres * 1_000)

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))

