# Proposals

## Table of Talks

- [Programación Funcional: Modelo mental y determinismo programático](#programación-funcional-modelo-mental-y-determinismo-programático)
- [TypeScript: Primitivos, inferencias, genéricos y todo eso que te abruma](#typescript-primitivos-inferencias-genéricos-y-todo-eso-que-te-abruma)
- [Rendimiento en JavaScript: scripts, imágenes, imperativo vs declarativo (VSCode), bundling, optimizando para el event loop](#rendimiento-en-javascript-scripts-imágenes-imperativo-vs-declarativo-vscode-bundling-optimizando-para-el-event-loop)
- [Event Loop y asincronía: el core de JavaScript](#event-loop-y-asincronía-el-core-de-javascript)
- [Hay pocos frameworks de JS… ¿y si creamos uno?](#hay-pocos-frameworks-de-js-¿y-si-creamos-uno)
- [¿Por qué, a pesar de todo, JavaScript funciona?](#¿por-qué-a-pesar-de-todo-javascript-funciona)
- [Una historia de validadores y terraformadores: Crea tu propia CLI con Node](#una-historia-de-validadores-y-terraformadores-crea-tu-propia-cli-con-node)
- [Cómo funcionan los bundlers](#cómo-funcionan-los-bundlers)
- [Cómo evoluciona JavaScript y el proceso de specs (TC39)](#cómo-evoluciona-javascript-y-el-proceso-de-specs-tc39)
- [Runtimes, bundlers, node: los pilares ocultos de JavaScript](#runtimes-bundlers-node-los-pilares-ocultos-de-javascript)
- [StackTrace, v8, Ecmascript, runtime](#stacktrace-v8-ecmascript-runtime)

## Programación Funcional: Modelo mental y determinismo programático

La mayoría de los recursos disponibles hablan en un lenguaje esotérico, a veces indescifrable. Pero los conceptos de Programación Funcional, y su propósito, nos ayudan a diseñar software más legible (siempre que los apliquemos con cabeza).

Veremos el qué, cómo, por qué y para qué de la Programación Funcional desde un enfoque basado en su modelo mental, hablaremos de pureza, efectos secundarios, idempotencia. Trataremos patrones y code smells funcionales para identificar las piedras en el camino de un código más legible y determinístico.

Y una vez hayamos comprendido la base de la Programación Funcional, la corromperemos con gestión de estado y máquinas de estado finitas.

## TypeScript: Primitivos, inferencias, genéricos y todo eso que te abruma

Usamos TypeScript en los proyectos como quien usa oxígeno, pero apenas estamos rascando la superficie de todo lo que tiene por ofrecernos. TypeScript no es solamente una librería para tipar propiedades, es un sistema de tipados integral. Y eso es en lo que profundizaremos en esta charla.

Veremos cómo crear tipos adaptativos, delegar a los casos de uso la especificación. Cruzaremos TypeScript con la Developer Experience. Tras todo el contenido empezarás a comprender como tipos complejos, basados en inferencias, recursividad y otras triquiñuelas, funcionan.

Tras esta charla ya no te impodrán tanto conceptos como genéricos, inferencia y literales dinámicos. Algunos de los conocimientos que abordaremos son:

- Sistemas de tipados, Hindley-Milner
- JavaScript, typeof y primitivos
- JSDoc y cuándo puede venirnos bien
- Inferencias y genéricos

... ¡no te quedes con las ganas y únete nuestra aventura!

## Rendimiento en JavaScript: scripts, imágenes, imperativo vs declarativo (VSCode), bundling, optimizando para el event loop

Nuestro trabajo es desarrollar software, y eso hacemos, pero... ¿lo que estamos haciendo es eficiente? Nos encanta resolver retos y tenemos la suerte de que ese sea neustro trabajo. Pero no siempre le prestamos haciendo a cómo llega esa solución, de la experiencia en rendimiento. Y aunque le prestemos atención, los recursos o son un dolor de cabeza o apenas existen. Y no todo el rendimiento es BigO y si no podemos pasar de un array a un set ya hemos perdido la guerra

Profiling, rendimiento, bundling, event loop son conceptos del mundo JavaScript que nos ayudan a abordar estos problemas, son nuestras herramientas para hacerle frente a una mala experiencia de usuario y a la mala conexión a internet (que a veces también nos quedamos sin datos y queremos seguir navegando). Para que la frustación sea mejor, vamos a adentrarnos en todos estos conceptos, cómo se integran en nuestras aplicaciones y cómo, web masters, frontends o backends, podemos aprovecharlo.

Únete a este viaje para comprender conceptos de desarrollo de software, navegadores, optimizaciones obtusas y cómo mejorar la experiencia de usuario optimizando la carga inicial... y no consumiéndole todos los datos innecesariamente :D. Veremos también casos de éxito como VSCode, optimizaciones para páginas estáticas y el temido event loop.

## Event Loop y asincronía: el core de JavaScript

A más tiempo lleves en el ecosistema de JavaScript, más probable es que hayas escuchado hablar del temido Event Loop, mencionado en entrevistas, a veces sale incluso en StackOverflow pero... ¿qué es el Event Loop? ¿qué propósito cumple? Si desarrollas software a través de framework, ¿te beneficia comprenderlo? Por otro lado, gestionamos peticiones, pero ¿realmente estamos comprendiendo la Programación Asíncrona?

Pues vamos a adentrarnos en todas esas preguntas y más, comprenderemos qué es el Event Loop, qué lo compone, para qué se usa dentro de JavaScript. Y una vez lo hayamos comprendido, abordaremos la Programación Asíncrona (enfocada a JavaScript). Con estos conceptos serás capaz de comprender algunas de las rarezas de JavaScript y podrás orquestar procesos con total confianza de lo que ocurrirá por detrás.

Desarrolles con Node, TypeScript o algún Framework, ahora podrás orquestar cargas y gestionar procesos siendo consciente de lo que estás haciendo, y gracias al modelo mental del Event Loop, podrás anticiparte a comportamientos extraños de esos que abruman y te hacen perder horas.

## Hay pocos frameworks de JS… ¿y si creamos uno?

Todas las ofertas de JavaScript ahora mismo están orientadas a frameworks concretos, da igual si desarrollas en Frontend o Backend, los frameworks están a la orden del día y han venido para quedarse. Pero ¿realmente comprendemos qué es un framework? No es necesario para el día a día, pero comprender todo lo que nos ofrece y qué decisiones han tomado puede ayudarnos a maximizar mejor todo lo que nos da.

En esta sesión vamos a ver qué compone un framework, las decisiones y su evolución, adopción de modelo mental, canaries. Veremos cómo podríamos crear nuestro propio framework de JavaScript y a qué retos nos enfrentaríamos en la aventura. Si alguna vez has sentido curiosidad por comprender JavaScript más allá del día a día... ¡¡esta es tu charla!!

## ¿Por qué, a pesar de todo, JavaScript funciona?

JavaScript es... raro, falla pero no cierra el navegador, a veces cuando falla ni si quiera te informa. Está en constante evolución y aún así las aplicaciones de más de 20 años siguen ejecutándose como si nada... ¿por qué? Vamos a detenernos y mirar hacia atrás. Hablaremos de cómo ha evolucionado el sistema y el lenguaje. Abordaremos ECMAScript, navegadores, runtimes, web APIs, Strict mode opt-in, retrocompatibilidad by design, tipado dinámico, prototipos

Si alguna vez has tenido curiosidad por saber todo lo que rodea a JavaScript y no es el código, está es tu oportunidad de tener una visión más horizontal, ¡no la dejes pasar!

## Una historia de validadores y terraformadores: Crea tu propia CLI con Node

A veces tenemos que cambiar estructuras de directorios, nos juntamos como equipo y vemos que la dirección en la que estamos evolucionando con el proyecto requiere nuevas nomenclaturas, cambiar el criterio por el que organizamos nuestro código. Pero claro, qué hacemos con todo lo que hemos trabajado hasta ahora...

Fitness functions, podemos crear nuestra propia CLI para terraformar nuestro código, y usar el terraformador para validar que nuestro código está siguiendo los nuevos estándares que hemos acordado. La última resulta crucial porque los viejos hábitos se mantienen con fuerza. Para ello, veremos cómo crear tu propia CLI con Node para terraformar tu codebase y lo abordaremos con conceptos de terraformación y validación

## Cómo funcionan los bundlers

Empiezas un proyecto y te dicen que configures Webpack o Babel... si eres como yo no sabes ni por dónde empezar, buscas configuraciones para copiar y pegarlas y cruzas los dedos para que te funcione la primera, con suerte funciona. Pero ¿por qué estamos usando bundlers? Si total, lo que queremos es desarrollar, no configurar.

Los bundlers son la piedra angular de los frameworks actuales, son casi el motor que hace que nuestras aplicaciones con un alto nivel de complejidad lleguen al navegador tal y como corresponde sin que tengamos que plantearnos scripts, cargas, optimizaciones, ofuscar, etc. Un bundler es nuestro traductor para entendernos con los navegadores y que nuestras soluciones funcionen tal y como esperamos

Tras esta charla vas a comprender qué son los bundlers, que trabajo hacen en nuestro nombre y las complejidades de los navegadores para que tu toolbelt sea más completo

## Cómo evoluciona JavaScript y el proceso de specs (TC39)

JavaScript es un lenguaje muy curioso y especial, es único en su especie, pues no tiene una única implementación, es más, el consejo que hace que JavaScript avance, no proporciona nada de código al respecto... "solo" trabaja son specs... y ¿qué son las specs? Especificaciones, JavaScript es un estándar para navegadores, un lenguaje común y universal para interactuar con el DOM y con distintos sistemas operativos, como tal, TC39/EcmaScript proporciona una guía del requisito funcional y no funcional que se espera que cumpla. Si te está pareciendo interesante, ¡¡pásate por la charla para saber más!!

## Runtimes, bundlers, node: los pilares ocultos de JavaScript

Runtimes, empaquetar el código, configurar node, de un `<script src="" />` a todo lo que ha evolucionado el sistema. Podemos hacer soluciones increíbles con una facilidad que nunca antes hemos tenido. Vamos a ver cómo funciona toda esa magia.

Indagaremos en runtimes, bundlers, ¿por qué existe node? saber cómo se integran tecnologías con propósitos tan diferentes nos puede ayudar a prevenir problemas son soluciones que se adapten al entorno para el que estamos diseñando nuestra solución. Usa estos conocimientos a tu disposición, adquiere confianza y siéntete más en control del entorno en el que trabajas, porque JavaScript no es sólamente JavaScript

## StackTrace, v8, Ecmascript, runtime

JavaScript tiene muchos conceptos que abruman, StackTrace, Event Loop, Node utiliza v8 como runtime engine, desarrollo JavaScript ¿pero es ECMAScript? Vamos a darle luz a todos estos conceptos y los desgranaremos para que te sean tan familiares como una variable, al fin y al cabo, ya los has usado de una manera u otra.

Únete para descubrir que son los runtime engines, cómo funciona el event loop, qué es ECMAScript en realidad y cómo te impacta en el día a día. En esta charla veremos conceptos que aportarán valor tanto a principiantes como a aquellas personas que ya lleven recorrido en el universo JavaScript. ¡No te quedes con la duda!
