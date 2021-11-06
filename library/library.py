import psutil

def cpu_percent():
    print("Porcentagem da CPU: {}".format(psutil.cpu_freq))
    return  psutil.cpu_freq()

def virtual_memory():
    print("Uso da mémoria virtual: {}".format(psutil.virtual_memory()))
    return psutil.virtual_memory()

def perc_ram():
    print("Percentual de uso da RAM: {}".format(psutil.virtual_memory().percent))
    return psutil.virtual_memory().percent

def cpu_status():
    print("Estatisticas da CPU", psutil.cpu_stats()) 
    return psutil.cpu_stats()

def avaible_memory():
    print("Memoria disponivel: {}".format(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total))
    return psutil.virtual_memory().available * 100 / psutil.virtual_memory().total

def prints():
    print("Porcentagem da CPU: {}".format(psutil.cpu_freq()))
    print("Uso da mémoria virtual: {}".format(psutil.virtual_memory()))
    print("Percentual de uso da RAM: {}".format(psutil.virtual_memory().percent))
    print("Estatisticas da CPU", psutil.cpu_stats()) 
    print("Memoria disponivel: {}".format(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total))

prints()