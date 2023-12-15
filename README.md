<table>
<tr>
<td><img src="BioNexusSentinel/BioNexusSentinel.png" alt="BioNexus Sentinel Image" width="150" height="150"/></td>
<td><h1>BioNexusSentinel</h1>A research biochemical network explorer and cytohistological encyclopedia for Windows.</td>
</tr>
</table>

---

### **BioNexusSentinel**<br>
is a nascent, ergonomic, experimental, research software for reaction network exploration, with a cytohistological genetic RNA-Seq encyclopedia component, featuring a dataset preprocessed with R. It was developed to explore, and potentially manipulate, bioinformatics data for ongoing multicellular simulation research (see also https://github.com/RichardMatzko/UnrealMulticell3D.git and https://www.mdpi.com/2073-4425/14/1/154). It is capable of loading SBML files for evaluation and visualization and can export visualizations in various format. Key features include network visualizations and tables, an experimental kinetics parameterization mechanism and time course simulation, a cytohistological genetics explorer and a biochemical model search engine for downloading and organizing models from Reactome. Pending successful publication, the link to the article will be available here, along with the R code for the data manipulations for the preprocessed dataset. The readily transformed dataset is depended on and distributed with this repository.

---

### **VERY IMPORTANT**<br>
Upon downloading the repository, please also download the 309 MB zipped expression data (too large for GitHub) from https://drive.google.com/file/d/1C4afBRIt4PArM1X4jlnVw_a1To5UtHVH/view?usp=drive_link and extract the folders Cell_Specific_Expression and ExpressionByGeneSymbol directly into the assets directory from HPA_EXPRESSION_DATA_TRANSFORMED.zip.

---

### **REQUIREMENTS**<br>
Created with Windows 11 with .NET Framework 4.7.2. You probably won't need to download .NET Framework separately as it should run out of the box with Windows 11 (and probably 10) installations.

---

### **LICENSE**<br>
BioNexusSentinel is provided under Creative Commons Attribution-NonCommercial (CC BY-NC) license, including all assets unless mentioned below.

SBO_OWL is available from https://github.com/EBI-BioModels/SBO under The Artistic License 2.0 and is included in BioNexusSentinel assets.

Reactome data follows the Reactome license agreement (https://reactome.org/license), specifically ReactomePathways.txt (obtained from https://reactome.org/download/current/ReactomePathways.txt) and ReactomePathwaysRelation.text (derived from https://reactome.org/download/current/ReactomePathwaysRelation.txt). Naturally, SBML models downloaded through BioNexusSentinel from Reactome follow these license agreements.

Human Protein Atlas data is given following novel alteration to its structure and hence falls under the BioNexusSentinel licensing as stated above. The original data was supplied under https://creativecommons.org/licenses/by-sa/3.0/ CC BY-SA 3.0 DEED license.

---

### **DISCLAIMER**<br>
It is recommended to read this entire page before use. Use this experimental software at your own risk. This software performs certain disk operations, including (but not necessarily exclusively) saving output files to the project folder and saving in documents to a folder it creates called BioNexusSentinel. This software has no intentional designs to collect any of your data and is designed to be as local to your machine as possible, although it makes API calls to access online bioinformatics resources, particularly from the Reactome database. It has been tested and used extensively, but still no guarantee will be given if you choose to use it. As the work is currently under development, certain features may work with limited effectiveness. Temporary files used in processing are saved to the executable folder subfolder "Temp" and these will need to be manually cleared. See also TENTATIVE FEATURES below.

---

### **SUMMARY OF INSTALLATION INSTRUCTIONS**<br>
1. Acquire HPA_EXPRESSION_DATA_TRANSFORMED.zip from https://drive.google.com/file/d/1C4afBRIt4PArM1X4jlnVw_a1To5UtHVH/view?usp=drive_link.
2. Download BioNexusSentinel repository.
3. Extract Cell_Specific_Expression and ExpressionByGeneSymbol from HPA_EXPRESSION_DATA_TRANSFORMED.zip.
4. Place Cell_Specific_Expression and ExpressionByGeneSymbol into BioNexusSentinel/Assets
5. Read ADDITIONAL INSTALLATION PREREQUISITES for full functionality.
6. Launch BioNexusSentinel via BioNexusSentinel.exe from BioNexusSentinel/Releases/BioNexusSentinel.exe

---

### **QUICK START**<br>
Please read the VERY IMPORTANT section above for instructions on how to acquire the required genetics data. Download the repository and navigate to "Release" folder and double click BioNexusSentinel.exe. Please note certain functions won't work without additional installs (see ADDITIONAL INSTALLATION PREREQUISITES).

---

### **ADDITIONAL INSTALLATION PREREQUISITES**<br>
For full functionality:<br>
->GraphViz for network graphics (https://graphviz.org/download/). BNS was built alongside version 8.0.5.<br>
->BioLayout 3.4 if you wish for 3D network graphics external visualization (https://github.com/biolayout/biolayout/releases)<br>
->Python3 installation (https://www.python.org/downloads/)<br>
->Python libraries should be installed for the experimental network solver solution. This should be installed alongside your correct interpreter path. It is possible to do within a Python IDE such as VS Code. Universally you can check your active Python interpreter path via (Get-Command python).Source in Windows PowerShell. Then install via:<br>
	->pip install tellurium<br>
	->pip install libsbml<br>
	->pip install python-libsbml<br>
	->pip install numpy<br>
 
 ---

### **TENTATIVE FEATURES**<br>
Not all experimental features described in the publication are included in this release for the sake of a smoother more complete experience. A very large network sometimes may have problems loading. It is recommended that if the initial visualization fails, you should apply pruning to the network to zero in on specific reactions or a range of reactions. Temporary files are stored in. You should be aware that the autokinetics and simulation features are tentative. It is very common that SBML models find incompatibility. System inputs and outputs needs review on the entry screen, since some system "inputs" currently overlap with dual reactant/products.

---
