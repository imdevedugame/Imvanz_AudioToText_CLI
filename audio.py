import speech_recognition as sr

def speech_to_text_from_microphone():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Silakan berbicara...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio, language="id-ID")
            print("Anda mengatakan:", text)
        except sr.UnknownValueError:
            print("Maaf, saya tidak dapat mengenali suara.")
        except sr.RequestError:
            print("Tidak dapat menghubungi layanan Google Speech Recognition.")

def speech_to_text_from_audio_file(file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio, language="id-ID")
            print("Teks dari audio:", text)
        except sr.UnknownValueError:
            print("Maaf, saya tidak dapat mengenali suara.")
        except sr.RequestError:
            print("Tidak dapat menghubungi layanan Google Speech Recognition.")


def main_menu():
    while True:
        print("\nImvanz audio to teks tools malas ngetik")
        print("1. Konversi suara dari mikrofon ke teks")
        print("2. Konversi suara dari file audio ke teks")
        print("3. sudah gak malas keluar dong")
        choice = input("pilih salah satu aja  ")
        
        if choice == '1':
            speech_to_text_from_microphone()
        elif choice == '2':
            file_path = "a.wav"  
            speech_to_text_from_audio_file(file_path)
        elif choice == '3':
            print("Keluar dari program.")
            break
        else:
            print("Opsi tidak valid. Silakan pilih kembali.")


main_menu()
