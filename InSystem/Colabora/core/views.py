from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView
from django.views.generic.base import View

from core.models import Colaborador, Formacao, Departamento, Funcao


def dashboard(request, template_name='base.html'):
    return render(request, template_name)

# =============== Security ================================================
# ============ Here starts User classes ===================================


class RegUser(View):

    def get (self, request, *args, **kwargs):
       return render(request, template_name='user/userRegistro.html')

    def post(self, request, *args, **kwargs):
           if request.method == 'POST':
              username = request.POST['username']
              #first_name=request.POST['first_name']
              #last_name=request.POST['second_name']
              email = request.POST['email']
              password = request.POST['password']
              tipo = request.POST['tipo_user']
              if tipo == 'Administrador':
                user = User.objects.create_user(username, email, password)
                user.is_staff = True
                user.save()
              else:
                user = User.objects.create_user(username,  email, password)
           return redirect('Colaborador/listuser/')


# ======================  Here starts Colaborador classes =====================

class ColaboradorCreate(View):
    def get(self, request):
        funcao = Funcao.objects.values_list('nomeFuncao', flat=True)
        departamento = Departamento.objects.values_list('nomeDepartamento',flat=True)
        context = {'funcao':funcao, 'departamento':departamento}
        return render(request,template_name='core/colaborador/newColaborador.html', context = context)

    def post(self, request):
        if request.method == 'POST':
            nome= request.POST['nome']
            nascimento= request.POST['nascimento']
            rg= request.POST['rg']
            cpf= request.POST['cpf']
            telefone= request.POST['telefone']
            cnh = request.POST['cnh']
            cnh_tipo= request.POST['cnh_tipo']
            sexo_choices = request.POST['sexo']
            #foto_colaborador = request.POST['foto_colaborador']

            colaborador= Colaborador.objects.get_or_create(nome=nome,
                                                    nascimento=nascimento, rg=rg,
                                                    cpf=cpf, telefone=telefone,
                                                    cnh=cnh, cnh_tipo=cnh_tipo, sexo_choices=sexo_choices)
            colaborador.save()
        return redirect('colabList/')


class ColabList(ListView):
    model = Colaborador
    template_name = 'colaborador/colabList.html'




# is missing detail view and generate report view



# Is missing the Update class for Colaborator

class ColabDelete(DeleteView):
    model = Colaborador
    template_name = 'colaborador/colab_delete.html'
    success_url = reverse_lazy('colabList/')
