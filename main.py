"""TẤT CẢ VỀ TRUYỆN KIỀU — khung website (FastAPI + Jinja2 + HTMX)."""

from pathlib import Path

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import data_dich_nghia
import data_ta_canh

BASE_DIR = Path(__file__).parent

app = FastAPI(title="Tất cả về Truyện Kiều")
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")

# Các mục chính hiển thị thành nút trên thanh điều hướng.
SECTIONS = {
    "dich-nghia": {
        "title": "Dịch nghĩa Truyện Kiều",
        "template": "partials/dich_nghia.html",
        "desc": "Đọc từng câu thơ — bấm vào một câu để xem phân tích chi tiết.",
    },
    "tom-tat": {
        "title": "Tóm tắt cốt truyện",
        "template": "partials/tom_tat.html",
        "desc": "Tóm tắt ba phần: Gặp gỡ và đính ước — Gia biến và lưu lạc — Đoàn tụ.",
    },
    "tac-gia": {
        "title": "Giới thiệu tác giả",
        "template": "partials/tac_gia.html",
        "desc": "Cuộc đời, thời đại và sự nghiệp sáng tác của Nguyễn Du.",
    },
    "tam-trang": {
        "title": "Tâm trạng Thuý Kiều & Kim Trọng",
        "template": "partials/tam_trang.html",
        "desc": "Diễn biến nội tâm của hai nhân vật qua các đoạn trích tiêu biểu.",
    },
    "chan-dung": {
        "title": "Nghệ thuật miêu tả chân dung",
        "template": "partials/chan_dung.html",
        "desc": "Bút pháp ước lệ khắc hoạ chân dung Thuý Vân, Thuý Kiều, Kim Trọng, Hoạn Thư, Tú Bà...",
    },
    "nghe-thuat-ta-canh": {
        "title": "Nghệ thuật tả cảnh",
        "template": "partials/ta_canh.html",
        "desc": "Những bức tranh thiên nhiên thuần tả cảnh trong Truyện Kiều: cảnh ngày xuân, lễ hội, đêm trăng, mùa hè...",
    },
    "ta-canh": {
        "title": "Nghệ thuật tả cảnh ngụ tình",
        "template": "partials/ngu_tinh.html",
        "desc": "Cảnh vật nhuốm màu tâm trạng — tiêu biểu là đoạn Kiều ở lầu Ngưng Bích.",
    },
}

def _is_htmx(request: Request) -> bool:
    return request.headers.get("HX-Request") == "true"


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request, "index.html", {"sections": SECTIONS, "active": None}
    )


@app.get("/muc/{slug}", response_class=HTMLResponse)
async def section(request: Request, slug: str):
    sec = SECTIONS.get(slug)
    if sec is None:
        raise HTTPException(status_code=404, detail="Không tìm thấy mục")
    ctx = {
        "sections": SECTIONS,
        "active": slug,
        "sec": sec,
        **_verse_panel_ctx(page=1),
        "excerpts": data_dich_nghia.EXCERPTS,
        "total_lines": data_dich_nghia.TOTAL,
        "scenes": data_ta_canh.SCENES,
        "featured": data_ta_canh.FEATURED,
        "parts": data_ta_canh.PARTS,
        "nt_scenes": data_ta_canh.NGU_TINH_SCENES,
        "nt_featured": data_ta_canh.NGU_TINH_FEATURED,
        "buon_trong_table": data_ta_canh.BUON_TRONG_TABLE,
    }
    # HTMX chỉ cần phần nội dung; truy cập trực tiếp thì trả về cả trang.
    template = sec["template"] if _is_htmx(request) else "index.html"
    return templates.TemplateResponse(request, template, ctx)


def _verse_panel_ctx(page: int = 1, focus: int | None = None) -> dict:
    """Dữ liệu cho khối danh sách câu thơ (theo trang)."""
    return {
        "mode": "page",
        "page": page,
        "page_count": data_dich_nghia.page_count(),
        "page_size": data_dich_nghia.PAGE_SIZE,
        "total_lines": data_dich_nghia.TOTAL,
        "verses": data_dich_nghia.page_verses(page),
        "focus": focus,
    }


@app.get("/dich-nghia/trang/{page}", response_class=HTMLResponse)
async def verse_page(request: Request, page: int):
    page = max(1, min(page, data_dich_nghia.page_count()))
    return templates.TemplateResponse(
        request, "partials/verse_panel.html", _verse_panel_ctx(page)
    )


@app.get("/dich-nghia/cau/{n}", response_class=HTMLResponse)
async def verse_jump(request: Request, n: int):
    n = max(1, min(n, data_dich_nghia.TOTAL))
    ctx = _verse_panel_ctx(data_dich_nghia.page_of(n), focus=n)
    return templates.TemplateResponse(request, "partials/verse_panel.html", ctx)


@app.get("/dich-nghia/tim", response_class=HTMLResponse)
async def verse_search(request: Request, q: str = ""):
    if not q.strip():
        return templates.TemplateResponse(
            request, "partials/verse_panel.html", _verse_panel_ctx(1)
        )
    results, count = data_dich_nghia.search(q)
    ctx = {"mode": "search", "q": q, "verses": results, "count": count, "focus": None}
    return templates.TemplateResponse(request, "partials/verse_panel.html", ctx)


@app.get("/phan-tich/{verse_id}", response_class=HTMLResponse)
async def verse_analysis(request: Request, verse_id: int):
    verse = data_dich_nghia.verse(verse_id)
    if verse is None:
        raise HTTPException(status_code=404, detail="Không tìm thấy câu thơ")
    a, b = verse["pair"]
    return templates.TemplateResponse(
        request,
        "partials/phan_tich.html",
        {
            "verse": verse,
            "pair_lines": [data_dich_nghia.verse(x) for x in (a, b) if data_dich_nghia.verse(x)],
            "prev_id": verse_id - 1 if verse_id > 1 else None,
            "next_id": verse_id + 1 if verse_id < data_dich_nghia.TOTAL else None,
        },
    )
