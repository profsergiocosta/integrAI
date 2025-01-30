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



#* Um exemplo simples de previsão
#* @post /predict
#* @param req O corpo da requisição (JSON contendo 'vala' e 'coas')
#* @serializer json
function(req) {
  
  # Parse do JSON recebido
  body <- jsonlite::fromJSON(req$postBody)
  
  # Validar se os campos esperados existem
  if (!"vala" %in% names(body) || !"coas" %in% names(body)) {
    return(list(error = "Os campos 'vala' e 'coas' são obrigatórios."))
  }
  
  # Carregar o modelo salvo
  modelo <- readRDS("modelo_linear.rds")
  
  # Criar um data frame com os valores recebidos
  novo_valor <- data.frame(
    vala = as.numeric(body$vala),  # Converte 'vala' para numérico
    coas = body$coas
  )
  
  # Fazer a previsão
  previsao <- predict(modelo, newdata = novo_valor)
  
  # Retorna a resposta no formato JSON
  list(previsao = previsao[1])
}