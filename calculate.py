import os
import time

clk_tck = os.sysconf("SC_CLK_TCK")   # Number of kernel clock ticks per second
page_size = os.sysconf("SC_PAGE_SIZE") # The size of each "memory page" in the system in bytes
prev_cpu_times = {} # Dictionary to store previous CPU values ​​of processes

def proc_runtime(uptime: float , starttime: int) : 
    '''
    Run time calculation
    '''
    try :
        runtime = uptime - (starttime / clk_tck)
        hours = int(runtime // 3600)
        minutes = int((runtime % 3600) // 60)
        seconds = int(runtime % 60)
    
        if hours > 0:
            return f"{hours}:{minutes:02d}:{seconds:02d}"
        else:
            return f"{minutes:02d}:{seconds:02d}"
    
    except Exception as error :
        return error



def proc_memory(rss: int , total: int):
    '''
    Calculating the percentage of process memory usage
    '''
    try :
        rss = rss * page_size # Convert to bytes
        mem_percent = (rss / total) * 100
        return round(mem_percent, 2)
    
    except Exception as error :
        return error
    

    
def proc_cpu(pid, utime, stime, cutime, cstime, cores_count):
    try:
        # محاسبه کل CPU مصرفی (به tick)
        total_cpu_time = utime + stime + cutime + cstime
        
        # زمان فعلی سیستم
        current_real_time = time.time()
        
        if pid in prev_cpu_times:
            # بازیابی مقادیر قبلی
            prev_cpu_time, prev_real_time = prev_cpu_times[pid]
            
            # محاسبه تفاوت‌ها
            cpu_diff_ticks = total_cpu_time - prev_cpu_time  # تفاوت CPU (tick)
            real_time_diff = current_real_time - prev_real_time  # تفاوت زمان (ثانیه)
            
            if real_time_diff > 0:
                # تبدیل tick به ثانیه
                cpu_diff_seconds = cpu_diff_ticks / clk_tck
                
                # محاسبه درصد استفاده از CPU
                # ضرب در 100 برای درصد، تقسیم بر تعداد هسته‌ها برای استفاده بهینه
                percent = (cpu_diff_seconds / real_time_diff) * 100
                
                # محدود کردن به 100% (یا 100% * تعداد هسته‌ها)
                max_percent = cores_count * 100
                if percent > max_percent:
                    percent = max_percent
                
                # ذخیره مقادیر جدید برای استفاده بعدی
                prev_cpu_times[pid] = (total_cpu_time, current_real_time)
                return round(percent, 1)
        
        # برای فرآیندهای جدید: محاسبه درصد از زمان شروع تا حالا
        # این کار باعث می‌شود فرآیندهای جدید درصد واقعی‌تری نشان دهند
        else:
            # این قسمت اختیاری است - می‌توانید 0.0 برگردانید یا محاسبه کنید
            # محاسبه از زمان شروع فرآیند تا حالا
            # نیاز به starttime دارید که در تابع stat دریافت می‌شود
            # اما اینجا به آن دسترسی نداریم، پس 0.0 برمی‌گردانیم
            prev_cpu_times[pid] = (total_cpu_time, current_real_time)
            return 0.0
            
    except Exception:
        return 0.0

