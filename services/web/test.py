from project.reinas import coloca_reinas
soluciones = [0,1,0,0,2,10,4,40,92,352,724,2680]

def test_soluciones():
    for i in range(len(soluciones)):
        aux = len(coloca_reinas(i))
        assert aux == soluciones[i]

def test_reina5():
    aux = len(coloca_reinas(5))
    assert aux == soluciones[5]

'''
Prueba que falla
def test_reina3():
    soluciones = [0,1,0,0,2,10,4,40,92,352,724,2680]
    aux = len(coloca_reinas(3))
    assert aux == soluciones[5]
'''
