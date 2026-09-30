# 🏋️ ForceTech Gym

Sistema de gestión de clientes, instructores y servicios

## 📖 Descripción del Proyecto

Es un sistema de gestión desarrollado en Python para organizar y administrar la información relacionada con los clientes, instructores, servicios, matrículas y reportes de un gimnasio.

El sistema busca centralizar la información y facilitar procesos como el registro y consulta de clientes, gestión de servicios, control de instructores, matrículas y generación de reportes.

El proyecto se desarrolla bajo el marco de trabajo SCRUM, utilizando Git y GitHub para el control de versiones y el trabajo colaborativo entre los integrantes del equipo.

## 🎯 Objetivo del Proyecto

Desarrollar un sistema que permita gestionar de manera organizada la información del gimnasio, facilitando el registro, consulta y actualización de los datos y reduciendo el manejo manual de la información.

## 👥 Integrantes

|     Integrante                | Responsabilidad / Módulo                             |          Rol               |  
| ----------------------------- | ---------------------------------------------------- | -------------------------- |
| Miguel Ricardo Calderón Serpa | Facilitar el Scrum y remover impedimentos            | Scrum Master               |
| Jasmin Sofía Carvajal Prada   | Construir, probar e integrar funcionalidades         | Development Team           |
| Juan Daniel Tapias            | Construir, probar e integrar funcionalidades         | Development Team           |
| Camilo Andrés Gonzales        | Definir y priorizar las funcionalidades del proyecto | Product Owner              |


## ⚙️ Módulos del Sistema

### 👤 Gestión de Clientes

Permite administrar la información de los clientes del gimnasio.

Entre los datos gestionados se encuentran:

* Número de identificación.
* Nombres.
* Apellidos.
* Dirección.
* Teléfono celular.
* Teléfono fijo.
* Estado del cliente.
* Nivel de riesgo.

Los estados contemplados son:

* En proceso de inscripción.
* Inscrito.
* Activo.
* Inactivo.

El nivel de riesgo puede clasificarse como:

* Alto.
* Medio.
* Bajo.

### 🏋️ Gestión de Servicios

Permite administrar los diferentes servicios ofrecidos por el gimnasio y controlar información relacionada con su disponibilidad y capacidad.

### 👨‍🏫 Gestión de Instructores

Permite gestionar la información correspondiente a los instructores encargados de los diferentes servicios y actividades del gimnasio.

### 📝 Gestión de Matrículas

Permite administrar la información relacionada con las matrículas de los clientes y su vinculación con los servicios ofrecidos.

### 📊 Gestión de Reportes

Permite generar información organizada a partir de los datos registrados en el sistema para facilitar la consulta y seguimiento de la información.

### 👨‍💼 Gestión de Administrador

Contiene funcionalidades destinadas a la administración general del sistema y a la gestión de los procesos que requieren permisos administrativos.

## 💾 Persistencia de Datos

El proyecto utiliza archivos **JSON** para almacenar información de manera persistente.

De esta forma, los datos registrados no se pierden al cerrar el programa y pueden ser consultados posteriormente.

## 🛠️ Tecnologías utilizadas

* **Python **
* **JSON**
* **Git**
* **GitHub**
* **Visual Studio Code**
* **SCRUM**

## 📁 Estructura del Proyecto

```text
ForceTech Gym/
│
├── main.py
├── README.md
├── .gitignore
│
├── menus/
│
└── src/
    │
    ├── functions_admin/
    │   ├── admin2clients.py
    │   ├── admin2instructors.py
    │   └── admin2services.py
    │
    ├── functions_clients/
    │   └── clientes.py
    |
    ├── functions_instructors/
    │   └── instructors.py
    │
    ├── functions_menu/
    │   └── menus.py
    │
    ├── functions_reports/
    │   └── reportes.py
    │
    └── functions_storage/
        └── storage.py

```
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

La rama principal utilizada en el proyecto es:

```text
main
```

Una de las ramas utilizadas para desarrollar funcionalidades específicas es:

```text
feature/gestion-clientes
```

### 📸 Evidencia de las ramas

<img width="428" height="365" alt="image" src="https://github.com/user-attachments/assets/7f6f1e53-e253-4691-83af-d0270a44c7ba" />



## 🔀 Integración de cambios

Una vez finalizado el desarrollo de una funcionalidad, los cambios pueden integrarse a la rama principal mediante un proceso de merge.

Para consultar el historial y observar la relación entre las ramas se utilizó:

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


# 🔄 Sincronización del proyecto

Para mantener sincronizados los repositorios locales y remotos se utilizaron los comandos:

```bash
git pull
```

y:

```bash
git push
```

`git pull` permite obtener los cambios realizados en el repositorio remoto y actualizar el repositorio local.

`git push` permite enviar los commits realizados localmente hacia el repositorio remoto.

## 🔄 Sincronización entre integrantes

Cada integrante debe actualizar su rama antes de continuar trabajando cuando existan cambios realizados por otros colaboradores.

### 📸 Evidencia de sincronización

<img width="1437" height="565" alt="image" src="https://github.com/user-attachments/assets/7c640122-d97b-443a-8481-fbe46dea7775" />


# 👥 Colaboración en GitHub

El desarrollo del proyecto se realizó mediante un flujo de trabajo colaborativo utilizando Git y GitHub.

Cada integrante trabajó en las funcionalidades asignadas mediante ramas independientes y registró sus avances utilizando commits.

## 👤 Miguel Ricardo Calderón Serpa

Su participación está relacionada con la integración y desarrollo general del proyecto, incluyendo la organización de la estructura y coordinación de los cambios realizados en las diferentes ramas.

### 📸 Evidencia de commits

<img width="908" height="277" alt="image" src="https://github.com/user-attachments/assets/8d0e83a3-58b0-42f4-906d-2e0b229e22da" />


## 👤 Jasmin Sofía Carvajal Prada

Su participación corresponde a la **gestión de clientes**.

El módulo permite registrar y administrar la información de los clientes del gimnasio, incluyendo sus datos personales, estado y nivel de riesgo.

También se implementó el almacenamiento de la información utilizando archivos JSON.

### 📸 Evidencia de commits

<img width="938" height="330" alt="image" src="https://github.com/user-attachments/assets/1a8d46cd-808a-482c-9160-ce163a6d2615" />


## 👤 Juan Daniel Tapias

Su participación corresponde al desarrollo de las funcionalidades asignadas dentro del sistema de gestión del gimnasio.

### 📸 Evidencia de commits

<img width="923" height="187" alt="image" src="https://github.com/user-attachments/assets/5f1f1bb3-75d6-4be8-b5aa-279d3a02c891" />


## 👤 Camilo Andrés Gonzales

Su participación corresponde al desarrollo de las funcionalidades asignadas del proyecto.


# ▶️ Ejecución del proyecto

Para ejecutar el sistema desde la terminal se utiliza:

```bash
python main.py
```

Al ejecutar el programa se muestra el menú principal, desde donde se puede acceder a las diferentes funcionalidades del sistema.

## 📌 Estado del Proyecto

**Proyecto académico en desarrollo.**

El sistema continúa incorporando y mejorando las funcionalidades definidas en los requerimientos del proyecto.

## 📚 Metodología de desarrollo

El proyecto utiliza **SCRUM** como marco de trabajo.

El desarrollo se organiza mediante:

* Historias de usuario.
* Requerimientos funcionales.
* Requerimientos no funcionales.
* Tareas de desarrollo.
* Ramas .
* Commits.
* Integración de funcionalidades.
* Seguimiento del avance del proyecto.

## 🔗 Repositorio

Repositorio oficial:

**ForceTech Gym**

`https://github.com/mcalderonserpa/Proyecto_SCRUM_CalderonMiguelCarvajalJasminTapiasJuanCespedesCamilo`

---

**ForceTech Gym — Sistema de gestión de clientes, instructores y servicios**


