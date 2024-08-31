// solicitar el ingreso de dos números y 
// calcular cual es mayor o si tienen el mismo valor. 
// En cualquier caso, debes mostrar un mensaje 
// indicando cuál de los números es mayor, 
// por ejemplo, si ingresamos 5 y 8

// solicitar el ingreso de dos números
var numeroUno = parseInt(prompt("ingrese el primer número"));
var numeroDos = parseInt(prompt("ingrese el segundo número"));


//calcular cual es mayor o si tienen el mismo valor
if (numeroUno > numeroDos) {
    //funcion alert(), para ejecutar una ventana emergente con un mensaje o valor
    alert(`${numeroUno} es mayor que ${numeroDos}`);
} else if(numeroUno == numeroDos){
    alert(`${numeroUno} y ${numeroDos} Son iguales`);
} else {
    alert(`${numeroDos} es mayor que ${numeroUno}`);
}