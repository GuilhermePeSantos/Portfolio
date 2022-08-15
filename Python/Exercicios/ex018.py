from math import sin,radians,cos,tan
AG = float(input('Digite o ângulo que você deseja:'))
SN = sin(radians(AG))
CO = cos(radians(AG))
TG = tan(radians(AG))
print('O angulo {}º tem o SENO de: {:.2f}'.format(AG,SN))
print('O angulo {}º tem o COSSENO de: {:.2f}'.format(AG,CO))
print('O angulo {}º tem a tangente de: {:.2f}'.format(AG,TG))