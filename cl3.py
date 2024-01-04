from datetime import datetime

class AttendanceSystem:
    def __init__(self):
        self.attendance_data = []
    
    def take_attendance(self):
        while True:
            enter_time_str = input("Enter entry time (HH:MM): ")
            exit_time_str = input("Enter exit time (HH:MM): ")
            choice = input("Enter 'no' to stop adding attendance, else press 'Enter' to continue: ").lower()

            enter_time = datetime.strptime(enter_time_str, "%H:%M")
            exit_time = datetime.strptime(exit_time_str, "%H:%M")
            break_time = (exit_time - enter_time).total_seconds() / 3600

            self.attendance_data.append({
                'enter_time': enter_time,
                'exit_time': exit_time,
                'break_time': break_time
            })

            if choice == 'no':
                break
    
    def calculate_total_working_hours(self):
        total_working_hours = sum(att['break_time'] for att in self.attendance_data)
        return total_working_hours
    
    def display_attendance_summary(self):
        total_hours = self.calculate_total_working_hours()
        hours, remainder = divmod(total_hours * 3600, 3600)
        minutes, _ = divmod(remainder, 60)
        print(f"Total working hours: {int(hours):02d}:{int(minutes):02d}")


# Usage
attendance_system = AttendanceSystem()
attendance_system.take_attendance()
attendance_system.display_attendance_summary()
