# eight-queens-challenge
Proyecto para la resolución del Coding Challenge de las ocho reinas

## Ejecución del entorno 

Clonar el repositorio actual

Posicionarse en el directorio raíz del proyecto y ejecutar el siguiente comando:
```
docker-compose build
```

Ejecutar los servicios necesarios para el funcionamiento del proyecto:

```
docker-compose up
```
***

Para determinar la solución para un número de reinas igual a 8, basta con ingresar en su navegador en la siguiente URL:

http://localhost:5000/

Se puede acceder a otras soluciones por medio de la barra de navegación. O escribiendo el número de reinas a colocar, por ejemplo para obtener una configuracion de 9 reinas:

http://localhost:5000/resuelve/9

Para guardar todas las posibles soluciones en la base de datos, se debe acceder al siguiente enlace, especificando de igual forma el número de configuraciones deseadas:

http://localhost:5000/dbinsert/10

***

## Definición del problema

[Here's the programming problem](https://en.wikipedia.org/wiki/Eight_queens_puzzle)

These are the different aspect of the project you can work on (in order):
1. <del>Determine all possible solutions for a given N where N ≥ 8 (within 10 mins on a laptop). Bonus points for a higher N where N is the size of the board / number of queens</del>
2. <del>Iterate over N and store the solutions in postgres using SQLAlchemy</del>
3. Write basic tests that at least verify the number of solutions for a given N match what's git online. I recommend using pytest
4. <del>Docker-ize the solution, so that I can run the code and tests without any assumption of my local setup (including running a postgres instance in docker-compose)</del>
5. <del>Setup Travis CI (or similar) for your public GitHub repo to run the tests automatically</del>

**Please commit everything in a public GitHub repo and use python3.**

>  You don't need to go through all of the steps, but there should be instructions on how I can run the code. I mainly want to see how you approach a problem and your coding style. There are multiple steps so you have the option to show me different skills. It's up to you.

>  You can borrow from an existing solution—except for Google's. If you borrow from someone else's code, please cite where you got the code and be ready to explain how the code works.

---

## TO-DO:
- [x] Visual styles in boostrap
- [x] Work like an API
- [ ] Make images of solved chess board

