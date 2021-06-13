# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 22:32:14 2021
Tử vi đấu số
@author: Oasis
"""
#Import datetime
from datetime import date



#Khai báo hàm today
today = date.today()
Day = today.day
Month = today.month
Year = today.year

# Định nghĩa tự điển Tử Vi
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
tuvi = {
'Tý' : """
Về sự nghiệp, tài lộc: Người tuổi Tý đặc biệt là nữ giới nên chú ý đến công việc hơn đặc biệt là những ai làm công việc có liên quan đến nghệ thuật. Nhất định bạn phải làm được điều gì đó đặc biệt thay vì chỉ nhìn người khác mà không cố gắng hết mình.

Về tình cảm: Chuyện tình cảm của tuổi Tý khá đẹp bởi bạn và người đó khá hiểu nhau nên có thể chia sẻ những niềm vui hay nỗi buồn trong cuộc sống.

Về sức khỏe: Thời tiết thay đổi khiến cho bản mệnh đau đầu nhức óc không chịu nổi.

Giờ tốt trong ngày: 14h - 16h
""",
'Sửu' : """
Về sự nghiệp, tài lộc: Những người tuổi Sửu nên cảm ơn người thân vì đã giúp đỡ mình đạt được nhiều thành tựu trong công việc. Bạn nên thầm cảm ơn vì xung quanh mình toàn người tốt đi. Bạn đừng tỏ ra mình giỏi rồi người khác nói gì cũng không muốn nghe.

Về tình cảm: Gia đình người tuổi Sửu anh em hòa thuận.

Về sức khỏe: Bạn ăn uống không ngon do đường tiêu hóa gặp vấn đề.

Giờ tốt trong ngày: 15h - 17h
""",
'Dần' : """
Về sự nghiệp, tài lộc: Hôm nay tuổi Dần làm gì cũng có phần thờ ơ và không muốn giải quyết triệt để, nếu có làm chỉ làm cho xong chứ không hiệu quả.

Về tình cảm: Tình duyên cũng không có dấu hiệu khởi sắc trong khi tuổi Dần đang tìm kiếm những điều mới mẻ thì người ấy lại gạt phắt đi sự cố gắng của bạn. Điều này làm cho tuổi Dần không được vui vẻ cho lắm.

Về sức khỏe: Thần kinh căng thẳng dẫn đến tình trạng bạn mệt mỏi liên miên.

Giờ tốt trong ngày: 16h – 18h
""",
'Mão' : """
Về sự nghiệp, tài lộc: Ngày hôm nay tuổi Mão đã làm một việc vô cùng đúng đắn khi bạn giúp đỡ những người yếu kém để họ cải thiện tình hình làm việc tốt hơn. Tài chính của bạn cũng được tăng lên không ít.

Về tình cảm: Tuổi Mão có một ngày vui vẻ, hạnh phúc bên những người thân của mình. Bạn sống lạc quan và yêu đời, nhờ vậy mọi người xung quanh cũng cảm nhận được năng lượng tích cực từ bạn.

Về sức khỏe: Bạn hãy giữ thói quen sinh hoạt lành mạnh như hiện tại nhé.

Giờ tốt trong ngày: 9h – 11h
""",
'Thìn' : """
Về sự nghiệp, tài lộc: Tử vi hôm nay dự báo tuổi Thìn không nên từ chối lời giúp đỡ từ người thân nếu không có họ bạn cũng sẽ không có thành công đâu.

Về tình cảm: Tiến triển trong tình yêu của cả hai khá chậm chạp vì vậy nếu là nam nhân hãy tiến lên một bước để đẩy mạnh mối quan hệ của mình nhé.

Về sức khỏe: Bạn gặp một số vấn đề có liên quan đến đại tràng, đường ruột hay dạ dày khi ăn các thực phẩm cay nóng.

Giờ tốt trong ngày: 10h –12h
""",
'Tỵ': """
Về sự nghiệp, tài lộc: Người tuổi Tỵ khiến cho người khác phật ý vì bạn quá thẳng tính khi làm việc. Một khi bạn đã nói gì thì người khác cũng không dám cãi lại bạn đâu.

Về tình cảm: Những ai đã và đang trong mối quan hệ tiến tới hôn nhân thì nên xem lại liệu đối phương có phải là người đi tiếp với mình đến cuối đời hay không.

Về sức khỏe: Sinh khí yếu khiến cho sức khỏe của bạn bị hao mòn theo thời gian.

Giờ tốt trong ngày: 11h – 13h
""",
'Ngọ' : """
Về sự nghiệp, tài lộc: Tuổi Ngọ cần phát huy tối đa ưu điểm sáng tạo của mình khi làm việc. Tuy nhiên đừng xa vời quá với hiện thực nếu không đồng nghiệp của bạn sẽ hiểu nhầm đó.

Về tình cảm: Nam mạng là người phong lưu đa tình, vì vậy chuyện tình cảm gặp không ít sóng gió khi bạn vô tình khiến cho người ấy buồn lòng nhiều vì mình.

Về sức khỏe: Bản mệnh mắc bệnh thiếu máu nên dễ bị chóng mặt hay tê bì chân tay.

Giờ tốt trong ngày: 16h - 18h
""",
'Mùi' : """
Về sự nghiệp, tài lộc: Kiệm lời của mình mà tuổi Mùi mất đi nhiều cơ hội để phát triển bản thân. Trong khi bạn luôn muốn tốt cho mình nhưng lại không muốn nói ra điều đó.

Về tình cảm: Với những ai bạn cảm thấy mình yêu thương thật lòng hãy cố gắng bảo vệ họ trước búa rìu dư luận nhé. Đừng để người ta thương bạn mà phải chịu thiệt thòi.

Về sức khỏe: Bản mệnh cần uống trà gừng mỗi khi thấy đầu óc choáng váng.

Giờ tốt trong ngày: 15h - 17h
""",
'Thân' : """
Về sự nghiệp, tài lộc: Vận trình tài lộc của người tuổi Thân có vẻ như không được thuận buồm xuôi gió cho lắm. Khi bạn cố gắng hoàn thành tốt điều gì đó thì tất cả lại như phản đối lại bạn.

Về tình cảm: Cuyện tình cảm nam nữ xuất hiện nhiều vết nứt nhỏ do bạn có một số biểu hiện khiến người đó nghi ngờ rằng mình không chung thủy.

Về sức khỏe: Bạn nên cố gắng ăn uống và tập luyện theo chế độ để có một sức khỏe tốt hơn.

Giờ tốt trong ngày: 16h - 18h
""",
'Dậu' : """
Về sự nghiệp, tài lộc: Hôm nay tuổi Dậu suy tính quá nhiều khiến cho mất cơ hội tốt trong những công việc. Tình hình tài chính dễ tụt dốc không phanh do thói quen chi tiêu không kiểm đếm.

Về tình yêu: Tình duyên tuổi Dậu không có sự khởi sắc, nhiều điều u sầu. Bạn luôn giúp đỡ người khác nhưng lại nhận về toàn sự giả dối.

Về sức khỏe: Bạn nên điều chỉnh lại múi giờ sinh hoạt của mình đi nhé.

Giờ tốt trong ngày: 15h – 17h
""",
'Tuất' : """
Về sự nghiệp, tài lộc: Ngày hôm nay tuổi Tuất làm việc lười biếng, không có sự tích cực. Khi gặp chuyện gì thì lại không dám nói, gặp trắc trở lập tức bi thương.

Về tình cảm: Chuyện tình cảm hôm nay trở nên xa cách, lạnh nhạt. Người độc thân cảm thấy buồn bực khi không có ai sẻ chia với mình.

Về sức khỏe: Bạn chú ý những chứng bệnh đau lưng, đau răng.

Giờ tốt trong ngày: 18h - 20h
""",
'Hợi' : """
Về sự nghiệp, tài lộc: Tuổi Hợi vốn dĩ hẹp hòi khi nghĩ đến lợi ích của bản thân mà quên mất đi ai mới là người giúp bạn lên vị trí này.

Về tình cảm: Chính vì sự độc đoán của mình khiến cho tuổi Hợi trở nên xa cách hơn với những thành viên trong gia đình của mình.

Về sức khỏe: Bản mệnh nên cẩn thận bệnh đau dạ dày tái phát trong ngày.

Giờ tốt trong ngày: 13h - 15h
"""
}  
# //Kết thúc phần tự điển Tử Vi
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

# Định nghĩa Thiên Can - Đia Chi bằng Dictionary
tc = {1:'Giáp', 2:'Ất', 3:'Bính', 4:'Đinh', 
      5:'Mậu', 6:'Kỷ', 7:'Canh', 8:'Tân', 9:'Nhâm', 0:'Quý'}
dc = {1:'Tý', 2:'Sửu', 3:'Dần', 4:'Mão', 
      5:'Thìn', 6:'Tỵ', 7:'Ngọ', 8:'Mùi', 
      9:'Thân', 10:'Dậu', 11:'Tuất', 0:'Hợi'}
# //Kết thúc phần Thiên Can - Địa Chi
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

#Nhập thông tin
ho_va_ten = str(input("Họ và tên: "))
gioi_tinh = str(input("Giới tính (Nam/Nữ): "))
ngay_sinh = int(input("Ngày sinh: "))
thang_sinh = int(input("Tháng sinh: "))
nam_sinh = int(input("Năm sinh: "))

# Tính tuổi
tuoi = today.year - nam_sinh
print("Chào {0} {1}, năm nay {0} {2} tuổi".format("ông" if gioi_tinh == "Nam" or gioi_tinh == "nam" else "bà", ho_va_ten, tuoi)) 

#Định nghĩa Thiên Can
thiencan = (nam_sinh - 3) % 10
#Định nghĩa Địa Chi
diachi = (nam_sinh - 3) % 12

#Định nghĩa Mệnh
menh = {'Giáp Tý': 'Hải Trung Kim (Vàng trong biển)', 
        'Ất Sửu': 'Hải Trung Kim (Vàng trong biển)',
        'Giáp Dần': 'Đại Khê Thủy (Nước khe lớn)',
        'Ất Mão': 'Đại Khê Thủy (Nước khe lớn)',
        'Giáp Thìn': 'Phú Đăng Hoả (Lửa đèn to)',
        'Giáp Thìn': 'Phú Đăng Hoả (Lửa đèn to)',
        'Giáp Ngọ': 'Sa Trung Kim (Vàng trong cát)',
        'Ất Mùi': 'Sa Trung Kim (Vàng trong cát)',
        'Giáp Thân': 'Tuyền Trung Thủy (Nước trong suối)',
        'Ất Dậu': 'Tuyền Trung Thủy (Nước trong suối)',
        'Giáp Tuất': 'Sơn Đầu Hoả (Lửa trên núi)',
        'Ất Hợi': 'Sơn Đầu Hoả (Lửa trên núi)',
        'Bính Tý': 'Giản Hạ Thuỷ (Nước khe suối)',
        'Đinh Sửu': 'Giản Hạ Thuỷ (Nước khe suối)',
        'Bính Dần': 'Lư Trung Hỏa (Lửa trong lò)',
        'Đinh Mão': 'Lư Trung Hỏa (Lửa trong lò)',
        'Bính Thìn': 'Sa Trung Thổ (Đất pha cát)',
        'Đinh Tỵ': 'Sa Trung Thổ (Đất pha cát)',
        'Bính Ngọ': 'Thiên Hà Thuỷ (Nước trên trời)',
        'Đinh Mùi': 'Thiên Hà Thuỷ (Nước trên trời)',
        'Bính Thân': 'Sơn Hạ Hoả (Lửa chân núi)',
        'Đinh Dậu': 'Sơn Hạ Hoả (Lửa chân núi)',
        'Bính Tuất': 'Ốc Thượng Thổ (Đất nóc nhà)',
        'Đinh Hợi': 'Ốc Thượng Thổ (Đất nóc nhà)',
        'Mậu Tý': 'Tích Lịch Hoả (Lửa sấm sét)',
        'Kỷ Sửu': 'Tích Lịch Hoả (Lửa sấm sét)',
        'Mậu Dần': 'Thành Đầu Thổ (Đất đắp thành)',
        'Kỷ Mão': 'Thành Đầu Thổ (Đất đắp thành)',
        'Mậu Thìn': 'Đại Lâm Mộc (Gỗ rừng già)',
        'Kỷ Tỵ': 'Đại Lâm Mộc (Gỗ rừng già)',
        'Mậu Ngọ': 'Thiên Thượng Hoả (Lửa trên trời)',
        'Kỷ Mùi': 'Thiên Thượng Hoả (Lửa trên trời)',
        'Mậu Thân': 'Đại Trạch Thổ (Đất nền nhà)',
        'Kỷ Dậu': 'Đại Trạch Thổ (Đất nền nhà)',
        'Mậu Tuất': 'Bình Địa Mộc (Gỗ đồng bằng)',
        'Kỷ Hợi': 'Bình Địa Mộc (Gỗ đồng bằng)',
        'Canh Tý': 'Bích Thượng Thổ (Đất tò vò)',
        'Tân Sửu': 'Bích Thượng Thổ (Đất tò vò)',
        'Canh Dần': 'Tùng Bách Mộc (Gỗ tùng bách)',
        'Tân Mão': 'Tùng Bách Mộc (Gỗ tùng bách)',
        'Canh Thìn': 'Bạch Lạp Kim (Vàng sáp ong)',
        'Tân Tỵ': 'Bạch Lạp Kim (Vàng sáp ong)',
        'Canh Ngọ': 'Lộ Bàng Thổ (Đất bên đường)',
        'Tân Mùi': 'Lộ Bàng Thổ (Đất bên đường)',
        'Canh Thân': 'Thạch Lựu Mộc (Gỗ cây lựu đá)',
        'Tân Dậu': 'Thạch Lựu Mộc (Gỗ cây lựu đá)',
        'Canh Tuất': 'Thoa Xuyến Kim (Vàng trang sức)',
        'Tân Hợi': 'Thoa Xuyến Kim (Vàng trang sức)',
        'Nhâm Tý': 'Tang Đố Mộc (Gỗ cây dâu)',
        'Quý Sửu': 'Tang Đố Mộc (Gỗ cây dâu)',
        'Nhâm Dần': 'Kim Bạch Kim (Vàng pha bạc)',
        'Quý Mão': 'Kim Bạch Kim (Vàng pha bạc)',
        'Nhâm Thìn': 'Trường Lưu Thuỷ (Nước chảy mạnh)',
        'Quý Tỵ': 'Trường Lưu Thuỷ (Nước chảy mạnh)',
        'Nhâm Ngọ': 'Dương Liễu Mộc (Gỗ cây dương)',
        'Quý Mùi': 'Dương Liễu Mộc (Gỗ cây dương)',
        'Nhâm Thân': 'Kiếm Phong Kim (Vàng chuôi kiếm)',
        'Quý Dậu': 'Kiếm Phong Kim (Vàng chuôi kiếm)',
        'Nhâm Tất': 'Đại Hải Thuỷ (Nước biển lớn)',
        'Quý Hợi': 'Đại Hải Thuỷ (Nước biển lớn)'
        }

# Dùng vòng lặp for xuất kết quả Can Chi và Tử vi dựa trên năm sinh
for a in tc:
    for b in dc:
        if thiencan == a and diachi == b:
            print("Nhằm năm",tc[a], dc[b])        
            for c in menh:
                if tc[a] + ' ' + dc[b] == c:
                    print("Thuộc mệnh",menh[c])   
            for d in tuvi:
                if dc[b] == d:
                    print(tuvi[d])

quit = input('Press Enter key to exit')


