import pyttsx3
import speech_recognition as sr
import datetime
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import scrolledtext
import threading
from modules import comandos_respostas as cr

# Inicialização única do sintetizador de voz
engine = pyttsx3.init()
engine.setProperty('rate', 200)
engine.setProperty('volume', 1)

def speak(audio):
    """Fala o texto passado como argumento."""
    def run():
        engine.say(audio)
        engine.runAndWait()
    threading.Thread(target=run).start()

def listen_microphone():
    """Escuta o microfone e retorna a frase capturada."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.8)
        log("Ouvindo...")
        try:
            audio = recognizer.listen(source)
            frase = recognizer.recognize_google(audio, language='pt-BR')
            log(f"Você disse: {frase}")
            return frase.lower()
        except sr.UnknownValueError:
            log('Não entendi')
            return ""
        except sr.RequestError as e:
            log(f"Erro ao acessar o serviço de reconhecimento de fala: {e}")
            return ""

class Assistant:
    def __init__(self, name):
        self.name = name
        self.shopping_list = []
        self.reminders = []

    def process_command(self, command):
        """Processa o comando reconhecido."""
        if any(phrase in command for phrase in cr.ADICIONAR_LISTA_COMPRAS):
            item = next((phrase for phrase in cr.ADICIONAR_LISTA_COMPRAS if phrase in command), "")
            self.add_to_shopping_list(command.replace(item, "").strip())
            return

        command_map = {
            tuple(cr.FUNCOES): self.list_features,
            tuple(cr.HORAS): self.tell_time,
            tuple(cr.DATA): self.tell_date,
            tuple(cr.TESTE): self.run_test,
            "mostrar lista de compras": self.show_shopping_list,
            "limpar lista de compras": self.clear_shopping_list,
            "adicionar lembrete": self.add_reminder,
            "mostrar lembretes": self.show_reminders,
            "limpar lembretes": self.clear_reminders,
        }

        for keys, action in command_map.items():
            if isinstance(keys, tuple) and any(key in command for key in keys):
                action()
                return
            elif isinstance(keys, str) and keys in command:
                action(command.replace(keys, "").strip())
                return

        if command == 'sair':
            speak("Até logo")
            root.quit()
            return

        speak("Comando não reconhecido")

    def add_to_shopping_list(self, item):
        self.shopping_list.append(item)
        log(f"{item} adicionado à lista de compras")
        speak(f"{item} adicionado à lista de compras")

    def show_shopping_list(self, *_):
        if self.shopping_list:
            items = ', '.join(self.shopping_list)
            log(f"Sua lista de compras tem: {items}")
            speak(f"Sua lista de compras tem: {items}")
        else:
            log("Sua lista de compras está vazia")
            speak("Sua lista de compras está vazia")

    def clear_shopping_list(self, *_):
        self.shopping_list.clear()
        log("Lista de compras limpa")
        speak("Lista de compras limpa")

    def add_reminder(self, reminder):
        self.reminders.append(reminder)
        log(f"Lembrete '{reminder}' adicionado")
        speak(f"Lembrete '{reminder}' adicionado")

    def show_reminders(self, *_):
        if self.reminders:
            items = ', '.join(self.reminders)
            log(f"Seus lembretes são: {items}")
            speak(f"Seus lembretes são: {items}")
        else:
            log("Você não tem lembretes")
            speak("Você não tem lembretes")

    def clear_reminders(self, *_):
        self.reminders.clear()
        log("Todos os lembretes foram apagados")
        speak("Todos os lembretes foram apagados")

    def list_features(self, *_):
        log(cr.FUNCIONALIDADES)
        speak(cr.FUNCIONALIDADES)

    def tell_time(self, *_):
        time = datetime.datetime.now().strftime('%H:%M')
        log(f"Agora são {time}")
        speak(f"Agora são {time}")

    def tell_date(self, *_):
        date = datetime.datetime.now().strftime('%d de %B de %Y')
        meses = {
            'January': 'janeiro', 'February': 'fevereiro', 'March': 'março', 'April': 'abril',
            'May': 'maio', 'June': 'junho', 'July': 'julho', 'August': 'agosto',
            'September': 'setembro', 'October': 'outubro', 'November': 'novembro', 'December': 'dezembro'
        }
        for eng, pt in meses.items():
            date = date.replace(eng, pt)
        log(f"Hoje é dia {date}")
        speak(f"Hoje é dia {date}")

    def run_test(self, *_):
        log("Teste executado com sucesso!")
        speak("Isso é uma fala de teste.")

# Função de log para a interface gráfica
def log(message):
    """Adiciona mensagens ao log da interface gráfica."""
    text_area.insert(tk.END, f"{message}\n")
    text_area.see(tk.END)

def start_listening():
    """Ativa o microfone e processa o comando capturado."""
    threading.Thread(target=listen_and_process).start()

def listen_and_process():
    command = listen_microphone()
    if assistant.name.lower() in command:
        command = command.replace(f"{assistant.name.lower()} ", "").strip()
        assistant.process_command(command)
    else:
        log("Nenhum comando reconhecido")

# Configuração da interface gráfica
assistant = Assistant(name="Eva")

root = tk.Tk()
root.title("Assistente Eva")

frame = tk.Frame(root)
frame.pack(pady=10)

display_image_path = "./assets/eva.png"
display_image = Image.open(display_image_path)
display_image = display_image.resize((100, 120), Image.LANCZOS)  # Redimensionar a imagem
display_photo = ImageTk.PhotoImage(display_image)
display_label = tk.Label(frame, image=display_photo)
display_label.pack(pady=10)

text_area = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=50, height=20, state='normal')
text_area.pack(pady=10)

microphone_image = Image.open("./assets/mic.png")
microphone_image = microphone_image.resize((30, 30), Image.LANCZOS)  # Redimensionar imagem
microphone_photo = ImageTk.PhotoImage(microphone_image)

# Botão com imagem do microfone
microphone_button = tk.Button(frame, image=microphone_photo, command=start_listening)
microphone_button.pack(pady=10, side=tk.BOTTOM)

log("Assistente ativada. Clique no botão para falar.")
speak("Eva está pronta para ajudar!")

root.mainloop()
