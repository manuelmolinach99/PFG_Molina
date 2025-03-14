# PFG_Molina
En este repositorio se incluyen los códigos que conforman el proyecto de fin de grado denominado "Técnicas de clasificación automática de gestos manuales para sujetos intactos y con amputación transradial"

En el informe del presente proyecto se explica en detalle cómo ejecutar todos los códigos de todas las secciones, excepto la última: Clasificación sobre datos de sujetos con amputación.
En lo que sigue se agrega la información necesaria para poder desarrollar la diferentes estrategias. 

Estrategia 1: 
1) Ejecutar generar_dataset_DB3 y generar los datos con la partición de datos por sujeto.
2) Ejecutar rnn_DB2, con la partición por sujeto, sin conjunto de test.
3) Ejecutar rnn_DB3, elegir partición por sujeto, y mandar todos los sujetos a test.
4) Generar las predicciones sobre test con el modelo entrenado sobre DB2.

Estrategia 2: 
1) Ejecutar generar_dataset_DB3 y generar los datos con la partición de datos por sujeto.
2) Ejecutar rnn_DB2, con la partición por sujeto, sin conjunto de test.
3) Ejecutar rnn_DB3, elegir partición por sujeto, conformar train, val y test.
4) Generar las predicciones sobre test con el modelo entrenado sobre DB2.

Estrategia 3: 
1) Ejecutar generar_dataset_DB3 y generar los datos con la partición de datos por sujeto.
2) Ejecutar rnn_DB3, eligiendo la partición de datos por sujeto, con conjunto de test.

Estrategia 4: 
1) Ejecutar generar_dataset_DB3 y generar los datos con la partición de datos por repetición, ya sea con normalización o no.
2) Ejecutar rnn_DB3, eligiendo la partición de datos por repetición, y fijando la variable sujeto_part en el numero del sujeto que se quiera usar para hacer los experimentos. No ejecutar ninguna celda de las secciones de Fine tuning ni optimización.

Estrategia 5:
1) Ejecutar generar_dataset_DB3 y generar los datos con la partición de datos por repetición, ya sea con normalización o no.
2) Ejecutar rnn_DB3, eligiendo la partición de datos por repetición, y fijando la variable sujeto_part en el numero del sujeto que se quiera usar para hacer los experimentos.
3) Ejecutar las celdas de fine tunning luego de ejecutar la celda que define la arquitectura del modelo.

