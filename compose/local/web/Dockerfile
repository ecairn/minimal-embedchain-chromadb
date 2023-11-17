FROM nginx:1.24.0

LABEL maintainer="denis.jean@ecairn.com"

# Update for security reason
RUN apt-get update && apt-get upgrade -q -y -o Dpkg::Options::="--force-confold"

# establish where Nginx should look for files
ENV APP_ROOT /app

# Set our working directory inside the image
WORKDIR $APP_ROOT

# create log directory
RUN mkdir log

# copy over static assets
COPY public public/

# Copy Nginx config template
COPY compose/local/web/nginx.conf /tmp/docker.nginx

# substitute variable references in the Nginx config template for real values from the environment
# put the final config in its place
RUN envsubst '$APP_ROOT' < /tmp/docker.nginx > /etc/nginx/conf.d/default.conf

EXPOSE 80

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Use the "exec" form of CMD so Nginx shuts down gracefully on SIGTERM (i.e. `docker stop`)
CMD [ "nginx", "-g", "daemon off;" ]
