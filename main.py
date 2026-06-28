import get_data as get_data
import calculate as calculate
import os
import time
from calculate import page_size

cores_count = os.cpu_count()

# ============================================
# رنگ‌ها
# ============================================
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
CYAN = '\033[96m'
WHITE = '\033[97m'
BOLD = '\033[1m'
END = '\033[0m'

# ============================================
# توابع کمکی
# ============================================
def format_uptime(uptime):
    seconds = int(uptime)
    days = seconds // 86400
    seconds %= 86400
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    secs = seconds % 60
    if days > 0:
        return f'{days}d {hours:02d}:{minutes:02d}:{secs:02d}'
    return f'{hours:02d}:{minutes:02d}:{secs:02d}'

def format_memory(bytes_val):
    if bytes_val >= 1024**3:
        return f"{bytes_val / (1024**3):.1f}GB"
    elif bytes_val >= 1024**2:
        return f"{bytes_val // (1024**2)}MB"
    elif bytes_val >= 1024:
        return f"{bytes_val // 1024}KB"
    return f"{bytes_val}B"

def get_color(status):
    if status == 'R': return GREEN
    if status == 'S': return BLUE
    if status == 'T': return YELLOW
    if status in ['Z', 'X']: return RED
    return WHITE

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

# ============================================
# تابع اصلی
# ============================================
def main():
    clear_screen()
    
    while True:
        # ========================================
        # جمع‌آوری داده
        # ========================================
        status_counts = {'sleeping': 0, 'running': 0, 'stopped': 0, 'zombie': 0, 'dead': 0}
        processes = []
        total_procs = 0
        total_mem_used = 0
        
        try:
            pids = os.listdir('/proc')
            load_avg = get_data.loadavg()
            uptime = get_data.uptime()
            mem_info = get_data.meminfo()
            mem_total = mem_info['mem_total']
            mem_free = mem_info['mem_free']
            
            for pid in pids:
                if not pid.isdigit():
                    continue
                status = get_data.stat(pid)
                if status is None:
                    continue
                
                st = status['status']
                if st == 'S':
                    status_counts['sleeping'] += 1
                elif st == 'R':
                    status_counts['running'] += 1
                elif st == 'T':
                    status_counts['stopped'] += 1
                elif st == 'Z':
                    status_counts['zombie'] += 1
                elif st == 'X':
                    status_counts['dead'] += 1
                else:
                    status_counts['sleeping'] += 1
                
                runtime = calculate.proc_runtime(uptime, status['starttime'])
                mem_percent = calculate.proc_memory(status['rss'], mem_total)
                cpu_percent = calculate.proc_cpu(
                    str(pid), status['utime'], status['stime'],
                    status['cutime'], status['cstime'], cores_count
                )
                
                total_mem_used += status['rss'] * page_size
                total_procs += 1
                
                processes.append({
                    'pid': status['pid'],
                    'user': status['uid'][:10],
                    'status': status['status'],
                    'cpu': cpu_percent,
                    'mem': mem_percent,
                    'time': runtime,
                    'command': status['command']
                })
        
        except Exception as e:
            print(f"{RED}Error: {e}{END}")
            time.sleep(1)
            continue
        
        # ========================================
        # مرتب‌سازی بر اساس CPU (بیشترین اول)
        # ========================================
        processes.sort(key=lambda x: x['cpu'], reverse=True)
        processes = processes[:20]  # ۲۰ تا اول
        
        # ========================================
        # نمایش
        # ========================================
        clear_screen()
        
        mem_used_percent = (total_mem_used / mem_total * 100) if mem_total > 0 else 0
        
        print(f"{CYAN}{'=' * 85}{END}")
        print(f"{BOLD}System Uptime:{END} {format_uptime(uptime)}")
        print(f"{BOLD}Load Average:{END} {load_avg['load_1']:.2f}  {load_avg['load_5']:.2f}  {load_avg['load_15']:.2f}")
        print(f"{BOLD}Memory:{END} Total: {format_memory(mem_total)} | Free: {format_memory(mem_free)} | Used: {format_memory(total_mem_used)} ({mem_used_percent:.1f}%)")
        print(f"{BOLD}CPU Cores:{END} {cores_count} | {BOLD}Processes:{END} {total_procs}")
        print(f"{GREEN}R:{status_counts['running']:03}{END}  {BLUE}S:{status_counts['sleeping']:03}{END}  {YELLOW}T:{status_counts['stopped']:03}{END}  {RED}Z:{status_counts['zombie']:03}{END}  {RED}X:{status_counts['dead']:03}{END}")
        print(f"{CYAN}{'=' * 85}{END}")
        print()
        
        # ========================================
        # هدر جدول
        # ========================================
        print(f"{BOLD}{'PID':>6}  {'USER':<12} {'S':<2}  {'%CPU':>6}  {'%MEM':>6}  {'TIME':>10}  COMMAND{END}")
        print(f"{CYAN}{'-' * 85}{END}")
        
        # ========================================
        # نمایش فرآیندها
        # ========================================
        for p in processes:
            status_color = get_color(p['status'])
            
            # رنگ CPU
            if p['cpu'] > 50:
                cpu_color = RED
            elif p['cpu'] > 25:
                cpu_color = YELLOW
            else:
                cpu_color = GREEN
            
            # رنگ MEM
            if p['mem'] > 50:
                mem_color = RED
            elif p['mem'] > 25:
                mem_color = YELLOW
            else:
                mem_color = GREEN
            
            print(f"{p['pid']:>6}  "
                  f"{p['user']:<12} "
                  f"{status_color}{p['status']:<2}{END}  "
                  f"{cpu_color}{p['cpu']:>6.1f}{END}  "
                  f"{mem_color}{p['mem']:>6.1f}{END}  "
                  f"{p['time']:>10}  "
                  f"{p['command']}")
        
        print()
        print(f"{CYAN}{'-' * 85}{END}")
        print(f"{YELLOW}Top 20 processes by CPU usage | Refresh: 1s | Press Ctrl+C to exit{END}")
        
        time.sleep(1)

# ============================================
# اجرا
# ============================================
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        clear_screen()
        print(f"{GREEN}Goodbye!{END}")