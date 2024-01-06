import json
from datetime import datetime, timedelta

class AttendanceTracker:
    def __init__(self):
        self.attendance_records = []
        self.attendance_date = None
        self.json_file = "attendance_data.json"

    def take_date(self):
        date_str = input("Enter date (YYYY-MM-DD): ")
        try:
            self.attendance_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print("Please enter the date in the format YYYY-MM-DD.")

    def take_attendance(self):
        while True:
            entry_time_str = input("Enter entry time (HH:MM) or 'no' to stop: ")
            if entry_time_str.lower() == 'no':
                break

            exit_time_str = input("Enter exit time (HH:MM): ")
            try:
                entry_time = datetime.strptime(entry_time_str, "%H:%M")
                exit_time = datetime.strptime(exit_time_str, "%H:%M")
            except ValueError:
                print("Please enter time in format HH:MM.")
                continue

            self.attendance_records.append((entry_time.strftime('%H:%M'), exit_time.strftime('%H:%M')))

    def calculate_working_hours(self):
        total_working_hours = timedelta()
        total_breaks = timedelta()

        for i in range(len(self.attendance_records)):
            entry_time_str, exit_time_str = self.attendance_records[i]

            if i < len(self.attendance_records) - 1:
                next_entry_time_str, _ = self.attendance_records[i + 1]
                break_duration = datetime.strptime(next_entry_time_str, "%H:%M") - datetime.strptime(exit_time_str, "%H:%M")
                total_breaks += max(break_duration, timedelta())  # Ensure positive break time

            work_duration = datetime.strptime(exit_time_str, "%H:%M") - datetime.strptime(entry_time_str, "%H:%M")
            total_working_hours += work_duration

        return total_working_hours, total_breaks

    def show_attendance_data(self):
        print(f"Attendance Data for {self.attendance_date}:")
        for entry_time, exit_time in self.attendance_records:
            print(f"Entry: {entry_time} - Exit: {exit_time}")

    def show_summary(self):
        total_work_hours, total_breaks = self.calculate_working_hours()
        total_working_and_breaks = str(total_work_hours + total_breaks)

        print("\nSummary:")
        print(f"Total working hours: {total_work_hours}")
        print(f"Total breaks: {total_breaks}")
        print(f"Total working hours + breaks: {total_working_and_breaks}")
        return str(total_work_hours), str(total_breaks), total_working_and_breaks

    def save_to_json(self):
        summary = {}
        summary['Date'] = str(self.attendance_date)
        summary['Attendance'] = self.attendance_records
        total_work_hours, total_breaks, total_working_and_breaks = self.show_summary()
        summary['Total working hours'] = total_work_hours
        summary['Total breaks'] = total_breaks
        summary['Total working hours + breaks'] = total_working_and_breaks

        try:
            with open(self.json_file, 'r') as json_file:
                data = json.load(json_file)
                data.append(summary)
        except FileNotFoundError:
            data = [summary]

        with open(self.json_file, 'w') as json_file:
            json.dump(data, json_file)

        print(f"Attendance data saved to {self.json_file}")

# Example usage
attendance = AttendanceTracker()
attendance.take_date()
attendance.take_attendance()
attendance.save_to_json()
