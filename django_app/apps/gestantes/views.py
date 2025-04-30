from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse

from apps.gestantes.models import Gestante, Avaliacao

from apps.gestantes.forms import GestanteForms, AvaliacaoForm





def index(request):
        
        if not request.user.is_authenticated:
                messages.error(request, 'Usuário não logado')
                return redirect('login')

            # Filtra as gestantes pelo usuário logado
        gestantes = Gestante.objects.filter(usuario=request.user).order_by("-data_cadastro")

        return render(request, 'gestantes/index.html', {"cards":gestantes})
        

def lista_gestantes(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')

    # Filtra as gestantes pelo usuário logado
    gestantes = Gestante.objects.filter(usuario=request.user).order_by("-data_cadastro")

    return render(request, 'gestantes/lista_gestantes.html', {"cards": gestantes})


def gestante(request, gestante_id):

        if not request.user.is_authenticated:
                messages.error(request, 'Usuário não logado')
                return redirect('login')

        gestante = get_object_or_404(Gestante, pk=gestante_id)

        # Obter a última avaliação associada à gestante
        ultima_avaliacao = Avaliacao.objects.filter(gestante=gestante).order_by('-data_aplicacao').first()

        return render(request, 'gestantes/gestante.html', {'gestante':gestante, 'ultima_avaliacao': ultima_avaliacao})

def buscar(request):

            
        if not request.user.is_authenticated:
                messages.error(request, 'Usuário não logado')
                return redirect('login')

        gestantes = Gestante.objects.order_by("data_cadastro")

        if "buscar" in request.GET:
                nome_a_buscar = request.GET['buscar']
                if nome_a_buscar: 
                    gestantes = gestantes.filter(nome__icontains=nome_a_buscar)


        return render (request, 'gestantes/lista_gestantes.html', {"cards":gestantes})

def nova_gestante(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')


    form = GestanteForms

    if request.method == 'POST':
        form = GestanteForms(request.POST, request.FILES)

        
        if form.is_valid():

            gestante = form.save(commit=False)
            gestante.usuario = request.user    # Define o usuário autenticado
            gestante.save()
            messages.success(request, 'Nova gestante cadastrada!')
            return redirect('lista_gestantes')
        else:
            # Imprime os erros do formulário
            for field in form:
                if field.errors:
                    print(f"Erros no campo {field.name}: {field.errors}")
            # Se preferir, pode imprimir todos os erros de uma vez
            print("Erros gerais:", form.errors)

    return render(request, 'gestantes/nova.html', {'form': form})


def editar_gestante(request, gestante_id):

    if not request.user.is_authenticated:
                messages.error(request, 'Usuário não logado')
                return redirect('login')

    gestante = Gestante.objects.get(id=gestante_id)
    form = GestanteForms(instance=gestante)

    if request.method == 'POST':
        form = GestanteForms(request.POST, request.FILES, instance=gestante)
        if form.is_valid():
            print(request.POST)
            form.save()
            messages.success(request, 'gestante editada com sucesso')
            return redirect('lista_gestantes')

    return render(request, 'gestantes/editar.html', {'form':form, 'gestante_id': gestante_id})



def deletar_gestante(request, gestante_id):
    if not request.user.is_authenticated:
                messages.error(request, 'Usuário não logado')
                return redirect('login')

    gestante = Gestante.objects.get(id=gestante_id)
    gestante.delete()
    messages.success(request, 'Deleção feita com sucesso!')
    return redirect('lista_gestantes')



#def filtro(request, categoria):
    #gestantes = gestante.objects.order_by("-data_cadastro").filter( sexo=categoria)

    #return render(request, 'gestantes/index.html', {"cards": gestantes})




def avaliacao(request, gestante_id):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')

    gestante = get_object_or_404(Gestante, id=gestante_id)

    if request.method == 'POST':
        form = AvaliacaoForm(request.POST)
        if form.is_valid():
            # Cria o questionário mas não salva ainda
            questionario = form.save(commit=False)
            questionario.gestante = gestante  # Associar o questionário à gestante

            # Salvar o questionário com as probabilidades calculadas (já calculadas no form)
            questionario.save()

            # Redirecionar após o cadastro
            return redirect(reverse('gestante', args=[gestante_id]))
    else:
        form = AvaliacaoForm()

    return render(request, 'avaliacao/questionario.html', {'form': form, 'gestante': gestante})


def detalhes_risco(request, gestante_id, risco):
    if not request.user.is_authenticated:
                messages.error(request, 'Usuário não logado')
                return redirect('login')

    gestante = get_object_or_404(Gestante, id=gestante_id)
    
    ultima_avaliacao = Avaliacao.objects.filter(gestante=gestante).order_by('-data_aplicacao').first()

    # Lógica para exibir os detalhes do risco
    return render(request, 'avaliacao/detalhes_risco.html', {'gestante': gestante, 'risco': risco, 'ultima_avaliacao':ultima_avaliacao})


def chat(request):
    if not request.user.is_authenticated:
                messages.error(request, 'Usuário não logado')
                return redirect('login')

    return render(request, 'avaliacao/chat.html')
