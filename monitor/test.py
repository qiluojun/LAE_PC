import time
import psutil

# 获取当前时间
def get_current_time():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

# 获取指定进程的名称
def get_process_name(pid):
    try:
        process = psutil.Process(pid)
        return process.name()
    except:
        return ''

# 监控程序
def monitor(start_time, end_time):
    print("it")
    # 打开数据文件
    with open('data.txt', 'w') as f:
        f.write('程序名称\t程序开始时间\t程序结束时间\t用户名称\n')
    
    # 监控循环
    while True:
        # 获取当前时间
        current_time = get_current_time()
        
        # 判断是否到达结束时间
        if current_time >= end_time:
            break
        
        # 获取当前正在运行的进程列表
        processes = psutil.process_iter(attrs=['pid', 'name', 'create_time','username'])
        # print(processes)
        # 遍历进程列表，记录需要监控的进程
        for process in processes:
            # print(process.info)
            process_name = get_process_name(process.info['pid'])
            create_time = get_current_time()# process.info['create_time']
            username = process.info['username']
            #print(process.info)
            if username in ['TANGJIA-LAP\\qiluo']:
                with open('data.txt', 'a') as f:
                    f.write('{}\t{}\t{}\t{}\n'.format(process_name, create_time, current_time,username))
            
            # 判断进程是否需要监控
            # if process_name in ['chrome.exe', 'firefox.exe','wpsoffice']:
            #     # 记录进程信息
            #     with open('data.txt', 'a') as f:
            #         f.write('{}\t{}\t{}\n'.format(process_name, create_time, current_time))
        
        # 休眠一段时间，减少CPU占用率
        time.sleep(10)
    
    # 监控结束
    print('监控结束')


def get_chrome_urls():
    urls = []
    for process in psutil.process_iter(attrs=['pid', 'name', 'cmdline']):
        if process.info['name'] == 'msedge.exe':
            print(process.info)
            for arg in process.info['cmdline']:
                if arg.startswith('http') or arg.startswith('https'):
                    urls.append(arg)
    return urls
# 测试代码
if __name__ == '__main__':  
    start_time = '2023-07-22 17:00:00'
    end_time = '2023-07-22 18:10:00'
    urls = get_chrome_urls()
    print(urls)
    monitor(start_time, end_time)

