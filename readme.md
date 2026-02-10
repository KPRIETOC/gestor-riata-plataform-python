# Comandos de GIT

git init // Inicializar repo
git clone <url-proyect> // clonar el repositorio
git fetch // Bajar cambios
git pull // Sincronizar cambios

git status // saber que cambios hay en el proyecto

git add . // agregar todos los cambios
git add [path-files]

git commit -m "especificación" // Crear registro con un comentario

git push -u origin // Subir cambios a la rama remoto / en la nube

// others
git branch [nuevo nombre de la rama]
git checkout -b [nuevo nombre de la rama]
git checkout [rama]

# Users

git config --global user.name kprietoc
git config --global user.email kdpc614@gmail.com
git config --global user.name VakanoDanSena
git config --global user.email vakanodan@gmail.com

# PREFIJOS PARA SUBIR CAMBIOS

git commit -m "[comand]"

feat: Se agrego o creo algo
fix: Se arreglo algo
remove: Se elimino
