# Generates Simulated Data for Exploration within Clickhouse

import sys
from random import randrange

# Get Gene Panel Data
def get_gene_list():
	gene_list = []
	fd = open("genes.txt")
	for line in fd:
		parts = line.split()
		merged = (parts[0], parts[1])
		gene_list.append(merged)
	return gene_list

NUM_MUTATIONS_PER_SAMPLE = 20
NUM_CNAS_PER_SAMPLE = 60
num_samples = int(sys.argv[1])
gene_list = get_gene_list()
num_genes = len(gene_list)
study_id = "cbio_sim"

# Create random samples
for i in range (0, num_samples):
	sample_id = "S%s" % i
	patient_id = "P%s" % i

	# Create Random Mutations
	for i in range (0, NUM_MUTATIONS_PER_SAMPLE):
		gene_index = randrange(num_genes)
		gene = gene_list[gene_index]
		gene_symbol = gene[0]
		entrez_id = gene[1]
		print("%s\t%s\t%s\t%s\t%s\t\tMUTATION\t\t1\t0.0"
			  % (study_id, sample_id, patient_id, entrez_id, gene_symbol))

	# Create Random CNAs
	for i in range (0, NUM_CNAS_PER_SAMPLE):
		gene_index = randrange(num_genes)
		gene = gene_list[gene_index]
		gene_symbol = gene[0]
		entrez_id = gene[1]
		cna_alt = randrange(2)
		if cna_alt == 0:
			cna_alt = -2
		else:
			cna_alt = 2
		print("%s\t%s\t%s\t%s\t%s\t\tCNA\t\t%s\t0.0"
			  % (study_id, sample_id, patient_id, entrez_id, gene_symbol, cna_alt))