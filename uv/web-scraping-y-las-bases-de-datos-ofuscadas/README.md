

    Bases de Datos, poniendo en situaci�n
        Definir un esquema (una estructura de los datos)
        Ingesta de datos (escritura/almacenamiento)
            Extracci�n de datos, de d�nde vienen?
                API
                IoT
                Explotaci�n (autogenerados de otros datos)
        Consulta de datos
            Objetivo final de los datos
            Warehouse y Lake, mencionar su existencia
        Vale, pero� �qu� son los datos?
            Google indexa las p�ginas, los sitios web tienen mucha informaci�n que se puede explotar ? Definici�n de a qu� se refieren
            Pir�mide del conocimiento, dato ? informaci�n ? conocimiento ? sabidur�a
        Bases de Datos Ofuscadas
            Similitudes entre una BDD y p�ginas que no proporcionan informaci�n amigablemente
    Web Scraping
        Lenguaje de marcas (HTML, XML)
        Pipeline
            Petici�n (request)
            Interpretaci�n (parser)
            Extracci�n (la chicha)
            ���Y ahora qu�???
                An�lisis
                Almacenamiento f�sico estructurado
                Alimentar una BDD
                etc
        Laboratorio, primeros pasos con web scraping
            Aqu� escoger�a unas pocas p�ginas webs que no den mucho problema al respecto
    Defensa ante ataques de Web Scraping
        Siendo el negocio con la p�gina, �qu� har�as para protegerte?
            Problemas de los �ataques�
                �Son maliciosos? no necesariamente
            robots.txt, tener respeto por la p�gina
        Problemas que causan el web scraping
            Escalabilidad, DDoS involuntario
            Competidores y la competencia del siglo XXI
            Throttling, agentes web
            Ofuscamiento (classnames, )
            Involuntariamente, frameworks y SPAs
        Laboratorio, problemas del web scraping en p�ginas modernas
            Amazon, Google im�genes, buscar�a m�s p�ginas como ejemplos
    Headless Web Scraping
        Qu� es un headless browser?
            Chromium
        �Qu� nos ofrece?
            Conexi�n ininterrumpida
            Simular un usuario
            Interactuar con la p�gina autom�ticamente
        �Por qu� lo necesitamos?
            Frameworks y SPAs
            Interactuar con la p�gina
                Siguiente p�gina de un resultado
                Filtrar por categor�as
                Contenido de un art�culo solo visible al hacer scroll
        Selenium, playwright, puppeteer
            Tambi�n usados para testing e2e
        Laboratorio, headless browser, la informaci�n a nuestro alcance
    Testing
        �Se puede testear el web scraping?
        E2E testing - End-to-End
            �Qu� es?
            �Qu� implicaciones tendr�amos en cuenta?
        �Nos hace falta?
            Los malos tests
            Mantenimiento de los tests
            Empresas dedicadas
        Ejemplos de bater�as de pruebas de web scraping
    Recapitulando
        Requisitos de una Bases de Datos
        Web Scraping y las Bases de Datos ofuscadas
        Headless Web Scraping
        Opciones profesionales de web scraping
            Scrapy
            BrightData
                https://www.youtube.com/watch?v=qo_fUjb02ns
                ?
                	
                Industrial-scale Web Scraping with AI & Proxy Networks
                Learn advanced web scraping techniques with Puppeteer and BrightData's scraping browser. We collect ecommerce data from sites like Amazon then analyze that data with ChatGPT. #javascript #datascience #chatgpt Get $10 Credit for BrightData https://get.brightdata.com/fireship Puppeteer Docs https://pptr.dev
                www.youtube.com
        Cr�ditos (har� por que sea una slide)


```mermaid
flowchart LR
    A[Esquema]-->B[Ingesta de Datos]
    B-->C[Consulta de Datos]
    C---->D[An�lisis de Datos]
```