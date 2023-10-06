from generatemodel import model


result = model.Generate('bootstrap.csv',10,'bootsvocab','bootsmodel').ModelCreateProcess()
print(result)
