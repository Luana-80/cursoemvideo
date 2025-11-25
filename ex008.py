#Desafio8: Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros
m = float(input('Escreva uma distancia em metros = '))
km = m / 1000
hm = m / 100
dam = m / 10
dcm = m * 10
cm = m * 100
mm = m * 1000
print('A medida de {:.1f} m corresponde a: \n{:.3f} Km, \n{:.2f} Hm, \n{:.1f} Dm, \n{:.1f} dcm, \n{:.2f} cm, \n{:.3f} mm'.format(m, km, hm, dam, dcm, cm, mm))
