from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CNAB
import pytz
from datetime import datetime
from .serializer import CNABSerializer
from django.db.models import Sum, Case, When, FloatField
from django.shortcuts import render

class CNABView(APIView):
    def post(self, request):
        file = request.FILES.get('file')
        if not file:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        dados = file.read().decode()
        lines = dados.split('\n')
        for dados in lines:
            tipo = dados[0]
            data = datetime.strptime(dados[1:5] + "/" + dados[5:7] + "/" + dados[7:9], '%Y/%m/%d') #8
            valor = dados[9:19]
            cpf = dados[19:30] 
            cartao = dados[30:42] 
            hora = dados[42:44] + ":" + dados[44:46] + ":" + dados[46:48]
            dono_loja = dados[48:61]
            nome_loja = dados[61:80]

            if tipo == "1":
                descricao = "Boleto"
                natureza = "Entrada"
                sinal = "+"

            elif tipo == "2":
                descricao = "Boleto"
                natureza = "Saida"
                sinal = "-"

            elif tipo == "3":
                descricao = "Boleto"
                natureza = "Saida"
                sinal = "-"

            elif tipo == "4":
                descricao = "Boleto"
                natureza = "Entrada"
                sinal = "+"

            elif tipo == "5":
                descricao = "Boleto"
                natureza = "Entrada"
                sinal = "+"

            elif tipo == "6":
                descricao = "Boleto"
                natureza = "Entrada"
                sinal = "+"

            elif tipo == "7":
                descricao = "Boleto"
                natureza = "Entrada"
                sinal = "+"

            elif tipo == "8":
                descricao = "Boleto"
                natureza = "Entrada"
                sinal = "+"

            elif tipo == "9":
                descricao = "Boleto"
                natureza = "Saida"
                sinal = "-"

            hora_utc = datetime.strptime(hora, '%H:%M:%S').replace(tzinfo=pytz.timezone('Brazil/East'))

            cnab = CNAB(tipo=tipo, descricao = descricao, data=data, valor= int(valor)/100, cpf=cpf,
                        cartao=cartao, hora=hora_utc, dono_loja=dono_loja,
                        nome_loja=nome_loja, natureza=natureza, sinal=sinal)
            cnab.save()
        
        return Response(status=status.HTTP_201_CREATED)


    def get(self, request):
        if CNAB.objects.all().exists():
            empresas = CNAB.objects.values('nome_loja').annotate(saldo=Sum(Case(When(natureza='Entrada', then='valor'), default=0, output_field=FloatField())) - Sum(Case(When(natureza='Saida', then='valor'), default=0, output_field=FloatField()))).order_by('nome_loja')
            operacoes = CNAB.objects.all()
            return render(request, 'form/forms.html', {'empresas': empresas, 'operacoes': operacoes})
        else:
            return render(request, 'form/forms.html')
