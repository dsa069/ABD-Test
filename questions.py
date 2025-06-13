# Cuestionario sobre Bases de Datos
questions = [
    #Exámen 22/23-2014
    {
        "question": "¿Qué determina el tamaño inicial de un Tablespace en Oracle?",
        "options": ["La cláusula INITIAL de la sentencia CREATE TABLESPACE.", 
                   "La cláusula MINEXTENTS de la sentencia CREATE TABLESPACE.", 
                   "La suma de las cláusulas INITIAL y NEXT de la cláusula CREATE TABLESPACE.", 
                   "La suma de los tamaños de todos los ficheros de datos especificados en la sentencia CREATE TABLESPACE."],
        "correct": 3
    },
    {
        "question": "En la siguiente sentencia creamos la tabla DEPARTAMENTOS:\nCREATE TABLE departamentos (Id NUMBER(4), Nombre VARCHAR2(30), Responsable_id NUMBER(4)) STORAGE (INITIAL 200K NEXT 200K PCTINCREASE 50 MINEXTENTS 1 MAXEXTENTS 7) TABLESPACE data;\n¿Cuál es el tamaño definido para la cuarta extensión?",
        "options": ["300K", "450K", "675K", "Ninguna de las anteriores es correcta"],
        "correct": 1
    },
    {
        "question": "En la siguiente sentencia creamos la tabla DEPARTAMENTOS:\nCREATE TABLE departamentos (Id NUMBER(4), Nombre VARCHAR2(30), Responsable_id NUMBER(4)) STORAGE (INITIAL 200K NEXT 200K PCTINCREASE 50 MINEXTENTS 1 MAXEXTENTS 7) TABLESPACE data;\n¿Cuál es el tamaño definido para la tercera extensión?",
        "options": ["300K", "450K", "675K", "Ninguna de las anteriores es correcta"],
        "correct": 0
    },
        {
        "question": "En la siguiente sentencia creamos la tabla DEPARTAMENTOS:\nCREATE TABLE departamentos (Id NUMBER(4), Nombre VARCHAR2(30), Responsable_id NUMBER(4)) STORAGE (INITIAL 200K NEXT 200K PCTINCREASE 50 MINEXTENTS 1 MAXEXTENTS 7) TABLESPACE data;\n¿Cuál es el tamaño definido para la quinta extensión?",
        "options": ["300K", "450K", "675K", "Ninguna de las anteriores es correcta"],
        "correct": 2
    },
    {
        "question": "Tenemos este conjunto de tablas, con las claves primarias subrayadas:\nAlumno ([NIF], Nombre, Fecha_nacimiento, Titulación)\nNota([NIF], [Codigo],[Fecha], Calificación)\nAsignatura([Codigo], Nombre, Créditos)\nTitulación([Titulación], Centro, Año_implantación)\nAplicando ingeniería inversa para obtener el esquema conceptual, podemos decir que",
        "options": ["Asignatura es un conjunto de entidades débil", 
                "Existe una relación uno a uno entre Alumno y Titulación", 
                "Nota es un conjunto de entidades fuerte con una agregación", 
                "Hay un conjunto de entidades débil en el esquema obtenido"],
        "correct": 3
    },
    {
        "question": "Tenemos este conjunto de tablas, con las claves primarias subrayadas:\nAlumno ([NIF], Nombre, Fecha_nacimiento, Titulación)\nNota([NIF], [Codigo],[Fecha], Calificación)\nAsignatura([Codigo], Nombre, Créditos)\nTitulación([Titulación], Centro, Año_implantación)\nAplicando ingeniería inversa para obtener el esquema conceptual, podemos decir que",
        "options": ["Asignatura es un conjunto de entidades débil", 
                   "Existe una relación uno a uno entre Alumno y Titulación", 
                   "Nota es un conjunto de 100% entidades débil dependiente de una agregación", 
                   "Nota es un conjunto de entidades fuerte con una agregación",
                   "No hay ningún conjunto de entidades débil en el esquema obtenido",
                   "Hay un conjunto de entidades débil en el esquema obtenido"],
        "correct": [2, 5],
        "type": "multiple"
    },
    {
        "question": "Tenemos que estimar el espacio ocupado por los datos de una base de datos que tiene 1.000.000 de registros actualmente y un crecimiento del 15 % anual a cinco años vista. Cada registro tiene 20 bytes de cabecera y 240 bytes de datos. Cada bloque tiene una cabecera de 64 bytes y un pie de página de 128 bytes. El grado de llenado del fichero es del 80%. Si el tamaño de bloque es de 512 bytes, podemos decir que:",
        "options": ["No cabe ni un registro en cada bloque", 
                   "Caben dos registros en cada bloque", 
                   "No sabemos cuantos registros van a caber en un bloque", 
                   "El archivo ocupará más de un gigabyte"],
        "correct": 0
    },
    {
        "question": "Tenemos que estimar el espacio ocupado por los datos de una base de datos que tiene 2.000.000 de registros actualmente y un crecimiento del 10 % anual a cuatro años vista. Cada registro tiene 20 bytes de cabecera y 240 bytes de datos. Cada bloque tiene una cabecera de 64 bytes y un pie de página de 128 bytes. El grado de llenado del fichero es del 80%. Si el tamaño de bloque es de 512 bytes, podemos decir que:",
        "options": ["Caben dos registros en cada bloque", 
                   "No sabemos cuántos registros van a caber en un bloque", 
                   "Solo cabe un registro en cada bloque", 
                   "El archivo ocupará más de un gigabyte"],
        "correct": 2
    },
    {
        "question": "Al integrar tres subesquemas de bases de datos, tenemos el conjunto de entidades Cliente/Persona en los tres.\n- En uno de ellos, la clave es NIF.\n- En el segundo, la clave es Identificador.\n- En el tercero, la clave es Id.\nPodemos decir que:",
        "options": ["Esto no supone ningún conflicto", 
                   "Es un conflicto de nombres", 
                   "Es un conflicto de nombres y de clave", 
                   "Es un conflicto de clave"],
        "correct": 2
    },
    {
        "question": "Cuales de la siguientes afirmaciones son ciertas respecto a las estructuras de almacenamiento de una BD ORACLE.",
        "options": ["Un tablespace puede manejar varios archivos de datos (datafiles).", 
                   "Un segmento puede abarcar varios archivos de datos.", 
                   "Un segmento puede pertenecer a varios tablespaces.", 
                   "Un segmento puede abarcar varios bloques de datos."],
        "correct": [0, 3],
        "type": "multiple"
    },
    {
        "question": "En una situación donde se ha producido un fallo del sistema que no ha producido daños en la BD, ¿qué se utilizaría en el proceso de recuperación?.",
        "options": ["Copias de seguridad y fichero log.", 
                   "Fichero log para deshacer y rehacer Transacciones.", 
                   "Rollback de la Transacción.", 
                   "Sólo copia de Seguridad con pérdida de Ultimas Transacciones."],
        "correct": 1
    },
    {
        "question": "Se ha ejecutado la siguiente sentencia SQL para crear una nueva cuenta de usuario: CREATE USER maria IDENTIFIED BY maria TEMPORARY TABLESPACE temp_tbs QUOTA 1M ON system QUOTA UNLIMITED ON data_tbs PROFILE apps_profile PASSWORD EXPIRE DEFAULT ROLE apps_dev_role;\n¿Por qué esta sentencia devuelve un error?",
        "options": ["No se puede asignar un rol a un usuario dentro de la sentencia CREATE USER.", 
                   "No se puede asignar un perfil a un usuario dentro de la sentencia CREATE USER.", 
                   "No se puede especificar la cláusula PASSWORD EXPIRE dentro de la sentencia CREATE USER.", 
                   "No se puede conceder al usuario cuota ilimitada dentro de la sentencia CREATE USER."],
        "correct": 0
    },
    {
        "question": "¿Qué sentencia se utilizaría para habilitar el rol dep_role?",
        "options": ["SET ROLE dep_role", 
                   "CREATE ROLE dep_role", 
                   "ENABLE ROLE dep_role", 
                   "SET ENABLE ROLE dep_role"],
        "correct": 0
    },
    #----Pregunta de ordenar
    {
        "question": "Ordena las siguientes estructuras por orden de jerarquía, comenzando con la Base de Datos",
        "options": ["Tablespace, Extensión, Segmento, Fila, Base de Datos, Bloque", 
                   "Base de Datos, Tablespace, Segmento, Extensión, Bloque, Fila", 
                   "Bloque, Extensión, Segmento, Fila, Tablespace, Base de Datos", 
                   "Base de Datos, Bloque, Segmento, Extensión, Tablespace, Fila"],
        "correct": 1
    },
    # Examen 2016
    {
        "question": "En el SGBD Oracle. ¿Cuál de las siguientes afirmaciones es correcta?",
        "options": ["Los usuarios con el rol de administrador de la base de datos son SYS, SYSTEM y cualquier otro usuario al que se le haya otorgado el rol DBA (Data Base Administrator).",
                   "Un esquema es una colección de usuarios que contienen objetos de este tipo.",
                   "Un usuario puede modificar el diccionario de datos de los objetos de su esquema.",
                   "Si una instancia de base de datos se encuentra en una máquina UNIX y los clientes de bases de datos, es decir, los usuarios o aplicaciones se conectan a ella con un único usuario, pero desde máquinas UNIX, LINUX y WINDOWS entonces el administrador de la base de datos definirá este usuario de conexión o usuario de Bases de Datos como 'externo'."],
        "correct": 0
    },
    {
        "question": "Los privilegios en el SGBD Oracle son. ¿Cuál de las siguientes afirmaciones es correcta?",
        "options": ["Permisos que se dan a los usuarios tanto sobre objetos del esquema como sobre el sistema. Estos privilegios, se dan también a los perfiles (\"profiles\").",
                   "Son tanto privilegios de sistema, como privilegios de objetos de esquema. Estos son asignados a roles y a usuarios.",
                   "Permisos que son manejados a través de los perfiles para limitar el uso de la CPU y para definir políticas sobre la contraseña (caducidad, complejidad de ésta, etc.)",
                   "Son un conjunto de permisos agrupados sobre los objetos de la base de datos que simplifican la gestión de la base de datos. En ningún caso se trata de permisos sobre el sistema."],
        "correct": 1
    },
    {
        "question": "En el procesamiento de una consulta SQL en el SGBD Oracle. ¿Cuál de las siguientes afirmaciones es correcta?",
        "options": ["El SGBD ofrece un mecanismo para optimizar el procesamiento de una consulta u optimizador, cuyo objetivo es minimizar los tiempos de respuesta.",
                   "El resultado de aplicar el optimizador de un SGBD es independiente de cómo este codificada la consulta previamente por el usuario.",
                   "El resultado de aplicar el optimizador de un SGBD depende únicamente de la evaluación de la carga sobre los recursos del sistema.",
                   "El optimizador del SGBD tiene como objetivo minimizar la carga de recursos al sistema."],
        "correct": 0
    },
    {
        "question": "En una empresa donde se utiliza ORACLE como SGBD, ha ocurrido un error de sistema que ha dañado los ficheros de datos (datafiles) de la BD, pero no a los ficheros log (redo log). Por la política de backup y recuperación llevada a cabo, se tienen copias de todos los ficheros esenciales de la Base de Datos en otro lugar seguro, y además existe sin daños un backup físico realizado diez horas antes del incidente. ¿Cuál de las siguientes afirmaciones es cierta?",
        "options": ["No es posible hacer un proceso de recuperación completo utilizando el backup físico y los ficheros redo log.",
                   "Al no disponer de backup lógicos, no se puede hacer un proceso de recuperación completo.",
                   "Tenemos un backup físico anterior al fallo de sistema, entonces se podría hacer un proceso de recuperación junto los ficheros log, pero sería incompleto con pérdida de información.",
                   "Si la BD se puede parar, se podrían sustituir los ficheros esenciales de la BD por los duplicados externos en el lugar seguro. Posteriormente se ha de levantar la BD, realizando así un proceso de recuperación completo."],
        "correct": 3
    },
    {
        "question": "¿Cuál de las siguientes afirmaciones es cierta? El diccionario de datos de una base de datos...",
        "options": ["Permite que cualquier usuario de la base de datos pueda realizar operaciones de modificación directa (mediante UPDATE) sobre él.",
                   "Almacena la definición de todos los objetos de la BD.",
                   "Está almacenado en el tablespace USERS y puede acceder a él cualquier usuario de la base de datos.",
                   "Es opcional. Es decir, pueden existir bases de datos sin diccionario de datos."],
        "correct": 1
    },
    {
        "question": "En relación con las transacciones y su procesamiento. ¿Cuál de las siguientes afirmaciones es cierta?",
        "options": ["Una transacción es una secuencia de operaciones que han de ejecutarse de forma atómica.",
                   "En Oracle, una transacción es una secuencia de sentencias SQL, pero por mecanismos propios del SGBD no es necesario tratarlo como una única unidad.",
                   "No existen errores a nivel transacción.",
                   "Cuando una transacción termina con éxito, las actualizaciones de que consta la transacción se graban con la sentencia ROLLBACK."],
        "correct": 0
    },
    {
        "question": "¿Cuál de las siguientes afirmaciones es correcta?",
        "options": ["El archivo de control, contiene el nombre de la base de datos, el lugar físico donde se encuentran los \"tablesplaces\", los SCN (Número de secuencia de Log actual) y el diccionario de datos.",
                   "En el fichero de \"Redo Log\" se guardan todos los datos confirmados, excepto el de algunas transacciones en los que se excluye dicha escritura.",
                   "Los ficheros de \"Redo Log\" sirven para recuperar una base de datos, pues en él se guardan todos los datos modificados y los antiguos datos, por si, por ejemplo, se ejecutara un ROLLBACK de la transacción.",
                   "El \"tablespace\" TEMPORAL, sirve para guardar datos temporales como el SCN (\"Número Secuencial del Log Actual\") e información temporal de las copias de seguridad que se hacen en un momento dado, entre otras cosas."],
        "correct": 1
    },
    {
        "question": "Una base de datos puede estar compuesta de varias instancias …:",
        "options": ["… si cada instancia tiene su propia SGA (\"System Global Area\") y la misma máquina compartida.",
                   "… si cada instancia reside en diferentes máquinas.",
                   "… que residen en uno o varios ordenadores, o máquinas, con diferentes nombres de Bases de Datos para recuperación más rápida de bases de datos.",
                   "No, pues una instancia con su propia SGA (\"System Global Area\") puede contener diferentes bases de datos. Por ejemplo, para planes de emergencia."],
        "correct": 1
    },
    {
        "question": "Dada la relación PERSONA (DNI, nombre, dirección, teléfono, nómina), si quisiéramos que sólo 3 usuarios (por ahora) sean capaces de consultar y modificar los datos referentes al teléfono y la nómina en la relación, deberíamos:",
        "options": ["Asignarle los permisos de selección y modificación de dichos campos a cada usuario que queramos que cumplan esos requisitos. Sería lo más eficiente.",
                   "Crear un rol, darle permisos de selección y modificación de dichos campos y asignar ese rol a cada usuario. Sería lo más eficiente.",
                   "Crear un perfil, darle permisos de selección y modificación de dichos campos y aplicar ese perfil a cada uno de los usuarios. Sería lo más eficiente.",
                   "Crear un perfil, aplicar ese perfil a cada uno de los usuario y, por último, darle permisos a ese perfil de selección y modificación de los campos adecuados. Sería lo más eficiente."],
        "correct": 1
    },
    {
        "question": "¿Cuál de las siguientes afirmaciones es cierta respecto a los ficheros de control en el Sistema Gestor de la Base de Datos ORACLE?",
        "options": ["Guardan información sobre la estructura lógica de la Base de Datos entre otras cosas.",
                   "Es el archivo de la BD, que almacena la ubicación y estado de las copias de seguridad.",
                   "Proporcionan el mecanismo para rehacer transacciones en caso de fallo en la BD.",
                   "Es el archivo de la BD, que almacena la definición de todos los objetos de la BD (tablas, vistas, índices, procedimientos, funciones, disparadores, etc.)"],
        "correct": 1
    },
    {
        "question": "¿Cuál de las siguientes afirmaciones es cierta respecto a la Recuperación en el Sistema Gestor de la Base de Datos ORACLE?",
        "options": ["Para poder realizar un backup en caliente es necesario estar en modo \"NO ARCHIVELOG\".",
                   "En Base de Datos que siempre tienen que estar funcionando sólo es posible hacer backup en frio.",
                   "La herramienta \"IMPORT\" de Oracle permite hace backup lógicos.",
                   "Un backup en caliente de un espacio de tablas consiste en copiar todos los ficheros de almacenamiento asociados al mismo mientras la base de datos está en modo \"ARCHIVELOG\"."],
        "correct": 3
    },
    {
        "question": "Respecto al diseño físico. ¿Cuál de las siguientes afirmaciones es cierta?",
        "options": ["Se recomienda definir índices si la clave sobre la que se crea es de gran tamaño.",
                   "Las tablas organizadas como índices sólo se recomiendan en tablas cuyo tamaño de fila es de gran tamaño.",
                   "Las tablas organizadas como índices sólo se recomiendan en tablas cuyo tamaño de fila es pequeño.",
                   "Para aumentar el rendimiento en el acceso a los datos se utilizan índices, tablas organizadas por índices, Clusters y Hash Cluster."],
        "correct": 3
    },
    {
        "question": "Una instancia de Oracle se compone de:",
        "options": ["El Área Global de Memoria Compartida (SGA).",
                   "El Área Global Privada de Memoria (PGA).",
                   "El SGA más los procesos de Oracle de acceso a la Base de Datos.",
                   "El PGA más los procesos de Oracle de acceso a la Base de Datos."],
        "correct": 2
    },
    {
        "question": "Indica la opción correcta sobre la siguiente sentencia:\nCREATE PROFILE perfil_usuario LIMIT\nCPU_PER_SESSION 30\nSESSION_PER_USER 3 PASSWORD_LIFE_TIME UNLIMITED",
        "options": ["La sentencia es correcta.",
                   "La sentencia es incorrecta, ya que no se pueden mezclar propiedades sobre el uso de recursos hardware y propiedades de la contraseña en una misma sentencia CREATE PROFILE.",
                   "La sentencia es incorrecta, ya que no se pueden administrar las propiedades de las contraseñas en la sentencia CREATE PROFILE.",
                   "La sentencia es incorrecta, ya que sólo se puede indicar el tiempo de vida de una contraseña en las sentencias CREATE/ALTER USER."],
        "correct": 0
    },
    {
        "question": "Ha ocurrido un error de sistema que ha perjudicado al disco donde se encuentra una BD produciéndose daños en ella. Se trata de una BD online en la que se realizan cambios continuamente, el único y último backup físico que se tiene es de dos horas antes a cuando ocurrió el fallo y la BD está en modo NO ARHIVELOG ¿Cuál de las siguientes afirmaciones es cierta?",
        "options": ["Como tenemos el backup físico, podemos hacer una recuperación completa.",
                   "Ante esta situación, se han perdido todos los datos, y no se puede recuperar nada de la BD.",
                   "Como tenemos el backup físico, podemos hacer una recuperación pero con pérdida de información.",
                   "Al estar en modo NO ARCHIVELOG, podemos hacer una recuperación completa utilizando el backup y los ficheros REDOLOG."],
        "correct": 2
    },
    {
        "question": "Se define un rol como:",
        "options": ["Un conjunto de usuarios.",
                   "Un conjunto de privilegios sobre el sistema.",
                   "Un conjunto de privilegios sobre objetos de esquemas de usuario.",
                   "Un conjunto de privilegios sobre el sistema y/o sobre objetos de esquemas de usuario."],
        "correct": 3
    },
    {
        "question": "Dentro de los problemas clásicos asociados a la concurrencia, una lectura no repetible o lectura borrosa:",
        "options": ["No ocurre, porque este tipo de problema no aparece en la concurrencia de los SGBD.",
                   "Ocurre cuando dos transacciones que acceden a los mismos ítems tienen sus operaciones intercaladas de tal forma que modifican o acceden al valor de algún ítem incorrectamente.",
                   "Ocurre cuando una transacción T1 lee un ítem de datos dos veces y otra transacción T2 modifica dicho ítem entre las dos lecturas y lo confirma.",
                   "Sucede cuando una transacción T1 lee un ítem de datos dos veces y otra transacción T2 modifica dicho ítem entre las dos lecturas, pero sin confirmar esta modificación."],
        "correct": 2
    },
    {
        "question": "El concepto de transacción en Oracle permite:",
        "options": ["Prevenir problemas de concurrencia.",
                   "Realizar optimizaciones sobre el diseño físico de la base de datos.",
                   "Permitir la recuperación ante fallos y prevenir problemas de concurrencia.",
                   "Ninguna de las anteriores."],
        "correct": 2
    },
    {
        "question": "De las siguientes definiciones, ¿Cuál es la correcta?",
        "options": ["En el tablespace SYSTEM se guardan datos de Oracle, como estadísticas, estado de la instancia y datos de un aplicativo como tablas, etc.",
                   "En el tablespace REDO se guardan los datos antiguos de una transacción y los nuevos en el UNDO.",
                   "El tablespace TEMP se utiliza como temporal de las operaciones join, order-by, hash, etc. de los diferentes usuarios que tengan como tablespace temporal por defecto el TEMP.",
                   "En el tablespace SYSTEM a parte de tener los datos del diccionario también guarda ciertos datos temporales de las operaciones join, order, etc. de los usuarios e incluso datos."],
        "correct": 2
    },
    {
        "question": "¿Qué herramienta proporciona Oracle para consultar el plan que ha seguido a la hora de ejecutar una consulta?",
        "options": ["SQL-Plus",
                   "SQL*Expert",
                   "SQL-Analyze (Explain plan)",
                   "SQL-Stat"],
        "correct": 2
    },
    {
        "question": "¿Cuál de las siguientes afirmaciones es cierta?",
        "options": ["Los segmentos rollback almacenan las últimas sentencias realizadas sobre la BD.",
                   "Los ficheros de control almacenan la estructura lógica de la BD.",
                   "Un backup de la BD es un fichero de almacenamiento de cambios en la BD.",
                   "Un backup lógico no es una copia de seguridad de la BD."],
        "correct": 0
    },
    {
        "question": "Después de haberse producido un fallo en mitad de procesamiento de una transacción, el SGBD pasa a restaurar la BD. ¿Cuál de las siguientes respuestas es cierta?",
        "options": ["Se recuperará la BD en estado inconsistente y habrá habido perdida de información.",
                   "Si la BD está en modo NO ARCHIVEDLOG, el SGBD no va a ser capaz de devolver la BD en estado consistente.",
                   "El SGBD debe de ser capaz de recuperar cualquier transacción afectada por un fallo.",
                   "El SGBD fuerza el commit de la transacción, y así devolverá la BD en estado consistente."],
        "correct": 2
    },
    {
        "question": "¿Cuál de las siguientes afirmaciones es cierta?: Las técnicas de control de la concurrencia optimistas …",
        "options": ["… no utilizan bloqueos y asignan un identificador único a cada transacción que equivale al tiempo de inicio de la misma.",
                   "… necesitan realizar una serie de chequeos previos a la ejecución de cada operación de la BD.",
                   "… necesitan que previamente se ejecuten las técnicas de control pesimistas para evitar problemas de concurrencia en las operaciones de las transacciones.",
                   "… permiten que las transacciones accedan libremente a los objetos, determinando antes de su finalización si ha habido o no interferencias."],
        "correct": 3
    },
    {
        "question": "¿Cuál de las siguientes afirmaciones es cierta?",
        "options": ["En un fichero de datos o \"Datafile\" se crea al menos un \"tablespace\" para contener los procedimientos almacenados, disparadores y tablas de un esquema.",
                   "En un fichero de datos o \"Datafile\" se crea al menos un \"tablespace\" para contener las tablas de un esquema.",
                   "Cuando se crea un objeto de base de datos, por ejemplo, una tabla o índice, se asigna a un \"tablespace\" mediante las opciones predeterminadas del usuario o mediante instrucciones específicas.",
                   "Un bloque lógico en Oracle este compuesto por segmentos lógicos en los cuales se guardan los objetos Oracle, como tablas, procedimientos almacenados, etc."],
        "correct": 2
    },
    {
        "question": "¿Cuál de las siguientes afirmaciones es cierta?",
        "options": ["Cada segmento consta de una serie de secciones denominadas extensiones, que son conjunto de bloques de Oracle contiguos. Cuando las extensiones existentes ya no pueden contener nuevos datos, el segmento obtiene una nueva extensión.",
                   "Cada segmento consta de una serie de secciones denominados bloques, que son conjunto de extensiones de Oracle contiguos. Cuando los bloques existentes ya no pueden contener nuevos datos, el segmento obtiene un nuevo bloque.",
                   "El segmento es el nivel más bajo de granularidad. Los datos de Oracle se almacenan en segmentos de datos.",
                   "Un bloque de datos se corresponde específicamente al número de segmentos de espacio en disco. Una base de datos usa y asigna (\"allocate\") espacio libre en segmentos de datos."],
        "correct": 0
    },
    {
        "question": "Optimización y procesamiento de consultas. ¿Cuál de las siguientes afirmaciones es cierta?",
        "options": ["El objetivo de la optimización lógica de una consulta es obtener una expresión en algebra relacional equivalente pero cuyo coste de ejecución se estime menor.",
                   "El objetivo de la optimización física es determinar el hardware necesario para ejecutar una consulta.",
                   "El objetivo de la optimización lógica de consultas es determinar si todos los elementos utilizados en la consulta existen en la base de datos.",
                   "La optimización física se realiza es independiente del esquema de nuestra base de datos."],
        "correct": 0
    },
    {
        "question": "En el SGBD Oracle. ¿Cuál de las siguientes afirmaciones es correcta?",
        "options": ["La SGA (\"System Global Area\") es un área de memoria reservada para cada proceso de usuario que se conecte a una base de datos.",
                   "El área \"Buffer Redo Log\" se ubica en la PGA (\"Program Global Area\"). En este área se almacenan los datos a rehacer (Guardados en el UNDO o segmentos de ROLLBACK en Oracle 8i).",
                   "En el SGA se guardan planes de ejecución de paquetes PL/SQL, bloques de datos recuperados de los \"tablespaces\" y registros denominados de \"redo log\".",
                   "La PGA contiene los planes de ejecución de paquetes PL/SQL, bloques de datos recuperados de los \"tablespaces\" y registros denominados de \"redo log\"."],
        "correct": 2
    },
    {
        "question": "En relación a la tarea de controlar la Integridad de la Base de Datos, en un sistema multiusuario como el SGBD Oracle, ¿Cuál de las siguientes afirmaciones es correcta?",
        "options": ["Para asegurar la integridad, es necesario que las transacciones se puedan ejecutar de forma serial, una detrás de otra.",
                   "Si se ejecutan transacciones simultáneas no es necesario establecer mecanismos de control de concurrencia para asegurar la consistencia de los datos.",
                   "Cuando se ejecutan transacciones usando el modelo de marcas multiversión de Oracle, los datos que ven las transacciones son exactamente los mismos.",
                   "Asegurar la integridad cuando tenemos varias transacciones concurrentes tiene una desventaja, afecta a la escalabilidad de la Base de Datos."],
        "correct": 0
    },
    # EXAMEN DE PEDRÍN
    {
        "question": "¿Qué proceso traslada los bloques modificados de la caché de base de datos desde la SGA a los ficheros de datos cuando se produce un checkpoint?",
        "options": ["LGWR", 
                   "SMON", 
                   "DBW0", 
                   "CKPT", 
                   "PMON"],
        "correct": 2 #CHATGPT (puede ser 3 tambien)
    },
    {
        "question": "Cuando creamos una nueva Base de Datos y no queremos que los usuarios usen el tablespace SYSTEM para operaciones de ordenación. ¿Qué debemos hacer?",
        "options": ["Crear un tablespace de UNDO", 
                   "Crear un tablespace temporal por defecto", 
                   "Crear un tablespace con la palabra UNDO", 
                   "Crear un tablespace con la palabra TEMPORARY"],
        "correct": 1
    },
    {
        "question": "Una transacción serializable (isolation level serializable) es aquella que:",
        "options": ["Ve sólo aquellos cambios que fueron confirmados en el momento en que comenzó la transacción, además de los cambios que realice la propia transacción durante su ejecución.", 
                   "Ve sólo aquellos cambios que fueron confirmados en el momento en que comenzó la transacción.", 
                   "Ve sólo aquellos cambios que fueron confirmados en el momento en que comenzó la transacción, además de los cambios que realice la propia transacción durante su ejecución. Además, no permiten sentencias insert/update/delete como parte de la transacción.", 
                   "Ninguna de las anteriores."],
        "correct": 0 #CHATGPT (segun pdf la 2 y 3 pueden ser)
    },
    {
        "question": "Dada la siguiente relación R(AT, DF) donde AT= {A, B, C, D, E} y DF={ABà D, ACà E, BCà D, Dà A, EàB} indicar cuál de las siguientes afirmaciones es cierta:",
        "options": ["A, B y C son los atributos principales y la relación está en 3FN", 
                   "A, B y C son los atributos principales y la relación está en FNBC", 
                   "A, B, C, D y E son los atributos principales y la relación está en 3FN", 
                   "A, B, C, D y E son los atributos principales y la relación está en FNBC"],
        "correct": 0
    },
    {
        "question": "En el proceso de establecer una conexión de usuario con un servidor dedicado (no compartido) en Oracle, ¿cuál/es de las siguientes afirmaciones son ciertas?",
        "options": ["El proceso de servidor es el que establece primero la conexión.", 
                   "El proceso de servidor interactúa directamente con Oracle Server.", 
                   "El proceso de usuario interactúa directamente con Oracle Server.", 
                   "El proceso de usuario ejecuta sentencias SQL en nombre del usuario."],
        "correct": [1, 3], #CHATGPT (el pdf dice 2)
        "type": "multiple"
    },
    {
        "question": "Cuál/es de las siguientes afirmaciones son falsas respecto a los ficheros de control de la Base de Datos ORACLE.",
        "options": ["Mantienen y mejoran las relaciones entre las estructuras físicas y de memoria.", 
                   "Es el archivo de la BD, que almacena la ubicación y estado de las copias de seguridad.", 
                   "Proporcionan el mecanismo para rehacer transacciones en caso de fallo en la BD.", 
                   "Es el archivo de la BD, que almacena la definición de todos los objetos de la BD (tablas, vistas, índices, procedimientos, funciones, disparadores, etc..)"],
        "correct": [2, 3],
        "type": "multiple"
    },
    {
        "question": "Para prevenir problemas de concurrencia ORACLE tiene como solución/es:",
        "options": ["Dispone de niveles de aislamiento: read commited, serializable, readonly.", 
                   "Modelo multiversión.", 
                   "La aplicación Recovery Manager.", 
                   "Mecanismos para hacer auditorias."],
        "correct": [0, 1],
        "type": "multiple"
    },
    {
        "question": "ORACLE dispone de mecanismo/s de seguridad como:",
        "options": ["Auditorias.", 
                   "Perfiles.", 
                   "Roles.", 
                   "RMAN."],
        "correct": 0
    },
    {
        "question": "¿Con qué sentencias borrarías el perfil actual y asignarías un nuevo perfil a un usuario? Marca la/s respuestas correctas:",
        "options": ["DELETE PROFILE …; GRANT PROFILE…;", 
                   "DROP PROFILE…; GRANT PROFILE…;", 
                   "DROP PROFILE…; ALTER USER SET PROFILE…;", 
                   "DELETE PROFILE…; ALTER USER SET PROFILE…;"],
        "correct": [1, 2],
        "type": "multiple"
    },
    {
        "question": "Supongamos un tamaño de bloque de datos de 4K. ¿Sería correcto planificar un espacio de tablas (tablespace) de 100K, suponiendo que se tienen extensiones de 3 bloques de datos, segmentos de 3 extensiones, y archivos de datos de 3 segmentos? (Esta pregunta es de respuesta libre)",
        "options": ["No, porque el tamaño necesario serían mis huevos con bigote", 
                   "Sí, porque el tamaño necesario sería: 3 segmentos × 3 extensiones × 3 bloques × 4K / 3.6 = 100K", 
                   "No, porque el espacio necesario debe ser de al menos 108K para este diseño (3 segmentos × 3 extensiones × 3 bloques × 4K)", 
                   "Sí, porque un tablespace de 100K puede almacenar 25 bloques, lo que es suficiente para 24 bloques necesarios"],
        "correct": 2 #CHATGPT
    }
    
]