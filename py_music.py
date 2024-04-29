import tkinter as tk
from pytube import YouTube
import humanize

#ejemplo de limite de edad
#https://www.youtube.com/watch?v=aezstCBHOPQ

def descargar_audio():
    url = entry_url.get()
    try:
        video = YouTube(url)
        audio = video.streams.filter(only_audio=True).first()
        file_size = audio.filesize
        file_size_readable = humanize.naturalsize(file_size)
        label_status.config(text=f"Tamaño del archivo: {file_size_readable}")
        audio.download(output_path='ruta_de_guardado')
        label_status.config(text="Audio descargado exitosamente.")
    except Exception as e:
        label_status.config(text="Error al descargar el audio.")
        print(e)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Descargador de audio de YouTube")
ventana.minsize(250, 100)

# Crear los widgets
label_url = tk.Label(ventana, text="Ingresa la URL del video:")
entry_url = tk.Entry(ventana)
boton_descargar = tk.Button(ventana, text="Descargar audio", command=descargar_audio)
label_status = tk.Label(ventana, text="")

# Organizar los widgets en la ventana
label_url.pack()
entry_url.pack()
boton_descargar.pack()
label_status.pack()

# Iniciar el bucle principal de la aplicación
ventana.mainloop()