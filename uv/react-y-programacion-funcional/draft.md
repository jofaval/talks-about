programaci�n funcional
template design pattern
react y hooks
lifecycle y rendercycle

jsx y multiples componentes en un mismo fichero
visualizaci�n y l�gica
observers (se�ales de solid) y contexto
adaptar la charla de programaci�n funcional, concepts of js

comentar tambi�n de pasada las clases
error boundary
proponer minitaller? no dar�a tiempo yo creo
librer�a o framework
- un framework trae opiniones y m�todos/flujos de trabajo

// introducci�n e historia
1. landscape del desarrollo web antes
- fullstack
- php, java y jsps
1. mundo antes de angular
1. mundo antes de react
1. �qu� es react?
- framework o librer�a
-- pregunta y luego responderla
- qu� es un framework de frontend, qu� se espera, expectativas
- qu� es lo que nos ofrece
1. jsx
- c�mo fue necesario al principio
- por qu� hac�a falta
- y qu� hab�a antes
- key
- namespaces
- muchos componentes un �nico fichero

// react
1. vDOM
- re-render
- million.js
- opt-in y opt-out de re-renders
- bucles y la key
-- por qu� hacen falta las keys, optimizaciones din�micas y est�ticas del vDOM
1. lifecycle, (con clases?)
1. rendercycle
1. hooks
- l�gica abstraida de la presentaci�n
1. useState y useReducer
- estados, qu� son
- qu� es un reducer
- funci�n de initialState
- c�mo crear constantes que no se re-renderizan
1. useMemo y useCallback
- prop�sito que cumplen
- cu�ndo usar cada uno de ellos
- estado derivado
1. useEffect
- c�mo funciona realmente
- bucle de dependencias
-- serializaci�n
- bucle infinito
- useEffect no es un setter de estados
-- para eso ya existen los onChange
- edge cases
- lifecycle
- seguimiento de estados externos
1. Composition over inheritance
- qu� entendemos por composici�n de componentes
- props drilling
1. contexto
- y observer
1. gesti�n de estado as�ncrona
- react query
1. gesti�n de estado no as�ncrona
- redux y rtk
-- flux y carlos azustre art�culo
- react hooks y contexto vs useRef y observer
1. Estilos
- Scss/Sass
-- M�dulos
- Tailwind
1. Solid.js
- opt-in re-render
- signals
1. Astro
1. Vue
- SFC -> Single File Component
1. Meta-Frameworks
- Next.js y Remix
- bling

crear un reto de todo-list, pero hacerlo outside-in, osease, dar la estructura final hecha, pero que se implemente todo lo necesario para hacerlo funcionar, sin pasar pr�cticamente props ni nada, la estructura m�nima necesaria para que se entiendan c�mo funcionan los componentes

hacer que los navs en verdad act�en de enlaces como corresponde
- tiempo de inversi�n para un detallito, pero que ser�a la leche la verdad
- y que el sidenav tambi�n funcione

memento, por lo de memo