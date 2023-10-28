# pip install pyreadstat
# pip install semopy
# pip install graphviz


from semopy import Model, semplot, Optimizer
from semopy.inspector import inspect
from pandas import read_spss

def main(model_text = None):
    path = "PATH_Aula.sav"
    data = read_spss(path)

    
    print(model_text)
    #mod = "SatisfTrab~Autonomia+Idade+Renda Renda~Autonomia Autonomia~Idade  Renda~Idade"
    mod = """
        SatisfTrab ~ Autonomia + Idade + Renda
        Renda ~ Autonomia
        Autonomia ~ Idade
        Renda ~ Idade
    """

    # if se o modelo for passado como parametro
    if model_text:
        mod = model_text

    model = Model(mod)
    model.fit(data)


    opt = Optimizer(model)
    objective_function_value = opt.optimize()
    print("inspect | \n",inspect(opt))


    g = semplot(model, "imagem_saida.png")


if __name__ == '__main__':
    main()