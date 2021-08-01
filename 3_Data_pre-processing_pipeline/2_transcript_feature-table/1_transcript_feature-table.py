from Bio import SeqIO
import mysql.connector
from mysql.connector import (connection)
import csv
import sys
#########################
db =connection.MySQLConnection(user='ensembl', password='ensuser',
                              host='scps-web1.scu.edu.au',
                              database='HEMA_arabidopsis_thaliana_core_40_93_11', charset='utf8')

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


################ transcript_feature function ####################  
def transcript_feature():
	table=[]
	feature = 'NA'
	index=0
	transcript=0


	transciption_feature = open('/home/amin/1_HEMA/githup/2_tables/2_transcript_feature/AT_transcript_feature_table.csv', 'wb')
	mywriter = csv.writer(transciption_feature)


	with open('/home/amin/1_HEMA/githup/2_tables/2_transcript_feature/temp.csv', 'rb') as f:
		reader = csv.reader(f, delimiter=',')
		for row in reader:
			if row [4]==feature and int(row[6])==transcript:
				if index!=0 and int(row[2])==1:
					index=index+1	
					record = index,table[0][6],feature,table[0][0],table[-1][0],table[0][5],table[-1][7]
					mywriter.writerow(record)
					feature = row[4]
					transcript = int(row[6])
					table=[]
					table.append(row)
				else:	
					table.append(row)
			else:	
				index=index+1
				record = index,table[0][6],feature,table[0][0],table[-1][0],table[0][5],table[-1][7]
				mywriter.writerow(record)	
				feature = row[4]
				transcript = int(row[6])
				table=[]
				table.append(row)
		

########### chromosome level
seq_pos_id=0
def chromosome_level(seq_file,seq_region_id):
		m=8	
		n = len(seq_file.seq)
		table = [[0 for i in xrange(m)] for i in xrange(n)]
		for x in xrange(n):
			global seq_pos_id
			seq_pos_id=seq_pos_id+1
			table [x][0]= seq_pos_id
			table [x][1]= seq_region_id
			table [x][2]= x+1
			table [x][3]= seq_file.seq[x]
			table [x][4]= 'NA'

		########### gene_process
		cur = db.cursor()	
		q=("SELECT gene.seq_region_id,gene.seq_region_start,gene.seq_region_end,gene.seq_region_strand,gene.biotype,biotype.biotype_id,coord_system.name,seq_region.name FROM seq_region 				INNER JOIN coord_system ON seq_region.coord_system_id = coord_system.coord_system_id INNER JOIN gene ON gene.seq_region_id = seq_region.seq_region_id INNER JOIN biotype ON 				gene.biotype = biotype.name  WHERE coord_system.attrib = 'default_version' and coord_system.name = 'chromosome' and biotype.object_type='gene' and gene.seq_region_id = %(value)s  				and biotype_id ORDER BY gene.seq_region_start")
		params = {'value':seq_region_id}
		cur.execute(q, params)
		genes = cur.fetchall()
	
		for x in range(len(genes)):
			gene_start = genes[x][1]
			gene_end = genes[x][2]
			biotype_id = genes[x][5]
			strand= genes[x][3]
			for i in range(gene_start-1, gene_end):
				code=table [i][4]
				if code != 'GS':
					table [i][4]='GS'
					table [i][5]=strand

		print '##########gene level##############'
		########### transcript_process 
		cur = db.cursor()
		q=("SELECT coord_system.name,seq_region.name,transcript.seq_region_start,transcript.seq_region_end,transcript.transcript_id FROM seq_region INNER JOIN coord_system ON 				seq_region.coord_system_id = coord_system.coord_system_id INNER JOIN transcript ON transcript.seq_region_id = seq_region.seq_region_id where transcript.seq_region_id = %(value)s and 			transcript.stable_id like '%.1' GROUP BY transcript.seq_region_start,transcript.seq_region_end,coord_system.name,seq_region.name  ORDER BY transcript.seq_region_start")
		params = {'value':seq_region_id}
		cur.execute(q, params)
		transcripts = cur.fetchall()
		query_len = len(transcripts)
		for x in xrange(query_len):
			start = transcripts[x][2]-1
			end = transcripts[x][3]
			transcript_id = transcripts[x][4]
			for i in range(start, end):
				code=table [i][4]
				if code!= 'TU':
					table [i][4]='TU'
					table [i][6]= transcript_id
		print '##########transcript level##############'
		########### exon_and_intron_process
		cur = db.cursor()
		q=("select stable_id,transcript_id,seq_region_strand from transcript where stable_id like '%.1' and seq_region_id = %(value)s order by seq_region_start")
		params = {'value':seq_region_id}
		cur.execute(q, params)
		transcript_list = cur.fetchall()
		for i in range(len(transcript_list)):
			stable_id = transcript_list[i][0]
			strand = transcript_list[i][2]
			exon_list=[]
			#print '#######', i , '#######', stable_id		
			cur = db.cursor()
			q="select t.transcript_id, e.exon_id, e.seq_region_start, e.seq_region_end, e.seq_region_strand, e.stable_id, et.rank from gene g, transcript t, exon_transcript et, exon e, 				seq_region sr where g.gene_id = t.gene_id and t.transcript_id = et.transcript_id and et.exon_id = e.exon_id and e.seq_region_id = sr.seq_region_id and t.stable_id =%(value)s  order 				by et.rank"
			params = {'value':stable_id}
			cur.execute(q, params)
			exon_list = cur.fetchall()
			if exon_list:
			########### exon_and_intron_process
				exon_numb = 0
				if len(exon_list) > 1:
					for first, second,i in zip(exon_list,exon_list[1:],range(len(exon_list))):
						exon_numb = exon_numb +1
						ex_start = first[2]	
						ex_end = first[3]
						for i in range(ex_start-1, ex_end):
							code = table [i][4]
							if code[:1] == 'T' and code[-2:]!= 'EX':
								table [i][4]='EX'
								table [i][7]= exon_numb
						if strand ==1:
							in_start=first[3]
							in_end=second[2]
						else:
							in_start=second[3]
							in_end=first[2] 
						for i in range(in_start, in_end-1):
							code = table [i][4]
							if code[:1] == 'T' and code[-2:]!= 'IN':
								table [i][4]='IN'
								table [i][7]= exon_numb
			
					ex_start = second[2]	
					ex_end = second[3]
					for i in range(ex_start-1, ex_end):
						code = table [i][4]
						if code[:1] == 'T' and code[-2:]!= 'EX':
							table [i][4]='EX'
							table [i][7]= exon_numb+1
				else: 
					ex_start = exon_list[0][2]
					ex_end = exon_list[0][3]
					for i in range(ex_start-1, ex_end):
						code = table [i][4]
						if code[:1] == 'T' and code[-2:]!= 'EX':
							table [i][4]='EX'
							table [i][7]= exon_numb+1
					#print '########## exon_and_intron level##############'

				########### Translation
				cur = db.cursor()
				q="select ts.translation_id,ts.transcript_id, ts.seq_start, ts.start_exon_id, ts.seq_end, ts.end_exon_id  from translation ts,  transcript t where ts.stable_id =%(value)s 					and ts.transcript_id=t.transcript_id" 
				params = {'value':stable_id}
				cur.execute(q, params)
				exon_start_end = cur.fetchall()
				if exon_start_end: ##if not it means that this transcript has only one exon without translation record
					start_exon_id= exon_start_end[0][3]
					end_exon_id= exon_start_end[0][5]
					seq_start= exon_start_end[0][2]-1
					seq_end= exon_start_end[0][4]-1
					first_exon_start = exon_list[0][2]
					first_exon_end = exon_list[0][3]
					last_exon_start = exon_list[-1][2]
					last_exon_end = exon_list[-1][3]

					#####################5utr	
					for i in range(len(exon_list)):
						if start_exon_id == exon_list[i][1]:
							exon_start =  exon_list[i][2]
							exon_end = exon_list[i][3]
					if strand ==1:
						utr5_start= first_exon_start
						utr5_end= exon_start + seq_start-1
		
					else:
						utr5_start= exon_end - seq_start+1
						utr5_end= first_exon_end



					for i in range(utr5_start-1, utr5_end):
						code = table [i][4] 
						if code[:1] == 'E'and code[-2:]!= 'E5':
							table [i][4]='E5'
						if code[:1] == 'I' and code[-2:]!= 'I5':
							table [i][4]='I5'
						#print '########## 5utr level##############'
						#####################3utr	
					for i in range(len(exon_list)):
						if end_exon_id == exon_list[i][1]:
							exon_start =  exon_list[i][2]
							exon_end = exon_list[i][3]
					if strand ==1:
						utr3_start= exon_start + seq_end+1 
						utr3_end= last_exon_end

					else:
						utr3_start= last_exon_start
						utr3_end= exon_end - seq_end-1


					for i in range(utr3_start-1, utr3_end):
						code = table [i][4]
						if code[:1] == 'E' and code[-2:]!= 'E3':
							table [i][4]='E3'
						if code[:1] == 'I' and code[-2:]!= 'I3':
							table [i][4]='I3'

						#print '########## 3utr level##############'
		########### seq_region_position
		seq_region_position = open('/home/amin/1_HEMA/githup/2_tables/2_transcript_feature/temp.csv', 'a')		
		mywriter = csv.writer(seq_region_position)
		for x in xrange(len(table)):
			row = table[x][0],table[x][1],table[x][2],table[x][3],table[x][4],table[x][5],table[x][6],table[x][7]
			mywriter.writerow(row)
		seq_region_position.close()
		print '########## seq_region_position##############'
################ Start ####################  

list_seq_region_id =[1,393,653,988,1198]
seq_region_pos_id = 1
run(list_seq_region_id)
transcript_feature()
db.close()
