# Web Scraping y las Bases de Datos Ofuscadas

Catedra de Universidad de Valencia con Capgemini

Taller: [https://github.com/jofaval/girls4stem-web-scraping](https://github.com/jofaval/girls4stem-web-scraping)

## Bases de Datos

### Diagrama de Flujo

```mermaid
flowchart LR
    A[Esquema]-->B[Ingesta de Datos]
    B-->C[Consulta de Datos]
    C---->D[Análisis de Datos]
```

## Web Scraping

### Básico

```mermaid
flowchart TD
    A[HTTP GET]-->|Consulta|B[Server devuelve HTML]
    B-->|Respuesta|C[Parseo del HTML]
    C-->|Búsqueda|D[Extracción de los datos]

    D-->E[XML]
    D-->F[xPath]
    D-->G[querySelector]

    E-->|Ingesta|H[Base de Datos]
    F-->|Ingesta|H
    G-->|Ingesta|H
```

clarifying
simplifying

### Headless

```mermaid
flowchart TD
    A[Iniciar headless browser]-->|Conexión|B[Entrar en la página]
    B-->|Servidor responde, el navegador sigue conectado|C[Server devuelve HTML]
    C-->|Carga de recursos e interpretación del JavaScript de la página|D[Headless browser interpreta el HTML]
    D-->|Clicar en ver más información, ver comentarios, etc.|E[Interacciones de usuario necesarias]
    E-->|Se obtiene el contenido deseado|F[Parseo del HTML]
    F-->|Se interpretan los datos|G[Extracción de los datos]

    G-->|Sigue navegando|E

    G-->|Búsqueda|H[XML]
    G-->|Búsqueda|I[xPath]
    G-->|Búsqueda|J[querySelector]

    H-->|Ingesta|K[Base de Datos]
    I-->|Ingesta|K
    J-->|Ingesta|K
```
