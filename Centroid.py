import os
import numpy as np
import math
import sys
if len(sys.argv) == 2:
    prot_name = sys.argv[1]
    pro_file = os.path.join(prot_name)
    x_co_list = []
    y_co_list = []
    z_co_list = []
    with open('centroid.txt', 'w+') as pdbfile:
        with open(pro_file) as f:
            data = f.readlines()
        for line in data:
            x_co, y_co, z_co = float(line[31:38]), float(line[39:46]), float(line[47:54])
            x_co_list.append(x_co)
            y_co_list.append(y_co)
            z_co_list.append(z_co)
        xn, yn, zn = np.mean(x_co_list), np.mean(y_co_list), np.mean(z_co_list)
        #pdbfile.write(xn, yn, zn)
        print(F'{xn},{yn},{zn}')
else:
    print("python centroid.py" + "<Protein PDB ID>")




