import glob
import os
import sys
path= os.getcwd()
if len(sys.argv) == 3:
    protein = sys.argv[1]
    centroid = sys.argv[2]
    files = glob.glob(path + '/*.pdb') #taking all pdb files from the current directory
    coord = []
    for f in files:
        ligand = f.split("/")[-1][:-4] + ".pdb "
        cord_split = centroid.split(",")
        x_cord = str(cord_split[0])
        y_cord = str(cord_split[1])
        z_cord = str(cord_split[2])
        coord.append(x_cord)
        coord.append(y_cord)
        coord.append(z_cord)
        os.system("python dock_centroid.py " + f'{protein} ' + ligand +str(coord[0])+","+str(coord[1])+","+str(coord[2]))
else:
    print('''python3 centroid_lig1.pdb <protein_pdb_file> <x,y,z>
eg.
python3 centroid_lig1.pdb 7k15.pdb 1.9392312138728325,-8.92228901734104,18.28384393063584
    ''')


