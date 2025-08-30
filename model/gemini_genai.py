from google import genai
from google.genai import types
def init_gemini():
    global client 
    client = genai.Client()



def question(text):

    response = client.models.generate_content(
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(
        system_instruction="Bạn là một trợ lí ảo thân thiện, bạn hãy trả lời người dùng bằng ngôn ngữ gọn gàng xúc tích như đang giao tiếp ngoài đời thật, không sử dụng các kí hiệu dấu câu như * - +,v... để trả lời câu hỏi"),
    contents=text
)
    respon = response.text
    return respon
