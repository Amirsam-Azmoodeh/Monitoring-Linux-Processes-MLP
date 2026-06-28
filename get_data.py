import pwd

def uptime() :
    '''
    Outputs system uptime
    '''
    try :
        with open(f"/proc/uptime" , 'r') as data :
            data = data.read()
            return float(data.split()[0])
        
    except Exception :
        return 0.0



def meminfo():
    '''
    Additional memory information
    Returns the sum of the total memory space and the amount of free space
    '''
    try :
        with open("/proc/meminfo", 'r') as data:
            memory_dict = {}
            counter = 0
            for line in data:
                if line.startswith("MemTotal"):
                    memory_dict['mem_total'] = int(line.split()[1]) * 1024 # Kilobyte -> Byte
                    counter += 1

                elif line.startswith("MemFree"):
                    memory_dict['mem_free'] = int(line.split()[1]) * 1024 # Kilobyte -> Byte
                    counter += 1

        return {'mem_total' : memory_dict['mem_total'] , 'mem_free' : memory_dict['mem_free']}
    
    except Exception :
       return {'mem_total': 0, 'mem_free': 0}
            
            

def loadavg():
    '''
    Returns the load avarage
    '''
    try :
        with open("/proc/loadavg", 'r') as data :
            data = data.read()
            data = data.split(' ')
            return {
                'load_1' : float(data[0]) ,
                'load_5' : float(data[1]) ,
                'load_15' : float(data[2])
            }


    except Exception :
        return {'load_1': 0.0, 'load_5': 0.0, 'load_15': 0.0}


def stat(pid: str) : 
    '''
    Extracts and returns the necessary information for the desired process
    '''
    try :
        with open(f"/proc/{pid}/stat" , 'r') as data :
            data = data.read()

            data = data.split()

            try :
                with open(f"/proc/{pid}/status", 'r') as f:
                    for line in f:
                        if line.startswith("Uid:"):
                            uid = int(line.split()[1])
                            uid = pwd.getpwuid(uid).pw_name

            except Exception :
                uid = '#'

            while len(data[2]) > 1 :  # To remove the extra value that clutters the table
                data.pop(2)

            return {
                'pid' : int(data[0]),
                'command' : data[1][1:-1],
                'status' : data[2],
                'utime' : int(data[13]),
                'stime' : int(data[14]),
                'cutime': int(data[15]), 
                'cstime': int(data[16]),
                'starttime' : int(data[21]),
                'rss' : int(data[23]) ,
                'uid' : uid
                } 
        
    except Exception :
        return None