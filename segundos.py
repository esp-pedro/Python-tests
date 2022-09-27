segundos = input ("Por favor, digite o número de segundos que deseja converter: ")
total_seg = int(segundos)

dias = total_seg // 86400
dias_restantes = total_seg % 86400
horas = dias_restantes // 3600
seg_restante = total_seg % 3600
minutos = seg_restante // 60
seg_restante_final = seg_restante % 60
anos = dias // 365

print(anos, "anos", dias, "dias,",horas, "horas,", minutos, "minutos e", seg_restante_final, "segundos.")