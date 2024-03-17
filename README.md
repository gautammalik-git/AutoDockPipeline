# AutoDockPipeline

AutoDockPipeline: Your one-stop solution for protein-ligand docking. This pipeline simplifies molecular docking, helping researchers study protein-ligand interactions efficiently. It offers clear instructions and customizable options for easy virtual screening. Simplify drug discovery, explore confidently!

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
2. Download the source code file.
3. Follow the Readme file to install the software.
4. Make sure to download the MGLtools tar file compatible with your system, which is essential for running both AutoDock GUI (ADT) and AutoDock4. It is available on their [website](https://ccsb.scripps.edu/mgltools/).
<br>
### For Mac users:
ADT is currently unavailable for Macs equipped with Apple Silicon chips. Consequently, this pipeline does not support AutoGrid calculations. However, AutoDock remains compatible with Macs featuring Apple Silicon chips. By installing AutoDock GPU, users can run AutoDock on macs and also enhance its performance speed.

## Installing AutoDock-GPU

Follow the same procedure above to install the 
To speed up docking on systems with GPUs, install AutoDock-GPU.

1. Visit their [GitHub page](https://github.com/ccsb-scripps/AutoDock-GPU) and follow the instructions.




