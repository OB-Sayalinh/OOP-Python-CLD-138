kilometers = 12.25
miles = 7.38

miles_to_meters = 1610
meters_to_miles = 1 / 1610
kilometer_to_meters = 1000

x_kilometers_to_miles = (kilometers * kilometer_to_meters) * meters_to_miles
x_miles_to_kilometers = (miles * miles_to_meters) * (1 / kilometer_to_meters)

print(miles, "miles is", round(x_miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(x_kilometers_to_miles,  2), "miles")

usd = round(812_629.1901, 2)
eur = round(1_035_868.8231, 2)

usd_to_eur = 0.90

# Interestingly enough the console is shows the emojis much darker than the code in dark mode
# than the light mode which I presume is just how they had to make it darker

print(usd, "dollars is", round(usd * usd_to_eur, 2), "💶 euros")
print(eur, "euros is", round(eur * 1 / usd_to_eur, 2), "💵 dollars")

