from django.shortcuts import render
import folium
import pandas as pd
from folium import plugins
from folium.plugins import HeatMap, Geocoder, MarkerCluster
from .models import NC
from datetime import datetime
from .filter import NCFilter
from django.db import models
from django.views.generic import TemplateView

### Home ####
class HomeView(TemplateView):
    
    template_name = "index.html"

### Mensagens#############3
def Messages (request):
    ncs = NC.objects.all()
    now = datetime.now().date()
    html = ['messages.html', 'index.html']
    messages = []
    messages_count = len(messages)
    for nc in ncs:
        if nc.Prazo <= now:
            messages.append('NC Vencida! A NC ' + nc.Numero + ' do TN ' + nc.TN + ' do município de ' + nc.Municipio + ' está vencida!')
    context = {
        'messages' : messages,
    }
    return render(request, html, context) 

########### Tabelas ####################
class Table(TemplateView):
    item = NC.objects.all()
    template_name = 'tables.html'

def items(request):
    item = NC.objects.all()
    context = {
        'item': item,
    }
    return render(request,'tables.html',context)


########## Dashboard #######################
def dashboard (request):
    
    item = NC.objects.all()

    #mapa
    nc_list = NC.objects.values_list('latitude', 'longitude')
   
    total_TN = item.count()
    #filtro
    myFilter = NCFilter(request.GET, queryset=item)
    item = myFilter.qs
    total_atendidas = item.filter(Situacao='Atendida').count()
    total_nao_atendidas = item.filter(Situacao='Pendente').count()
  
    #Criar o mapa

    
    map1 = folium.Map(location=[-27.13, -50.9219642], zoom_start=7,  tiles='cartodbpositron')
    plugins.MarkerCluster(nc_list).add_to(map1)
    map1 = map1._repr_html_()


    # alertas
    ncs = NC.objects.all()
    now = datetime.now().date()
    messages = []
    messages_count = len(messages)
    for nc in ncs:
        if nc.Prazo <= now and nc.Situacao == 'Pendente':
            messages.append('NC Vencida! A NC ' + nc.Numero + ' do TN ' + nc.TN + ' do município de ' + nc.Municipio + ' está vencida!')
    
    
    #Grafico de barras para vencidas e não vencidas

    vencidas = 0
    concluidas = 0
    nao_vencidas =0
    for nc in ncs:
        if nc.Prazo <= now and nc.Situacao == 'Pendente':
            vencidas = vencidas +1
        if nc.Situacao == 'Atendida':
            concluidas = concluidas + 1
        if nc.Prazo <= now and nc.Situacao == 'Pendente':
            nao_vencidas = nao_vencidas + 1
    
    context = {
        'myFilter': myFilter,
        'vencidas': vencidas,
        'nao_vencidas': nao_vencidas,
        'concluidas': concluidas,
        'item': item,
        'map1': map1,
        'messages':messages,
        'messages_count': messages_count, 
        'total_atendidas': total_atendidas,
        'total_TN': total_TN,
        'total_nao_atendidas': total_nao_atendidas,

    }

    

    return render(request, 'dashboard.html', context)

