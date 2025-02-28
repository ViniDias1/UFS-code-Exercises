#!/bin/bash

echo ¨Adicionando users- ¨

useradd -m admin1
usermod -aG sudo admin1
passwd $admin1

useradd -m admin2
usermod -aG sudo admin2
passwd $admin2


<<comment
    usuario=$1

    adduser $usuario

    echo ¨senha-¨
    passwd $usuario
comment
