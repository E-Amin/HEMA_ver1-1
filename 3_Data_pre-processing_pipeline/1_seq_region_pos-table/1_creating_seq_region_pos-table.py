from Bio import SeqIO
import mysql.connector
from mysql.connector import (connection)
import csv
################ switch ####################  
def switch(chromosome):
	switcher = { 
		1: "/home/amin/ensembl_database/1_arabidopsis_thaliana/sources/Arabidopsis_thaliana.TAIR10.dna.chromosome.1.fa",
		393: "/home/amin/ensembl_database/1_arabidopsis_thaliana/sources/Arabidopsis_thaliana.TAIR10.dna.chromosome.2.fa",
		653: "/home/amin/ensembl_database/1_arabidopsis_thaliana/sources/Arabidopsis_thaliana.TAIR10.dna.chromosome.3.fa",
		988: "/home/amin/ensembl_database/1_arabidopsis_thaliana/sources/Arabidopsis_thaliana.TAIR10.dna.chromosome.4.fa",
		1198: "/home/amin/ensembl_database/1_arabidopsis_thaliana/sources/Arabidopsis_thaliana.TAIR10.dna.chromosome.5.fa"
		}
	return switcher.get(chromosome)

################ run function ####################  
def run(list_seq_region_id):
	for i in range(len(list_seq_region_id)):
		seq_region_id = list_seq_region_id[i]
		chr_fa = str(switch(seq_region_id)) 
		seq_file = SeqIO.read(open(str(chr_fa)),"fasta")
		chromosome_level(seq_file,seq_region_id)


################ chromosome_level function ####################  
def chromosome_level(seq_file,seq_region_id):
	m=4	
	n = len(seq_file.seq)
	table = [[0 for i in xrange(m)] for i in xrange(n)]
	for j in xrange(n):
		global seq_region_pos_id
		table [j][0]= seq_region_pos_id + j
		table [j][1]= seq_region_id
		table [j][2]= j + 1
		table [j][3]= seq_file.seq[j]
	seq_region_pos_id = seq_region_pos_id + n
	seq_region_pos = open("/home/amin/1_HEMA/githup/2_tables/AT_seq_region_pos_table.csv", 'a')
	mywriter = csv.writer(seq_region_pos)
	for i in xrange(len(table)):
		row = table[i][0],table[i][1],table[i][2],table[i][3]
		mywriter.writerow(row)
	seq_region_pos.close()

################ Start ####################  

list_seq_region_id =[1,393,653,988,1198]
seq_region_pos_id = 1
run(list_seq_region_id)

