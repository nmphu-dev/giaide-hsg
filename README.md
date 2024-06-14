# Ha Noi Contest 2023
## Câu 1 (5,0 điểm): Thời gian
Một trung tâm lái xe tổ chức một đợt sát hạch vào lúc 8 giờ 00 phút sáng. Thời gian thực hiện bài sát hạch tối đa là 100 phút. Đợt sát hạch gồm $n$ thí sinh được đánh số từ 1 đến $n$. Thí sinh thứ $i$ hoàn thành bài sát hạch trong $\mathrm{T}_{i}$ phút ($1 \le i \le n$).
__Yêu cầu:__ Hãy lập trình đưa ra thời điểm kết thúc bài sát hạch của mỗi thí sinh giúp trung tâm.
##### Dữ liệu: Vào từ tệp văn bản TG.INP:
- Dòng đầu tiên chứa một số nguyên $n$ là số lượng thí sinh ($1 \le n \le 20$).
- Dòng thứ i trong $n$ dòng tiếp theo chứa một số nguyên $\mathrm{T}_{i}$ là thời gian hoàn thành bài sát hạch của thí sinh thứ i ($0 < \mathrm{T}_{i} \le 100$; $1 \le i \le n$).
##### Kết quả: Ghi ra tệp văn bản TG.OUT:
Gồm $n$ dòng; mỗi dòng là thời điểm bài sát hạch kết thúc của từng thí sinh có cấu trúc giờ:phút (không chứa dấu cách). Nếu giờ và phút nhỏ hơn 10 thì ghi thêm một chữ số 0 trên đầu (ví dụ: 8 giờ 5 phút viết là 08:05).
##### Ví dụ:
| TG.INP | TG.OUT |
|-------|---------|
| 3 <br> 5 <br> 10 <br> 65 | 08:05 <br> 08:10 <br> 08:05 | 

## Câu 2 (5,0 điểm): Mật mã
Một mật thư chứa mật mã bí ẩn được tạo ra là một xâu kí tự chỉ gồm các chữ số và các kí tự in thường. Mật mã bí ẩn là số lượng các số nguyên phân biệt xuất hiện trong thư.
__Ví dụ:__ Với mật thư as00023dkrf23smk1asmk1asd23sam09aa9 chứa 3 số nguyên phân biệt 23, 1, 9 nên mật mã là 3.
__Yêu cầu:__ Hãy lập trình đưa ra mật mã bí ẩn.
__Dữ liệu: Vào từ tệp văn bản MM.INP:__ Một xâu có độ dài $\le$ 100 gồm các chữ số và các kí tự in thường. Tất cả các số nguyên trong xâu có nhiều nhất 3 chữ số.
__Kết quả: Ghi ra tệp văn bản MM.OUT:__ Một số nguyên duy nhất là kết quả bài toán.
##### Ví dụ:
| MM.INP | MM.OUT |
|--------|--------|
| abc123abc2a3a1 | 4 |
| as00023dkrf23smk1asmk1asd23sam09aa9 | 3 |

## Câu 3 (4,0 điểm): Trạm phát sóng
Các trạm thu, phát sóng viễn thông của thành phố được đặt trên một đường tròn. Đường tròn này được chia thành 106 điểm cách đều nhau theo chiều kim đồng hồ. Một vị trí trên đường tròn được chọn là mốc 0. Có $n$ trạm thu sóng được đánh thứ tự từ 1 đến $n$, trạm thứ $i$ đặt ở vị trí $\mathrm{a}_{i}$ ($1 \le i \le n$).

Thành phố dự kiến sẽ đầu tư $k$ trạm phát sóng với phạm vi phát như nhau. Tuy nhiên, một trạm phát sóng với phạm vi phát sóng càng dài thì chi phí càng cao. Vì vậy, cần tính toán để đầu tư các trạm phát sóng có phạm vi ngắn nhất và phải đảm bảo các trạm thu sóng đều nhận được tín hiệu.

Khi một trạm phát sóng có phạm vi phát là $R$ thì các trạm thu sóng trong khoảng cách $R $theo cả hai chiều kim đồng hồ đều nhận được tín hiệu. Ví dụ: Trạm phát sóng tại vị trí 3 với phạm vi phát 1 thì cả trạm thu sóng ở vị trí 2 và 4 đều nhận được tín hiệu.

__Yêu cầu:__ Tìm phạm vi phát ngắn nhất của $k$ trạm sóng sẽ đầu tư để n trạm thu sóng đều nhận được tín hiệu.
__Dữ liệu:__ Vào từ tệp văn bản TPS.INP:
- Dòng đầu tiên chứa số nguyên dương n ($1 \le n \le 103$)
- Dòng thứ i trong n dòng tiếp theo chứa một số nguyên $\mathrm{a}_{i}$ là vị trí trạm thu sóng thứ $i$. Không có hai trạm phát sóng nào cùng vị trí ($0 \le \mathrm{a}_{i} < 106$; $1 \le i \le n$)

__Kết quả:__ Ghi ra tệp văn bản TPS.OUT: Số nguyên duy nhất là phạm vi phát sóng ngắn nhất của $k$ trạm phát sóng
__Ví dụ:__

| TPS.INP | TPS.OUT | Giải thích |
|---------|---------|------------|
| 4 <br> 5 <br> 1000 <br> 12345 <br> 987 <br> 2 | 498	| Đặt một trạm phát sóng ở vị trí 503 và một trạm phát sóng ở vị trí 12340 có phạm vi phát sóng là 498.|
| 2 <br> 1 <br> 999999 <br> 1 | 1 | Đặt một trạm phát sóng ở vị trí 0 có phạm vi phát sóng là 1.

## Câu 4 (3,0 điểm): Triển lãm
Bảo tàng thành phố có $n$ bức tranh được đánh số thứ tự từ 1 đến $n$. Bức tranh thứ $i$ có kích thước là $\mathrm{A}_{i}$ và được định giá là $\mathrm{B}_{i}$ ($1 \le i \le n$). Giám đốc bảo tàng muốn chọn một số bức tranh trưng bày trong buổi triển lãm để thu được lợi nhuận lớn nhất thỏa mãn các tiêu chí:
- Phải trưng bày ít nhất một bức tranh
- Chênh lệch về kích thước giữa các bức tranh được trưng bày càng nhỏ càng tốt.
- Tổng giá trị các bức tranh được trưng bày là lớn nhất.

Gọi $\mathrm{A}_{min}$ là kích thước nhỏ nhất, $\mathrm{A}_{max}$ là kích thước lớn nhất, $S$ là tổng các giá trị của các bức tranh được lựa chọn trưng bày. Lợi nhuận của bảo tàng được tính theo công thức:
$H = S – (\mathrm{A}_{max} – \mathrm{A}_{min})$
__Yêu cầu:__ Hãy giúp Giám đốc bảo tàng tìm H lớn nhất?
__Dữ liệu:__ Vào từ tệp văn bản TL.INP:
- Dòng đầu tiên chứa số nguyên n là số lượng các bức tranh (2 ≤ n ≤ 500 000).
- Dòng thứ i trong n dòng tiếp theo chứa hai số nguyên Ai và Bi là kích thước và định giá của bức tranh thứ i (1 ≤ Ai ≤ 1015 ; 1 ≤ Bi ≤ 109; 1 ≤ i ≤ n).

__Kết quả:__ Ghi ra tệp văn bản TL.OUT: Số nguyên H lớn nhất tìm được.
__Ràng buộc:__
- Có 25% số test tương ứng 25% số điểm có $n \le 16$.
- 25% số test tương ứng 25% số điểm có $n \le 300$.
- 25% số test tương ứng 25% số điểm có $n \le 5 000$.
- 25% số test còn lại tương ứng 25% số điểm không có ràng buộc gì thêm.

__Ví dụ:__
| TL.INP | TL.OUT | Giải thích |
|--------|--------|------------|
| 3 <br> 2 3 <br> 9 2 <br> 4 5 | 6 | Chọn bức tranh 1 và 3 thì: <br> $H = (3+5)–(4-2) = 6$ nên H=6 là lớn nhất. |

## Câu 5 (3,0 điểm)
Trong giờ số học, cô giáo đưa ra dãy $A$ gồm $n$ số nguyên dương từ 1 đến $n$. Cô cho mỗi học sinh chọn một dãy con $B$ gồm các phần tử liên tiếp của $A$. Dãy con $B$ được gọi là dãy đẹp nếu ta sắp xếp $B$ theo thứ tự tăng dần thì được một dãy số nguyên liên tiếp. Dãy con chỉ gồm 1 phần tử cũng được gọi là dãy đẹp. Ví dụ: $B = \left\{ 2, 4, 3 \right\}$ là dãy đẹp trong khi $\left\{ 2, 3, 2 \right\}$ thì không.
__Yêu cầu:__ Hãy giúp cả lớp đếm số lượng dãy con đẹp của A theo yêu cầu của cô giáo.
__Dữ liệu:__ Vào từ tệp văn bản DD.INP:
- Dòng đầu tiên là số nguyên dương $n$ ($1 \le n \le 105$).
- Dòng thứ hai chứa $n$ số nguyên dương $\mathrm{A}_{1}$, $\mathrm{A}_{2}$, $\mathrm{A}_{3}$, $\mathrm{A}_{n}$ ($1 \le Ai \le n$; $ 1 ≤ i ≤ n$)

__Kết quả:__ Một số nguyên duy nhất là số lượng dãy con đẹp của $A$.
__Ràng buộc:__
- Có 30% số test tương ứng 30% số điểm có $n \le 200$.
- 30% số test tương ứng 30% số điểm có $n \le 2 000$ và các phần tử của A đôi một phân biệt.
- 20% số test tương ứng 20% số điểm có $n \le 105$ và các phần tử của A đôi một phân biệt.
- 20% số test còn lại tương ứng 20% số điểm không có ràng buộc gì thêm.

__Ví dụ:__
| DD.INP | DD.OUT | Giải thích |
|--------|--------|------------|
| 3 <br> 1 2 3 | 6 | Có 6 dãy con đẹp là: <br> {1}, {2}, {3}, {1, 2}, {2, 3}, {1, 2, 3} |
| 3 <br> 2 2 1 | 4 | Có 4 dãy con đẹp là: <br> {2}, {2}, {1}, {2, 1} |
