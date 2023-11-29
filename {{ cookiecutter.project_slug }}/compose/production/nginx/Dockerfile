FROM nginx:latest

RUN rm /etc/nginx/conf.d/default.conf
COPY default.conf /etc/nginx/conf.d

# ENV HOME=/home/app
# ENV APP_HOME=/home/app/web
# RUN mkdir ${APP_HOME}
# RUN mkdir ${APP_HOME}/static
# WORKDIR ${APP_HOME}