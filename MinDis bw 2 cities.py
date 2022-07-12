#Code: Minimum distance between 2 cities (by using UCS application)

from queue import PriorityQueue #to use the class PriorityQueue from the queue library thus we can access put and get functions also

open_list = PriorityQueue()# Now the open list will be maintained as a priority queue
closed_list= [] #to store the visitied cities

city = { #dictionary data structure used to store all the city names and their corresponding cities and distances
    "Arad" : [("Zerind", 75), ("Sibiu", 140), ("Timisoara", 118)],
    "Bucharest" : [("Fagaras", 211), ("Pitesti", 101), ("Urziceni", 85), ("Giurgiu", 90)],
    "Craiova" : [("Drobeta", 120), ("Rimnicu Vilcea", 146), ("Pitesti", 138)],
    "Drobeta" : [("Mehadia", 75), ("Craiova", 120)],
    "Eforie" : [("Hirsova", 86)],
    "Fagaras" : [("Sibiu", 99), ("Bucharest", 211)],
    "Giurgiu" : [("Bucharest", 90)],
    "Hirsova" : [("Urziceni", 98), ("Eforie", 86)],
    "Iasi" : [("Neamt", 87), ("Vaslui", 92)],
    "Lugoj" : [("Timisoara", 111), ("Mehadia", 70)],
    "Mehadia" : [("Lugoj", 70), ("Drobeta", 75)],
    "Neamt" : [("Iasi", 87)],
    "Oradea" : [("Zerind", 71), ("Sibiu", 151)],
    "Pitesti" : [("Rimnicu Vilcea", 97), ("Bucharest", 101), ("Craiova", 138)],
    "Rimnicu Vilcea" : [("Sibiu", 80), ("Pitesti", 97), ("Craiova", 146)],
    "Sibiu" : [("Oradea", 151), ("Arad", 140), ("Fagaras", 99), ("Rimnicu Vilcea", 80)],
    "Timisoara" : [("Arad", 118), ("Lugoj", 111)],
    "Urziceni" : [("Bucharest", 85), ("Vaslui", 142), ("Hirsova", 98)],
    "Vaslui" : [("Iasi", 92), ("Urziceni", 142)],
    "Zerind" : [("Oradea", 71), ("Arad", 75)]
}

     #since here we are not changing the graph, we could use tuple (for storing values) here.
      #Else, list is the best data structure to be used here, if we want to change the values.       
start_city = input("Enter starting city = ") 
if start_city not in city.keys():
    print("Please enter a valid start city!! ")
    exit(0)   
dest_city = input("Enter destination city = ")
if dest_city not in city.keys():
    print("Please enter a valid dest_city!! ")
    exit(0)
open_list.put([0, start_city])
while open_list:
    curr_pop = open_list.get() #variable to store the topmost element of the open list
    dist = curr_pop[0]
    curr_city = curr_pop[1]
    if curr_city not in closed_list:
        closed_list.append(curr_city)
        if curr_city == dest_city:
            print("Minimum distance travelled is " + str(dist) + " km.") 
            break
        for j in city[curr_city]:
            if j not in closed_list:
                total_min_dist = dist + j[1]
                open_list.put([total_min_dist, j[0]]) 

# We could print all the intermediate visited cities by printing the closed list.
