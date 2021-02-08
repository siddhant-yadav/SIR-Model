import subprocess

def install_dependecies():
    print('Downloading dependencies. Please wait...')
    for package in ['numpy', 'pandas', 'cv2-python']:
        p1 = subprocess.run(['pip','install', package], shell=True, capture_output=True, text=True)
        print(p1.stdout)
    print('Dependencies installed. Exiting.')

if __name__ == '__main__':
    install_dependecies()
