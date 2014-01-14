#!/usr/local/bin/env python
#python 2.7.5 requires biopython

########### promer2circos ############

#A script for converting show-coords output for sequence matches from the Mummerplot package to circos link-track format.


#Version 1. Adam Taranto, January 2014.
#Contact Adam Taranto, adam.p.taranto@gmail.com

###Import modules
import sys;
import argparse;
import re;

#coords_input=open('data/promerdata.txt','rU').readlines()

def justLinks(coords_input):
	##Find first row after header
	i=0
	for row in coords_input:
		if len(re.split(r'\t+', row)) >3:
			headerRow=i+1
			break
		else:
			i+=1

	return coords_input[headerRow:None]

def main(coords_input):
	with open(coords_input, 'rU') as infile:
		rawLinks=justLinks(infile.readlines());

	i=1
	for row in rawLinks:
		l=re.split(r'\t+', row.rstrip('\n'))
		#print l[14]
		print 'Link'+str(i)+'\t'+l[0]+'\t'+l[1]+'\t'+l[13]+'\n'+'Link'+str(i)+'\t'+l[2]+'\t'+l[3]+'\t'+l[14]
		#sys.stdout.write
		i+=1


if __name__== '__main__':
    ###Argument handling.
    arg_parser = argparse.ArgumentParser(description='');
    arg_parser.add_argument("coords_input", help="Directory to show-coords tab-delimited input file.");
    args = arg_parser.parse_args();

    ###Variable Definitions
    coords_input=args.coords_input;

    ##Run main
    main(coords_input);


