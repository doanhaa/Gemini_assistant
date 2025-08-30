from model import gemini_genai as gemini
import speech_recognition as sr
from model import text_to_speech as ttp

ttp.text_to_speech_init()
request = sr.Recognizer()
gemini.init_gemini()

while True:
    with sr.Microphone() as source:
        print("Hãy đưa câu hỏi: ")
        request.adjust_for_ambient_noise(source)
        # Lắng nghe âm thanh từ micro
        audio_data = request.listen(source)
        print("Đang tiến hành xử lí: ")
    
    try:
        text = request.recognize_google(audio_data, language = "vi-VI")
        print(f"User: {text}")
        print("Gemini", end=": ")
        phan_hoi_AI = gemini.question(text)
        print(phan_hoi_AI)
        ttp.AI_say(phan_hoi_AI)
    except sr.UnknownValueError:
        print("Google không thể hiểu được âm thanh bạn nói.")

    # Bắt lỗi khi không kết nối được tới Google
    except sr.RequestError as e:
            print(f"Không thể kết nối tới dịch vụ của Google; {e}")