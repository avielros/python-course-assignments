from datetime import datetime, timedelta
from collections import defaultdict

def parse_time(s):
    return datetime.strptime(s, "%H:%M")

def read_log_file(filename):
    with open(filename) as f:
        content = f.read()
    return [block.strip().splitlines() for block in content.strip().split("\n\n")]

def process_session(session):
    report_lines = []
    activity_durations = defaultdict(int)
    times = []
    
    for line in session:
        time_str, activity = line[:5], line[6:].strip()
        time = parse_time(time_str)
        times.append((time, activity))

    for i in range(len(times) - 1):
        start, activity = times[i]
        end, _ = times[i + 1]
        duration = int((end - start).total_seconds() / 60)
        activity_durations[activity] += duration
        report_lines.append(f"{start.strftime('%H:%M')}-{end.strftime('%H:%M')} {activity}")
    
    return report_lines, activity_durations

def generate_report(input_file, output_file):
    sessions = read_log_file(input_file)
    total_activity = defaultdict(int)
    all_lines = []

    for session in sessions:
        session_lines, activity_durations = process_session(session)
        all_lines.extend(session_lines)
        all_lines.append("")  # separate sessions
        for activity, duration in activity_durations.items():
            total_activity[activity] += duration

    # Remove last empty line
    if all_lines[-1] == "":
        all_lines.pop()

    # Add summary
    all_minutes = sum(total_activity.values())
    summary = sorted(total_activity.items(), key=lambda x: (-x[1], x[0]))
    all_lines.append("")
    for activity, minutes in summary:
        percent = round(minutes / all_minutes * 100)
        all_lines.append(f"{activity:<25}{minutes:>3} minutes   {percent:>2}%")

    with open(output_file, "w") as f:
        f.write("\n".join(all_lines))
