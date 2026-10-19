import datetime
import ipaddress
import json
from pathlib import Path


def is_valid_line(line: list) -> bool:
    
    levels = ["INFO", "ERROR", "WARNING"]
    if len(line) == 5:
        try:
            datetime.datetime.strptime(line[0], '%Y-%m-%d')
            datetime.datetime.strptime(line[1], '%H:%M:%S')
            ipaddress.ip_address(line[3])
        except ValueError:
            return False
        else:
            if line[2] in levels:
                return True
    return False


def analyze_log(path: Path, json_path: Path) -> Path:

    if not path.exists():
        raise FileNotFoundError('Файл server.log не найден.')

    analyze_result = {
        "levels": {'INFO': 0, 'WARNING': 0, 'ERROR': 0},
        "top_error_ip" : None,
        "errors_by_hour": {},
        'broken_lines': 0,
    }
    
    contents = path.read_text().rstrip().splitlines()
    ip_vocab = {}

    for line in contents:
        if not line.strip(): continue

        splitted_line = line.split(maxsplit=4)

        if not is_valid_line(splitted_line):  # Ошибки
            analyze_result['broken_lines'] += 1
            continue

        analyze_result['levels'][splitted_line[2]] +=1 # Уровни

        if splitted_line[2] == "ERROR":
            err_by_hour_vocab = analyze_result['errors_by_hour'] # Ошибки по часам
            hour = splitted_line[1].split(':')[0]
            err_by_hour_vocab[hour] = err_by_hour_vocab.get(hour, 0) + 1

            ip = splitted_line[3]
            ip_vocab[ip] = ip_vocab.get(ip, 0) + 1

    if ip_vocab:
        top_error_ip = max(ip_vocab, key=lambda ip: ip_vocab[ip])
        analyze_result['top_error_ip'] = top_error_ip

    analyze_result_json = json_path.write_text(json.dumps(
        analyze_result, ensure_ascii=False, indent=4),
        encoding='UTF-8'
        )
    return analyze_result_json

path = Path('server.log')
json_path = Path('analyze_result.json')
result = analyze_log(path, json_path)

