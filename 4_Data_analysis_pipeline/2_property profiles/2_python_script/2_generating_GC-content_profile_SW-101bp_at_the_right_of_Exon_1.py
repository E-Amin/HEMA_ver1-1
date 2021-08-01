from Bio import SeqIO
#from turbodbc import connect
import mysql.connector
from mysql.connector import (connection)
import csv
import statistics
import numpy as np
from scipy.stats import kurtosis, skew
#from collections import Counter
#####################################
db =connection.MySQLConnection(user='your_user', password='your_password',
                              host='your_host',
                              database='your_database', charset='utf8')# charset='utf8' sovled the error of ERROR 1115 (42000) : Unknown character set: 'utf8mb4' in mysql
###############Number of Feature##############
m=1001
cur = db.cursor()
cur.execute("select tf.transcript_id,tf.seq_region_strand,tf.seq_region_pos_start, tf.seq_region_pos_end, t.seq_region_id from HEMA_arabidopsis_thaliana_core_40_93_11.transcript_feature tf, HEMA_arabidopsis_thaliana_core_40_93_11.transcript t where tf.transcript_id=t.transcript_id and  tf.feature_id ='EX' and tf.rank=1 and t.biotype ='protein_coding' and t.seq_region_id !=1617 and t.seq_region_id!=1619 order by t.seq_region_id,tf.seq_region_pos_start")
features = cur.fetchall()

table = [[0 for i in xrange(m)] for i in xrange(len(features))]
################Feature_prop_value_Level#####################
for i in range(len(features)):
	strand = int(features[i][1])
	seq_region_id= features[i][4]
	if strand == 1:

		start = features[i][3]-500
		end= features[i][3]+500
	else:
		start = features[i][2] -500
		end = features[i][2] +500

	cur = db.cursor()
	cur.execute("SELECT srpav.value FROM HEMA_arabidopsis_thaliana_core_40_93_11.seq_region_pos_attrib_value srpav where srpav.attrib_analysis_id=10005 and srpav.seq_region_pos_id between %s and %s" % (start, end))
	transcript_prop_value = cur.fetchall()
	#print len(transcript_prop_value)
	l=len(transcript_prop_value)
	#print l

	for j in range(len(transcript_prop_value)):
		#print l,j
		#print i,j,len(transcript_prop_value)
		if transcript_prop_value[j][0] != 'Null':
			#print transcript_prop_value[j][0]
			if strand == 1:
				table[i][j]=float(transcript_prop_value[j][0])
			else:
				table[i][l-(j+1)]=float(transcript_prop_value[j][0])
		#print table[i][j]


################
cols = zip(*table)
for i in range(len(cols)):
	Mean=statistics.mean(cols[i])
	#Median=round(statistics.median(cols[i]),2)
	#Mode=max(set(cols[i]), key=cols[i].count)
	SD=statistics.pstdev(cols[i])
	#Skew= round(skew(cols[i]),2)
	#Kurtosis= round(kurtosis(cols[i]),2)
	print i+1,',',Mean,',',SD#Mean##,',',Median,',',Mode,',',SD,',',Skew,',',Kurtosis