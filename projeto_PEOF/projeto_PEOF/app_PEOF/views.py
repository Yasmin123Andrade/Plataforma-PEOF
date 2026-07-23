from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render


def logout_view(request):
    logout(request)
    return redirect('login')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def home(request):
    return render(request, 'index.html')


@login_required
def sobre(request):
    return render(request, 'sobre.html')


@login_required
def conteudos(request):
    return render(request, 'conteudos.html')


@login_required
def medalhistas(request):
    return render(request, 'medalhistas.html')


@login_required
def depoimentos(request):
    return render(request, 'depoimentos.html')


@login_required
def materiais(request):
    return render(request, 'materiais.html')


@login_required
def contato(request):
    return render(request, 'contato.html')
