#parametros de entrada

cliente={}
cliente['compras_90_dias']=int(input())
cliente['valor_total']=int(input())
cliente['quejas']=int(input())
cliente['interacciones']=int(input())
cliente['seciones_app']=int(input())
cliente['dias_sin_compra']=int(input())

#base de conocimiento

if cliente['dias_sin_compra']>90:
    cliente['status']='riesgo_alto'
elif cliente['quejas']>2:
    cliente['status']='insatisfecho'
elif cliente['seciones_app']<2:
    cliente['status']='señal_desenganche'
else:
    cliente['status']='regular'

#ingenieria de features

valor_promedio=100
score_recencia=1/(1+cliente['dias_sin_compra'])
score_frecuencia=cliente['compras_90_dias']/90
score_monetario=cliente['valor_total']/valor_promedio
score_compromiso=cliente['seciones_app']/7
if cliente['interacciones']>0:
    score_satisfaccion=1-(cliente['quejas']/cliente['interacciones'])
else:
    score_satisfaccion=1

#modelo

probabilidad = (
    0.3 * (1 - score_recencia) +
    0.2 * (1 - score_frecuencia) +
    0.2 * (1 - score_monetario) +
    0.2 * (1 - score_compromiso) +
    0.1 * (1 - score_satisfaccion)
    )
probabilidad = max(0, min(probabilidad, 1))

#decisiones

if cliente['status']=='insatisfecho' or probabilidad > 0.8:
    acciones="llamada + descuento"
elif probabilidad > 0.5:
    acciones="descuento"
elif probabilidad > 0.3:
    acciones="promocion"
else:
    acciones="nada"

#valor cliente

CLV=cliente['valor_total']*2

#salida

print('status del cliente: ', cliente['status'])
print(f'Cliente tiene una probabilidad de: {probabilidad:.2%}')
print('debe de tomar la siguientes acciones: ',acciones)
print('valor que se pierde si se deja ir al cliente: ', CLV)