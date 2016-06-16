print("Welcome to Highland Scrutineer")

dancers = []
dances = []
dancer_placings = {}

dancers = []
dancer_num = int(input("How many dancers were there?: "))
while len(dancers) + 1 <= dancer_num:
    dancers.append(input("What was the number of the dancer? "))

print("The list of dancers is:")
for dancer in dancers:
    print(dancer)

dances = []
dance_num = int(input("How many dances did these dancers compete in? "))

while len(dances) + 1 <= dance_num:
    dances.append(input("What was the name of the dance? "))

print("The list of dances is:")
for dance in dances:
    print(dance)

for dancer in dancers:
	dancer_placings[dancer] = []
	for dance in dances:
		place = input("What was " + dancer + "'s placing in the " + dance + " from")
		dancer_placings[dancer].append({dance:(judge, place)})

print(dancer_placings)