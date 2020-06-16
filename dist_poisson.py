from scipy.stats import poisson

## Média de acidentes de carro = 2/dia

## Qual a probabilidade de ocorrerem 3 acidentes no dia?
probExata = poisson.pmf(12, 10)

## Qual a probabilidade de ocorrerem no máximo 3 acidentes no dia?
probMenor = poisson.cdf(3, 2)

## Qual a probabilidade de ocorrerem mais de 3 acidentes no dia?
probMaior = poisson.sf(3, 2)

print()
print('Os resultados das probabilidades sao: ')
print(probExata)
print(probMenor)
print(probMaior)
print()