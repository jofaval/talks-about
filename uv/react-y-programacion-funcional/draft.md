programación funcional
template design pattern
react y hooks
lifecycle y rendercycle

jsx y multiples componentes en un mismo fichero
visualización y lógica
observers (señales de solid) y contexto
adaptar la charla de programación funcional, concepts of js

comentar también de pasada las clases
error boundary
proponer minitaller? no daría tiempo yo creo
librería o framework
- un framework trae opiniones y métodos/flujos de trabajo

// introducción e historia
1. landscape del desarrollo web antes
- fullstack
- php, java y jsps
1. mundo antes de angular
1. mundo antes de react
1. ¿qué es react?
- framework o librería
-- pregunta y luego responderla
- qué es un framework de frontend, qué se espera, expectativas
- qué es lo que nos ofrece
1. jsx
- cómo fue necesario al principio
- por qué hacía falta
- y qué había antes
- key
- namespaces
- muchos componentes un único fichero

// react
1. vDOM
- re-render
- million.js
- opt-in y opt-out de re-renders
- bucles y la key
-- por qué hacen falta las keys, optimizaciones dinámicas y estáticas del vDOM
1. lifecycle, (con clases?)
1. rendercycle
1. hooks
- lógica abstraida de la presentación
1. useState y useReducer
- estados, qué son
- qué es un reducer
- función de initialState
- cómo crear constantes que no se re-renderizan
1. useMemo y useCallback
- propósito que cumplen
- cuándo usar cada uno de ellos
- estado derivado
1. useEffect
- cómo funciona realmente
- bucle de dependencias
-- serialización
- bucle infinito
- useEffect no es un setter de estados
-- para eso ya existen los onChange
- edge cases
- lifecycle
- seguimiento de estados externos
1. Composition over inheritance
- qué entendemos por composición de componentes
- props drilling
1. contexto
- y observer
1. gestión de estado asíncrona
- react query
1. gestión de estado no asíncrona
- redux y rtk
-- flux y carlos azustre artículo
- react hooks y contexto vs useRef y observer
1. Estilos
- Scss/Sass
-- Módulos
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

crear un reto de todo-list, pero hacerlo outside-in, osease, dar la estructura final hecha, pero que se implemente todo lo necesario para hacerlo funcionar, sin pasar prácticamente props ni nada, la estructura mínima necesaria para que se entiendan cómo funcionan los componentes

hacer que los navs en verdad actúen de enlaces como corresponde
- tiempo de inversión para un detallito, pero que sería la leche la verdad
- y que el sidenav también funcione

memento, por lo de memo