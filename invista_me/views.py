
from aiohttp import request
from django.shortcuts import render, redirect, HttpResponse
from .models import Gasto, Investimento
from .forms import GastoForm, InvestimentoForm
# Parte de investimentos


def investimentos(request):
    dados = {
        'dados': Investimento.objects.all()
    }
    return render(request, 'investimentos/investimentos.html', context=dados)


def detalheInvestimento(request, id_investimento):
    dados = {
        'dados': Investimento.objects.get(pk=id_investimento)
    }
    return render(request, 'investimentos/detalheInvestimento.html', context=dados)


def criarInvestimento(request):
    if request.method == 'POST':
        investimento_form = InvestimentoForm(request.POST)
        if investimento_form.is_valid():
            investimento_form.save()
        return redirect('investimentos')
    else:
        investimento_form = InvestimentoForm()
        formulario = {
            'formulario': investimento_form
        }
        return render(request, 'investimentos/novo_investimento.html', context=formulario)


def editarInvestimento(request, id_investimento):
    investimento = Investimento.objects.get(pk=id_investimento)
    # novo_investimento/1 -> GET
    if request.method == 'GET':
        formulario = InvestimentoForm(instance=investimento)
        return render(request, 'investimentos/novo_investimento.html', {'formulario': formulario})
    # caso requisição seja POST
    else:
        formulario = InvestimentoForm(request.POST, instance=investimento)
        if formulario.is_valid():
            formulario.save()
        return redirect('investimentos')


def excluirInvestimento(request, id_investimento):
    investimento = Investimento.objects.get(pk=id_investimento)
    if request.method == 'POST':
        investimento.delete()
        return redirect('investimentos')
    return render(request, 'investimentos/confirmarExclusaoInvestimento.html', {'item': investimento})
# Parte de gastos


def gastos(request):
    dadoGasto = {
        'dadoGasto': Gasto.objects.all()
    }
    return render(request, 'gastos/gastos.html', context=dadoGasto)


def detalheGasto(request, id_gasto):
    dadoDetalheGasto = {
        'dadoDetalheGasto': Gasto.objects.get(pk=id_gasto)
    }
    return render(request, 'gastos/detalheGasto.html', context=dadoDetalheGasto)


def criarGasto(request):
    if request.method == 'POST':
        gasto_form = GastoForm(request.POST)
        if gasto_form.is_valid():
            gasto_form.save()
        return redirect('gastos')
    else:
        gasto_form = GastoForm()
        formularioGasto = {
            'formularioGasto': gasto_form
        }
        return render(request, 'gastos/novo_gasto.html', context=formularioGasto)


def editarGasto(request, id_gasto):
    gasto = Gasto.objects.get(pk=id_gasto)
    # novo gasto /1 -> GET
    if request.method == 'GET':
        formularioGasto = GastoForm(instance=gasto)
        return render(request, 'gastos/novo_gasto.html', {'formularioGasto': formularioGasto})
    # caso a requisição seja POST
    else:
        formularioGasto = GastoForm(request.POST, instance=gasto)
        if formularioGasto.is_valid():
            formularioGasto.save()
        return redirect('gastos')


def excluirGasto(request, id_gasto):
    gasto = Gasto.objects.get(pk=id_gasto)
    if request.method == 'POST':
        gasto.delete()
        return redirect('gastos')
    return render(request, 'gastos/confirmarExclusaoGasto.html', {'item': gasto})
