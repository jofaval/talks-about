# Proposals

## Table of Talks

- [Git sin morir en el intento](#git-sin-morir-en-el-intento)
- [Web Scraping y las Bases de Datos ofuscadas](#web-scraping-y-las-bases-de-datos-ofuscadas)
- [Arquitecturas Front: Más allá de la estructura de ficheros](#arquitecturas-front-más-allá-de-la-estructura-de-ficheros)
- [Programación Funcional: Modelo mental y determinismo programático](#programación-funcional-modelo-mental-y-determinismo-programático)
- [TypeScript: Primitivos, inferencias, genéricos y todo eso que te abruma](#typescript-primitivos-inferencias-genéricos-y-todo-eso-que-te-abruma)
- [Una historia de terraformadores y validadores](#una-historia-de-terraformadores-y-validadores)
- [Headless UI: Componentes flexibles sin calentarse la cabeza](#headless-ui-componentes-flexibles-sin-calentarse-la-cabeza)

## Git sin morir en el intento

Git es nuestro pan de cada día, pero... a veces parece que no sabemos lo que estamos comiendo.

Veremos el modelo mental de Git de una manera diferente y cercana para ayudarte a entender por qué funcionan las cosas como funcionan y que la herramienta que usas día a día se convierta en tu mayor aliada. Sé la persona que mejor conoce Git de tu equipo, y piérdele el miedo a los comandos.

Syllabus:

- modelo mental
- workingTree, workingCopy, staging, unstaged
- commits, ramas, repository y remote
- merge, rebase y cherry-pick
- ...y mucho más

A lo largo de la charla irás familiarizándote con los comandos hasta perderles el miedo, y entenderás algunas casuísticas del día a día de una manera más clara. ¿Qué diferencias hay entre un merge y un rebase? ¿qué incluye un commit? ¿por qué tengo que hacer pull después de un amend? ¡Acompáñame en este viaje!

## Web Scraping y las Bases de Datos ofuscadas

Vivimos en un mundo plagado de datos, "Ahora todo es datos" dicen... ¿cómo se extraen estos datos? ¿cómo están compitiendo las empresas entre sí?. Exploraremos el poder de los datos, la pirámide del conocimiento, la ética en juego y el impacto de la competencia entre las grandes empresas. Comprenderemos cómo hoy en día las bases de datos son públicas... pero puñeteras.

También veremos cómo estas técnicas, con más impacto del que somos conscientes en nuestro día a día, nos pueden ayudar a organizarnos mejor, crear alertas personalizadas y (re)descubrir el funcionamiento de algunos de los procesos esenciales para internet.

## Arquitecturas Front: Más allá de la estructura de ficheros

Frontend, el gran olvidado del desarrollo de software, tiene que resolverlo todo a la vez y sin embargo, los recursos de arquitectura de Front te hablan de reestructurar tu codebase o cómo evitar el polling... sin profundizar en todo lo que da de sí la Arquitectura de Front.

¿Qué es la Arquitectura de Front? Es aplicar los Conceptos de Arquitectura de Software al mundo Frontend. Siguiendo estos conceptos y fundamentos podremos gestionar la complejidad en nuestras aplicaciones, mejorar la mantenibilidad y evolucionar nuestro código base desde un enfoque más determinista.

Porque con una buena Arquitectura Front contribuiremos a mejorar la Developer Experience (DevEx) de nuestro equipo, sin importar si eres Individual Contributor, Líder, Manager, etc.

¡Únete a este viaje! Abordaremos temas como:

- La separación entre feature y plataforma
- Desarrollo por componente (de arquitectura) para construir aplicaciones mínimamente acopladas
- Diseño de estrategias de plataforma que habiliten equipos a desarrollar necesidades de producto
- Cómo visualizar arquitecturas Frontend, documentarlas y democratizar las decisiones de arquitectura

## Programación Funcional: Modelo mental y determinismo programático

La mayoría de los recursos disponibles hablan en un lenguaje esotérico, a veces indescifrable. Pero los conceptos de Programación Funcional, y su propósito, nos ayudan a diseñar software más legible (siempre que los apliquemos con cabeza).

Veremos el qué, cómo, por qué y para qué de la Programación Funcional desde un enfoque basado en su modelo mental, hablaremos de pureza, efectos secundarios, idempotencia. Trataremos patrones y code smells funcionales para identificar las piedras en el camino de un código más legible y determinístico.

Y una vez hayamos comprendido la base de la Programación Funcional, la corromperemos con gestión de estado y máquinas de estado finitas.

## TypeScript: Primitivos, inferencias, genéricos y todo eso que te abruma

Usamos TypeScript en los proyectos como quien respira oxígeno, pero apenas estamos rascando la superficie de todo lo que tiene por ofrecernos. TypeScript no es JavaScript con tipos, es un lenguaje de programación en sí mismo. Y eso es en lo que profundizaremos en esta charla.

Veremos cómo crear tipos adaptativos, delegar a los casos de uso la especificación. Cruzaremos TypeScript con la Developer Experience. Tras todo el contenido empezarás a comprender cómo, tipos complejos, basados en inferencias, recursividad y otras triquiñuelas, funcionan.

Tras esta charla ya no te impondrán tanto miedo conceptos como genéricos, inferencia y literales dinámicos. Algunos de los conocimientos que abordaremos son:

- Sistemas de tipados, Hindley-Milner
- JavaScript, typeof y primitivos
- JSDoc y cuándo puede venirnos bien
- Inferencias y genéricos

... ¡no te quedes con las ganas y únete a nuestra aventura!

## Una historia de terraformadores y validadores

A veces tenemos que cambiar estructuras de directorios, nos juntamos como equipo y vemos que la dirección en la que estamos evolucionando con el proyecto requiere nuevas nomenclaturas, cambiar el criterio por el que organizamos nuestro código. Pero claro, qué hacemos con todo lo que hemos trabajado hasta ahora...

Fitness functions, podemos crear nuestra propia CLI para terraformar nuestro código, y usar el terraformador para validar que nuestro código está siguiendo los nuevos estándares que hemos acordado. La última resulta crucial porque los viejos hábitos se mantienen con fuerza. Para ello, veremos cómo crear tu propia CLI con Node para terraformar tu codebase y lo abordaremos con conceptos de terraformación y validación

## Headless UI: Componentes flexibles sin calentarse la cabeza

No ha habido una manera concreta y establecida de desarrollar UI, es más, me atrevería a decir que es la parte más cambiante respecto a patrones, buenas prácticas y librerías. A lo largo de su historia han surgido distintas filosofías y librerías, pero todas con un elemento en común. Tienes que adaptarte o sobreescribir cientos de estilos previos.

¡Not anymore! Headless UI es una manera más elegante de atajar ese problema de raíz, ahora es la librería la que se adapta a tus necesidades, y todo gracias al uso de frameworks más modernos como React, Vue, Solid. Esta charla será un breve repaso sobre la historia de UIs, matices de DDD y el recordatorio práctico de que Composición es preferible por encima de Herencia.

De esta charla saldrás con una idea de cómo aliviar algunos problemas de adaptabilidad en tus proyectos de Front, y detectarás lo que hace a algunas librerías más costosas de implementar. Las buenas prácticas no son sólo cosa de Back
