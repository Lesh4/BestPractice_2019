""" Подсчет количества денег на отправку тектового сообщения """
STRING = str(input())
COAST_SIM = 23
COAST = 0
for SIM in STRING:
    COAST += COAST_SIM
RUB = COAST//100
COP = COAST%100
print(STRING, '   ', RUB, ' р. ', COP, ' коп.')
