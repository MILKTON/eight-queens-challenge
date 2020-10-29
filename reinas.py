def tablero_valido(tablero, renglon, columna):
    """
    Parameters
    ----------
    tablero : list
        Lista de las posicion actual de las piezas
    columna : int
        Valor correspondiente a la columna actual
    renglon: int 
        Valor correspondiente al renglon actual
    Returns
    -------
    bool : bool
        Valor que determina si la posicion fue valida
    """
    mismo_renglon = renglon not in tablero
    diagonales_validas = True
    for i in range(0, columna):
        # Verificando la diagonal inferior ↗
        if tablero[i] - i == renglon - columna:
            diagonales_validas = False
            break
        # Verificando diagonal superior ↙
        if tablero[i] + i == renglon + columna:  
            diagonales_validas = False
            break
    return mismo_renglon and diagonales_validas

def resolverNReinas(tablero,columna,soluciones,tam_tablero):
    """
    Parameters
    ----------
    tam_tablero : int
        Numero de reinas a colocar / tamaño del tablero
    tablero : list
        Lista de las posicion actual de las piezas
    columna : int
        Valor correspondiente a la iteracion en cuestion
    soluciones: int 
        Lista de soluciones parciales
    Returns
    -------
    solucion list<list:int>
        Lista que contiene listas con las posiciones validas de las reinas
    """
    if columna >= tam_tablero:
        return soluciones

    for renglon in range(0, tam_tablero):
        if tablero_valido(tablero, renglon, columna):
            tablero[columna] = renglon
            if -1 not in tablero:
                soluciones.append(tablero)
            resolverNReinas(tablero.copy(), columna + 1, soluciones, tam_tablero)
    return soluciones

def coloca_reinas(tam_tablero):
    """
    Funcion encargada de ejecutar la logica del programa
    Parameters
    ----------
    tam_tablero : int
        Numero de reinas a colocar / tamaño del tablero
    Returns
    -------
    solucion list<list:int>
        Lista que contiene listas con las posiciones validas de las reinas
    """
    solucion_temp = [-1] * tam_tablero
    soluciones = resolverNReinas(solucion_temp, 0, [], tam_tablero)
    return soluciones
