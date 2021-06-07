# Roger Crishtofer Tomairo Paniagua
___

# GIT 
Es un software diseñado para el uso de control de versiones de código de forma distribuida.
## Primeros Pasos
___

Establecer el nombre de usuario

```
git config --global user.name "nombre de usuario"
```
Establecer el Correo Electrónico

```
git config --global user.email correo_electronic@.com
```
Para comprobar la configuración realizar el siguiente comando:

```
git config --list
```
# Iniciando Repositorio

Creamos un Carpeta de nombre Prueba99, dentro de ella abrimos
la terminal e insertamos el siguiente comando para dar inicio.

```
git init
```
Creamos un archivo con el siguiente comando

```
touch readme.md
```
Realizamos el siguiente comando para insertar al control de versiones
```
git add readme.md
```

Para mostrar los cambios que se han realizado

```
git status
```

Realizamos el primer commit que va acompañado del mensaje:

```
git commit -m "Insertar mensaje"
```

# Uso del git Clone
Hacemos uso de los servicios de github, y creamos un repositorio luego obtenemos el enlace.

GitHub es una plataforma de desarrollo colaborativo para alojar proyecto mendiante el uso de sistema de control de versiones de Git

Para clonar un repositorio hacemos uso del siguiente comando:

```
git clone "[url del repositorio]"
```

Realiamos los pasos anteriores, luego de haber hecho un commit:

Hacemos uso **Git Push** para enviar la confirmación de los cambios

```
git push
```

# Uso de las Ramas

Permite obtener el codigo fuente del proyecto en una nueva carpeta para solucionar algun error que se presente, una ves el error ya solucionado este se debe incorporar al proyecto orinal estableciendo los cambios que se han realizado.

Para crear una rama

```
git branch "nombre de la rama"
```
Para realizar los cambios realizados e integrandolo a la rama principal hacemos uso de **merge**

```
git merge master origin/nombre de la rama
```

Para movernos por las distintas ramas, hacemos uso del comando:

```
git checkout "nombre de la rama"
```
Para listar todas las ramas

```
git branch --a
```

# Uso del Fork
Permite obtener una copia del proyecto y poder realizarle cambios
sin alterar al proyecto orignal.

Para agregar un remoto, permite asociar el repositorio de otro
```
git remote add upstream [url ]
```

Permite traer los cambios de la rama remoto principal a la rama individual

```
git fecth upstream
```

Permite integrar cambios de la rama Principal a la rama individual 

```
git merge develop upstream/develop
```

Para mostrar los cambios del repositorio a la maquina realizar lo siguente

```
git pull
```

> Roger Tomairo Paniagua
