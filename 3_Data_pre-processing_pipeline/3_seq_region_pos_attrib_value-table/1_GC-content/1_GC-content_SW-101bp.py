from Bio import SeqIO
from Bio.SeqUtils import GC
import itertools
import csv
import sys

n=0
##########chr_1
fasta_file = "/home/amin/HEMA/2_Analysis/1_arabidopsis_thaliana/0_sources/1_fasta/Arabidopsis_thaliana.TAIR10.1_remove_N.fa"
with open('/home/amin/HEMA/1_MySQL/1_ensembl_core_database/1_arabidopsis_thaliana/2_attached_table/3_table_seq_region_position_attrib_value/1_dinucleotide/1_GC-content/4_sliding_window_101bp_10004/1_GC.csv', 'wb') as csvFile:

	writer = csv.writer(csvFile)
	for seq in SeqIO.parse(fasta_file,"fasta"):
		for i in range(50):
			atcg = seq.seq[i]
			value =0
			row = [atcg,value]
    			writer.writerow(row)

	for seq in SeqIO.parse(fasta_file,"fasta"):
		for i in range(len(seq)-100):
			value = int(round(GC(seq.seq[i:i+101])))
			atcg = seq.seq[i+50]
			row = [atcg,value]
    			writer.writerow(row)

	for seq in SeqIO.parse(fasta_file,"fasta"):
		for i in range(len(seq.seq)-50,len(seq.seq)-0):
			atcg = seq.seq[i]
			value =0
			row = [atcg,value]
    			writer.writerow(row)


fasta_file = "/home/amin/HEMA/2_Analysis/1_arabidopsis_thaliana/0_sources/1_fasta/Arabidopsis_thaliana.TAIR10.dna.chromosome.1.fa"
with open('/home/amin/HEMA/1_MySQL/1_ensembl_core_database/1_arabidopsis_thaliana/2_attached_table/3_table_seq_region_position_attrib_value/1_dinucleotide/1_GC-content/4_sliding_window_101bp_10004/1_GC.csv', 'r') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	lines = list(readCSV)
	c=0
	for seq in SeqIO.parse(fasta_file,"fasta"):
		for i in range(len(seq.seq)):
			if seq.seq[i] == 'N':
				c=c+1
				n=n+1
				print n,',',10004,',',0
			else:
				n=n+1				
				print n,',',10004,',',lines[i-c][1]

##########chr_2
fasta_file = "/home/amin/HEMA/2_Analysis/1_arabidopsis_thaliana/0_sources/1_fasta/Arabidopsis_thaliana.TAIR10.2_remove_N.fa"
with open('/home/amin/HEMA/1_MySQL/1_ensembl_core_database/1_arabidopsis_thaliana/2_attached_table/3_table_seq_region_position_attrib_value/1_dinucleotide/1_GC-content/4_sliding_window_101bp_10004/1_GC.csv', 'wb') as csvFile:

	writer = csv.writer(csvFile)
	for seq in SeqIO.parse(fasta_file,"fasta"):
		for i in range(50):
			atcg = seq.seq[i]
			value =0
			row = [atcg,value]
    			writer.writerow(row)

	for seq in SeqIO.parse(fasta_file,"fasta"):
		for i in range(len(seq)-100):
			value = int(round(GC(seq.seq[i:i+101])))
			atcg = seq.seq[i+50]
			row = [atcg,value]
    			writer.writerow(row)

	for seq in SeqIO.parse(fasta_file,"fasta"):
		for i in range(len(seq.seq)-50,len(seq.seq)-0):
			atcg = seq.seq[i]
			value =0
			row = [atcg,value]
    			writer.writerow(row)


fasta_file = "/home/amin/HEMA/2_Analysis/1_arabidopsis_thaliana/0_sources/1_fasta/Arabidopsis_thaliana.TAIR10.dna.chromosome.2.fa"
with open('/home/amin/HEMA/1_MySQL/1_ensembl_core_database/1_arabidopsis_thaliana/2_attached_table/3_table_seq_region_position_attrib_value/1_dinucleotide/1_GC-content/4_sliding_window_101bp_10004/1_GC.csv', 'r') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	lines = list(readCSV)
	c=0
	for seq in SeqIO.parse(fasta_file,"fasta"):
		for i in range(len(seq.seq)):
			if seq.seq[i] == 'N':
				c=c+1
				n=n+1
				print n,',',10004,',',0
			else:
				n=n+1				
				print n,',',10004,',',lines[i-c][1]


##########chr_3
fasta_file = "/home/amin/HEMA/2_Analysis/1_arabidopsis_thaliana/0_sources/1_fasta/Arabidopsis_thaliana.TAIR10.3_remove_N.fa"
with open('/home/amin/HEMA/1_MySQL/1_ensembl_core_database/1_arabidopsis_thaliana/2_attached_table/3_table_seq_region_position_attrib_value/1_dinucleotide/1_GC-content/4_sliding_window_101bp_10004/1_GC.csv', 'wb') as csvFile:

	writer = csv.writer(csvFile)
	for seq in SeqIO.parse(fasta_file,"fasta"):
		for i in range(50):
			atcg = seq.seq[i]
			value =0
			row = [atcg,value]
    			writer.writerow(row)

	for seq in SeqIO.parse(fasta_file,"fasta"):
		for i in range(len(seq)-100):
			value = int(round(GC(seq.seq[i:i+101])))
			atcg = seq.seq[i+50]
			row = [atcg,value]
    			writer.writerow(row)

	for seq in SeqIO.parse(fasta_file,"fasta"):
		for i in range(len(seq.seq)-50,len(seq.seq)-0):
			atcg = seq.seq[i]
			value =0
			row = [atcg,value]
    			writer.writerow(row)

fasta_file = "/home/amin/HEMA/2_Analysis/1_arabidopsis_thaliana/0_sources/1_fasta/Arabidopsis_thaliana.TAIR10.dna.chromosome.3.fa"
with open('/home/amin/HEMA/1_MySQL/1_ensembl_core_database/1_arabidopsis_thaliana/2_attached_table/3_table_seq_region_position_attrib_value/1_dinucleotide/1_GC-content/4_sliding_window_101bp_10004/1_GC.csv', 'r') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	lines = list(readCSV)
	c=0
	for seq in SeqIO.parse(fasta_file,"fasta"):
		for i in range(len(seq.seq)):
			if seq.seq[i] == 'N':
				c=c+1
				n=n+1
				print n,',',10004,',',0
			else:
				n=n+1				
				print n,',',10004,',',lines[i-c][1]

##########chr_4
fasta_file = "/home/amin/HEMA/2_Analysis/1_arabidopsis_thaliana/0_sources/1_fasta/Arabidopsis_thaliana.TAIR10.4_remove_N.fa"
with open('/home/amin/HEMA/1_MySQL/1_ensembl_core_database/1_arabidopsis_thaliana/2_attached_table/3_table_seq_region_position_attrib_value/1_dinucleotide/1_GC-content/4_sliding_window_101bp_10004/1_GC.csv', 'wb') as csvFile:

	writer = csv.writer(csvFile)
	for seq in SeqIO.parse(fasta_file,"fasta"):
		for i in range(50):
			atcg = seq.seq[i]
			value =0
			row = [atcg,value]
    			writer.writerow(row)

	for seq in SeqIO.parse(fasta_file,"fasta"):
		for i in range(len(seq)-100):
			value = int(round(GC(seq.seq[i:i+101])))
			atcg = seq.seq[i+50]
			row = [atcg,value]
    			writer.writerow(row)

	for seq in SeqIO.parse(fasta_file,"fasta"):
		for i in range(len(seq.seq)-50,len(seq.seq)-0):
			atcg = seq.seq[i]
			value =0
			row = [atcg,value]
    			writer.writerow(row)


fasta_file = "/home/amin/HEMA/2_Analysis/1_arabidopsis_thaliana/0_sources/1_fasta/Arabidopsis_thaliana.TAIR10.dna.chromosome.4.fa"
with open('/home/amin/HEMA/1_MySQL/1_ensembl_core_database/1_arabidopsis_thaliana/2_attached_table/3_table_seq_region_position_attrib_value/1_dinucleotide/1_GC-content/4_sliding_window_101bp_10004/1_GC.csv', 'r') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	lines = list(readCSV)
	c=0
	for seq in SeqIO.parse(fasta_file,"fasta"):
		for i in range(len(seq.seq)):
			if seq.seq[i] == 'N':
				c=c+1
				n=n+1
				print n,',',10004,',',0
			else:
				n=n+1				
				print n,',',10004,',',lines[i-c][1]

##########chr_5
fasta_file = "/home/amin/HEMA/2_Analysis/1_arabidopsis_thaliana/0_sources/1_fasta/Arabidopsis_thaliana.TAIR10.5_remove_N.fa"
with open('/home/amin/HEMA/1_MySQL/1_ensembl_core_database/1_arabidopsis_thaliana/2_attached_table/3_table_seq_region_position_attrib_value/1_dinucleotide/1_GC-content/4_sliding_window_101bp_10004/1_GC.csv', 'wb') as csvFile:

	writer = csv.writer(csvFile)
	for seq in SeqIO.parse(fasta_file,"fasta"):
		for i in range(50):
			atcg = seq.seq[i]
			value =0
			row = [atcg,value]
    			writer.writerow(row)

	for seq in SeqIO.parse(fasta_file,"fasta"):
		for i in range(len(seq)-100):
			value = int(round(GC(seq.seq[i:i+101])))
			atcg = seq.seq[i+50]
			row = [atcg,value]
    			writer.writerow(row)

	for seq in SeqIO.parse(fasta_file,"fasta"):
		for i in range(len(seq.seq)-50,len(seq.seq)-0):
			atcg = seq.seq[i]
			value =0
			row = [atcg,value]
    			writer.writerow(row)

fasta_file = "/home/amin/HEMA/2_Analysis/1_arabidopsis_thaliana/0_sources/1_fasta/Arabidopsis_thaliana.TAIR10.dna.chromosome.5.fa"
with open('/home/amin/HEMA/1_MySQL/1_ensembl_core_database/1_arabidopsis_thaliana/2_attached_table/3_table_seq_region_position_attrib_value/1_dinucleotide/1_GC-content/4_sliding_window_101bp_10004/1_GC.csv', 'r') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	lines = list(readCSV)
	c=0
	for seq in SeqIO.parse(fasta_file,"fasta"):
		for i in range(len(seq.seq)):
			if seq.seq[i] == 'N':
				c=c+1
				n=n+1
				print n,',',10004,',',0
			else:
				n=n+1				
				print n,',',10004,',',lines[i-c][1]


