from datetime import datetime, timedelta


class AttendanceTracker:
    def __init__(self):
        self.attendance_records = []
        self.attendance_date = None
        

    def take_date(self):
        date_str = input("Enter date (YYYY-MM-DD): ")
        try:
            self.attendance_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print("Please enter the date in the format YYYY-MM-DD.")

    def take_attendance(self):
        while True:
            in_time_str = input("Enter entry time (HH:MM) or 'no' to stop: ")
            if in_time_str.lower() == 'no':
                break

            out_time_str = input("Enter exit time (HH:MM): ")
            try:
                entry_time = datetime.strptime(in_time_str, "%H:%M")
                exit_time = datetime.strptime(out_time_str, "%H:%M")
            except ValueError:
                print("Please enter time in format HH:MM.")
                continue

            self.attendance_records.append((entry_time, exit_time))

    def calculate_working_hours(self):
        total_working_hours = timedelta()
        total_breaks = timedelta()

        for i in range(len(self.attendance_records)):
            entry_time, exit_time = self.attendance_records[i]

            if i < len(self.attendance_records) - 1:
                next_entry_time, _ = self.attendance_records[i + 1]
                break_duration = next_entry_time - exit_time
                total_breaks += max(break_duration, timedelta())  # Ensure positive break time

            work_duration = exit_time - entry_time
            total_working_hours += work_duration

        return total_working_hours, total_breaks

    def show_attendance_data(self):
        print(f"Attendance Data for {self.attendance_date}:")
        for entry_time, exit_time in self.attendance_records:
            print(f"Entry: {entry_time.strftime('%H:%M')} - Exit: {exit_time.strftime('%H:%M')}")

    def show_summary(self):
        total_work_hours, total_breaks = self.calculate_working_hours()
        total_working_and_breaks = total_work_hours + total_breaks

        print("\nSummary:")
        print(f"Total working hours: {total_work_hours}")
        print(f"Total breaks: {total_breaks}")
        print(f"Total working hours + breaks: {total_working_and_breaks}")
        return total_work_hours, total_breaks, total_working_and_breaks


# Example usage
attendance = AttendanceTracker()
attendance.take_date()
attendance.take_attendance()
attendance.show_attendance_data()
attendance.show_summary()
