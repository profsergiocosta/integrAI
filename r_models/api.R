library(plumber)
# 'app.R' is the location of the file containing your endpoint functions
r <- plumb("app.R")
# get port number from environment variable
#port <- strtoi(Sys.getenv("PORT"))

#r$setCors("*")  # Permite requisições de todas as origens

r$run(port=5000, host='0.0.0.0')


