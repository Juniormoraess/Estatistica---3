import pandas as pd
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import MultiComparison

tratamento = pd.read_csv('anova.csv', sep = ';')

tratamento.boxplot(by = 'Remedio', grid = False)

modelo1 = ols('Horas ~ Remedio', data = tratamento).fit()
resultado1 = sm.stats.anova_lm(modelo1)

modelo2 = ols('Horas ~ Remedio * Sexo', data = tratamento).fit()
resultado2 = sm.stats.anova_lm(modelo2)

mc = MultiComparison(tratamento['Horas'], tratamento['Remedio'])
resultado_teste = mc.tukeyhsd()

print()
print(resultado_teste)
print()
grafico = resultado_teste.plot_simultaneous()
grafico.show()
print()
