
'''
在原来timelineV3.3.2 的基础上：
    可以给活动计时 时间显示在屏幕上 并且 可以暂停 
    也可以记录到文档里~哦吼吼~

'''

# Create a new variable to track the pause state
is_paused = False
activity_lenth = timedelta(seconds=0)

def update_activity():
    global is_paused, start_time,timer2
    # Start the time counting
    start_time = datetime.now()
    is_paused = False
    timer2 = QTimer()
    # Connect the timer's timeout signal to the update_label function
    timer2.timeout.connect(update_label)

    # Start the timer to update the label every second
    timer2.start(1000)  # Update every 1000 milliseconds (1 second)

    
    # Update the label with the current time
    #main_window.ui.current_period_name_label.setText("Name: " + start_time.strftime("%H:%M"))



def update_label():
    global is_paused, start_time,activity_lenth,formatted_time
    
    

    if not is_paused:
        # Calculate the elapsed time
        activity_lenth += timedelta(seconds=1)

        total_seconds = activity_lenth.total_seconds()
        hours = int(total_seconds // 3600)
        minutes = int((total_seconds % 3600) // 60)
        seconds = int(total_seconds % 60)

        formatted_time = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        # Update the label with the formatted time
        main_window.ui.current_period_name_label.setText("Name: " + formatted_time)

def pause_resume_activity():
    global is_paused,start_time
    # Toggle the pause state
    is_paused = not is_paused




def end_activity():
    global is_paused, start_time, paused_time, timer2
    # Stop the time counting
    end_time = datetime.now()

    # Write the starting point, ending point, and total time length to the md file
    content = f"Start Time: {start_time.strftime('%H:%M')}\n"
    content += f"End Time: {end_time.strftime('%H:%M')}\n"
    content += f"Total Time: {activity_lenth}\n"

    with open(r"D:\学习and学校\obsidian\qiluo\00-BASE\for_text.md", "a", encoding="utf-8") as f:
        f.write(content)

    # Clear the label and reset the pause state
    main_window.ui.current_period_name_label.setText("Name: 空")
    is_paused = False
    timer2.stop()



main_window.ui.basic_state_record_button.clicked.connect(pause_resume_activity)


