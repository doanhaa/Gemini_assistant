# Gemini Assistant

Gemini Assistant là một trợ lý ảo sử dụng mô hình Gemini của Google để trả lời câu hỏi bằng tiếng Việt, tích hợp nhận diện giọng nói và chuyển văn bản thành giọng nói.

## Tính năng

- Nhận diện giọng nói tiếng Việt từ micro.
- Gửi câu hỏi đến mô hình Gemini và nhận phản hồi.
- Đọc phản hồi bằng giọng nói tiếng Việt.

## Cài đặt

1. **Clone repo:**
    ```sh
    git clone <repo-url>
    cd gemini_assistant
    ```

2. **Cài đặt các thư viện cần thiết:**
    ```sh
    pip install -r requirements.txt
    ```

## Sử dụng

Chạy file chính:

```sh
python gemini_assistant.py
```

Sau đó, nói câu hỏi vào micro và nhận phản hồi từ trợ lý ảo.

## Cấu trúc thư mục

```
gemini_assistant.py
model/
    gemini_genai.py
    text_to_speech.py
```

- `gemini_assistant.py`: Chương trình chính, tích hợp các module.
- `model/gemini_genai.py`: Tương tác với mô hình Gemini.
- `model/text_to_speech.py`: Chuyển văn bản thành giọng nói.

## Lưu ý

- Đảm bảo micro hoạt động tốt.
- Cần kết nối Internet để sử dụng dịch vụ nhận diện giọng nói và Gemini.

---

**Tác giả:**  
Bạn có thể bổ sung thông tin liên hệ hoặc đóng góp tại đây.
