#parametros de entrada
cliente={}
cliente['compras_ultimos_90_dias']=int(input())
cliente['RFM']=input()
cliente['dias_desde_ultima_compra']=input()
cliente['quejas']=input()
cliente['interacciones_con_el_servicio_al_cliente']=input()
cliente['seciones_app']=int(input())
cliente['dias_sin_compra']=int(input())
print(cliente)

#base de conocimiento

if cliente['compras_ultimos_90_dias']>90:
    cliente['riesgo']='alto'
if cliente['quejas']>2:
    cliente['status']='insatisfecho'
if cliente['uso_app']


#ingenieria de features
score_recencia=1/(1+cliente['dias_sin_compra'])
score_frecuencia=cliente['compras_ultimos_90_dias']/90
score_monetario=
score_compromiso=cliente['seciones_app']/7
score_satisfaccion=1-(cliente['quejas']/cliente['interacciones_con_el_servicio_al_cliente'])

#salida
print('cliente tiene una probabilidad de: ',posibilidad_de_retirarse)
print('debe de tomar la siguientes acciones: ',acciones)
print('valor que se pierde si se deja ir al cliente: ', CLV)