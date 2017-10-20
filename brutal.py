#
# +--------------------------------------------------+
# | All Code by Chen Wang - wangc29 				 |
# | TSP_brute-force | CSE564 | Fall 2017 | Dr. Bravo |
# +--------------------------------------------------+
#

#! /usr/bin/env python
from sys import argv
import parser as ps
#+--------------------------------------------+
# we input cities_tups and dimension of a TSP that are 
# obtained by TSBLIB parser 
def find_min(cities_tups,dimension):
	min_length = float("inf")
	min_route = []	
	route_perm = candidate_route(dimension)
	for i in route_perm:
		list_i = [1]+list(i)+[1]
		node_pair_list = create_moving_window(list_i)
		present_length = cal_route_length(cities_tups,node_pair_list)
		if present_length < min_length:
			min_length = present_length
			min_route = list_i
	return min_route
#+---------------------------------------------+	
# we generate all possible hamiltonia circuits started with vertice 1
def candidate_route(dimension):
	from itertools import permutations
	num_list = [i for i in range(2,dimension+1)]
	candidate_route = permutations(num_list)
	return candidate_route
#+---------------------------------------------+
# generate all edges of a specific hamiltonia circuit
def create_moving_window(route_list):
	mega_list = []
	for i in range(len(route_list)-1):
		node_tup = (route_list[i],route_list[i+1])
		mega_list.append(node_tup)
	return mega_list
#+----------------------------------------------+
# calculate weight of an edge
def cal_distance(cities_tups,node_pair):
	start,end = node_pair
	start_co = [float(i) for i in cities_tups[start-1]]
	end_co = [float(i) for i in cities_tups[end-1]]
	distance = (start_co[0]-end_co[0])**2 +(start_co[1]-start_co[1])**2
	return distance
#+----------------------------------------------+
# calculate weight of aa specific hamotania circuit
def cal_route_length(cities_tups,mega_list):
	route_length = 0
	for pair in mega_list:
		route_length += cal_distance(cities_tups,pair)
	return route_length
#+-----------------------------------------------+
# loop over all circuits and return the circuit of
# minimum weight
def main():
	from sys import argv
	import parser as ps
	file = argv[1]
	data = ps.read_tsp_data(argv[1])
	dimension =int(ps.detect_dimension(data))
	cities_set = ps.get_cities(data,dimension)
	cities_tups = ps.city_tup(cities_set)
	print find_min(cities_tups,dimension)
#+------------------------------------------------+
if __name__ == '__main__':
	main()







