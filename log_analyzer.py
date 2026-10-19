from pathlib import Path
import datetime
import ipaddress

def is_valid_line(line: list):
    levels = ["INFO", "ERROR", "WARNING"]
    if len(line) == 5:
        try:
            datetime.datetime.strptime(line[0], '%Y-%m-%d')
            datetime.datetime.strptime(line[1], '%H:%M:%S')
            ipaddress.ip_address(line[3])
        except:
            return False
        else:
            if line[2] in levels:
                return True
    return False

def analyze_log(path: Path):
    analyze_result = {
        "levels": {'INFO': 0, 'WARNING': 0, 'ERROR': 0},
        "top_error_ip" : None,
        "errors_by_hour": {},
        'broken_lines': 0,
    }
    contents = path.read_text().rstrip().splitlines()
    ip_vocab = {}

    for line in contents:
        splitted_line = line.split(maxsplit=4)

        if not is_valid_line(splitted_line):  # Ошибки
            analyze_result['broken_lines'] += 1
            continue

        analyze_result['levels'][splitted_line[2]] +=1 # Уровни

        if splitted_line[2] == "ERROR":
            err_by_hour_vocab = analyze_result['errors_by_hour'] # Ошибки по часам
            hour = splitted_line[1].split(':')[0]
            if not err_by_hour_vocab.get(hour, 0):
                err_by_hour_vocab[hour] = 0
            err_by_hour_vocab[hour] +=1


            ip = splitted_line[3]
            if not ip_vocab.get(ip):
                ip_vocab[ip] = 0
            ip_vocab[ip] +=1

    if contents:
        top_error_ip = max(ip_vocab, key=lambda ip: ip_vocab[ip])
        analyze_result['top_error_ip'] = top_error_ip

    return analyze_result



result = analyze_log(Path('server.log'))
print(result)
assert result['levels'] == {'INFO': 3, 'WARNING': 1, 'ERROR': 3}
assert result['top_error_ip'] == '192.168.1.22'
assert result['errors_by_hour'] == {'09': 1, '10': 1, '11': 1}
assert result['broken_lines'] == 1