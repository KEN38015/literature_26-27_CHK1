"""Các đoạn tả cảnh tiêu biểu trong Truyện Kiều.

Mỗi đoạn gồm:
- featured: True nếu là đoạn đặc sắc (được ghim lên đầu và highlight)
- why: lí do đặc sắc (hiện trong thẻ ghim)
- marks: các từ ngữ được tô sáng trong câu thơ
"""

from markupsafe import Markup, escape

PARTS = [
    ("I", "Phần I: Gặp gỡ và đính ước"),
    ("II", "Phần II: Gia biến và lưu lạc"),
    ("III", "Phần III: Đoàn tụ"),
]

SCENES = [
    # ---------------- Phần I ----------------
    {
        "id": "ngay-xuan",
        "part": "I",
        "label": "Mùa xuân",
        "title": "Bức tranh ngày xuân",
        "context": "Mở đầu đoạn chị em Kiều đi chơi xuân trong tiết Thanh minh.",
        "verses": [
            "Ngày xuân con én đưa thoi,",
            "Thiều quang chín chục đã ngoài sáu mươi.",
            "Cỏ non xanh tận chân trời,",
            "Cành lê trắng điểm một vài bông hoa.",
        ],
        "marks": ["con én đưa thoi", "xanh tận chân trời", "trắng điểm"],
        "notes": [
            "\"Con én đưa thoi\" vừa gợi mùa xuân, vừa gợi thời gian trôi nhanh như thoi đưa.",
            "Nền cỏ non xanh trải \"tận chân trời\", điểm xuyết sắc trắng hoa lê: màu sắc hài hoà, trong trẻo, khoáng đạt.",
            "Chữ \"điểm\" khiến bức tranh sinh động, có hồn như một nét vẽ của hoạ sĩ.",
        ],
        "featured": True,
        "why": "Bốn câu thơ tả cảnh xuân hay bậc nhất văn học Việt Nam, kết tinh bút pháp chấm phá cổ điển.",
    },
    {
        "id": "le-hoi",
        "part": "I",
        "label": "Lễ hội",
        "title": "Cảnh lễ hội tiết Thanh minh",
        "context": "Không khí ngày hội đạp thanh, chị em Kiều đi tảo mộ.",
        "verses": [
            "Thanh minh trong tiết tháng ba,",
            "Lễ là tảo mộ, hội là đạp thanh.",
            "Gần xa nô nức yến anh,",
            "Chị em sắm sửa bộ hành chơi xuân.",
            "Dập dìu tài tử, giai nhân,",
            "Ngựa xe như nước áo quần như nêm.",
        ],
        "marks": ["nô nức", "sắm sửa", "Dập dìu", "Ngựa xe như nước áo quần như nêm"],
        "notes": [
            "Hàng loạt từ ghép, từ láy (nô nức, sắm sửa, dập dìu) gợi không khí rộn ràng, náo nhiệt.",
            "Ẩn dụ \"yến anh\" (chim én, chim oanh) ví dòng người đi hội như đàn chim ríu rít.",
            "Phép so sánh \"ngựa xe như nước, áo quần như nêm\" gợi cảnh đông đúc, tấp nập.",
        ],
        "featured": False,
    },
    {
        "id": "chieu-tan-hoi",
        "part": "I",
        "label": "Chiều xuân",
        "title": "Cảnh chị em du xuân trở về",
        "context": "Buổi chiều, lễ hội tan, chị em Kiều ra về.",
        "verses": [
            "Tà tà bóng ngả về tây,",
            "Chị em thơ thẩn dan tay ra về.",
            "Bước dần theo ngọn tiểu khê,",
            "Lần xem phong cảnh có bề thanh thanh.",
            "Nao nao dòng nước uốn quanh,",
            "Dịp cầu nho nhỏ cuối ghềnh bắc ngang.",
        ],
        "marks": ["Tà tà", "thơ thẩn", "thanh thanh", "Nao nao", "nho nhỏ"],
        "notes": [
            "Cảnh vẫn thanh, dịu của mùa xuân nhưng nhịp điệu đã chậm lại, nhạt dần theo bóng chiều.",
            "Các từ láy vừa tả cảnh, vừa gợi tâm trạng bâng khuâng, xao xuyến khi cuộc vui tàn.",
        ],
        "featured": False,
    },
    {
        "id": "mo-dam-tien",
        "part": "I",
        "label": "Nấm mồ",
        "title": "Mộ Đạm Tiên",
        "context": "Trên đường về, chị em Kiều gặp nấm mồ vô chủ của ca nhi Đạm Tiên.",
        "verses": [
            "Sè sè nấm đất bên đàng,",
            "Dàu dàu ngọn cỏ nửa vàng nửa xanh.",
        ],
        "marks": ["Sè sè", "Dàu dàu", "nửa vàng nửa xanh"],
        "notes": [
            "Từ láy \"sè sè\", \"dàu dàu\" gợi nấm mồ thấp lè tè, hoang lạnh, không người chăm sóc.",
            "Tương phản gay gắt với cảnh lễ hội tấp nập vừa tả trước đó.",
            "Cảnh như một điềm báo trước cho số phận \"hồng nhan bạc mệnh\" của chính Kiều.",
        ],
        "featured": False,
    },
    {
        "id": "gap-kim",
        "part": "I",
        "label": "Bên cầu",
        "title": "Cảnh chia tay sau lần đầu gặp Kim Trọng",
        "context": "Kim Trọng lên ngựa ra về, Kiều đứng nhìn theo.",
        "verses": [
            "Dưới cầu nước chảy trong veo,",
            "Bên cầu tơ liễu bóng chiều thướt tha.",
        ],
        "marks": ["trong veo", "tơ liễu", "thướt tha"],
        "notes": [
            "Cảnh thơ mộng: dòng nước trong, rặng liễu rủ dưới nắng chiều.",
            "Từ láy \"thướt tha\" gợi dáng liễu mềm mại, uyển chuyển trong ánh nắng chiều.",
        ],
        "featured": False,
    },
    {
        "id": "dem-trang",
        "part": "I",
        "label": "Đêm trăng",
        "title": "Cảnh đêm trăng trong vườn",
        "context": "Cảnh đêm trăng trong vườn nhà Kiều sau buổi gặp Kim Trọng.",
        "verses": [
            "Mảnh trăng chênh chếch dòm song,",
            "Vàng gieo ngấn nước, cây lồng bóng sân.",
            "Hải đường lả ngọn đông lân,",
            "Giọt sương gieo nặng cành xuân la đà.",
        ],
        "marks": ["chênh chếch dòm song", "Vàng gieo", "lồng bóng", "la đà"],
        "notes": [
            "Trăng được nhân hoá: \"mảnh trăng\" \"dòm\" qua cửa sổ như có hồn.",
            "Ánh trăng như vàng rải trên mặt nước, bóng cây đan lồng trên sân: cảnh đêm xuân lung linh, huyền ảo.",
            "Cành hải đường trĩu nặng giọt sương, ngả \"la đà\": cảnh vật có dáng điệu, có trọng lượng cụ thể.",
        ],
        "featured": True,
        "why": "Bức tranh đêm trăng lung linh: trăng được nhân hoá \"dòm song\", ánh trăng như \"vàng gieo\" trên mặt nước.",
    },
    {
        "id": "mua-he",
        "part": "I",
        "label": "Mùa hè",
        "title": "Cảnh hè ở nhà Thuý Kiều",
        "context": "Mở đầu đoạn Kiều ở nhà một mình rồi sang tìm Kim Trọng.",
        "verses": [
            "Dưới trăng quyên đã gọi hè,",
            "Đầu tường lửa lựu lập loè đâm bông.",
        ],
        "marks": ["quyên đã gọi hè", "lửa lựu lập loè"],
        "notes": [
            "Âm thanh tiếng chim quyên báo hè kết hợp với sắc đỏ rực của hoa lựu.",
            "Ẩn dụ \"lửa lựu\" cùng từ láy \"lập loè\" khiến hoa như những đốm lửa chập chờn, cảnh tràn đầy sức sống.",
        ],
        "featured": True,
        "why": "Chỉ hai câu mà đủ cả âm thanh, màu sắc, ánh sáng; hình ảnh \"lửa lựu lập loè\" độc đáo, nổi tiếng.",
    },
    {
        "id": "dem-the",
        "part": "I",
        "label": "Đêm thề",
        "title": "Vầng trăng đêm thề nguyền",
        "context": "Kiều và Kim Trọng thề nguyền gắn bó trọn đời.",
        "verses": [
            "Vầng trăng vằng vặc giữa trời,",
            "Đinh ninh hai mặt một lời song song.",
        ],
        "marks": ["vằng vặc"],
        "notes": [
            "Vầng trăng sáng tỏ giữa trời như chứng giám cho lời thề.",
            "Từ láy \"vằng vặc\" gợi ánh trăng sáng trong, toả khắp không gian đêm.",
        ],
        "featured": False,
    },
    # ---------------- Phần II ----------------
    {
        "id": "ngung-bich",
        "part": "II",
        "label": "Lầu Ngưng Bích",
        "title": "Không gian quanh lầu Ngưng Bích",
        "context": "Kiều bị Tú Bà giam lỏng ở lầu Ngưng Bích.",
        "verses": [
            "Trước lầu Ngưng Bích khóa xuân,",
            "Vẻ non xa, tấm trăng gần, ở chung.",
            "Bốn bề bát ngát xa trông,",
            "Cát vàng cồn nọ, bụi hồng dặm kia.",
        ],
        "marks": ["khóa xuân", "Bốn bề bát ngát", "Cát vàng", "bụi hồng"],
        "notes": [
            "\"Khóa xuân\" gợi cảnh Kiều bị giam hãm, tuổi xuân bị khoá chặt.",
            "Không gian mở ra nhiều chiều: non xa, trăng gần, bốn bề bát ngát.",
            "Hình ảnh rời rạc, xa xôi (cát vàng, bụi hồng) gợi sự rợn ngợp, trống trải, không một bóng người.",
        ],
        "featured": False,
    },
    {
        "id": "buon-trong",
        "part": "II",
        "label": "Lầu Ngưng Bích",
        "title": "Tám câu \"Buồn trông\"",
        "context": "Kết thúc đoạn Kiều ở lầu Ngưng Bích, trước khi mắc lừa Sở Khanh.",
        "verses": [
            "Buồn trông cửa bể chiều hôm,",
            "Thuyền ai thấp thoáng cánh buồm xa xa?",
            "Buồn trông ngọn nước mới sa,",
            "Hoa trôi man mác, biết là về đâu?",
            "Buồn trông nội cỏ dàu dàu,",
            "Chân mây mặt đất một màu xanh xanh.",
            "Buồn trông gió cuốn mặt ghềnh,",
            "Ầm ầm tiếng sóng kêu quanh ghế ngồi.",
        ],
        "marks": ["Buồn trông", "thấp thoáng", "xa xa", "man mác", "dàu dàu", "xanh xanh", "Ầm ầm"],
        "notes": [
            "Điệp ngữ \"buồn trông\" lặp bốn lần như điệp khúc của nỗi buồn dâng trào từng đợt.",
            "Cảnh đi từ xa đến gần, màu sắc từ nhạt đến đậm, âm thanh từ tĩnh đến động.",
            "Mỗi cảnh ứng với một nỗi lòng: nhớ nhà, lo cho thân phận trôi nổi, buồn chán vô vọng, rồi hãi hùng trước tai hoạ.",
            "Các từ láy và câu hỏi tu từ nhấn mạnh tâm trạng cô đơn, bế tắc của Kiều.",
        ],
        "featured": True,
        "why": "Đỉnh cao của bút pháp tả cảnh ngụ tình trong toàn bộ Truyện Kiều: mỗi cảnh là một tâm trạng.",
    },
    {
        "id": "lau-xanh",
        "part": "II",
        "label": "Lầu xanh",
        "title": "\"Cảnh nào cảnh chẳng đeo sầu\"",
        "context": "Kiều bị ép tiếp khách ở lầu xanh của Tú Bà.",
        "verses": [
            "Đôi phen gió tựa, hoa kề,",
            "Nửa rèm tuyết ngậm, bốn bề trăng thâu.",
            "Cảnh nào cảnh chẳng đeo sầu,",
            "Người buồn, cảnh có vui đâu bao giờ!",
        ],
        "marks": ["gió tựa, hoa kề", "tuyết ngậm", "Cảnh nào cảnh chẳng đeo sầu", "Người buồn, cảnh có vui đâu bao giờ"],
        "notes": [
            "Cảnh gió, hoa, tuyết, trăng vốn đẹp, nhưng trong mắt Kiều đều nhuốm buồn.",
            "Hai câu cuối được xem là \"tuyên ngôn\" của nghệ thuật tả cảnh ngụ tình: cảnh vật luôn mang tâm trạng con người.",
        ],
        "featured": True,
        "why": "Hai câu \"Cảnh nào cảnh chẳng đeo sầu / Người buồn, cảnh có vui đâu bao giờ\" đúc kết quan niệm tả cảnh của Nguyễn Du.",
    },
    {
        "id": "chia-tay-thuc-sinh",
        "part": "II",
        "label": "Mùa thu",
        "title": "Cảnh chia tay Thúc Sinh",
        "context": "Thúc Sinh về quê thăm vợ cả Hoạn Thư, Kiều tiễn chàng.",
        "verses": [
            "Người lên ngựa kẻ chia bào,",
            "Rừng phong thu đã nhuốm màu quan san.",
            "Dặm hồng bụi cuốn chinh an,",
            "Trông người đã khuất mấy ngàn dâu xanh.",
            "Người về chiếc bóng năm canh,",
            "Kẻ đi muôn dặm một mình xa xôi.",
            "Vầng trăng ai xẻ làm đôi,",
            "Nửa in gối chiếc, nửa soi dặm trường.",
        ],
        "marks": ["nhuốm màu quan san", "Dặm hồng bụi cuốn", "Vầng trăng ai xẻ làm đôi", "Nửa in gối chiếc, nửa soi dặm trường"],
        "notes": [
            "Rừng phong đỏ lá mùa thu; chữ \"nhuốm\" cho thấy sắc thu như thấm dần vào cảnh chia li.",
            "Bụi đường cuốn theo vó ngựa, bóng người khuất dần sau \"mấy ngàn dâu xanh\".",
            "Hình ảnh \"vầng trăng ai xẻ làm đôi\" vô cùng sáng tạo: một nửa soi người ở, một nửa theo người đi.",
        ],
        "featured": True,
        "why": "Câu thơ \"Vầng trăng ai xẻ làm đôi\" là một trong những hình ảnh chia li đẹp và độc đáo nhất của thơ ca Việt Nam.",
    },
    {
        "id": "tron-di",
        "part": "II",
        "label": "Đêm trốn chạy",
        "title": "Kiều trốn khỏi nhà Hoạn Thư",
        "context": "Kiều bỏ trốn khỏi Quan Âm các trong đêm.",
        "verses": [
            "Mịt mù dặm cát đồi cây,",
            "Tiếng gà điếm nguyệt dấu giày cầu sương.",
        ],
        "marks": ["Mịt mù", "Tiếng gà điếm nguyệt", "dấu giày cầu sương"],
        "notes": [
            "Con đường mịt mù cát bụi, đồi cây, gợi hành trình xa xôi, vô định.",
            "Câu thơ sau lấy ý thơ Đường (Ôn Đình Quân): tiếng gà gáy nơi quán trọ dưới trăng, dấu giày in trên cầu phủ sương.",
            "Cảnh đêm vắng lạnh làm nổi bật nỗi cô đơn, sợ hãi của người con gái một mình trốn chạy.",
        ],
        "featured": False,
    },
    # ---------------- Phần III ----------------
    {
        "id": "vuon-thuy",
        "part": "III",
        "label": "Vườn Thuý",
        "title": "Kim Trọng trở lại vườn Thuý",
        "context": "Hết tang chú, Kim Trọng quay về thì Kiều đã bán mình, nhà cửa vắng tanh.",
        "verses": [
            "Đầy vườn cỏ mọc lau thưa,",
            "Song trăng quạnh quẽ vách mưa rã rời.",
            "Trước sau nào thấy bóng người,",
            "Hoa đào năm ngoái còn cười gió đông.",
        ],
        "marks": ["cỏ mọc lau thưa", "quạnh quẽ", "rã rời", "Hoa đào năm ngoái còn cười gió đông"],
        "notes": [
            "Khu vườn xưa giờ hoang tàn: cỏ mọc đầy, lau thưa, vách nát vì mưa.",
            "Câu cuối lấy ý thơ Thôi Hộ (đời Đường): hoa đào vẫn vô tình \"cười\" trong gió xuân như năm trước.",
            "Cảnh còn mà người mất, nỗi đau của Kim Trọng càng thêm thấm thía.",
        ],
        "featured": True,
        "why": "Phép đối lập cảnh cũ – người xưa, hình ảnh \"hoa đào năm ngoái còn cười gió đông\" gợi nỗi tiếc nuối khôn nguôi.",
    },
]


def _highlight(line: str, marks: list[str]) -> Markup:
    html = str(escape(line))
    for m in marks:
        m_html = str(escape(m))
        html = html.replace(m_html, f"<mark>{m_html}</mark>")
    return Markup(html)


# Các đoạn mang tính tả cảnh ngụ tình: không hiển thị ở mục "Nghệ thuật tả cảnh",
# giữ lại để dùng cho mục "Nghệ thuật tả cảnh ngụ tình" sau này.
NGU_TINH_IDS = {"chieu-tan-hoi", "ngung-bich", "buon-trong", "lau-xanh", "chia-tay-thuc-sinh", "tron-di", "vuon-thuy"}
NGU_TINH_SCENES = [s for s in SCENES if s["id"] in NGU_TINH_IDS]
SCENES = [s for s in SCENES if s["id"] not in NGU_TINH_IDS]

for _s in SCENES + NGU_TINH_SCENES:
    _s["verses_html"] = [_highlight(v, _s.get("marks", [])) for v in _s["verses"]]

# Thứ tự hiển thị trong khu vực ghim.
PIN_ORDER = ["ngay-xuan", "dem-trang", "mua-he"]
FEATURED = sorted(
    (s for s in SCENES if s.get("featured")),
    key=lambda s: PIN_ORDER.index(s["id"]) if s["id"] in PIN_ORDER else len(PIN_ORDER),
)

# ---------------- Dữ liệu cho mục "Nghệ thuật tả cảnh ngụ tình" ----------------
# Tâm trạng nhân vật được gửi gắm qua từng cảnh.
TINH = {
    "chieu-tan-hoi": ("Chị em Kiều", "Bâng khuâng, xao xuyến, như linh cảm điều chẳng lành khi cuộc vui kết thúc."),
    "ngung-bich": ("Thuý Kiều", "Cô đơn, trơ trọi, bị giam hãm giữa không gian mênh mông, rợn ngợp."),
    "buon-trong": ("Thuý Kiều", "Nỗi buồn tăng dần: nhớ nhà, lo âu cho thân phận, buồn chán vô vọng, rồi hoảng sợ trước tai hoạ."),
    "lau-xanh": ("Thuý Kiều", "Buồn tủi, chán chường: cảnh dù đẹp mà lòng người không thể vui."),
    "chia-tay-thuc-sinh": ("Thuý Kiều, Thúc Sinh", "Lưu luyến, xót xa; nỗi cô đơn của cả người ở lẫn người đi."),
    "tron-di": ("Thuý Kiều", "Bơ vơ, lo sợ của người con gái một mình trốn chạy trong đêm."),
    "vuon-thuy": ("Kim Trọng", "Đau đớn, hụt hẫng, tiếc nuối khi cảnh cũ còn đó mà người xưa đã không còn."),
}
for _s in NGU_TINH_SCENES:
    _s["who"], _s["tinh"] = TINH[_s["id"]]

NT_PIN_ORDER = ["buon-trong", "lau-xanh", "chia-tay-thuc-sinh", "vuon-thuy"]
NGU_TINH_FEATURED = sorted(
    (s for s in NGU_TINH_SCENES if s.get("featured")),
    key=lambda s: NT_PIN_ORDER.index(s["id"]) if s["id"] in NT_PIN_ORDER else len(NT_PIN_ORDER),
)

# Bảng phân tích tám câu "Buồn trông".
BUON_TRONG_TABLE = [
    ("Cửa bể chiều hôm, cánh buồm thấp thoáng xa xa",
     "Nhớ nhà, khát khao được sum họp; càng thấy mình cô đơn, lạc lõng."),
    ("Ngọn nước mới sa, cánh hoa trôi man mác",
     "Lo cho thân phận trôi nổi, vô định như cánh hoa giữa dòng nước."),
    ("Nội cỏ dàu dàu, chân mây mặt đất một màu xanh xanh",
     "Buồn chán, bế tắc; tương lai mịt mờ, không lối thoát."),
    ("Gió cuốn mặt ghềnh, sóng kêu ầm ầm quanh ghế ngồi",
     "Hoảng sợ, linh cảm những tai hoạ sắp ập đến (Kiều mắc lừa Sở Khanh ngay sau đó)."),
]
