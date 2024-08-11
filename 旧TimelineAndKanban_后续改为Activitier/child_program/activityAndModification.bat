@echo off
chcp 65001
start "" "D:\useful_apps\SQLite_related\SQLiteStudio.exe" "D:\学习and学校\搞事情\LAE\TimelineAndKanban\activity.db"
start /B python "D:\学习and学校\搞事情\LAE\TimelineAndKanban\ui\functions\db_modification.py"
start /B python "D:\学习and学校\搞事情\LAE\reminderANDwatcher\goal_allocation_expectation.py"
echo.
pause