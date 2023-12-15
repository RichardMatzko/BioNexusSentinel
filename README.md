<table>
<tr>
<td><img src="BioNexusSentinel/BioNexusSentinel.png" alt="BioNexus Sentinel Image" width="150" height="150"/></td>
<td><h1>BioNexusSentinel</h1>A research biochemical network explorer and cytohistological encyclopedia for Windows.</td>
</tr>
</table>

---

**BioNexusSentinel**<br>
is a nascent, ergonomic, experimental, research software for reaction network exploration, with a cytohistological genetic encyclopedia component, featuring a dataset preprocessed with R. It was developed to explore, and potentially manipulate, bioinformatics data for ongoing multicellular simulation research. It is capable of loading SBML files for evaluation and visualization and can export visualizations in various format. Key features include network visualizations and tables, an experimental kinetics parameterization mechanism and time course simulation, a cytohistological genetics explorer and a biochemical model search engine for downloading and organizing models from Reactome. Pending successful publication, the link to the article will be available here, along with the R code for the data manipulations for the preprocessed dataset, albeit the transformed dataset is depended on and distributed with this repository.

---

**REQUIREMENTS**<br>
Created with Windows 11.

---

### **LICENSE**<br>
Creative Commons Attribution-NonCommercial (CC BY-NC) license

---

**DISCLAIMER**<br>
It is recommended to read this entire page before use. Use this experimental software at your own risk. This software performs certain disk operations, including (but not necessarily exclusively) saving output files to the project folder and saving in documents to a folder it creates called BioNexusSentinel. This software has no intentional designs to collect any of your data and is designed to be as local to your machine as possible, although it makes API calls to access online bioinformatics resources, particularly from the Reactome database. It has been tested and used extensively, but still no guarantee will be given if you choose to use it. As the work is currently under development, certain features may work with limited effectiveness. Temporary files used in processing are saved to the executable folder subfolder "Temp" and these will need to be manually cleared. See also TENTATIVE FEATURES below.

---

**QUICK START**<br>
Download repository and navigate to "Release" folder and double click BioNexusSentinel.exe. Please note certain functions won't work without additional installs.

---

**ADDITIONAL INSTALLATION PREREQUISITES**<br>
For full functionality:
->GraphViz for network graphics (https://graphviz.org/download/). BNS was built alongside version 8.0.5.
->BioLayout 3.4 if you wish for 3D network graphics external visualization (https://github.com/biolayout/biolayout/releases)
->Python3 installation (https://www.python.org/downloads/)
->Python libraries should be installed for the experimental network solver solution. This should be installed alongside your correct interpreter path. It is possible to do within an IDE. Universally you can check your active Python interpreter path via (Get-Command python).Source in Windows PowerShell. Then install via:
	->pip install tellurium
	->pip install libsbml
	->pip install python-libsbml
	->pip install numpy

 ---

**TENTATIVE FEATURES**<br>
Not all experimental features described in the publications are included in this release, for the sake of a smoother more complete experience. A very large network sometimes may have problems loading. It is recommended that if the initial visualization fails, you should apply pruning to the network to zero in on specific reactions or a range of reactions. Temporary files are stored in. You should be aware that the autokinetics and simulation features are tentative. It is very common that SBML models find incompatibility. System inputs and outputs needs review on the entry screen, since some system "inputs" currently overlap with dual reactant/products.

---
