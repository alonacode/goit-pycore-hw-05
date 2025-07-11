import sys


def parse_log_line(line: str) -> dict:
    """
    Парсить рядок логу у словник з ключами: date, time, level, message.
    """
    parts = line.strip().split(' ', 3)
    if len(parts) < 4:
        raise ValueError(f"Invalid log line format: {line}")
    return {
        "date": parts[0],
        "time": parts[1],
        "level": parts[2],
        "message": parts[3]
    }


def load_logs(file_path: str) -> list:
    """
    Зчитує лог-файл та повертає список словників для кожного запису.
    """
    logs = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if line.strip():
                    logs.append(parse_log_line(line))
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        sys.exit(1)
    except IOError as e:
        print(f"Error reading file: {e}")
        sys.exit(1)
    return logs


def filter_logs_by_level(logs: list, level: str) -> list:
    """
    Фільтрує список логів за рівнем логування.
    """
    return list(filter(lambda log: log["level"].lower() == level.lower(), logs))


def count_logs_by_level(logs: list) -> dict:
    """
    Підраховує кількість записів для кожного рівня логування.
    """
    counts = {}
    for log in logs:
        lvl = log["level"]
        counts[lvl] = counts.get(lvl, 0) + 1
    return counts


def display_log_counts(counts: dict):
    """
    Форматує та виводить таблицю зі статистикою по рівнях логування.
    """
    print("\nРівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<16} | {count}")


def display_logs_details(logs: list, level: str):
    """
    Виводить детальні записи для вказаного рівня логування.
    """
    print(f"\nДеталі логів для рівня '{level.upper()}':")
    for log in logs:
        print(f"{log['date']} {log['time']} - {log['message']}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <log_file_path> [log_level]")
        sys.exit(1)

    file_path = sys.argv[1]
    level = sys.argv[2] if len(sys.argv) > 2 else None

    logs = load_logs(file_path)
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if level:
        filtered = filter_logs_by_level(logs, level)
        if filtered:
            display_logs_details(filtered, level)
        else:
            print(f"\nNo logs found for level '{level.upper()}'.")


if __name__ == "__main__":
    main()
