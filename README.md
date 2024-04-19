for Chinese version → [here](README_ZH.md)
中文版，请看[这里](README_ZH.md)

# LAE_PC
live and enjoy! with help from PC!

## What is "LAE program"? What can it do?

The LAE program is a series of self-regulation assistance programs designed with the purpose of "live and enjoy." The PC version has more features, while the mobile version is still in the early stages of development.

### Specific Features

Overall, the specific features are still under continuous development and await integration. Current features include:

- Record

  (Manual operation required) It records the time spent and content of activities, automatically archiving them to the corresponding position in the activity notes.

  It provides a quick self-assessment (equivalent to a simple scale) for various conditions of the day (such as sleep, exercise).

- Monitor & Identify

  Identifies the current activity (by recognizing the name of the front-end window), and thus provides reminders for abnormal situations.
  > For example, a reminder will pop up when visiting entertainment websites during study periods.

- Reminder & Display

  Regular reminders: Customized prompts that can pop up at specific times.

  Timed reminders: (The function of a reminder) Custom prompts can pop up after a set amount of time. (To prevent prolonged sitting!)

- Analysis

  It can analyze the time spent on specific types of activities during a certain period and compare it with expected goals to assist in task management.

### Implementation Methods

Core of the program: Python
> pyQT (UI design)

> sqlite (Data processing)

> There are also other small libraries used to implement functions such as recognizing front-end windows and monitoring keyboard and mouse input.

External software:
> Obsidian (Note-management software using md format files)

> Zotero (Literature management software)