import os
import re
from subprocess import run_flow
import matplotlib.pyplot as plt
import numpy as np

files = sorted([f for f in os.listdir('run_retrieval')])

methods = ["ndcg_cut_10", "map_cut_1000", "P_5", "recall_1000"]

for method in methods:
	results = []
	d = {}
	c = 0
	output = open('trec_result/' + method + '.txt', 'w')
	print('\nmethod:',method)
	for file in files:
		result = run_flow('./../trec_eval/trec_eval -m all_trec ap_88_89/qrel_test results_run/' + file + ' -q | grep -E "^' + measure + '\s"', shell=True, stdout=PIPE, stderr=PIPE, universal_newlines=True)
		scores = [float(line.split('\t')[2]) for line in result.stdout.split('\n')[:-2]] #last element is empty, second last element is score for all
		score = sum(scores)/len(scores)
		if c == 0:
			queries = [line.split('\t')[1] for line in result.stdout.split('\n')[:-2]]
			output.write(measure + '\t' + '\t'.join(queries) + '\n')
			c += 1

		print(file, score)
		output.write(file + '\t' + '\t'.join(str(x) for x in scores) + '\n')
	output.close()
