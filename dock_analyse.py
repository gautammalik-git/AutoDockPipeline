import sys
import os
import shutil

if len(sys.argv) == 5:
	lig_file = sys.argv[1] 
	dlg_file = sys.argv[2]
	out_fold = sys.argv[3]
	prot_file = sys.argv[4]
	directory_name = os.getcwd()
	path_out = directory_name+'/'+out_fold
	
	if not os.path.exists(path_out):
		os.mkdir(path_out)
	else:
		shutil.rmtree(path_out)
		os.mkdir(path_out)
	a_line = open(lig_file,"r")
	aline = a_line.readlines()
	
	b_line = open(dlg_file, "r")
	bline = b_line.readlines()
	shutil.copy(directory_name+"/"+lig_file, path_out+"/"+lig_file)
	shutil.copy(directory_name+"/"+dlg_file, path_out+"/"+dlg_file)
	shutil.copy(directory_name+"/"+prot_file, path_out+"/"+prot_file)
	def prot(prot_file):
		a_line = open(prot_file, "r")
		aline = a_line.readlines()
		prt = ""	
		for line in aline:
			prt += line
		return prt
	prt = prot(prot_file)
	
	def dlg_count(dlg_file):
		b_line = open(dlg_file, "r")
		bline = b_line.readlines()
		count = 0
		for line in bline:
			if "USER    Cluster Rank = " in line:
				count += 1
		return count
	dlg_occ = dlg_count(dlg_file)
	#print dlg_occ
	def arr_clu_ran(bline, dlg_occ):
		arr1 = ""
		arr2 = []
		cc = 0
		cc1 = 1
		#out = open("out1","w")
		for line in bline:
			if cc1 < dlg_occ+1 :
				asss =0
				if line[:24] == "USER    Cluster Rank = "+str(cc1):
					print line
					cc = 1
					#print cc1
				if cc == 1:
					arr1 += line
				if "ENDMDL" in line[:6]:
					cc = 0
					cc1 += 1
					arr2.append(arr1)
					arr1 = ""
		return arr2
	arr2 = arr_clu_ran(bline, dlg_occ)
	#print arr2
	def fil_op(dlg_occ, arr2):
		i = 1
		if i < dlg_occ+1:
			for line in arr2:
				#print line
				out = open(directory_name+"/"+out_fold+"/out"+str(i), "w")
				out.write(line)
				out.close()
				i += 1
					
			
	fil_op(dlg_occ, arr2)
	
	def comp(lig_file, out_fold, prt):
		a_line = open(path_out+"/"+lig_file)
		aline = a_line.readlines()
		dir_lis = os.listdir(path_out)
		count = 1
		for dir_lis_line in dir_lis:
			#print dir_lis_line
			if "out" in dir_lis_line[:3]:
				
				out = open(path_out+"/"+str(count)+"doc.pdb", "w")
				b_line = open(path_out+"/"+dir_lis_line)
				bline = b_line.readlines()
				for line1 in aline:
					for line2 in bline:
						if line1[11:26] == line2[11:26]:
							if line1[11:26].count(" ") > 1 :
								#print line1[11:26]
								#print line1[11:26].count(" ")
								out.write(line1[:26]+line2[26:54]+line1[54:])
				#out.write("END \n")
				out.write(prt)
				out.close()
				count += 1

	
	def lig_merge():
		dir_lis = os.listdir(path_out)
		out = open(path_out+"/"+"merge.pdb",'w')
		dir_lis1 = []
		for l1 in dir_lis:
			if l1[:3] == "out":
				dir_lis1.append(l1)
		dir_lis1 = sorted(dir_lis1, key = lambda x1 : x1[3:])
		for line in range(1, len(dir_lis1)+1):
			#print line
			if "out"+str(line) in dir_lis1:
				#print "sgf"
				a_line = open(path_out+"/"+"out"+str(line),'r')
				aline = a_line.readlines()
				for line1 in aline:
					if line1[:4] == "ATOM":
						line1 = line1.replace("ATOM  ","HETATM")
						out.write(line1)
				out.write("END\n")
		out.close()
	lig_merge()
	
		
else:
	print "Usage: python dock_analyse.py ligand.pdb dlg_file output_folder protein.pdb"
	sys.exit()
