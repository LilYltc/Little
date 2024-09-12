import os
import subprocess

def check_java_version():
    try:
        # Verificamos la versión instalada de Java
        output = subprocess.check_output(["java", "-version"], stderr=subprocess.STDOUT)
        version_line = output.decode().split('\n')[0]
        # Extraemos el número de versión
        if "version" in version_line:
            version = version_line.split('"')[1]
            if version.startswith("21"):
                print("JDK 21 ya está instalado.")
                return True
        return False
    except Exception as e:
        print(f"No se pudo verificar la versión de Java: {e}")
        return False

def install_jdk_21():
    # Descargar JDK 21 de OpenJDK
    print("Instalando JDK 21...")
    os.system("wget https://download.oracle.com/java/21/latest/jdk-21_linux-x64_bin.tar.gz")
    os.system("tar -xvzf jdk-21_linux-x64_bin.tar.gz")
    
    # Mover el JDK a /opt
    os.system("sudo mv jdk-21 /opt/")
    
    # Configurar variables de entorno
    os.system("sudo update-alternatives --install /usr/bin/java java /opt/jdk-21/bin/java 1")
    os.system("sudo update-alternatives --install /usr/bin/javac javac /opt/jdk-21/bin/javac 1")
    
    # Establecer JDK 21 como predeterminado
    os.system("sudo update-alternatives --set java /opt/jdk-21/bin/java")
    os.system("sudo update-alternatives --set javac /opt/jdk-21/bin/javac")

    # Comprobar si se instaló correctamente
    if check_java_version():
        print("JDK 21 instalado correctamente.")
    else:
        print("Hubo un problema durante la instalación de JDK 21.")

# Verificar si ya está instalado JDK 21, si no, proceder con la instalación
if not check_java_version():
    install_jdk_21()
