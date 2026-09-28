# 15-Minute Compute Job on GitHub Actions

Dự án này thực hiện mô phỏng Monte Carlo để xấp xỉ số Pi ($\pi$) liên tục trong vòng **15 phút** trên máy chủ đám mây của GitHub (GitHub-hosted Runner - Ubuntu).

## Cấu trúc thư mục
- `compute_pi.py`: Script Python thực hiện hàng tỷ phép tính ngẫu nhiên, xuất log tiến độ mỗi phút một lần và lưu kết quả cuối cùng.
- `.github/workflows/calculate.yml`: Kịch bản GitHub Actions tự động kích hoạt khi push code hoặc khi bấm nút **Run workflow**.

## Cách kích hoạt chạy trên GitHub
1. Vào tab **Actions** trên repository GitHub của bạn.
2. Chọn workflow **15-Minute Compute Job**.
3. Bấm **Run workflow** $\rightarrow$ **Run workflow**.
4. Quá trình tính toán sẽ diễn ra trong 15 phút. Bạn có thể xem log thời gian thực hoặc tải file kết quả sau khi hoàn thành.
