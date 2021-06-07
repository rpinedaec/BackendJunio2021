# Roger Crishtofer Tomairo Paniagua
___

# GIT 
Es un software diseñado para el uso de control de versiones de código de forma distribuida.
## Primeros Pasos
___

Establecer el nombre de usuario

```
git config --global user.name "Roger Tomairo"
```
Establecer el Correo Electrónico

```
git config --global user.email royertomairo@gmail.com
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

Hacemos uso **Git Push** para enviar la confirmación

```
git clone "[url del repositorio]"
```