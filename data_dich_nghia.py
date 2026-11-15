"""Nguyên văn 3.254 câu Truyện Kiều cùng dịch nghĩa, phân tích riêng từng câu (câu 1–38 và đoạn Trao duyên 723–756).

Nguyên văn lấy từ data/truyen_kieu.json (bản trên vietnamesetypography.com).
Muốn thêm dịch nghĩa cho câu nào, thêm một dòng vào _RAW.
"""

import json
import unicodedata
from pathlib import Path

LINES: list[str] = json.loads(
    (Path(__file__).parent / "data" / "truyen_kieu.json").read_text(encoding="utf-8")
)
TOTAL = len(LINES)
PAGE_SIZE = 100

GROUPS = {
    "mo-dau": "Lời mở đầu (câu 1–8)",
    "gia-dinh": "Giới thiệu gia đình họ Vương (câu 9–14)",
    "chi-em": "Chị em Thuý Kiều (câu 15–38)",
    "trao-duyen": "Trao duyên (câu 723–756)",
}

# (số câu, nhóm, câu thơ, dịch nghĩa, phân tích)
_RAW = [
    (1, "mo-dau", "Trăm năm trong cõi người ta,",
     "Trong cuộc đời của mỗi con người (một kiếp người thường được tính là trăm năm).",
     "Cách nói ước lệ \"trăm năm\" chỉ một đời người. Câu thơ mở đầu bằng giọng suy tưởng, khái quát, đặt vấn đề về số phận con người nói chung."),
    (2, "mo-dau", "Chữ tài chữ mệnh khéo là ghét nhau.",
     "Tài năng và số mệnh dường như luôn ghét bỏ, đố kị nhau.",
     "Nêu thuyết \"tài mệnh tương đố\": người có tài thường gặp số phận hẩm hiu. Hai chữ \"khéo là\" vừa mỉa mai vừa xót xa. Đây là chủ đề bao trùm toàn bộ tác phẩm."),
    (3, "mo-dau", "Trải qua một cuộc bể dâu,",
     "Trải qua những biến đổi lớn lao của cuộc đời, như biển cả hoá thành ruộng dâu.",
     "\"Bể dâu\" là điển cố \"thương hải tang điền\" (biển xanh biến thành ruộng dâu), chỉ sự thay đổi dữ dội của cuộc đời. Câu thơ gợi thời đại đầy biến động mà Nguyễn Du đã sống."),
    (4, "mo-dau", "Những điều trông thấy mà đau đớn lòng.",
     "Những điều tận mắt chứng kiến khiến lòng đau xót.",
     "\"Trông thấy\" nhấn mạnh trải nghiệm chân thực của tác giả; \"đau đớn lòng\" bộc lộ trực tiếp tấm lòng nhân đạo, thương xót con người."),
    (5, "mo-dau", "Lạ gì bỉ sắc tư phong,",
     "Chẳng có gì lạ khi trời lấy bớt chỗ này để bù vào chỗ khác.",
     "\"Bỉ sắc tư phong\" (bên kia kém thì bên này dồi dào) là quan niệm được cái này thì mất cái kia: người đã đẹp, đã tài thường phải chịu bất hạnh."),
    (6, "mo-dau", "Trời xanh quen thói má hồng đánh ghen.",
     "Ông trời vốn quen thói ghen ghét những người con gái đẹp.",
     "\"Má hồng\" là hoán dụ chỉ người phụ nữ đẹp; \"trời xanh\" bị nhân hoá như kẻ đố kị. Câu thơ thể hiện quan niệm \"hồng nhan bạc mệnh\" và cả sự bất bình ngầm của tác giả."),
    (7, "mo-dau", "Cảo thơm lần giở trước đèn,",
     "Bên ngọn đèn, tác giả lần giở từng trang sách quý.",
     "\"Cảo thơm\" là bản thảo, sách quý. Hình ảnh người đọc sách bên đèn cho biết câu chuyện được kể lại từ sách xưa, đồng thời thể hiện sự trân trọng."),
    (8, "mo-dau", "Phong tình cổ lục còn truyền sử xanh.",
     "Cuốn sách cũ ghi chuyện tình vẫn còn lưu truyền trong sử sách.",
     "\"Phong tình cổ lục\" là sách cũ chép chuyện tình; \"sử xanh\" là sử sách (xưa chép trên thẻ tre xanh). Câu thơ khẳng định câu chuyện có thật và chuyển sang phần kể chuyện."),
    (9, "gia-dinh", "Rằng: Năm Gia Tĩnh triều Minh,",
     "Chuyện kể rằng: vào năm Gia Tĩnh đời nhà Minh.",
     "Gia Tĩnh là niên hiệu của vua Minh Thế Tông (Trung Quốc, thế kỉ XVI). Mở đầu theo lối kể chuyện truyền thống, đặt câu chuyện vào bối cảnh Trung Quốc."),
    (10, "gia-dinh", "Bốn phương phẳng lặng, hai kinh vững vàng.",
     "Khắp nơi yên ổn, hai kinh đô vững vàng.",
     "\"Hai kinh\" là Bắc Kinh và Nam Kinh. Bối cảnh thái bình làm nền cho câu chuyện, càng làm nổi bật bi kịch về sau đến từ chính xã hội."),
    (11, "gia-dinh", "Có nhà viên ngoại họ Vương,",
     "Có một gia đình viên ngoại họ Vương.",
     "\"Viên ngoại\" vốn là chức quan ngoài biên chế, về sau dùng để gọi người có của, có danh vọng trong vùng."),
    (12, "gia-dinh", "Gia tư nghĩ cũng thường thường bậc trung.",
     "Gia sản cũng chỉ ở mức trung bình.",
     "Gia đình Kiều không giàu sang, quyền thế. Chi tiết này giúp lí giải vì sao khi gia biến, Kiều phải bán mình để chuộc cha."),
    (13, "gia-dinh", "Một trai con thứ rốt lòng,",
     "Có một người con trai là con út.",
     "\"Rốt lòng\" nghĩa là con sinh sau cùng."),
    (14, "gia-dinh", "Vương Quan là chữ, nối dòng nho gia.",
     "Tên là Vương Quan, nối tiếp truyền thống nhà nho.",
     "Cho thấy gia đình có truyền thống học hành, nề nếp gia phong."),
    (15, "chi-em", "Đầu lòng hai ả tố nga,",
     "Hai người con gái đầu là hai thiếu nữ xinh đẹp.",
     "\"Tố nga\" là người con gái đẹp (như Hằng Nga). Cách gọi trang trọng, thể hiện thái độ ngợi ca, trân trọng của tác giả."),
    (16, "chi-em", "Thúy Kiều là chị, em là Thúy Vân.",
     "Thuý Kiều là chị, Thuý Vân là em.",
     "Giới thiệu ngắn gọn thứ bậc hai chị em. Tên cả hai đều có chữ \"Thuý\" (màu xanh biếc của ngọc), gợi vẻ đẹp quý phái."),
    (17, "chi-em", "Mai cốt cách, tuyết tinh thần,",
     "Cốt cách thanh tao như hoa mai, tinh thần trong trắng như tuyết.",
     "Bút pháp ước lệ: lấy mai, tuyết làm chuẩn mực cho vẻ đẹp con người. Phép đối và nhịp 3/3 tạo sự cân xứng, hài hoà."),
    (18, "chi-em", "Mỗi người một vẻ, mười phân vẹn mười.",
     "Mỗi người một vẻ đẹp riêng, nhưng đều hoàn hảo, trọn vẹn.",
     "Thành ngữ \"mười phân vẹn mười\" chỉ sự hoàn hảo. Câu thơ vừa khái quát vẻ đẹp chung, vừa mở ra việc tả riêng từng người."),
    (19, "chi-em", "Vân xem trang trọng khác vời,",
     "Thuý Vân có vẻ đẹp đoan trang, cao sang khác thường.",
     "\"Trang trọng\" là nét chung của vẻ đẹp Vân; câu thơ như lời giới thiệu khái quát cho cả đoạn tả Vân."),
    (20, "chi-em", "Khuôn trăng đầy đặn, nét ngài nở nang.",
     "Khuôn mặt tròn đầy như trăng rằm, lông mày sắc nét như mày con ngài.",
     "Ẩn dụ \"khuôn trăng\", \"nét ngài\" cùng các tính từ \"đầy đặn\", \"nở nang\" gợi vẻ đẹp phúc hậu, đầy sức sống."),
    (21, "chi-em", "Hoa cười ngọc thốt đoan trang,",
     "Miệng cười tươi như hoa, giọng nói trong như ngọc, dáng vẻ đoan trang.",
     "So sánh với hoa, ngọc, những thứ đẹp và quý nhất, cho thấy vẻ đẹp hài hoà, đoan chính của Vân."),
    (22, "chi-em", "Mây thua nước tóc, tuyết nhường màu da.",
     "Mái tóc óng ả hơn mây, làn da trắng mịn hơn tuyết.",
     "Thiên nhiên chỉ \"thua\", \"nhường\", tức chịu thua một cách êm ái. Đây là dự báo cho cuộc đời bình lặng, suôn sẻ của Thuý Vân."),
    (23, "chi-em", "Kiều càng sắc sảo, mặn mà,",
     "Kiều còn sắc sảo về trí tuệ, mặn mà về tâm hồn hơn Vân.",
     "Chữ \"càng\" cùng nghệ thuật đòn bẩy (tả Vân trước để làm nổi bật Kiều) khẳng định Kiều đẹp hơn hẳn."),
    (24, "chi-em", "So bề tài sắc lại là phần hơn.",
     "So về cả tài lẫn sắc, Kiều đều hơn Vân.",
     "Khẳng định vẻ đẹp toàn diện của Kiều: cả nhan sắc lẫn tài năng."),
    (25, "chi-em", "Làn thu thủy, nét xuân sơn,",
     "Đôi mắt trong như làn nước mùa thu, lông mày thanh như dáng núi mùa xuân.",
     "Ẩn dụ ước lệ. Tác giả tập trung tả đôi mắt, \"cửa sổ tâm hồn\", cho thấy vẻ đẹp của Kiều có chiều sâu trí tuệ và tâm hồn."),
    (26, "chi-em", "Hoa ghen thua thắm, liễu hờn kém xanh.",
     "Hoa phải ghen vì kém thắm, liễu phải hờn vì kém xanh.",
     "Thiên nhiên \"ghen\", \"hờn\", tức đố kị với Kiều. Đây là dự báo cho số phận éo le, bị tạo hoá ghen ghét của nàng."),
    (27, "chi-em", "Một hai nghiêng nước nghiêng thành,",
     "Vẻ đẹp khiến nước nghiêng, thành đổ.",
     "Điển cố \"nhất cố khuynh nhân thành, tái cố khuynh nhân quốc\": vẻ đẹp tuyệt thế có sức cuốn hút mãnh liệt."),
    (28, "chi-em", "Sắc đành đòi một, tài đành họa hai.",
     "Về nhan sắc chỉ có một, về tài năng thì may ra có người thứ hai.",
     "Khẳng định Kiều là tuyệt sắc, tuyệt tài, gần như độc nhất vô nhị."),
    (29, "chi-em", "Thông minh vốn sẵn tính trời,",
     "Kiều có trí thông minh trời phú.",
     "Tài năng của Kiều là bẩm sinh, có sẵn từ trời."),
    (30, "chi-em", "Pha nghề thi họa, đủ mùi ca ngâm.",
     "Giỏi cả làm thơ, vẽ tranh, ca hát, ngâm vịnh.",
     "Liệt kê các tài năng theo chuẩn mực của người phụ nữ phong kiến: cầm, kì, thi, hoạ."),
    (31, "chi-em", "Cung thương làu bậc ngũ âm,",
     "Thông thạo năm cung bậc của âm nhạc.",
     "\"Ngũ âm\" gồm cung, thương, giốc, chuỷ, vũ. Kiều am hiểu âm luật một cách tinh thông."),
    (32, "chi-em", "Nghề riêng ăn đứt hồ cầm một trương.",
     "Tài riêng là chơi đàn hồ cầm, vượt hẳn mọi người.",
     "Đàn là tài năng nổi bật nhất của Kiều, gắn bó với nàng suốt cuộc đời lưu lạc."),
    (33, "chi-em", "Khúc nhà tay lựa nên chương,",
     "Kiều tự tay soạn được những bản nhạc riêng.",
     "Kiều không chỉ biểu diễn mà còn sáng tác, cho thấy tài năng ở mức xuất chúng."),
    (34, "chi-em", "Một thiên bạc mệnh lại càng não nhân.",
     "Khúc \"Bạc mệnh\" do nàng soạn càng làm người nghe sầu não.",
     "Tên khúc nhạc như lời dự báo số phận \"bạc mệnh\" của Kiều; tài năng gắn liền với nỗi buồn."),
    (35, "chi-em", "Phong lưu rất mực hồng quần,",
     "Là bậc phong lưu, thanh lịch nhất trong giới phụ nữ.",
     "\"Hồng quần\" (quần hồng) là hoán dụ chỉ người phụ nữ."),
    (36, "chi-em", "Xuân xanh xấp xỉ tới tuần cập kê.",
     "Tuổi xuân đã gần đến tuổi cài trâm (khoảng 15 tuổi).",
     "\"Cập kê\" là tuổi người con gái cài trâm, tức đến tuổi lấy chồng."),
    (37, "chi-em", "Êm đềm trướng rủ màn che,",
     "Cuộc sống êm đềm sau màn che, trướng rủ.",
     "Gợi cuộc sống khuê các nề nếp, kín đáo của hai chị em."),
    (38, "chi-em", "Tường đông ong bướm đi về mặc ai.",
     "Mặc cho khách tìm hoa đi lại ngoài tường đông.",
     "\"Tường đông\" là điển cố chỉ nơi ở của người con gái đẹp; \"ong bướm\" chỉ khách tìm hoa. Hai chị em vẫn giữ mình, chưa vướng bận chuyện tình."),
]

_RAW += [
    (723, "trao-duyen", "Cậy em, em có chịu lời,",
     "Chị nhờ cậy em, em có chịu nhận lời không.",
     "Chữ “cậy” thay cho “nhờ” vừa có nghĩa nhờ vả vừa chứa niềm tin tuyệt đối, gửi gắm điều hệ trọng. “Chịu” (thay cho “nhận”) hàm ý ép buộc nhẹ nhàng: Vân khó lòng từ chối. Điệp “em” liên tiếp cho thấy lời nói tha thiết, khẩn khoản."),
    (724, "trao-duyen", "Ngồi lên cho chị lạy rồi sẽ thưa.",
     "Em hãy ngồi lên để chị lạy em rồi chị sẽ nói.",
     "Hành động “lạy” và từ “thưa” đảo ngược trật tự chị – em thông thường: Kiều hạ mình vì coi Vân là ân nhân. Điều đó cho thấy việc sắp nhờ cực kỳ hệ trọng và Kiều đặt hết hy vọng vào em."),
    (725, "trao-duyen", "Giữa đường đứt gánh tương tư,",
     "Mối tình đang dang dở thì bị đứt giữa chừng.",
     "Thành ngữ “giữa đường đứt gánh” diễn tả mối tình tan vỡ đột ngột. “Tương tư” cho thấy đó là tình yêu hai chiều, sâu nặng."),
    (726, "trao-duyen", "Loan giao chắp mối tơ thừa mặc em.",
     "Việc nối lại mối tình còn dở dang ấy chị trông cậy vào em.",
     "“Loan giao” (keo loan – thứ keo nối dây đàn bị đứt) chỉ việc hàn gắn tình duyên; nhiều bản SGK chép là “keo loan”. “Tơ thừa” là cách nói khiêm nhường, coi mối tình của mình chỉ là phần thừa trao lại cho em – nhưng cũng hàm chứa nỗi đau tiếc nuối. “Mặc em” – phó thác hoàn toàn."),
    (727, "trao-duyen", "Kể từ khi gặp chàng Kim,",
     "Kể từ khi chị gặp chàng Kim,",
     "Kiều bắt đầu kể lại mối tình, giọng chậm rãi như hồi tưởng; cách gọi “chàng Kim” thân thương mà trân trọng."),
    (728, "trao-duyen", "Khi ngày quạt ước, khi đêm chén thề.",
     "Có khi ngày trao quạt hẹn ước, có khi đêm cùng uống chén rượu thề.",
     "Điệp “khi” và phép đối “ngày – đêm”, “quạt ước – chén thề” gợi những kỷ niệm thiêng liêng, gắn bó. Kiều nhấn mạnh tình yêu đã có lời thề nguyền để Vân hiểu sự nặng nề của nó."),
    (729, "trao-duyen", "Sự đâu sóng gió bất kỳ,",
     "Nào ngờ tai hoạ bất ngờ ập đến,",
     "Ẩn dụ “sóng gió” chỉ tai biến gia đình; “bất kỳ” nhấn mạnh tính đột ngột, không lường trước."),
    (730, "trao-duyen", "Hiếu tình khôn lẽ hai bề vẹn hai!",
     "Chữ hiếu và chữ tình không thể vẹn toàn cả hai.",
     "Câu thơ nêu rõ bi kịch của Kiều: phải chọn giữa hiếu và tình. Điệp “hai” nhấn mạnh thế lưỡng nan; Kiều đã chọn hiếu, nên phải trao duyên."),
    (731, "trao-duyen", "Ngày xuân em hãy còn dài,",
     "Tuổi xuân của em vẫn còn dài,",
     "Lý lẽ thứ nhất: Vân còn trẻ, còn nhiều thời gian. Lời lẽ vừa thuyết phục vừa thể hiện sự quan tâm của người chị."),
    (732, "trao-duyen", "Xót tình máu mủ, thay lời nước non.",
     "Vì thương tình ruột thịt, em hãy thay chị giữ lời thề non nước.",
     "Lý lẽ thứ hai: tình chị em “máu mủ”. “Lời nước non” chỉ lời thề nguyền bền vững. Kiều khéo léo đánh vào tình cảm ruột thịt để Vân không thể chối từ."),
    (733, "trao-duyen", "Chị dù thịt nát xương mòn,",
     "Dù chị có chết đi, thịt nát xương mòn,",
     "Thành ngữ “thịt nát xương mòn” chỉ cái chết. Kiều đã nghĩ đến cái chết ngay từ đây – linh cảm bi thương bao trùm."),
    (734, "trao-duyen", "Ngậm cười chín suối hãy còn thơm lây.",
     "Thì nơi chín suối chị vẫn mỉm cười, được thơm lây vì em.",
     "“Ngậm cười chín suối” – mãn nguyện nơi cõi chết; “thơm lây” – được hưởng phúc lây. Lý lẽ thứ ba: Vân nhận lời là làm phúc cho chị. Đoạn đầu kết thúc với lời thuyết phục thấu tình đạt lý."),
    (735, "trao-duyen", "Chiếc thoa với bức tờ mây,",
     "Chiếc thoa và bức thư thề ước,",
     "Kiều trao kỷ vật: “chiếc thoa” (chiếc trâm Kim Trọng nhặt được và trả lại hôm gặp nhau; bản SGK chép “chiếc vành”), “tờ mây” (tờ giấy hoa văn mây ghi lời thề) – những chứng tích thiêng liêng của mối tình."),
    (736, "trao-duyen", "Duyên này thì giữ vật này của chung.",
     "Duyên thì em giữ lấy, còn kỷ vật này là của chung hai chị em.",
     "Câu thơ chứa mâu thuẫn nội tâm: trao duyên nhưng không nỡ trao tình. Hai chữ “của chung” cho thấy Kiều vẫn muốn níu giữ, lý trí trao đi mà tình cảm níu lại."),
    (737, "trao-duyen", "Dù em nên vợ nên chồng,",
     "Dù sau này em nên vợ nên chồng với chàng,",
     "Kiều hình dung tương lai của Vân và Kim Trọng – lời dặn dò hướng về ngày sau."),
    (738, "trao-duyen", "Xót người mệnh bạc, ắt lòng chẳng quên.",
     "Thương người bạc mệnh thì chắc em cũng không quên chị.",
     "Kiều tự gọi mình là “người mệnh bạc” – ý thức rõ số phận bi kịch. Lời dặn thể hiện khao khát được nhớ đến."),
    (739, "trao-duyen", "Mất người còn chút của tin,",
     "Người đã mất thì còn lại chút kỷ vật làm tin,",
     "Kiều nói về mình như người đã chết (“mất người”); “của tin” là chứng tích cuối cùng còn lại."),
    (740, "trao-duyen", "Phím đàn với mảnh hương nguyền ngày xưa.",
     "Là phím đàn và mảnh hương thề nguyền ngày trước.",
     "“Phím đàn”, “hương nguyền” gắn với đêm thề nguyền và tiếng đàn cho Kim Trọng nghe – kỷ niệm sâu đậm nhất của mối tình."),
    (741, "trao-duyen", "Mai sao dầu có bao giờ.",
     "Mai sau dù có lúc nào,",
     "Bắt đầu lời dặn hướng về tương lai khi Kiều đã không còn – giọng thơ chuyển sang u uất, như lời trăng trối."),
    (742, "trao-duyen", "Đốt lò hương ấy, so tơ phím này.",
     "Em có đốt lò hương ấy, gảy lại phím đàn này,",
     "Các động từ “đốt”, “so” gợi cảnh tưởng niệm; kỷ vật tình yêu trở thành vật cúng tế – nỗi đau xót xa."),
    (743, "trao-duyen", "Trông ra ngọn cỏ lá cây,",
     "Thì hãy nhìn ra ngọn cỏ, lá cây,",
     "Hình ảnh thiên nhiên “ngọn cỏ lá cây” mở ra không gian cõi âm, chuẩn bị cho sự hiện về của hồn Kiều."),
    (744, "trao-duyen", "Thấy hiu hiu gió thì hay chị về.",
     "Thấy gió thổi hiu hiu thì biết là hồn chị trở về.",
     "Từ láy “hiu hiu” gợi làn gió nhẹ, lạnh lẽo. Kiều hình dung mình là hồn ma vật vờ trở về – hình ảnh vừa ám ảnh vừa thê lương."),
    (745, "trao-duyen", "Hồn còn mang nặng lời thề,",
     "Hồn chị vẫn còn mang nặng lời thề với chàng,",
     "Dù chết, Kiều vẫn không quên lời thề – tình yêu sâu nặng vượt qua cả sinh tử."),
    (746, "trao-duyen", "Nát thân bồ liễu, đền nghì trúc mai;",
     "Dù thân yếu đuối có tan nát cũng xin đền đáp tình nghĩa gắn bó.",
     "“Bồ liễu” – thân phận người con gái yếu đuối; “trúc mai” – tình nghĩa bền chặt. Lời nguyện hy sinh để đền đáp mối tình."),
    (747, "trao-duyen", "Dạ đài cách mặt khuất lời,",
     "Nơi chín suối cách mặt, không còn nói được lời nào,",
     "“Dạ đài” (đài đêm) chỉ cõi chết. “Cách mặt khuất lời” – sự chia lìa vĩnh viễn giữa âm và dương."),
    (748, "trao-duyen", "Rẩy xin chén nước cho người thác oan.",
     "Xin em rảy một chén nước cho người chết oan.",
     "Kiều tự coi mình là “người thác oan” – chết oan ức. Lời xin nhỏ bé “chén nước” mà xót xa vô cùng. Đến đây Kiều gần như quên mất Vân, chìm vào thế giới nội tâm."),
    (749, "trao-duyen", "Bây giờ trâm gẫy bình tan,",
     "Bây giờ trâm đã gãy, bình đã vỡ,",
     "Thành ngữ “trâm gẫy bình tan” (trâm gãy, bình vỡ; SGK chép “trâm gãy gương tan”) chỉ tình duyên tan vỡ. Hai chữ “bây giờ” kéo Kiều về thực tại phũ phàng – tâm trạng chuyển từ tưởng tượng sang đối diện hiện thực."),
    (750, "trao-duyen", "Kể làm sao xiết muôn vàn ái ân.",
     "Kể sao cho hết muôn vàn ân tình đã có!",
     "Câu cảm thán và cụm từ “muôn vàn ái ân” cho thấy tình yêu quá lớn, không lời nào kể hết – nỗi tiếc nuối tràn ngập."),
    (751, "trao-duyen", "Trăm nghìn gửi lại tình quân,",
     "Xin gửi lại người yêu trăm nghìn lời tạ lỗi,",
     "Từ đây Kiều chuyển sang độc thoại, hướng về Kim Trọng. “Trăm nghìn gửi lại tình quân” – gửi lại cho người yêu muôn vàn tình cảm và lời tạ lỗi (SGK chép “gửi lạy”); “tình quân” – cách gọi người yêu đầy trân trọng."),
    (752, "trao-duyen", "Tơ duyên ngắn ngủi có ngần ấy thôi.",
     "Duyên phận của chúng ta ngắn ngủi chỉ có bấy nhiêu thôi!",
     "“Ngắn ngủi”, “có ngần ấy thôi” – Kiều cay đắng thừa nhận mối tình đã chấm dứt; giọng thơ nghẹn ngào."),
    (753, "trao-duyen", "Phận sao phận bạc như vôi,",
     "Sao số phận lại bạc bẽo như vôi thế này?",
     "Câu hỏi tu từ, điệp “phận” và so sánh “bạc như vôi” – tiếng than thân trách phận đầy đau đớn."),
    (754, "trao-duyen", "Đã đành nước chẩy hoa trôi lỡ làng.",
     "Đành chịu số phận như hoa trôi theo dòng nước, lỡ làng.",
     "Thành ngữ “nước chảy hoa trôi” ẩn dụ thân phận trôi nổi, lỡ làng. Chữ “đã đành” cho thấy sự cam chịu, bất lực."),
    (755, "trao-duyen", "Ôi Kim lang! Hỡi Kim lang!",
     "Ôi chàng Kim! Hỡi chàng Kim!",
     "Câu thơ ngắt nhịp 3/3 với hai thán từ “Ôi”, “Hỡi” và điệp ngữ “Kim lang” – tiếng kêu đứt ruột, đỉnh điểm cảm xúc của đoạn trích. Kiều như gào gọi người yêu trong tuyệt vọng."),
    (756, "trao-duyen", "Thôi thôi thiếp đã phụ chàng từ đây!",
     "Thôi thôi, thiếp đã phụ chàng từ nay!",
     "Điệp “thôi thôi” như tiếng nấc nghẹn ngào, chấm dứt tất cả. Kiều tự nhận mình là người “phụ chàng” dù nàng là nạn nhân – thể hiện nhân cách cao đẹp, luôn nghĩ cho người khác. Kết thúc đoạn trích bằng nỗi đau tột cùng."),
]

_NOTES = {n: (m, a) for n, _g, _t, m, a in _RAW}

# Nghĩa của từng cặp lục bát: data/nghia/*.json, khoá là số câu lục (câu lẻ).
_COUPLETS: dict[int, str] = {}
for _f in sorted((Path(__file__).parent / "data" / "nghia").glob("*.json")):
    for _k, _v in json.loads(_f.read_text(encoding="utf-8")).items():
        _COUPLETS[int(_k)] = _v

# Phân tích từng cặp lục bát: data/phan_tich/*.json, khoá là số câu lục.
_COUPLET_NOTES: dict[int, str] = {}
for _f in sorted((Path(__file__).parent / "data" / "phan_tich").glob("*.json")):
    for _k, _v in json.loads(_f.read_text(encoding="utf-8")).items():
        _COUPLET_NOTES[int(_k)] = _v

# Các đoạn trích thường học (số câu theo bản nguyên văn ở trên).
EXCERPTS = [
    ("Lời mở đầu", 1, 8),
    ("Chị em Thuý Kiều", 15, 38),
    ("Cảnh ngày xuân", 39, 56),
    ("Mã Giám Sinh mua Kiều", 623, 652),
    ("Trao duyên", 723, 756),
    ("Kiều ở lầu Ngưng Bích", 1033, 1054),
    ("Chí khí anh hùng", 2213, 2230),
    ("Thuý Kiều báo ân báo oán", 2325, 2378),
    ("Lời kết", 3241, 3254),
]


def excerpt_of(n: int):
    return next((e for e in EXCERPTS if e[1] <= n <= e[2]), None)


def verse(n: int) -> dict | None:
    if not 1 <= n <= TOTAL:
        return None
    meaning, analysis = _NOTES.get(n, (None, None))
    # Cặp lục bát: câu lẻ là câu lục (6 chữ), câu chẵn là câu bát (8 chữ).
    pair = n + 1 if n % 2 else n - 1
    return {
        "id": n,
        "text": LINES[n - 1],
        "meaning": meaning,
        "analysis": analysis,
        "kind": "lục" if n % 2 else "bát",
        "pair": [min(n, pair), max(n, pair)],
        "couplet_meaning": _COUPLETS.get(min(n, pair)),
        "couplet_analysis": _COUPLET_NOTES.get(min(n, pair)),
        "excerpt": excerpt_of(n),
    }


def page_of(n: int) -> int:
    return (n - 1) // PAGE_SIZE + 1


def page_count() -> int:
    return (TOTAL + PAGE_SIZE - 1) // PAGE_SIZE


def page_verses(page: int) -> list[dict]:
    start = (page - 1) * PAGE_SIZE + 1
    return [verse(n) for n in range(start, min(start + PAGE_SIZE, TOTAL + 1))]


def _fold(text: str) -> str:
    """Bỏ dấu và chữ hoa để tìm kiếm không phân biệt dấu."""
    text = text.lower().replace("đ", "d")
    return "".join(c for c in unicodedata.normalize("NFD", text) if unicodedata.category(c) != "Mn")


_FOLDED = [_fold(l) for l in LINES]


def search(q: str, limit: int = 200) -> tuple[list[dict], int]:
    q = q.strip()
    if not q:
        return [], 0
    exact = q.lower()
    folded = _fold(q)
    hits = [i + 1 for i, l in enumerate(LINES) if exact in l.lower()]
    if not hits:  # không khớp đúng dấu thì tìm không dấu
        hits = [i + 1 for i, l in enumerate(_FOLDED) if folded in l]
    return [verse(n) for n in hits[:limit]], len(hits)


def has_note(n: int) -> bool:
    return n in _NOTES or (n if n % 2 else n - 1) in _COUPLETS
