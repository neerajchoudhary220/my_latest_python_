from kanren import run,Relation,facts,var
x= var()
capital = Relation()
facts(capital,("Homer","lisa"),("tata","abc"),("moms","Homer"))
result = run(1, x, capital(x, "Homer"))
print(result)