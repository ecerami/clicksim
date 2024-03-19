# Generates Simulated Data for Exploration within Clickhouse

import sys
from random import randrange
from clinical_data_element import ClinicalDataElement

# Get Gene Panel Data
def get_gene_list():
    gene_list = []
    fd = open("genes.txt")
    for line in fd:
        parts = line.split()
        merged = (parts[0], parts[1])
        gene_list.append(merged)
    return gene_list

def get_clinical_data_elements():
    clinical_list = []
    fd = open("clinical.txt")
    for line in fd:
        if not line.startswith("clinical_attribute_id"):
            parts = line.split()
            data_element = ClinicalDataElement(parts[0], parts[1], parts[2], parts[3],
                                               parts[4], parts[5])
            clinical_list.append(data_element)
    return clinical_list

NUM_MUTATIONS_PER_SAMPLE = 20
NUM_CNAS_PER_SAMPLE = 60
num_samples = int(sys.argv[1])
gene_list = get_gene_list()
num_genes = len(gene_list)
clinical_list = get_clinical_data_elements()
study_id = "cbio_sim"

# Create random samples
for i in range(0, num_samples):
    sample_id = "S%s" % i
    patient_id = "P%s" % i

    # Create Random Mutations
    for i in range(0, NUM_MUTATIONS_PER_SAMPLE):
        gene_index = randrange(num_genes)
        gene = gene_list[gene_index]
        gene_symbol = gene[0]
        entrez_id = gene[1]
        print("%s\t%s\t%s\t%s\t%s\t\tMUTATION\t\t1\t0.0"
              % (study_id, sample_id, patient_id, entrez_id, gene_symbol))

    # Create Random CNAs
    for i in range(0, NUM_CNAS_PER_SAMPLE):
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

    # Create Random Clinical Attributes
    for clinical_element in clinical_list:
        value = clinical_element.get_random()
        if clinical_element.attribute_type == "continuous":
            print("%s\t%s\t%s\t\t\t%s\tCLINICAL_%s_CONTINOUS\t\t%s\t0.0"
                  % (study_id, sample_id, patient_id, clinical_element.clinical_attribute_id,
                     clinical_element.belongs_to, value))
        else:
            print("%s\t%s\t%s\t\t\t%s\tCLINICAL_%s_DISCRETE\t%s\t\t0.0"
                  % (study_id, sample_id, patient_id, clinical_element.clinical_attribute_id,
                     clinical_element.belongs_to, value))
