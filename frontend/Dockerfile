FROM teracy/angular-cli as frontendbuilder
RUN mkdir -p /repo_analyzer

COPY ./angular.json /frontend_dir/angular.json
COPY ./package.json /frontend_dir/package.json
COPY ./tsconfig.json /frontend_dir/tsconfig.json
COPY ./tslint.json /frontend_dir/tslint.json

WORKDIR /frontend_dir
RUN npm install
COPY ./e2e /frontend_dir/e2e
COPY ./src     /frontend_dir/src
COPY ./browserslist /frontend_dir
COPY ./karma.conf.js /frontend_dir
COPY ./package-lock.json /frontend_dir
COPY ./tsconfig.app.json /frontend_dir
COPY ./tsconfig.spec.json /frontend_dir
RUN ng build --prod
FROM nginx:alpine
ENV DEBIAN_FRONTEND noninteractive


# Setup nginx
COPY ./nginx.conf /etc/nginx/nginx.conf
COPY ./frontend.conf /etc/nginx/conf.d/
RUN rm /etc/nginx/conf.d/default.conf


COPY --from=frontendbuilder /frontend_dir/dist/frontend /static

