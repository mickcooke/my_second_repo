stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]
print(stops)
#1. Add "Edinburgh Waverley" to the end of the list
stops.append("Edinburgh Waverley")
print(stops)
#2. Add "Glasgow Queen St" to the start of the 
stops.insert(0, "Glasgow Queen St")
print(stops)
#3. Add "Polmont" at the appropriate point (between "Falkirk High" and "Linlithgow")
stops.insert(4, "Polmont")
print(stops)
#4. Print out the index position of "Linlithgow"
index = stops.index("Linlithgow")
print(index)
#5. Remove "Livingston" from the list using its name
stops.remove("Livingston")
print(stops)
#6. Delete "Cumbernauld" from the list by index
del stops[2]
print(stops)
#7. Print the number of stops there are in the list
print(len(stops))
#8. Sort the list alphabetically
sorted_stops = sorted(stops)
print(sorted_stops)
#9. Reverse the positions of the stops in the list
print(stops)
stops.reverse()
print(stops)
#10 Print out all the stops using a for loop
for stop in stops:
    print(stop)









