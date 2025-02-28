FROM nginx:1.24.0-alpine-slim

LABEL version="1.0.0" description="blackcandy" mantainer="vinidias <vinidias@academico.ufs.br"

WORKDIR /usr/share/nginx/html

COPY /Lab-de-Redes/nginx.conf /usr/share/nginx/
COPY /Lab-de-Redes/index.html /usr/share/nginx/html
COPY /Lab-de-Redes/blackcandy /usr/share/nginx/

EXPOSE 80

CMD ["nginx"]
