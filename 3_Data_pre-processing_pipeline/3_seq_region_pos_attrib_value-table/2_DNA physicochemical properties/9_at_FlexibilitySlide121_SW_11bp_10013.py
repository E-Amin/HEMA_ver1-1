from __future__ import division
from Bio import SeqIO
from Bio.SeqUtils import GC
from Bio import SeqIO
from itertools import product
from numpy import empty
from numpy import *
import itertools
import csv
import sys
import re
import numpy
import numpy as np
#numpy.set_printoptions(threshold='nan')


n=0
############

#FlexibilitySlide121_10013-10014
dinValue = np.array([('AA',13.72), ('AC',9.57), ('AG',7.58), ('AT',11.69),
		    ('CA',1.35), ('CC',7.36),('CG',4.02), ('CT',7.58), 
		    ('GA',10.28), ('GC',4.34), ('GG',7.36),('GT',9.57), 
		    ('TA',7.13), ('TC',10.28),('TG',1.35), ('TT',13.72)], dtype=object)

window=11
############
def sliding_window(window):
	for i in range(len(seq)-(window)):
		index=int(((window-1)/2)+i)
		#print array[0,i:i+window]
		array[1][index]=round(mean(array[0,i:i+window]),2)		

############
def generate_din(seq):
	for i in range(len(seq)-1):
		din= (seq[i])+(seq[i+1])

		for j in range(len(dinValue)):
			if din==dinValue[j][0]:
				array[0][i]=dinValue[j][1]
				break



##########chr_1
fasta_file = "/home/amin/ensembl_database/1_arabidopsis_thaliana/sources/Arabidopsis_thaliana.TAIR10.1_remove_N.fa"
for seq in SeqIO.parse(fasta_file,"fasta"):
	array=numpy.empty(shape=(2,len(seq)), dtype=object)
	for i in range(len(seq)):
		array[1][i]=0
		array[0][i]=0
	generate_din(seq.seq)
	sliding_window(window)


fasta_file = "/home/amin/ensembl_database/1_arabidopsis_thaliana/sources/Arabidopsis_thaliana.TAIR10.dna.chromosome.1.fa"
with open ('/home/amin/1_HEMA/1_MySQL/1_ensembl_core_database/1_arabidopsis_thaliana/2_attached_table/3_table_seq_region_position_attrib_value/3_physicochemical properties/9_at_FlexibilitySlide121_SW_11bp_10013.csv', 'a') as csvfile:
	writer = csv.writer(csvfile, delimiter=',')
	c=0
	for seq in SeqIO.parse(fasta_file,"fasta"):

		for i in range(len(seq.seq)):
			if seq.seq[i] != 'N':
				n=n+1
				writer.writerow([n,10013,array[1][c]])
				c=c+1
			else:
				n=n+1
				writer.writerow([n,10013,'Null'])

##########chr_2
fasta_file = "/home/amin/ensembl_database/1_arabidopsis_thaliana/sources/Arabidopsis_thaliana.TAIR10.2_remove_N.fa"
for seq in SeqIO.parse(fasta_file,"fasta"):
	array=numpy.empty(shape=(2,len(seq)), dtype=object)
	for i in range(len(seq)):
		array[1][i]=0
		array[0][i]=0
	generate_din(seq.seq)
	sliding_window(window)


fasta_file = "/home/amin/ensembl_database/1_arabidopsis_thaliana/sources/Arabidopsis_thaliana.TAIR10.dna.chromosome.2.fa"
with open ('/home/amin/1_HEMA/1_MySQL/1_ensembl_core_database/1_arabidopsis_thaliana/2_attached_table/3_table_seq_region_position_attrib_value/3_physicochemical properties/9_at_FlexibilitySlide121_SW_11bp_10013.csv', 'a') as csvfile:
	writer = csv.writer(csvfile, delimiter=',')
	c=0
	for seq in SeqIO.parse(fasta_file,"fasta"):

		for i in range(len(seq.seq)):
			if seq.seq[i] != 'N':
				n=n+1
				writer.writerow([n,10013,array[1][c]])
				c=c+1
			else:
				n=n+1
				writer.writerow([n,10013,'Null'])


##########chr_3

fasta_file = "/home/amin/ensembl_database/1_arabidopsis_thaliana/sources/Arabidopsis_thaliana.TAIR10.3_remove_N.fa"
for seq in SeqIO.parse(fasta_file,"fasta"):
	array=numpy.empty(shape=(2,len(seq)), dtype=object)
	for i in range(len(seq)):
		array[1][i]=0
		array[0][i]=0
	generate_din(seq.seq)
	sliding_window(window)


fasta_file = "/home/amin/ensembl_database/1_arabidopsis_thaliana/sources/Arabidopsis_thaliana.TAIR10.dna.chromosome.3.fa"
with open ('/home/amin/1_HEMA/1_MySQL/1_ensembl_core_database/1_arabidopsis_thaliana/2_attached_table/3_table_seq_region_position_attrib_value/3_physicochemical properties/9_at_FlexibilitySlide121_SW_11bp_10013.csv', 'a') as csvfile:
	writer = csv.writer(csvfile, delimiter=',')
	c=0
	for seq in SeqIO.parse(fasta_file,"fasta"):

		for i in range(len(seq.seq)):
			if seq.seq[i] != 'N':
				n=n+1
				writer.writerow([n,10013,array[1][c]])
				c=c+1
			else:
				n=n+1
				writer.writerow([n,10013,'Null'])



##########chr_4
fasta_file = "/home/amin/ensembl_database/1_arabidopsis_thaliana/sources/Arabidopsis_thaliana.TAIR10.4_remove_N.fa"
for seq in SeqIO.parse(fasta_file,"fasta"):
	array=numpy.empty(shape=(2,len(seq)), dtype=object)
	for i in range(len(seq)):
		array[1][i]=0
		array[0][i]=0
	generate_din(seq.seq)
	sliding_window(window)


fasta_file = "/home/amin/ensembl_database/1_arabidopsis_thaliana/sources/Arabidopsis_thaliana.TAIR10.dna.chromosome.4.fa"
with open ('/home/amin/1_HEMA/1_MySQL/1_ensembl_core_database/1_arabidopsis_thaliana/2_attached_table/3_table_seq_region_position_attrib_value/3_physicochemical properties/9_at_FlexibilitySlide121_SW_11bp_10013.csv', 'a') as csvfile:
	writer = csv.writer(csvfile, delimiter=',')
	c=0
	for seq in SeqIO.parse(fasta_file,"fasta"):

		for i in range(len(seq.seq)):
			if seq.seq[i] != 'N':
				n=n+1
				writer.writerow([n,10013,array[1][c]])
				c=c+1
			else:
				n=n+1
				writer.writerow([n,10013,'Null'])

##########chr_5
fasta_file = "/home/amin/ensembl_database/1_arabidopsis_thaliana/sources/Arabidopsis_thaliana.TAIR10.5_remove_N.fa"
for seq in SeqIO.parse(fasta_file,"fasta"):
	array=numpy.empty(shape=(2,len(seq)), dtype=object)
	for i in range(len(seq)):
		array[1][i]=0
		array[0][i]=0
	generate_din(seq.seq)
	sliding_window(window)


fasta_file = "/home/amin/ensembl_database/1_arabidopsis_thaliana/sources/Arabidopsis_thaliana.TAIR10.dna.chromosome.5.fa"
with open ('/home/amin/1_HEMA/1_MySQL/1_ensembl_core_database/1_arabidopsis_thaliana/2_attached_table/3_table_seq_region_position_attrib_value/3_physicochemical properties/9_at_FlexibilitySlide121_SW_11bp_10013.csv', 'a') as csvfile:
	writer = csv.writer(csvfile, delimiter=',')
	c=0
	for seq in SeqIO.parse(fasta_file,"fasta"):

		for i in range(len(seq.seq)):
			if seq.seq[i] != 'N':
				n=n+1
				writer.writerow([n,10013,array[1][c]])
				c=c+1
			else:
				n=n+1
				writer.writerow([n,10013,'Null'])

csvfile.close()




