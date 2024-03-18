import os
import sys


if len(sys.argv) == 4:
    prot_name = sys.argv[1]
    HET_name = sys.argv[2]
    ID_name = sys.argv[3]
    covid_file = os.path.join(prot_name)
    with open(prot_name[:4]+"site.pdb", 'w+') as pdbfile:
        with open(covid_file) as f:
            data = f.readlines()
        ATOM_list = []
        ATM_list = []
        HET_list = []
        RES_list = []
        HETATM_list = []
        atm_lim_d_list = []
        het_lim_d_list = []
        new_items_list = []
        new_items_list_het = []
        for line in data:
            if "ATOM" == line[:4]:
                ATM = line
                ATM_list.append(ATM)
       
        for lines in data:
            if "HETATM" == lines[:6:]:
                HETATM = lines
                HETATM_list.append(HETATM)
        for item in HETATM_list:
            if HET_name in item[17:22]:
                residue = item
                RES_list.append(residue)
        for items in RES_list:
            if ID_name in items[21:23]:
                id_name = items
                HET_list.append(id_name)
        
        for item in ATM_list:
            atm = item[:80]
            x_atm = float(item[31:38])
            y_atm = float(item[39:46])
            z_atm = float(item[47:54])
            for items in HET_list:
                het = items[:80]
                x_het, y_het, z_het = float(items[31:38]), float(items[39:46]), float(items[47:54])
                x_dis, y_dis, z_dis = (x_het - x_atm), (y_het - y_atm), (z_het - z_atm)

                d = ((x_dis) * (x_dis)) + ((y_dis) * (y_dis)) + ((z_dis) * (z_dis))
                distance = pow(d, 0.5)
                atm_lim = (F'{atm}')
                het_lim = (F'{het}')
                if distance <= 4.5:
                    atm_lim_d = (atm_lim)
                    het_lim_d = (het_lim)
                    atm_lim_d_list.append(atm_lim_d)
                    het_lim_d_list.append(het_lim_d)
        
        for item in atm_lim_d_list:
            for items in ATM_list:
                if item[17:27] == items[17:27]:
                    new_items = items
                    new_items_list.append(new_items)
        lines_list = []
        for lines in new_items_list:
            if lines not in lines_list:
                lines_list.append(lines)
                pdbfile.write(F'{lines}')
else:
    print("site.py"+" <protein_name.pdb>"+'<Ligand_residue_name>'+"<Character>")

