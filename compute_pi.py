import sys
import io
import time
import math
import random
import json
from datetime import datetime

# Đảm bảo in tiếng Việt chuẩn không bị lỗi mã hóa font trên mọi hệ điều hành
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def run_pi_monte_carlo(duration_minutes=15):
    total_seconds = duration_minutes * 60
    start_time = time.time()
    end_time = start_time + total_seconds

    print("=" * 60)
    print(" BAT DAU CHUONG TRINH TINH TOAN TREN MAY CHU GITHUB")
    print(f" Thoi gian du kien: {duration_minutes} phut ({total_seconds} giay)")
    print(f" Thoi diem bat dau: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(" Thuat toan: Mo phong Monte Carlo de xap xi so Pi (pi)")
    print("=" * 60, flush=True)

    inside_circle = 0
    total_points = 0
    batch_size = 500_000 # 500k điểm mỗi đợt để phản hồi nhanh
    
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

        # Báo cáo tiến độ mỗi 60 giây (hoặc nếu là đợt test ngắn thì báo cáo ngay)
        if current_time - last_report_time >= report_interval:
            minute_counter += 1
            pi_approx = 4.0 * inside_circle / total_points
            error = abs(pi_approx - math.pi)
            speed = total_points / elapsed

            print(f"[{datetime.now().strftime('%H:%M:%S')}] "
                  f"Phut {minute_counter:02d}/{int(duration_minutes):02d} "
                  f"({(elapsed / total_seconds) * 100:.1f}%) | "
                  f"Da thu: {total_points:,} diem | "
                  f"Toc do: {speed:,.0f} diem/giay | "
                  f"Pi xap xi: {pi_approx:.8f} (Sai so: {error:.8f})", 
                  flush=True)
            
            last_report_time = current_time

    # Kết thúc
    total_elapsed = time.time() - start_time
    final_pi = 4.0 * inside_circle / total_points
    final_error = abs(final_pi - math.pi)

    print("\n" + "=" * 60)
    print(" HOAN THANH TINH TOAN TREN GITHUB ACTIONS!")
    print(f" Thoi diem ket thuc: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f" Tong thoi gian chay thuc te: {total_elapsed:.2f} giay")
    print(f" Tong so diem da mo phong: {total_points:,} diem")
    print(f" Gia tri Pi tinh duoc: {final_pi:.10f}")
    print(f" Gia tri Pi thuc te:   {math.pi:.10f}")
    print(f" Sai so tuyet doi:     {final_error:.10f}")
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
        f.write("=== KET QUA TINH TOAN TU MAY CHU GITHUB ===\n")
        f.write(f"Thoi gian hoan thanh: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Tong thoi gian: {total_elapsed:.2f}s\n")
        f.write(f"Tong so diem mo phong: {total_points:,}\n")
        f.write(f"So Pi tinh duoc: {final_pi:.10f}\n")
        f.write(f"So Pi chuan:     {math.pi:.10f}\n")
        f.write(f"Do lech:         {final_error:.10f}\n")

    with open("summary.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=4, ensure_ascii=False)

    print(" [OK] Da luu ket qua vao file 'result.txt' va 'summary.json'.")

if __name__ == "__main__":
    # Mac dinh chay 15 phut
    run_pi_monte_carlo(duration_minutes=15)
