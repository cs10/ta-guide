"""
This script will automatically assign AIs based on the max flow algorithm, and is
largely taken from the original script written by Lara McConnaughey. 

Before calling the script, there are a few variables for you to edit: 

NUM_LABS: A dictionary with the number of units as the key and the number of labs
an AI should be assigned as the value

LESS_WEIGHT, MORE_WEIGHT: lists of lab sections that should have more or fewer AIs. 
Be sure to include the lab name exactly as it appears on your sheet. 

LESS_WEIGHT_CAPACITY, MORE_WEIGHT_CAPACITY, NORMAL_CAPACITY: The maximum number of 
AIs assigned to labs of each kind of capacity. 

To call this file, call python3 AIAssigner.py <AI.tsv>, where AI.tsv is a TSV
with the following headers (in this order):

Name | Units | Sections

The sections should be separated by commas, and the headers should be in the TSV.

Note that this algorithm does not have a deterministic output. If you are not satisfied
with the assignments you get after running it once, you can run it again and you will 
get different assignments.

"""


import networkx as nx
import numpy as np
import sys

from networkx.algorithms import bipartite

lab_counts = {}
lab_availabilities = {}
labs = []

#TODO: Fill these variables in before running

# Number of labs assigned for each unit count
NUM_LABS = {0: 1, 1: 1, 2: 2}

# Labs that should get more or fewer Academic Interns
LESS_WEIGHT = []
MORE_WEIGHT = []
LESS_WEIGHT_CAPACITY = 2
MORE_WEIGHT_CAPACITY = 6
NORMAL_CAPACITY = 4

def parse_tsv(tsv):
	global lab_counts, lab_availabilities, labs 

	f = open(tsv, 'r')
	f.readline()
	for line in f:
		line_list = line.split('\t')
		lab_counts[line_list[0]] = NUM_LABS[int(line_list[1])]
		lab_availabilities[line_list[0]] = [l.strip().replace('"', '') for l in line_list[2].split(',')]
		labs += lab_availabilities[line_list[0]]

def create_graph():
	g = nx.DiGraph()
	g.add_nodes_from(set(labs), bipartite=0)
	g.add_nodes_from(lab_counts.keys(), bipartite=1)

	for ai in lab_counts.keys():
		for lab in lab_availabilities[ai]:
			g.add_edges_from([(ai, lab)], capacity=1)

		g.add_edges_from([('source', ai)], capacity=lab_counts[ai])

	for lab in set(labs):
		if lab in LESS_WEIGHT:
			g.add_edges_from([(lab, 'sink')], capacity=LESS_WEIGHT_CAPACITY)
		elif lab in MORE_WEIGHT:
			g.add_edges_from([(lab, 'sink')], capacity=MORE_WEIGHT_CAPACITY)
		else:
			g.add_edges_from([(lab, 'sink')], capacity=NORMAL_CAPACITY)

	return g

def create_assignments(g):
	flow_value, flow_dict = nx.maximum_flow(g, 'source', 'sink')

	assignments = {}
	num_assignments = {}

	for lab in labs:
		assignments[lab] = []

	for ai, l in flow_dict.items():
		if ai in lab_counts:
			assigned = 0
			for lab, val in l.items():
				if val == 1:
					assignments[lab].append(ai)
					assigned += 1
				num_assignments[ai] = assigned

	print("The following AIs have not been matched to the correct number of labs:")
	for ai in num_assignments:
		if num_assignments[ai] != lab_counts[ai]:
			print("AI: {}, Expected: {}, Assigned: {}".format(ai, lab_counts[ai], num_assignments[ai]))

	print()
	print("Below are the assignments. Feel free to rerun this algorithm if they are not satisfactory.")
	for lab in assignments:
		print('----{}----'.format(lab))
		for ai in assignments[lab]: 
			print(ai)

tsv = sys.argv[1]
parse_tsv(tsv)
create_assignments(create_graph())
