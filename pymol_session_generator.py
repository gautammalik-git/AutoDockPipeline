import sys
import os
import shutil
import time

if len(sys.argv) == 3:
	prot_pdb = sys.argv[1]
	lig_pdb = sys.argv[2]
	
else:
	print ("python a.py <protein_pdb> <ligand_pdb>")
	sys.exit()

dire = os.getcwd()

'''
def a():
	out = open(dire+"/hetatm.pdb", 'w')
	pdb = "" 
	for i in os.listdir(dire+"/"+fold+"/analyse"):
		#print i
		if i[-4:] == ".pdb":
			if i.count("_") == 1:
				pdb = i
				shutil.copy(dire+"/"+fold+"/analyse/"+i, dire)
		if i == "merge.pdb":
			aline = open(dire+"/"+fold+"/analyse/"+i, 'r').readlines()
			for line in aline:
				line = line.strip()
				if line == "END":
					break
				out.write(line+"\n")
			out.close()
	return pdb	
pdb = a()
'''

import __main__
__main__.pymol_argv = ['pymol','-rqkc'] # Pymol: quiet and no GUI
import pymol
from pymol import cmd
from pymol import util
#pymol.finish_launching() # not needed for recent pymol versions
'''
one_letter ={'VAL':'V', 'ILE':'I', 'LEU':'L', 'GLU':'E', 'GLN':'Q', \
'ASP':'D', 'ASN':'N', 'HIS':'H', 'TRP':'W', 'PHE':'F', 'TYR':'Y',    \
'ARG':'R', 'LYS':'K', 'SER':'S', 'THR':'T', 'MET':'M', 'ALA':'A',    \
'GLY':'G', 'PRO':'P', 'CYS':'C'}

label n. ca, one_letter[resn]
'''

def b(pdb):
	obj1 = "prot"
	obj2 = "heta"
	obj3 = "bs"
	obj4 = "bsca"
	#pymol.cmd.extend("one_letter",one_letter)
	pymol.cmd.load(pdb, obj1)
	pymol.cmd.hide("everything",obj1)
	pymol.cmd.show_as("cartoon", obj1)
	pymol.cmd.set("cartoon_fancy_helices", 1)
	pymol.cmd.set("cartoon_smooth_loops", 1)
	pymol.cmd.color("gray90", obj1)
	pymol.cmd.bg_color("white")
	pymol.cmd.load(lig_pdb, obj2)
	pymol.cmd.hide("everything",obj2)
	pymol.cmd.show_as("stick", obj2)
	pymol.cmd.color("magenta", obj2)
	pymol.cmd.set("stick_radius",.1)
	pymol.util.cbam(obj2)
	#sleep(.1)
	#select obj1, bb w. 4 of resi 303
	#select sele, byres(obj1 w. 4A of obj2)
	pymol.cmd.select("sele",'byres('+obj1+" w. 4A of "+obj2+')')
	pymol.cmd.create(obj3,"sele")
	pymol.cmd.hide("everything",obj3)
	pymol.cmd.show_as("line",obj3)
	pymol.cmd.color("deepteal", obj3)
	pymol.util.cbac(obj3)
	pymol.cmd.distance("hbonds",obj1, obj2, 4.5, mode=2)
	pymol.cmd.set("dash_color","black")
	pymol.cmd.set("dash_width","2")
	pymol.cmd.hide("label","hbonds")
	pymol.cmd.set("line_width",1.5)
	#pymol.cmd.label(obj3,"residue")
	pymol.cmd.set("label_color","black")
	pymol.cmd.select("sele",obj3+" and  name ca")
	pymol.cmd.create(obj4,"sele")
	one_letter = {'VAL':'V', 'ILE':'I', 'LEU':'L', 'GLU':'E', 'GLN':'Q', \
'ASP':'D', 'ASN':'N', 'HIS':'H', 'TRP':'W', 'PHE':'F', 'TYR':'Y',    \
'ARG':'R', 'LYS':'K', 'SER':'S', 'THR':'T', 'MET':'M', 'ALA':'A',    \
'GLY':'G', 'PRO':'P', 'CYS':'C'}
	#pymol.cmd("o",one_letter)
	#pymol.cmd.extend("o",one_letter)
	#pymol.cmd.label(obj4,"o['resn']"+'-'+"resi")
	pymol.cmd.label(obj4,"resn+'-'+resi")
	cmd.set('ray_shadows','off')
	#pymol.cmd.label(obj4,"%s+%s" % ("resn","resi"))
	#pymol.cmd.color("deepteal", obj3)
	pymol.cmd.save("pymol.pse")
	
	
b(prot_pdb)
	
	
	
