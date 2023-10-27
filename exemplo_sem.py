# pip install pyreadstat
# pip install semopy
# pip install graphviz


from semopy import Model, semplot, Optimizer
from semopy.inspector import inspect
from pandas import read_spss

data = read_spss("dados.sav")

mod = """
    SatisfTrab ~ Autonomia + Idade + Renda
    Renda ~ Autonomia
    Autonomia ~ Idade
    Renda ~ Idade
"""


model = Model(mod)
model.fit(data)


opt = Optimizer(model)
objective_function_value = opt.optimize()
print("inspect | \n",inspect(opt))


g = semplot(model, "pd2.png")
