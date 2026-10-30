import datetime
import ipaddress
import json
from pathlib import Path


def is_valid_line(parts: list) -> bool:
    ''' Проверка строки логи на правильность '''

    levels = ["INFO", "ERROR", "WARNING"]

    if len(parts) == 5:
        date, time, level, ip, message = parts
        try:
            datetime.datetime.strptime(date, '%Y-%m-%d')
            datetime.datetime.strptime(time, '%H:%M:%S')
            ipaddress.ip_address(ip)
        except ValueError:
            return False
        else:
            if level in levels:
                return True
    return False


def save_result(result, json_path) -> None:
    ''' Вывод результата анализа лог в json-файл.'''
    analyze_result_json = json_path.write_text(json.dumps(
            result, ensure_ascii=False, indent=4),
            encoding='UTF-8'
            )
    

def read_lines(path: Path):
    with path.open(encoding='UTF-8') as f:
        for line in f:
            yield line.rstrip()

def parse(lines):
    for line in lines:
        if not line.rstrip(): 
            continue

        if not is_valid_line(line.split(maxsplit=4)):  # Ошибки
            yield None
            continue

        date, time, level, ip, message = line.split(maxsplit=4)
        yield {'date': date, 'time': time, 'level': level, 'ip': ip, 'message': message}


def aggregate(records: dict|None) -> dict:
    analyze_result = {
                "levels": {'INFO': 0, 'WARNING': 0, 'ERROR': 0},
                "top_error_ip" : None,
                "errors_by_hour": {},
                'broken_lines': 0,
            }
    
    ip_vocab = {}
    
    for record in records:

        if not record:
            analyze_result['broken_lines'] += 1
            continue
        level, time, ip = record['level'], record['time'], record['ip']

        analyze_result['levels'][level] +=1

        if level == "ERROR":
            err_by_hour_vocab = analyze_result['errors_by_hour'] # Ошибки по часам
            hour = time.split(':')[0]
            err_by_hour_vocab[hour] = err_by_hour_vocab.get(hour, 0) + 1
            ip_vocab[ip] = ip_vocab.get(ip, 0) + 1

    if ip_vocab:
        top_error_ip = max(ip_vocab, key=lambda ip: ip_vocab[ip])
        analyze_result['top_error_ip'] = top_error_ip
        
    return analyze_result

if __name__ == '__main__':
    # result = analyze_log(Path('server.log'))
    result = aggregate(parse(read_lines(Path('server.log'))))
    save_result(result, Path('analyze_result.json'))
