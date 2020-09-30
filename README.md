# bitwise-operators-template

Este proyecto sirve para aprender los operadores a nive de bit y mostrar una referencia visual sin necesidad de una placa con LEDs

## Requisitos

* linux
* python3
* matplotlib


Para instalarlos desde linux, en una consola se puede hacer (sin escribir los $)
```
$ sudo apt update
$ sudo apt install python3 python3-matplotlib
```

## Descarga

Se puede descargar el proyecto clonando este repositorio haciendo (sin escribir los $)

```
$ git clone https://github.com/claudiojpaz/bitwise-operators-template.git
```

o descargando y descomprimiendo el proyecto desde [aquí][master]

[master]: https://github.com/claudiojpaz/bitwise-operators-template/archive/master.zip

## Uso

Una vez descomprimido o clonado, se ingresa al directorio, y si se cumplen todos los requisitos, se compila con
```
$ make
```
y eso crea un archivo `echo_byte` que se puede ejecutar con
```
$ ./echo_byte
```
El programa de ejemplo imprime en la pantalla un byte, bit a bit realizando una secuencia cada 500ms

Se puede visualizar usando python haciendo

```
$ ./echo_byte | python3 leds.py
```

En cualquier momento, haciendo foco en la pantalla de los LEDs y presionando la letra `q` se termina la ejecución

## Como probar otro código

Se puede editar el archivo `echo_byte.c` para probar otro código. Es necesario que se mantenga el `while(1)` con sus llaves y agregar el código a evaluar dentro.  
También es necesaria la línea `fflush(stdout);` ya que es usada por el script de python.  

La función `msleep` espera un valor en milisegundos que la aplicación se detiene, para posibilitar la visualización de los LEDs, valores menores a 20ms no permiten apreciar los cambios, se recomienda 500ms.

La función `integer2byte_rep` devuelve un entero pero solo compuesto de 0 o 1, representando un número en base binaria

```C class: lineNo
#include <stdio.h>
#include "timer.h"
#include "print_tools.h"

int main (void)
{
  unsigned char b = 1;

  while (1) {
    printf("%08u\n", integer2byte_rep(b)); // recomendado no borrar

    b <<= 1;
    if (b == 0)
      b = 1;

    msleep(500); // ms
    fflush(stdout); // no borrar
  }

  return 0;
}
```
