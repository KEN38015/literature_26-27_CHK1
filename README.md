# TẤT CẢ VỀ TRUYỆN KIỀU

Website tìm hiểu *Truyện Kiều* của Nguyễn Du. Trang được viết bằng FastAPI, Jinja2 và HTMX.

Các mục chính:

- Dịch nghĩa và phân tích đủ 3.254 câu thơ
- Tóm tắt cốt truyện
- Giới thiệu tác giả
- Tâm trạng Thuý Kiều và Kim Trọng
- Nghệ thuật miêu tả chân dung
- Nghệ thuật tả cảnh
- Nghệ thuật tả cảnh ngụ tình

## Cách chạy

Máy cần cài **Python 3.10 trở lên**. Có thể tải tại https://www.python.org/downloads/. Trên Windows, khi cài nhớ tick ô *Add Python to PATH*.

1. Giải nén thư mục dự án, mở Terminal (macOS) hoặc Command Prompt (Windows), rồi `cd` vào thư mục đó.
2. Tạo môi trường ảo và cài thư viện:

   **macOS / Linux**
   ```bash
   python3 -m venv ~/.venvs/truyen-kieu
   source ~/.venvs/truyen-kieu/bin/activate
   pip install -r requirements.txt
   ```

   **Windows**
   ```bat
   python -m venv %USERPROFILE%\venvs\truyen-kieu
   %USERPROFILE%\venvs\truyen-kieu\Scripts\activate
   pip install -r requirements.txt
   ```

   Môi trường ảo được đặt ngoài thư mục dự án vì Python không tạo được venv ở đường dẫn có dấu `:`.

3. Chạy web:
   ```bash
   uvicorn main:app --port 8000
   ```
4. Mở trình duyệt và vào **http://localhost:8000**. Nhấn `Ctrl + C` trong Terminal để tắt.

## Đưa lên mạng (Render)

Repo đã có sẵn file `render.yaml`. Các bước:

1. Vào https://render.com, đăng nhập bằng tài khoản GitHub.
2. Chọn **New → Blueprint**, rồi chọn repo `literature_26-27_CHK1`.
3. Bấm **Apply**. Render sẽ tự cài thư viện và chạy web, sau đó cấp link dạng `https://truyen-kieu-xxxx.onrender.com`.

Mỗi lần push code mới lên nhánh `main`, Render sẽ tự triển khai lại. Ở gói miễn phí, nếu một lúc lâu không có ai truy cập, lần mở đầu tiên sau đó sẽ mất khoảng 30–50 giây.

## Cấu trúc thư mục

| Đường dẫn | Nội dung |
|---|---|
| `main.py` | Các route của web |
| `data_dich_nghia.py` | Nguyên văn, dịch nghĩa và phân tích riêng từng câu (câu 1–38 và đoạn Trao duyên) |
| `data_ta_canh.py` | Dữ liệu cho phần tả cảnh và tả cảnh ngụ tình |
| `data/truyen_kieu.json` | Nguyên văn 3.254 câu |
| `data/nghia/*.json` | Dịch nghĩa theo từng cặp lục bát |
| `data/phan_tich/*.json` | Phân tích theo từng cặp lục bát |
| `templates/` | Giao diện (Jinja2 + HTMX) |
| `static/style.css` | CSS |

Sau khi sửa các file `.json`, cần tắt rồi chạy lại server thì trang mới hiện nội dung mới.

Nguyên văn lấy từ bản trên vietnamesetypography.com. Một vài chữ khác với sách giáo khoa, ví dụ “loan giao” so với “keo loan”, hay “chiếc thoa” so với “chiếc vành”.
