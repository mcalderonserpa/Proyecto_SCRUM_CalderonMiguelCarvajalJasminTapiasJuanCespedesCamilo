# 🏋️ ForceTech Gym

Sistema de gestión de clientes, instructores y servicios

## 📖 Descripción del Proyecto

ForceTech Gym es un sistema de consola desarrollado en Python para organizar la información de un gimnasio: clientes, servicios, matrículas, instructores y reportes.

Permite inscribir clientes, matricularlos en servicios con control de cupos, registrar su asistencia y sus evaluaciones de condición física, y consultar reportes de progreso y rendimiento. La información se guarda en archivos JSON, así que no se pierde al cerrar el programa.

El proyecto se desarrolló bajo el marco de trabajo SCRUM, con Git y GitHub para el control de versiones y el trabajo colaborativo.

## 🎯 Objetivo del Proyecto

Desarrollar un sistema que permita gestionar de manera organizada la información del gimnasio, facilitando el registro, consulta y actualización de los datos y reduciendo el manejo manual de la información.

## 👥 Integrantes

|     Integrante                | Responsabilidad / Módulo                             |          Rol               |  
| ----------------------------- | ---------------------------------------------------- | -------------------------- |
| Miguel Ricardo Calderón Serpa | Facilitar el Scrum y remover impedimentos            | Scrum Master - Development Team               |
| Jasmin Sofía Carvajal Prada   | Construir, probar e integrar funcionalidades         | Development Team            |
| Juan Daniel Tapias            | Construir, probar e integrar funcionalidades         | Development Team           |
| Camilo Andrés Gonzales        | Definir y priorizar las funcionalidades del proyecto | Product Owner              |


## ⚙️ Módulos del Sistema

### 👤 Módulo de clientes

| Opción | Función |
| --- | --- |
| 1. Solicitud nuevo registro | El cliente ingresa su cédula, nombres, apellidos, dirección, teléfonos y nivel de riesgo. La solicitud queda pendiente de aprobación. |
| 2. Ver perfil | El cliente ingresa con su cédula y accede a su perfil. |
 
Dentro del **perfil**:
 
| Opción | Función |
| --- | --- |
| 1. Ver datos de perfil | Muestra los datos personales, el estado y el nivel de riesgo. |
| 2. Matricular servicio | Inscribe al cliente en un servicio, con fecha de inicio y de finalización. |
| 3. Seguimiento de proceso | Muestra la asistencia, las evaluaciones, la tendencia y el rendimiento en cada servicio. |
| 4. Modificar datos | Permite actualizar nombres, apellidos, dirección y teléfonos (dejar vacío para no cambiar). |
| 5. Volver al menú principal | |

### 👨‍🏫 Módulo de instructores

El instructor ingresa con su **cédula** y solo ve los servicios que tiene asignados.
 
| Opción | Función |
| --- | --- |
| 1. Registrar asistencia | Elige un servicio y una fecha, y responde **SI** o **NO** por cada cliente matriculado. |
| 2. Registrar evaluación de rendimiento | Elige un servicio y un cliente, y registra una nota de **0.1 a 10** con observaciones opcionales. Al guardar muestra el score actualizado del cliente. |
| 3. Volver al menú principal | |
 
Ejemplo de registro de asistencia:
 
```text
Asistencia de yoga - 20-09-2026  (SI = asistio, NO = no asistio)
  [1001] ana perez: si
  [2002] luis gomez: NO
 
Asistencia guardada: 1 asistentes, 1 ausentes.
```

### 👨‍💼 Módulo de administrador

| Opción | Función |
| --- | --- |
| 1. Admitir inscripciones clientes | Muestra cada solicitud pendiente y permite aceptarla; las no aceptadas siguen pendientes. |
| 2. Listar clientes | Muestra todos los clientes registrados. |
| 3. Gestión de servicios | Registrar, listar y modificar servicios (agregar o quitar cupos). |
| 4. Gestión de instructores | Registrar, listar y eliminar instructores. |
| 5. Volver al menú principal | |
 
> "Eliminar instructor" **desactiva** al instructor en lugar de borrarlo, para conservar las asistencias y evaluaciones que registró. Un instructor desactivado no puede iniciar sesión.


### 📊 Módulo de reportes

| Opción | Contenido |
| --- | --- |
| 1. Clientes inscritos | Todos los clientes con sus datos. |
| 2. Servicios y capacidad | Cada servicio con sus cupos disponibles y su instructor. |
| 3. Instructores activos | Instructores con estado activo. |
| 4. Clientes con riesgo alto | Clientes con **riesgo alto o con bajo rendimiento**, con su score y nivel. |
| 5. Progreso de clientes | Para cada cliente matriculado: asistencia, historial de evaluaciones, tendencia y score por servicio. |
 
---

## 📋 Reglas del negocio

### Clientes
 
- La cédula debe ser numérica y no puede repetirse.
- Nombres y apellidos son obligatorios.
- El teléfono móvil debe tener exactamente 10 dígitos.
- Niveles de riesgo: **Alto**, **Medio**, **Bajo**.
- Estados: **En proceso de inscripción** (al registrarse) → **Inscrito** (cuando el administrador lo acepta).
  
### Servicios y matrículas
 
- El nombre del servicio es único. Se guarda en minúsculas, así que "Yoga" y "yoga" son el mismo servicio.
- Los cupos deben ser un número mayor que 0 y nunca quedan negativos.
- Solo se pueden matricular clientes **Inscritos** o **Activos**.
- Un cliente no puede matricularse dos veces en el mismo servicio.
- Cada matrícula descuenta un cupo; si no hay cupos, se rechaza.
  
### Instructores
 
- La cédula debe ser numérica y única.
- El nombre es obligatorio y no puede repetirse (los servicios se asignan por nombre).
  
### Asistencia y evaluaciones
 
- Todas las fechas se escriben en formato **DD-MM-AAAA** (por ejemplo, `20-09-2026`). Si la fecha se deja vacía se usa la de hoy.
- No se puede registrar dos veces la asistencia del mismo servicio en la misma fecha.
- Las calificaciones van de **0.1 a 10** y aceptan punto o coma decimal (`9.5` o `9,5`).
  
### Cálculo del rendimiento
 
```text
score = (suma de calificaciones ÷ número de evaluaciones) − 0.1 × inasistencias
```
 
El resultado se limita entre 0 y 10, y se clasifica así:
 
| Score | Rendimiento |
| --- | --- |
| Menor que 5.0 | Bajo |
| De 5.0 a menos de 7.0 | Medio |
| 7.0 o más | Alto |
 
Ejemplo: un cliente con evaluaciones de 6.5 y 8.0 y una inasistencia tiene un score de `(6.5 + 8.0) ÷ 2 − 0.1 = 7.15` → rendimiento **alto**.

### Validación de entradas
 
Si se escribe texto donde se espera un número, una opción fuera de la lista o una fecha con formato incorrecto, el sistema muestra un mensaje y vuelve a preguntar o regresa al menú; el programa no se cierra.
 
---

## 💾 Persistencia de Datos

La información se guarda en archivos **JSON** que el programa crea automáticamente la primera vez que los necesita:
 
| Archivo | Contenido |
| --- | --- |
| `clients.json` | Clientes registrados |
| `services.json` | Servicios, cupos, instructor asignado y matrículas |
| `instructors.json` | Instructores, estado y servicios asignados |
| `asistencias.json` | Una entrada por sesión: servicio, fecha, instructor, asistentes y ausentes |
| `evaluaciones.json` | Evaluaciones: cliente, servicio, instructor, fecha, calificación y observaciones |
 
- Si un archivo no existe, el sistema empieza con una lista vacía.
- Si un archivo está vacío o dañado, el sistema muestra un aviso y sigue funcionando.
- Los archivos `.json` están excluidos del repositorio (`.gitignore`), así cada instalación empieza con sus propios datos.
- Para hacer una **copia de seguridad**, basta con copiar estos cinco archivos.
---


## 🛠️ Tecnologías utilizadas
 
* **Python 3.10+**
* **JSON**
* **Git** y **GitHub**
* **Visual Studio Code**
* **Notion** (gestión SCRUM)
---

## 📁 Estructura del Proyecto
 
```text
ForceTech Gym/
│
├── main.py                          # Punto de entrada: menú principal y navegación
├── README.md
├── .gitignore
│
└── src/
    ├── functions_admin/
    │   ├── admin2clients.py         # Admitir inscripciones y matrículas
    │   ├── admin2instructors.py     # Registrar instructores
    │   └── admin2services.py        # Registrar, listar y modificar servicios
    │
    ├── functions_clients/
    │   └── clientes.py              # Registro, perfil y modificación de clientes
    │
    ├── functions_instructors/
    │   └── instructors.py           # Login, asistencia, evaluaciones, score y reportes
    │
    ├── functions_menu/
    │   └── menus.py                 # Textos de todos los menús
    │
    ├── functions_reports/
    │   └── reportes.py              # Reservado para los reportes
    │
    ├── functions_storage/
    │   └── storage.py               # Lectura y escritura de los archivos JSON
    │
    └── functions_utils/
        └── validaciones.py          # Validación de números y fechas
```
---

## ⚠️ Limitaciones conocidas

Estas funciones quedaron registradas en el Product Backlog para una próxima versión:
 
- El cliente todavía no puede **retirarse** de un servicio.
- El perfil del cliente no tiene una opción para **ver sus servicios matriculados** ni la **lista de servicios disponibles**. Los servicios se consultan desde el administrador o los reportes.
- El reporte "Servicios y capacidad" muestra los **cupos disponibles**, no la capacidad máxima original.
- Los datos se guardan localmente en archivos JSON, pensados para un solo equipo a la vez.
---


# 🔄 Proceso de desarrollo
 
## 📚 Metodología SCRUM
 
El proyecto se gestionó con **SCRUM** en Notion, mediante:
 
* Product Backlog con historias de usuario, prioridades y criterios de aceptación.
* Sprint Planning, Daily Stand-up, Sprint Review y Sprint Retrospective.
* Tareas de desarrollo por módulo y seguimiento del avance.
* Ramas, commits y Pull Requests en GitHub para integrar cada funcionalidad.


⚙️ Instalación, configuración y repositorio local

Al inicio del proyecto se configuró Git en los equipos de los integrantes para permitir el control de versiones y el trabajo colaborativo.

Cada integrante configuró su identidad mediante los comandos:

```bash
git config --global user.name "Nombre del usuario"
git config --global user.email "correo@example.com"
```

La configuración puede verificarse mediante:

```bash
git config --list
```

## 📦 Inicialización del repositorio

El repositorio local se creó utilizando:

```bash
git init
```

Este comando permitió convertir la carpeta del proyecto en un repositorio Git e iniciar el control de versiones.

## 🔗 Repositorio remoto

El proyecto se vinculó con el repositorio remoto de GitHub mediante:

```bash
git remote add origin URL_DEL_REPOSITORIO
```

Para comprobar la conexión con el repositorio remoto se utilizó:

```bash
git remote -v
```

## 📥 Clonación del repositorio

Para obtener una copia del repositorio remoto se utilizó el comando:

```bash
git clone URL_DEL_REPOSITORIO
```

Este proceso permitió que los integrantes trabajaran con una copia local del proyecto.

### 📸 Evidencia de clonación

<img width="1429" height="288" alt="image" src="https://github.com/user-attachments/assets/136a2b1d-4314-4cd3-b5de-9734d902433c" />


# 🔄 Proceso de Integración y Merges

## 🌿 Ramas creadas en el proyecto

Las ramas se utilizaron para separar el desarrollo de las diferentes funcionalidades y evitar trabajar directamente sobre la rama principal.

Para consultar las ramas locales y remotas se utilizó:

```bash
git branch -a
```

| Rama | Propósito |
| --- | --- |
| `main` | Rama principal y estable |
| `refactor/nueva-estructura-proyecto` | Estructura de carpetas `src/` |
| `feature/storage-instructor` | Almacenamiento JSON de instructores |
| `feature/administrador` | Módulo de administrador |
| `feature/gestion-clientes` | Módulo de clientes |
| `features/instructor_tools` | Módulo de instructores (asistencia, evaluaciones, score) |
| `fix/correccion_menu` · `fix/menu-final` | Ajustes de menús |
| `fix/ajustes-compatibilidad` | Compatibilidad entre módulos |
| `fix_project` | Corrección general antes de la entrega |

### 📸 Evidencia de las ramas

<img width="428" height="365" alt="image" src="https://github.com/user-attachments/assets/7f6f1e53-e253-4691-83af-d0270a44c7ba" />



## 🔀 Integración de cambios (Pull Requests)
 
Cada funcionalidad terminada se integró a `main` mediante un Pull Request revisado por el equipo:
 
| PR | Rama | Contenido |
| --- | --- | --- |
| #1 | `refactor/nueva-estructura-proyecto` | Nueva estructura del proyecto |
| #2 | `feature/storage-instructor` | Almacenamiento de instructores |
| #3 | `fix/correccion_menu` | Corrección de menús |
| #4, #7 | `feature/gestion-clientes` | Módulo de clientes |
| #5 | `features/instructor_tools` | Módulo de instructores |
| #8 | `fix/ajustes-compatibilidad` | Compatibilidad entre módulos |
| #9 | `fix_project` | Corrección de 12 errores detectados en pruebas |
 
Para consultar el historial y la relación entre ramas:
 
```bash
git log --oneline --graph --all
```

 
### 📸 Evidencia del historial de ramas

<img width="731" height="272" alt="image" src="https://github.com/user-attachments/assets/a3d9df1d-92e0-42f5-80de-a87ac90e3298" />


# 📝 Commits y Conventional Commits

Durante el desarrollo se utilizaron commits para registrar los cambios realizados en el proyecto.

El historial puede consultarse mediante:

```bash
git log --oneline
```

También se utilizaron mensajes siguiendo la estructura de **Conventional Commits**, por ejemplo:

```text
feat: actualizar gestion de clientes
```

```text
docs: agregar README del proyecto
```

```text
fix: corregir registro de clientes
```

Los tipos principales utilizados son:

* `feat`: nueva funcionalidad.
* `fix`: corrección de errores.
* `docs`: cambios en documentación.
* `refactor`: modificación de código sin cambiar su funcionalidad.

### 📸 Evidencia de Conventional Commits

<img width="660" height="296" alt="image" src="https://github.com/user-attachments/assets/89a0daa5-df90-4c3e-a7fc-f80d8c18be36" />


## 🔄 Sincronización del proyecto
 
Para mantener sincronizados el repositorio local y el remoto:
 
```bash
git pull   # trae los cambios del remoto y actualiza la copia local
git push   # envía los commits locales al remoto
```
 
Cada integrante actualizaba su rama antes de continuar cuando otros colaboradores habían integrado cambios.
 
### 📸 Evidencia de sincronización
 
<img width="1437" height="565" alt="image" src="https://github.com/user-attachments/assets/7c640122-d97b-443a-8481-fbe46dea7775" />


## 🔄 Sincronización entre integrantes

Cada integrante debe actualizar su rama antes de continuar trabajando cuando existan cambios realizados por otros colaboradores.

### 📸 Evidencia de sincronización

<img width="1437" height="565" alt="image" src="https://github.com/user-attachments/assets/7c640122-d97b-443a-8481-fbe46dea7775" />


## 👥 Colaboración en GitHub
 
Cada integrante trabajó sus funcionalidades en ramas independientes, registró sus avances con commits y los integró mediante Pull Requests.
 
### 👤 Camilo Andrés Gonzales — Product Owner
 
Definió y priorizó las funcionalidades del Product Backlog, validó los criterios de aceptación y revisó los incrementos entregados en la Sprint Review.
 
### 👤 Miguel Ricardo Calderón Serpa — Scrum Master · Development Team
 
Facilitó las ceremonias SCRUM y la remoción de impedimentos. En desarrollo, se encargó de la estructura del proyecto, el almacenamiento en JSON, el módulo de administrador y la integración de las ramas (PR #1, #2, #3 y #8).
 
#### 📸 Evidencia de commits
 
<img width="908" height="277" alt="image" src="https://github.com/user-attachments/assets/8d0e83a3-58b0-42f4-906d-2e0b229e22da" />

### 👤 Jasmin Sofía Carvajal Prada — Development Team
 
Desarrolló el **módulo de clientes**: solicitud de registro, perfil, modificación de datos, estados y nivel de riesgo, con su almacenamiento en JSON (PR #4 y #7).
 
#### 📸 Evidencia de commits
 
<img width="938" height="330" alt="image" src="https://github.com/user-attachments/assets/1a8d46cd-808a-482c-9160-ce163a6d2615" />

### 👤 Juan Daniel Tapias — Development Team
 
Desarrolló el **módulo de instructores**: inicio de sesión por cédula, registro de asistencia, evaluaciones de rendimiento, cálculo del score y las funciones que usan los reportes de riesgo y progreso (PR #5). Como corrector, uso la rama `fix_project`, que corrigió  errores antes de la entrega (PR #9).
 
#### 📸 Evidencia de commits
 
<img width="923" height="187" alt="image" src="https://github.com/user-attachments/assets/5f1f1bb3-75d6-4be8-b5aa-279d3a02c891" />
---

# ▶️ Ejecución del proyecto

Para ejecutar el sistema desde la terminal se utiliza:

```bash
python main.py
```

Al ejecutar el programa se muestra el menú principal, desde donde se puede acceder a las diferentes funcionalidades del sistema.

## 📌 Estado del Proyecto
 
**Proyecto finalizado y entregado.**
 
Las funcionalidades pendientes están descritas en [Limitaciones conocidas](#️-limitaciones-conocidas) y registradas en el Product Backlog.
 
## 🔗 Repositorio
 
`https://github.com/mcalderonserpa/Proyecto_SCRUM_CalderonMiguelCarvajalJasminTapiasJuanCespedesCamilo`
 
---
 
**ForceTech Gym — Sistema de gestión de clientes, instructores y servicios**


