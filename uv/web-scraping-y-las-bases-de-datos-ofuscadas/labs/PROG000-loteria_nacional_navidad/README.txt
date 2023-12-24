# Loter�a Nacional de Navidad

Puedes probar con el script para generarte nuevos n�meros.
- puede generar tantos archivos como hagan falta

No vale hacer trampa y mirarlo a mano, pierde la gracia.

## Entrada

Recibes 100 n�meros en un CSV, de cada n�mero tienes:

- N�mero de loter�a
- N�mero de d�cimos
- (Opcional) EUR/participaci�n
    - Por defecto, 20

## C�mo averiguar si ha ganado un n�mero

### P�gina web oficial

[Loter�a Nacional de Navidad](...)

### Pagina de cada n�mero

```
https://www.nacionalloteria.es/loteria-navidad/Comprobar-Loteria-Navidad.php?numero={numero_loteria}#comprobador
```

Evaluar las distintas p�ginas

**PISTA**: si la p�gina es diferente que la de "No has ganado" es que tiene premio (y as� no hace falta evaluar a mano todos los n�meros :D)

### Formato del n�mero

A fecha de escritura, n <= 99999, no tiene por qu� tener left padding (12 pasar�a 00012)

## Salida

Debes devolver (o insertar en BDD):

- N�mero de loter�a
- Si ha ganado o no
    - 0 -> no
    - 1 -> s�
- Si ha ganado, cu�nto por d�cimo
- Total ganado de este n�mero

Tambi�n interesa que, al final del programa, se anuncie:

- Dinero total jugado (num_decimo * participacion)
- Dinero total ganado (num_decimo * din_decimo)
- Balance total (total_ganado - total_jugado)