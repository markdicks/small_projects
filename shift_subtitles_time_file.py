import re
import sys

def parse_time_shift(time_shift):
    """Parse the time shift input into milliseconds."""
    if ',' in time_shift:
        time_shift = time_shift.replace(',', '.')
    if ':' in time_shift:
        parts = time_shift.split(':')
        if len(parts) == 2:
            minutes, seconds = parts
            return int(float(minutes) * 60000 + float(seconds) * 1000)
    return int(float(time_shift) * 1000)

def shift_time(time_str, shift_ms):
    """Shift a time string by the specified milliseconds."""
    hh, mm, ss_ms = time_str.split(':')
    ss, ms = ss_ms.split(',')
    total_ms = int(hh) * 3600000 + int(mm) * 60000 + int(ss) * 1000 + int(ms)
    total_ms += shift_ms
    if total_ms < 0:
        total_ms = 0 # Clamp to 0 if time goes negative
    hh = total_ms // 3600000
    total_ms %= 3600000
    mm = total_ms // 60000
    total_ms %= 60000
    ss = total_ms // 1000
    ms = total_ms % 1000
    return f"{hh:02}:{mm:02}:{ss:02},{ms:03}"

def process_srt_file(input_file, output_file, shift_ms):
    """Process the SRT file and shift all timestamps."""
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            if re.match(r'\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}', line):
                start, end = line.strip().split(' --> ')
                new_start = shift_time(start, shift_ms)
                new_end = shift_time(end, shift_ms)
                outfile.write(f"{new_start} --> {new_end}\n")
            else:
                outfile.write(line)

def main():
    if len(sys.argv) != 4:
        print("Usage: python shift_subtitles.py <input_file.srt> <time_shift> <output_file.srt>")
        sys.exit(1)

    input_file = sys.argv[1]
    time_shift = sys.argv[2]
    output_file = sys.argv[3]

    try:
        shift_ms = parse_time_shift(time_shift)
    except ValueError:
        print("Invalid time shift format. Accepted examples: 0,1 | 0,5 | 1 | 100 | 1:2,8 | 2,3")
        sys.exit(1)

    process_srt_file(input_file, output_file, shift_ms)
    print(f"Subtitles shifted by {time_shift} and saved to {output_file}")

if __name__ == "__main__":
    main()
