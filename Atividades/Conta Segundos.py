segundos_str = input("Por favor, entre com o número de segundos que deseja converter: ")
total_segs = int(segundos_str) # Esse comando converte a entrada dos segundo de string para números inteiros

horas = total_segs // 3600 # Aqui é feita uma divisão inteira, ou seja, pega-se apenas o resultado inteiro e não é considerado o resto da divisão e, portanto, não se considera as dizimas.
segs_restantes = total_segs % 3600 # Ao utilizar o "%" na divisão pega-se o resto da divisão, apenas
minutos = segs_restantes // 60 # Idem linha 4
segs_restantes_final = segs_restantes % 60 # Idem linha 5

print(horas, "horas, ", minutos, "minutos e", segs_restantes_final, "segundos.")