import sys
import os
import subprocess
import shutil


if len(sys.argv) == 4:
	prot_name1 = sys.argv[1]
	os.system("python PDB_process.py "+prot_name1)
	prot_name = prot_name1[:-4]+"a.pdb"
	lig_name = sys.argv[2]
	centroid = sys.argv[3]
	print(prot_name)
	directory_name = os.getcwd()
	path_out = directory_name+'/'+prot_name[:-4]+'_'+lig_name[:-4]
	if not os.path.exists(path_out):
		os.mkdir(path_out)
	else:
		shutil.rmtree(path_out)
		os.mkdir(path_out)
	shutil.copy(prot_name, path_out)
	shutil.copy(lig_name, path_out)
	shutil.copy(directory_name+'/Repository/autogrid4', path_out)
	shutil.copy(directory_name+'/Repository/autodock4', path_out)
	os.chdir(path_out)
	try:
		pre_rec = 'python ../Repository/prepare_receptor4.py -r '+prot_name+' -A bonds_hydrogens '
		subprocess.call(pre_rec, shell=True)
	except:
		pre_rec = 'python ../Repository/prepare_receptor4.py -r '+prot_name
		subprocess.call(pre_rec, shell=True)
	try:
		pre_lig = 'python ../Repository/prepare_ligand4.py -l'+lig_name+' -A bonds_hydrogens'
		subprocess.call(pre_lig, shell=True)
	except:
		pre_lig = 'python ../Repository/prepare_ligand4.py -l'+lig_name
		subprocess.call(pre_lig, shell=True)
		
	grid_para = 'python ../Repository/prepare_gpf4.py -l '+lig_name[:-4]+'.pdbqt -r '+prot_name[:-4]+'.pdbqt -p gridcenter='+centroid+' -o grid_pf.gpf'
	subprocess.call(grid_para, shell=True)
	
	dock_para = 'python ../Repository/prepare_dpf4.py -l '+lig_name[:-4]+'.pdbqt -r '+prot_name[:-4]+'.pdbqt -o dock_pf.dpf'
	subprocess.call(dock_para, shell=True)
	def a():
		a_line = open("dock_pf.dpf", 'r')
		aline = a_line.readlines()
		out = open("dock_pf1.dpf", 'w')
		for line in aline:
			#print line
			if line[:6] == "ga_run":
				a = line[:6]+" 10"+line[10:]
				out.write(a)
			else:
				out.write(line)
		out.close()
	a()
	os.remove('dock_pf.dpf')
        subprocess.call('./autogrid4 -p grid_pf.gpf -l grid_pf.glg ', shell=True)
        os.system('./autodock4 -p dock_pf1.dpf -l dock_pf1.dlg')
	
	#shutil.move(prot_name[:-4], path_out+prot_name[:-4])
	os.system("rm autodock-intel-omp-nompi")
	os.system("rm autogrid4")
	os.chdir(directory_name)

		
else:
	print("Usage python dock.py <prot_name> <lig_name> <centroid_coordinate>")
	sys.exit()
