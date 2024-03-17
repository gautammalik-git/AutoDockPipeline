# AutoDockPipeline

Your one-stop solution for protein-ligand docking. This pipeline simplifies molecular docking of library of ligands against a protien, helping researchers study protein-ligand interactions efficiently. It offers clear instructions and customizable options for easy virtual screening. 

Simplify drug discovery, explore confidently!

---

## About AutoDock 

This pipeline is built upon **AutoDock4**
<br>
AutoDock consists of two main programs:

- **AutoGrid**: Pre-calculates the grids describing the target protein for use in the docking process.
- **AutoDock**: Facilitates the docking of the ligand to a grid representation of the target protein.

---

## Installing AutoDock4 on CPU

To install AutoDock4 ,visit [AutoDock website](https://autodock.scripps.edu/download-autodock4/).
<br>
1. Download the AutoDock4 sofware compatible with your system.
2. Follow the Readme file to install the software.
3. Make sure to download the MGLtools tar file compatible with your system, which is essential for running both AutoDock GUI (ADT) and AutoDock4. It is available on their [website](https://ccsb.scripps.edu/mgltools/).

### For Mac users:

ADT is currently unavailable for Macs equipped with Apple Silicon chips. Consequently, this pipeline does not support AutoGrid calculations. However, AutoDock remains compatible with Macs featuring Apple Silicon chips. By installing AutoDock GPU, users can run AutoDock on macs and also enhance its performance speed.

## Installing AutoDock-GPU

To install AutoGrid, follow the same steps as described above. For faster docking on systems with GPUs, install AutoDock-GPU. 

1. To compile AutoDock-GPU, simply navigate to this [GitHub page](https://github.com/ccsb-scripps/AutoDock-GPU) and follow the provided instructions.
2. I've created a dedicated repository for AutoDock-GPU, covering the setup process and the entire pipeline. If you're using AutoDock-GPU, you can find more information [here]().

## Organizing Files and Setting up Repository

To ensure clarity, create a new directory and move the AutoDock and MGLTools tar files there. Follow these steps:

1. Navigate to the directory containing these tar files.
2. `mkdir AutoDock`
3. `cp <autodock-tar.gz> <mgltools-tar.gz> ./AutoDock`
4. `cd AutoDock`
5. `tar xfz <autodock-tar.gz>`
6. `tar xfz <mgltools-tar.gz>`

Now, create another directory named 'Repository'.

7. `mkdir Repository && cp ./<autodock-directory>/autogrid ./Repository && cp ./<autodock-directory>/autodock ./Repository && cp -r <mgltools-directory> ./Repository`

Copy these Python files into the Repository as well:

8. `cp ./<mgltools-directory>/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_*4.py ./Repository`

Replace `<autodock-tar.gz>` and `<mgltools-tar.gz>` with the names of the AutoDock and MGLTools tar files you downloaded from the website. Similarly, replace `<autodock-directory>` and `<mgltools-directory>` with the directories you extracted from the respective tar files.

'Repository' serves as the primary directory. It must be present in your working directory whenever docking is conducted.

## Pre-Docking Steps

Ensure Python2 and Python3 are installed on your system.

1. Create a directory containing all your ligand PDB files and your protein PDB file.
2. Add 'Repository' in your current working directory (cwd).
3. Copy all the Python scripts provided in this repository to your cwd.
4. Extract the binidng pocket out from the protein PDB file-
   
   `python3 targeted_site.py <protein_name> <ligand_name_as_mentioned_in_pdb_file> <CHAIN_ID_for_ligand>`

   For example:
   <br>
   `python3 targeted_site.py 7k15.pdb VRJ A`

   This will give 7k15_site.pdb as output.

   
5. Get the Centroid of the extracted binding site:
   
   `python3 Centroid.py <bind_site>`

   
   For example:
   <br>
   `python3 Centroid.py 7k15_site.pdb`

   This will print out the <x,y,z> coordinated. 

 ## Docking

 1. Change path:

    `export PATH=./Repository/<mgltools-directory>/bin:$PATH`

2. Perform docking:

   Make sure you are in the cwd with all the ligand PDB files, protein PDB file, 'Repository' and all the python scripts attached with this github repository.

    `python3 centroid_lig1.py <prot_name> <x,y,z>`

   This initiates the docking process for the ligands located in the current working directory (cwd) with the specified protein.

If you want to run single protein-ligand docking:

`python2 dock_centroid.py <prot_name> <ligand_name> <x,y,z>`

For example:
<br>
`python2 dock_centroid.py 7k15.pdb VRJ.pdb 1.9392312138728325,-8.92228901734104,18.28384393063584`

This will generate a new directory named '7k15a_9'. Within this directory, you'll find all the input and output files produced during the docking."

## Analyze docking Results

1. To get the binding energy values out from the dlg file:

   `python3 binding_energy.py`
   

 

 











