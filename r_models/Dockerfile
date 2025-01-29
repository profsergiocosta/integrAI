
FROM rstudio/plumber
# Create and change to the app directory.

WORKDIR /usr/src/app
# Copy local code to the container image.

COPY . .

#RUN Rscript requirements.R

EXPOSE 5000
# Run the web service on container startup.
CMD [ "Rscript", "api.R"]