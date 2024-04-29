from pytube import YouTube

# URL del video de YouTube
url = 'https://www.youtube.com/watch?v=lc1Xaf6VVCw'

# Crear objeto YouTube
video = YouTube(url)

# Descargar el audio en la mejor calidad disponible
audio = video.streams.filter(only_audio=True).first()
audio.download(output_path='ruta_de_guardado')

print("Audio descargado exitosamente.")