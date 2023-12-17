#!/usr/bin/env python

# load a .tsv file with two columns (domain and selector), group by selector
# and print the selectors and corresponding domains sorted by the number of domains

import sys
import collections


def main():
	domainSelectorDict = collections.defaultdict(list)
	if len(sys.argv) != 2:
		print('usage: selector_statistics.py file.tsv')
		sys.exit(1)
	tsvFile = sys.argv[1]
	# read .tsv file
	with open(tsvFile, 'r') as f:
		for line in f:
			line = line.rstrip('\n')
			domain, selector = line.split('\t')
			domainSelectorDict[selector].append(domain)

	# sort by number of domains
	domainSelectorDict = dict(
	    sorted(domainSelectorDict.items(),
	           key=lambda x: len(x[1]),
	           reverse=True))
	for selector, domains in domainSelectorDict.items():
		print(selector)
		for domain in domains:
			print(f'\t{domain}')


if __name__ == '__main__':
	main()