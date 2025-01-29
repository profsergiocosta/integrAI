#* @apiTitle Plumber Example API
#* @apiDescription Plumber example description.

#* Echo back the input
#* @param msg The message to echo
#* @get /echo
function(msg = "") {
    list(msg = paste0("The message is: '", msg, "'"))
}

#* Plot a histogram
#* @serializer png
#* @get /plot
function() {
    rand <- rnorm(100)
    hist(rand)
}

#* Return the sum of two numbers
#* @param a The first number to add
#* @param b The second number to add
#* @post /sum
function(a, b) {
    as.numeric(a) + as.numeric(b)
}

#* Retorna uma mensagem de boas-vindas
#* @get /hello
function() {
  list(message = "Olá! Sua API Plumber está rodando no Docker.")
}

#* Calcula a média de um vetor numérico
#* @post /mean
#* @param nums:numeric Lista de números
function(nums) {
    # Calcula a média
    resultado <- mean(as.numeric(nums))
    
    # Retorna a resposta no formato esperado pelo frontend
    list(data = resultado)  # O campo 'data' conterá o valor da média
}
