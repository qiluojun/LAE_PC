import datetime

class Period:
    def __init__(self,name=" ",start_time=None,start_wait_time=None,abnormity=[],need_settlement_mannuly='',need_start_manually='',start_action=''):
        self.name=name
        self.start_time=start_time # 字符串 类似0120 代表01：20
        self.start_wait_time= start_wait_time # 字符串 类似0020 代表20min 如果是 0120 代表一个小时20min
        self.need_settlement_mannuly =need_settlement_mannuly
        self.need_start_manually =need_start_manually
        self.start_action =start_action 
        self.abnormity=abnormity 

class Today:
    def __init__(self,activities=[],periods=[],current_period=None,next_period=None,db=None):
        self.activities=activities
        self.periods=periods
        self.current_period=current_period 
        self.next_period=next_period
        self.db=db
    def get_periods(self,db,table):
        # self.db是数据库的路径
        # 在这里根据db文件的table"Period",把对应数据赋值给 self.periods。其中，self.periods是一个Period对象的列表 
        #w列表里 每一个period对象都有name和start_time等属性，名字和db的table列名一致，按此进行赋值
        pass
    
    def find_supposed_period(self,current_time):
        current_time=current_time
        supposed_period=''
        # supposed_period = #w根据self.periods，寻找current_time刚好在其列表里哪一个period的starttime之后，又在其下一个period的starttime之前，然后把当前时间所属的 period 赋值给supposed_period
        return supposed_period
    def start_period_auto(self,supposed_period): # 这里适用于 非手动开启时段的情况 
        #w根据规则&异常情况 生成self.current_period和self.next_period 两个Period对象
        #t并且要向db对应表格里写入记录 异常则要写入异常情况
        supposed_period =  supposed_period
        window_action=[]
        
        #T 根据时段特性 来决定触发的具体动作
        return window_action
    def record_period_start(self,supposed_period):
        supposed_period = supposed_period
        #t向db [对应表格] 里写入时段开始记录 记录supposed_period.name对应的时段的开始情况 
        #t以及如果 self.current_period.abonormity 不为空，则写入异常情况
    def set_period_in_today_pad(self,supposed_period):
        supposed_period = supposed_period 
        #w 把self.db 中表“Today_pad” 的 current_period 列值改为 supposed_period.name
    def check_period(self):
        
        current_time= datetime.datetime.now()
        current_time= current_time.strftime("%H%M") #w换成四位数，例如 0920代表09：20
        current_period_name= " "
        next_period_name = " "
        supposed_period = None 
        supposed_period = self.find_supposed_period(current_time)
        
        window_action=[]
        
        # 读取 self.db 中表“Today_pad”的数据，其中有两列 名为 current_period 和 next_period
        # w赋值给 current_period_name 和 current_period_name
        
        
        # 检查 pad里的当前时段名称是否正常 正常 则直接返回 啥都不干
        if current_period_name==" ":  
            
            self.current_period.abnormity.add('empty_current_period') 
        elif current_period_name != supposed_period.name:
            self.current_period.abnormity.add('current_period_mismatch')
        
        if self.current_period.abnormity==[]:
            return window_action  #一切正常 无需执行任何动作
        # pad里的当前时段名称不正常
        else:  
            if  'empty_current_period' in self.current_period.abnormity : # 当前时段为空
                if supposed_period.need_start_manually=='10': #如果应当时段为自动开启类 则自动开启
                    window_action=self.start_period_auto(supposed_period) 
                elif supposed_period.need_start_manually=='11' and (current_time >=supposed_period.start_time + supposed_period.wait_time): #w如果应对时段需要手动开启，且当前时间超过了应当时段的开始时间+等待时间
                    self.current_period.abnormity.add('未及时手动开始时段') #如果应当时段为手动开启类  且超过等待事件  
                    self.record_period_start(supposed_period) # 同样调用 【记录时段开始】函数 并且写入异常  
                    
            elif "current_period_mismatch" in self.current_period.abnormity and (current_time >=supposed_period.start_time + supposed_period.wait_time): #w且当前时间超过了应当时段的开始时间+等待时间  :
                self.current_period.abnormity.add('未及时手动开始时段') # 当前时段不为空  但是不对 而且超过等待时长
                self.record_period_start(supposed_period) # 同样调用 【记录时段开始】函数 并且写入异常
            self.set_period_in_today_pad(supposed_period) # 最后把当前pad的时段改成对的


        
        return window_action
            
