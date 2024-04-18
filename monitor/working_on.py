import psutil

def monitor():
    app_names = {}
    for proc in psutil.process_iter(['name']):
        if psutil.Process(proc.pid).status() != psutil.STATUS_ZOMBIE:
            app_name = proc.info['name']
            if app_name not in app_names:
                app_names[app_name] = True
                print(app_name)

monitor()