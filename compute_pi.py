import time
import math
import random
import json
from datetime import datetime

def run_pi_monte_carlo(duration_minutes=15):
    total_seconds = duration_minutes * 60
    start_time = time.time()
    end_time = start_time + total_seconds

    print("=" * 60)
    print(" BẮT ĐẦU CHƯƠNG TRÌNH TÍNH TOÁN TRÊN MÁY CHỦ GITHUB")
    print(f" Thời gian dự kiến: {duration_minutes} phút ({total_seconds} giây)")
    print(f" Thời điểm bắt đầu: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(" Thuật toán: Mô phỏng Monte Carlo để xấp xỉ số Pi (π)")
    print("=" * 60, flush=True)

    inside_circle = 0
    total_points = 0
    batch_size = 5_000_000 # 5 triệu điểm mỗi đợt tính
    
    last_report_time = start_time
    report_interval = 60 # Cập nhật kết quả mỗi 1 phút (60 giây)
    minute_counter = 0

    while time.time() < end_time:
        # Tính toán theo batch
        for _ in range(batch_size):
            x = random.random()
            y = random.random()
            if x * x + y * y <= 1.0:
                inside_circle += 1
        total_points += batch_size

        current_time = time.time()
        elapsed = current_time - start_time

        # Báo cáo tiến độ mỗi 60 giây
        if current_time - last_report_time >= report_interval:
            minute_counter += 1
            pi_approx = 4.0 * inside_circle / total_points
            error = abs(pi_approx - math.pi)
            speed = total_points / elapsed

            print(f"[{datetime.now().strftime('%H:%M:%S')}] "
                  f"Phút {minute_counter:02d}/{duration_minutes:02d} "
                  f"({(elapsed / total_seconds) * 100:.1f}%) | "
                  f"Đã thử: {total_points:,} điểm | "
                  f"Tốc độ: {speed:,.0f} điểm/giây | "
                  f"Pi xấp xỉ: {pi_approx:.8f} (Sai số: {error:.8f})", 
                  flush=True)
            
            last_report_time = current_time

    # Kết thúc
    total_elapsed = time.time() - start_time
    final_pi = 4.0 * inside_circle / total_points
    final_error = abs(final_pi - math.pi)

    print("\n" + "=" * 60)
    print(" HOÀN THÀNH TÍNH TOÁN TRÊN GITHUB ACTIONS!")
    print(f" Thời điểm kết thúc: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f" Tổng thời gian chạy thực tế: {total_elapsed:.2f} giây")
    print(f" Tổng số điểm đã mô phỏng: {total_points:,} điểm")
    print(f" Giá trị Pi tính được: {final_pi:.10f}")
    print(f" Giá trị Pi thực tế:   {math.pi:.10f}")
    print(f" Sai số tuyệt đối:     {final_error:.10f}")
    print("=" * 60)

    # Xuất kết quả ra file
    summary = {
        "status": "COMPLETED",
        "start_time": datetime.fromtimestamp(start_time).isoformat(),
        "end_time": datetime.fromtimestamp(time.time()).isoformat(),
        "elapsed_seconds": round(total_elapsed, 2),
        "total_simulated_points": total_points,
        "pi_estimated": final_pi,
        "pi_actual": math.pi,
        "absolute_error": final_error,
        "points_per_second": round(total_points / total_elapsed, 2)
    }

    with open("result.txt", "w", encoding="utf-8") as f:
        f.write("=== KẾT QUẢ TÍNH TOÁN TỪ MÁY CHỦ GITHUB ===\n")
        f.write(f"Thời gian hoàn thành: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Tổng thời gian: {total_elapsed:.2f}s\n")
        f.write(f"Tổng số điểm mô phỏng: {total_points:,}\n")
        f.write(f"Số Pi tính được: {final_pi:.10f}\n")
        f.write(f"Số Pi chuẩn:     {math.pi:.10f}\n")
        f.write(f"Độ lệch:         {final_error:.10f}\n")

    with open("summary.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=4, ensure_ascii=False)

    print(" Đã lưu kết quả vào file 'result.txt' và 'summary.json'.")

if __name__ == "__main__":
    # Chạy tính toán đúng 15 phút (900 giây)
    run_pi_monte_carlo(duration_minutes=15)
