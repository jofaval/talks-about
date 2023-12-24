# Lotería Nacional de Navidad

Puedes probar con el script para generarte nuevos números.
- puede generar tantos archivos como hagan falta

No vale hacer trampa y mirarlo a mano, pierde la gracia.

## Entrada

Recibes 100 números en un CSV, de cada número tienes:

- Número de lotería
- Número de décimos
- (Opcional) EUR/participación
    - Por defecto, 20

## Cómo averiguar si ha ganado un número

### Página web oficial

[Lotería Nacional de Navidad](...)

### Pagina de cada número

```
https://www.nacionalloteria.es/loteria-navidad/Comprobar-Loteria-Navidad.php?numero={numero_loteria}#comprobador
```

Evaluar las distintas páginas

**PISTA**: si la página es diferente que la de "No has ganado" es que tiene premio (y así no hace falta evaluar a mano todos los números :D)

### Formato del número

A fecha de escritura, n <= 99999, no tiene por qué tener left padding (12 pasaría 00012)

## Salida

Debes devolver (o insertar en BDD):

- Número de lotería
- Si ha ganado o no
    - 0 -> no
    - 1 -> sí
- Si ha ganado, cuánto por décimo
- Total ganado de este número

También interesa que, al final del programa, se anuncie:

- Dinero total jugado (num_decimo * participacion)
- Dinero total ganado (num_decimo * din_decimo)
- Balance total (total_ganado - total_jugado)