import os
import sys
if len(sys.argv) == 3:
     energy = sys.argv[1]
     decimal = sys.argv[2]
     
     with open("Energy.txt","w+") as energy_file:
         final_energy = energy + "." + decimal
         file_name = "dock_pf1.dlg"
         cwd = os.getcwd()
         dir_name = cwd.split("/")

         for root, dirs, files in os.walk(cwd):
             if file_name in files:
                 file_path = os.path.join(root, file_name)
                 # print(file_path)

                 with open(file_path) as file:
                     data = file.readlines()

                     for lines in data:

                         if final_energy in lines[10:15]:
                             line_1 = lines
                             if "1" == line_1[3]:
                                 list = []
                                 list.append(lines)
                                 #print(list)
                                 split = file_path.split("/")

                                 result = (split[-2] + ": " + list[0][10:16] + " kcal/mol")
                                 if "analyse" not in result:
                                     print(result)
                                     energy_file.write(F'{result} \n')
else:
    print('''  python binding_energy_decimal_write.py <approximate Binding energy you want> <digit_after_decimal>
           exp:python binding_energy.py -12 7''')

                     


                    






