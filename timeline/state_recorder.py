







# add a button and three entries for the user to input a new name, time, and content for the selected reminder
new_name_entry = tk.Entry(left_frame, font=("TkDefaultFont", 20))
new_name_entry.pack()
new_time_entry = tk.Entry(left_frame, font=("TkDefaultFont", 20))
new_time_entry.pack()
new_content_entry = tk.Entry(left_frame, font=("TkDefaultFont", 20))
new_content_entry.pack()

def update_reminder():
    # get the selected reminder from the listbox
    selected_index = listbox.curselection()
    if selected_index:
        selected_index = int(selected_index[0])
        # update the selected reminder with the values entered in the new entries
        reminder_list[selected_index] = (new_name_entry.get(), new_time_entry.get(), new_content_entry.get())
        # update the listbox with the new name of the selected reminder
        listbox.delete(selected_index)
        listbox.insert(selected_index, new_name_entry.get())
        # save the updated reminder_list to a JSON file
        with open('reminders.json', 'w') as f:
            json.dump(reminder_list, f)

update_button = tk.Button(left_frame, text="Update Reminder", command=update_reminder, font=("TkDefaultFont", 20))
update_button.pack()

# start the reminder checking function in a separate thread
reminder_timer = threading.Thread(target=check_reminder)
reminder_timer.start()

# start the main loop
root.mainloop()