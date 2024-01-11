import calendar
from datetime import datetime
data_hoje = datetime.now()
ano = data_hoje.year
mes = data_hoje.month
calendario = calendar.month(ano, mes)
print(f'Calendário de {calendar.month_name[mes]} de {ano}:\n')
print(calendario)