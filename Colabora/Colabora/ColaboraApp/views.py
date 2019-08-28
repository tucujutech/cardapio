from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST, require_GET
from django.views.generic import ListView, DetailView, DeleteView
from django.views.generic.base import View
from django_weasyprint import WeasyTemplateResponseMixin

from .utils import generate_pdf
from .models import *


def Login(request,template_name='login.html'):
    next=request.GET.get('next','dashboard/')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(next)
        else:
            messages.error(request,'Usuário ou senha incorretos')
            return HttpResponseRedirect(settings.LOGIN_URL)
    return render(request,template_name,{'redirect_to':next})

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
        return render(request,template_name='colaborador/newColaborador.html')

    def post(self, request):
        if request.method == 'POST':
            nome= request.POST['nome']
            sobrenome= request.POST['sobrenome']
            nascimento= request.POST['nascimento']
            rg= request.POST['rg']
            cpf= request.POST['cpf']
            telefone= request.POST['telefone']
            cnh = request.POST['cnh']
            cnh_tipo= request.POST['cnh_tipo']
            sexo_choices = request.POST['sexo']
            #foto_colaborador = request.POST['foto_colaborador']

            colaborador= Colaborador.objects.get_or_create(nome=nome, sobrenome=sobrenome,
                                                    nascimento=nascimento, rg=rg,
                                                    cpf=cpf, telefone=telefone,
                                                    cnh=cnh, cnh_tipo=cnh_tipo, sexo_choices=sexo_choices)
            colaborador.save()
        return redirect('colabList/')


class ColabList(ListView):
    model = Colaborador
    template_name = 'colaborador/colabList.html'


class ColabDetail(View):

    def get(self, request, pk, *args, **kwargs):
        colab= Colaborador.objects.filter(pk=pk)
        formacao= Formacao.objects.filter(colaborador=pk)
        context = {'colab':colab, 'formacao':formacao}
        template_name = 'colaborador/colabDetail.html'
        pdf = generate_pdf(template_name, context)
        return HttpResponse(pdf, content_type='application/pdf')
        #return render(request,template_name,context)





# Is missing the Update class for Colaborator

class ColabDelete(DeleteView):
    model = Colaborador
    template_name = 'colaborador/colab_delete.html'
    success_url = reverse_lazy('colabList/')


# =================== Here starts Academics Formations classes ===========================
class FormacaoCreate(View):

    def get(self,request):
        colaborador= Colaborador.objects.values_list('nome', flat= True)
        tipo_formacao  = TipoFormacao.objects.values_list('tipo_formacao',flat=True)
        context = {'object':colaborador, 'object2':tipo_formacao}
        template_name = 'formacao/formaRegister.html'
        return render(request,template_name=template_name,context=context)


    def post(self, request):
        colaborador = request.POST['colaborador']
        colaborador = Colaborador.objects.get(nome=colaborador)
        tipo_formacao = request.POST['tipo_formacao']
        tipo_formacao = TipoFormacao.objects.get(tipo_formacao=tipo_formacao)
        nome_curso = request.POST['nome_curso']
        instituicao = request.POST['instituicao']
        dt_inicio = request.POST['dt_inicio']
        dt_termino = request.POST['dt_termino']

        formacao=Formacao.objects.create(colaborador=colaborador, tipo_formacao=tipo_formacao, nome_curso=nome_curso, instituicao=instituicao,
                                         dt_inicio=dt_inicio, dt_termino=dt_termino)
        formacao.save()
        return redirect('formaList/')


class FormacaoList(ListView):
    model = Formacao
    template_name = 'formacao/formaList.html'

class FormacaoDelete(DeleteView):
    model = Formacao
    template_name = 'formacao/formaDelete.html'
    success_url = reverse_lazy('formaList/')


# =========================== Here starts Department classes ==============================

class DerpartmentView(View):
    def get(self,request):
        template_name='department/departmentRegister.html'
        departamento= Departamento.objects.all()

        return render(request, template_name,context={'object_list':departamento})

    def post(self,request):
        nomeDepartamento = request.POST['nomeDepartamento']

        departamento = Departamento.objects.create(nomeDepartamento=nomeDepartamento)
        departamento.save()
        return redirect('departamento/')


class DepartmentDelete(DeleteView):
    model = Departamento
    template_name = 'department/departmentDelete.html'
    success_url = reverse_lazy('departamento/')


# ==================== Here starts Função classes ===============================================
class FuncaoRegister(View):

    def get(self, request):
        depart = Departamento.objects.values_list('nomeDepartamento', flat=True)
        funcao= Funcao.objects.all()
        template_name = 'funcao/funcaoRegister.html'
        return render(request, template_name, context={'object': depart, 'object2':funcao})

    def post(self,request):
        nomeFuncao= request.POST['nomeFuncao']
        departamento = request.POST['departamento']
        departamento = Departamento.objects.get(nomeDepartamento=departamento)

        funcao=Funcao.objects.create(nomeFuncao=nomeFuncao, departamento=departamento)
        funcao.save()
        return redirect('funcao/')


class FuncaoDelete(DeleteView):
    model = Funcao
    template_name = 'funcao/funcaoDelete.html'
    success_url = reverse_lazy('funcao/')


# ======================================================================


