pip install pgmpy
from pgmpy.models import BayesianNetwork
from pgmpy.inference import VariableElimination
from pgmpy.factors.discrete import TabularCPD
model = BayesianNetwork([('Rain', 'Traffic'), ('Traffic', 'Accident')])
cp_rain = [0.8, 0.2]  
cp_traffic = [[0.9, 0.5],  
               [0.1, 0.5]] 
cp_accident = [[0.95, 0.2],  
                [0.05, 0.8]]  
model.add_cpds(
    TabularCPD(variable='Rain', variable_card=2, values=cp_rain),
    TabularCPD(variable='Traffic', variable_card=2, 
               values=cp_traffic, evidence=['Rain'], 
               evidence_card=[2]),
    TabularCPD(variable='Accident', variable_card=2, 
               values=cp_accident, evidence=['Traffic'], 
               evidence_card=[2])
)
assert model.check_model()
inference = VariableElimination(model)
query_result = inference.query(variables=['Accident'], evidence={'Rain': 1}) 
print("Probability of Accident given it is raining:")
print(query_result)
query_result_traffic = inference.query(variables=['Traffic'], evidence={'Accident': 1}) 
print("\nProbability of Traffic given there is an Accident:")
print(query_result_traffic)