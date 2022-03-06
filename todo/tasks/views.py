from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Task
from .forms import TaskForm
from django.contrib import messages
import datetime


@login_required  # restricao..so loga quem tiver login no sistema
def taskList(request):
    # implementando o search
    search = request.GET.get('search')
    filter = request.GET.get('filter')  # esse filter eh da busca de tarefa
    
    # aqui eu estou filtrando as tarefas do ultimos 30 dias para o dashboard --tarefa pronta e ainda mostra o usuario
    tasksDoneRecently = Task.objects.filter(done='done', updated_at__gt=datetime.datetime.now()-datetime.timedelta(days=30), user=request.user).count()
    tasksDone = Task.objects.filter(done = 'done', user=request.user).count() # tarefa pronta
    tasksDoing = Task.objects.filter(done = 'doing', user=request.user).count() # tarefa em andamento
    
    
    if search:
        # filtra o usuario que ta autentiacado
        tasks = Task.objects.filter(title__icontains=search, user=request.user)

    # filtrando as tarefas concluidas
    elif filter:
        # filtra o usuario que ta autentiacado
        tasks = Task.objects.filter(done=filter, user=request.user)

    else:
        # pegando todos os objetos do banco
        tasks_list = Task.objects.all().order_by(
            '-created_at').filter(user=request.user)  # usuario autenticado
        # implementando paginacao, vai no template de list.html
        paginator = Paginator(tasks_list, 3)
        page = request.GET.get('page')
        tasks = paginator.get_page(page)
        # jogando pro template
        # jogando o resultado do dashboard no template(tasksrecently, tasksdone,tasksdoing ) 
    return render(request, 'tasks/list.html', {'tasks': tasks, 
                                               'tasksrecently': tasksDoneRecently,'tasksdone': tasksDone, 'tasksdoing':tasksDoing}) 


@login_required
def taskView(request, id):
    task = get_object_or_404(Task, pk=id)  # retornando um objeto apenas
    # jogando para o template
    return render(request, 'tasks/task.html', {'task': task})


@login_required
def newTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():  # ele salva e volta pra home..pagina principal
            task = form.save()
            task.done = 'doing'
            task.save()
            # mostra qdo o usuario add uma tarefa e aparece apenas para este user logado
            task.user = request.user
            messages.info(request, 'Tarefa criada com sucesso !')
            return redirect('/')
    else:
        form = TaskForm()  # adicionando nova tarefa
        return render(request, 'tasks/addtask.html', {'form': form})


@login_required
def editTask(request, id):  # editando uma tarefa
    task = get_object_or_404(Task, pk=id)
    form = TaskForm(instance=task)

    if(request.method == 'POST'):
        form = TaskForm(request.POST, instance=task)

        if(form.is_valid()):
            task.save()
            messages.info(request, 'Tarefa atualizada com sucesso !')
            return redirect('/')
        else:
            return render(request, 'tasks/edittask.html', {'form': form, 'task': task})
    else:
        return render(request, 'tasks/edittask.html', {'form': form, 'task': task})


@login_required
def deleteTask(request, id):  # delete uma tarefa
    task = get_object_or_404(Task, pk=id)  # busca a tarefa
    task.delete()
    # mensagem dizendo que apagou, depois ir no template list.html
    messages.info(request, 'Tarefa deletado com sucesso !')
    return redirect('/')


@login_required
def changeStatus(request, id):
    task = get_object_or_404(Task, pk=id)

    if(task.done == 'doing'):  # se tarefa tiver pronta.. pronta
        task.done = 'done'
    else:
        task.done = 'doing'  # senao esta fazendo
    task.save()

    return redirect('/')


@login_required
def helloWorld(request):
    return HttpResponse('Ola mundo')


@login_required
def yourName(request, name):
    return render(request, 'tasks/yourname.html', {'name': name})
