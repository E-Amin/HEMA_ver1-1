-- MySQL dump 10.13  Distrib 5.7.33, for Linux (x86_64)
--
-- Host: scps-web1.scu.edu.au    Database: HEMA_arabidopsis_thaliana_core_40_93_11
-- ------------------------------------------------------
-- Server version	5.1.73


--
-- Table structure for table `attrib_analysis`
--

DROP TABLE IF EXISTS `attrib_analysis`;
CREATE TABLE `attrib_analysis` (
  `attrib_analysis_id` smallint(5) unsigned NOT NULL,
  `attrib_type_id` int(11) unsigned NOT NULL,
  `analysis_id` smallint(5) unsigned DEFAULT NULL,
  `window` smallint(5) unsigned DEFAULT NULL,
  `run_date` date DEFAULT NULL,
  `algorithm` text,
  `parameters` text,
  `by_whom` varchar(255) DEFAULT NULL,
  `comments` text,
  PRIMARY KEY (`attrib_analysis_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AVG_ROW_LENGTH=98 CHECKSUM=1;

--
-- Table structure for table `attrib_class`
--

DROP TABLE IF EXISTS `attrib_class`;
CREATE TABLE `attrib_class` (
  `attrib_class_id` smallint(5) unsigned NOT NULL,
  `attrib_class_name` varchar(255) NOT NULL,
  `description` text,
  PRIMARY KEY (`attrib_class_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 CHECKSUM=1;

--
-- Table structure for table `attrib_frequencies`
--

DROP TABLE IF EXISTS `attrib_frequencies`;
CREATE TABLE `attrib_frequencies` (
  `attrib_frequency_id` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
  `attrib_analysis_id` smallint(5) unsigned NOT NULL,
  `scope` varchar(255) NOT NULL,
  `bin_size` smallint(5) unsigned DEFAULT NULL,
  `x_axis_start` int(10) NOT NULL,
  `x_axis_end` int(10) NOT NULL,
  `values` text,
  PRIMARY KEY (`attrib_frequency_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Table structure for table `attrib_kmer`
--

DROP TABLE IF EXISTS `attrib_kmer`;
CREATE TABLE `attrib_kmer` (
  `attrib_kmer_id` int(11) unsigned NOT NULL,
  `attrib_type_id` int(11) unsigned NOT NULL,
  `kmer_id` int(11) unsigned NOT NULL,
  `value` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`attrib_kmer_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Table structure for table `attrib_type_detail`
--

DROP TABLE IF EXISTS `attrib_type_detail`;
CREATE TABLE `attrib_type_detail` (
  `attrib_type_id` int(11) unsigned NOT NULL,
  `attrib_class_id` smallint(5) unsigned DEFAULT NULL,
  `molecule` varchar(10) NOT NULL DEFAULT '',
  `units` varchar(25) DEFAULT NULL,
  `doi` varchar(50) DEFAULT NULL,
  `pmid` varchar(20) DEFAULT NULL,
  `basis` varchar(20) DEFAULT NULL,
  `kmer_length` int(11) DEFAULT NULL,
  PRIMARY KEY (`attrib_type_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 CHECKSUM=1;

--
-- Table structure for table `feature_attrib_analysis`
--

DROP TABLE IF EXISTS `feature_attrib_analysis`;
CREATE TABLE `feature_attrib_analysis` (
  `feature_attrib_analysis_id` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
  `attrib_analysis_id` smallint(5) unsigned NOT NULL,
  `feature_id` varchar(2) DEFAULT NULL,
  `biotype` varchar(40) DEFAULT NULL,
  `feature_counter` smallint(3) DEFAULT NULL,
  `context` varchar(255) DEFAULT NULL,
  `context_start` int(10) DEFAULT NULL,
  `context_end` int(10) DEFAULT NULL,
  `data_type` varchar(255) DEFAULT NULL,
  `run_date` date DEFAULT NULL,
  `by_whom` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`feature_attrib_analysis_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Table structure for table `feature_attrib_analysis_output`
--

DROP TABLE IF EXISTS `feature_attrib_analysis_output`;
CREATE TABLE `feature_attrib_analysis_output` (
  `feature_attrib_analysis_output_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `feature_attrib_analysis_id` smallint(5) unsigned DEFAULT NULL,
  `values` text,
  PRIMARY KEY (`feature_attrib_analysis_output_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Table structure for table `genomic_feature`
--

DROP TABLE IF EXISTS `genomic_feature`;
CREATE TABLE `genomic_feature` (
  `feature_id` varchar(2) NOT NULL,
  `feature_name` varchar(255) NOT NULL,
  `description` text,
  PRIMARY KEY (`feature_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AVG_ROW_LENGTH=98 CHECKSUM=1;

--
-- Table structure for table `kmer`
--

DROP TABLE IF EXISTS `kmer`;
CREATE TABLE `kmer` (
  `kmer_id` int(11) unsigned NOT NULL,
  `kmer` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`kmer_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COMMENT='ordered list of k-mers';

--
-- Table structure for table `seq_region_pos`
--

DROP TABLE IF EXISTS `seq_region_pos`;
CREATE TABLE `seq_region_pos` (
  `seq_region_pos_id` bigint(20) unsigned NOT NULL,
  `seq_region_id` int(10) DEFAULT NULL,
  `seq_region_position` int(10) DEFAULT NULL,
  `base` char(1) DEFAULT NULL,
  PRIMARY KEY (`seq_region_pos_id`),
  UNIQUE KEY `UNQ_seq_region_id_seq_region_position` (`seq_region_id`,`seq_region_position`),
  KEY `IDX_seq_region_pos_seq_region_id` (`seq_region_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AVG_ROW_LENGTH=28;

--
-- Table structure for table `seq_region_pos_attrib_value`
--

DROP TABLE IF EXISTS `seq_region_pos_attrib_value`;
CREATE TABLE `seq_region_pos_attrib_value` (
  `seq_region_pos_id` bigint(20) unsigned NOT NULL,
  `attrib_analysis_id` smallint(5) unsigned NOT NULL,
  `value` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`seq_region_pos_id`,`attrib_analysis_id`),
  KEY `attrib_type_id` (`attrib_analysis_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AVG_ROW_LENGTH=23 CHECKSUM=1;

--
-- Table structure for table `transcript_feature`
--

DROP TABLE IF EXISTS `transcript_feature`;
CREATE TABLE `transcript_feature` (
  `transcript_feature_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `transcript_id` int(10) unsigned DEFAULT NULL,
  `feature_id` varchar(2) CHARACTER SET utf8 DEFAULT NULL,
  `seq_region_pos_start` bigint(20) DEFAULT NULL,
  `seq_region_pos_end` bigint(20) DEFAULT NULL,
  `seq_region_strand` tinyint(2) DEFAULT NULL,
  `rank` int(10) DEFAULT NULL,
  PRIMARY KEY (`transcript_feature_id`),
  KEY `IDX_transcript_feature_feature_id` (`feature_id`),
  KEY `IDX_transcript_feature_transcript_id` (`transcript_id`),
  KEY `tf_trans_id_feat_id_rank` (`transcript_id`,`feature_id`,`rank`),
  KEY `tranfeature_trans_id_feat_id_rank` (`transcript_id`,`feature_id`,`rank`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AVG_ROW_LENGTH=30;
