import subprocess
import requests
import time
import sys


def get_hwid():
    """
    Obtiene el HWID de la máquina utilizando el comando 'wmic csproduct get uuid'.
    """
    output = subprocess.check_output('wmic csproduct get uuid').decode().strip()
    hwid = output.split('\n')[1].strip()
    return hwid


def check_device_authorization(auth_url, hwid):
    """
    Verifica si el dispositivo está autorizado mediante una solicitud GET al enlace de autorización.
    Devuelve True si el dispositivo está autorizado y False si no lo está.
    """
    try:
        response = requests.get(auth_url, timeout=5)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print('[ERROR] Failed to fetch authorization data:', str(e))
        time.sleep(5)
        sys.exit(1)

    if hwid in response.text:
        print('[SUCCESS] Device authorized.')
        print('[LOGS] Welcome!')
        return True
    else:
        print('[ERROR] Device not authorized.')
        print('[LOGS] HWID:', hwid)
        time.sleep(5)
        sys.exit(1)


def set_terminal_title(title):
    """
    Establece el título de la ventana del terminal.
    """
    if sys.platform.startswith('win32'):
        os.system(f'title {title}')
    else:
        sys.stdout.write(f'\x1b]2;{title}\x07')
        

def main():
    # Obtener el HWID de la máquina
    hwid = get_hwid()

    # Realizar la verificación de autorización
    auth_url = 'yourpastebinrawlink'
    is_authorized = check_device_authorization(auth_url, hwid)
    
    # Establecer el título de la ventana del terminal
    set_terminal_title('Device Authorization')

    # Esperar a que el usuario presione una tecla para salir
    if is_authorized:
        input('[INFO] Press any key to exit.')
    else:
        print('[INFO] Exiting...')
        time.sleep(5)


if __name__ == '__main__':
    main()
