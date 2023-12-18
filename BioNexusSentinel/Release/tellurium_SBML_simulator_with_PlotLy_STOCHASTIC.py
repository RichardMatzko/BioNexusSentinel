import argparse
import tellurium as te
import numpy as np
import libsbml
import plotly.graph_objects as go
import plotly.offline as py

def get_species_names(sbml_file):
    reader = libsbml.SBMLReader()
    document = reader.readSBML(sbml_file)
    model = document.getModel()
    species_names = [species.getName() for species in model.getListOfSpecies()]
    return species_names

parser = argparse.ArgumentParser(description='Simulate SBML model and create a plot.')
parser.add_argument('model_file', type=str, help='Path to the SBML model file.')
parser.add_argument('start_time', type=float, help='Start time of the simulation.')
parser.add_argument('end_time', type=float, help='End time of the simulation.')
parser.add_argument('num_points', type=int, help='Number of data points to generate in the simulation.')

args = parser.parse_args()

rr = te.loadSBMLModel(args.model_file)
rr.integrator = 'gillespie'  # Change the solver to Gillespie's method
result = rr.simulate(args.start_time, args.end_time, args.num_points)

species_names = get_species_names(args.model_file)
species_concentrations = np.array(result[:, 1:])
time = np.array(result[:, 0])

fig = go.Figure()

for i, name in enumerate(species_names):
    fig.add_trace(go.Scatter(x=time, y=species_concentrations[:,i], mode='lines', name=name))

fig.update_layout(height=1000, width=1500, title_text="Species concentrations over time")
# fig is your Figure object
py.plot(fig, filename='my_plot.html', auto_open=False)
fig.show()