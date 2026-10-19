from log_analyzer import analyze_lines, analyze_log


def test_empty_log():
    result = analyze_lines([])
    assert result['broken_lines'] == 0
    assert result['top_error_ip'] is None


def test_empty_lines_are_skipped():
    result = analyze_lines(['', '   ', 'битая строка'])
    assert result['broken_lines'] == 1


def test_broken_line():
    result = analyze_lines(['Поломка!!'])
    assert result['broken_lines'] == 1


def test_incorrcect_date():
    result = analyze_lines(['2026-10/15 09:12:01 INFO 192.168.1.10 User login'])
    assert result['broken_lines'] == 1


def test_incorrcect_ip():
    result = analyze_lines(['2026-10-15 09:12:01 INFO 266.168.1.10 User login'])
    assert result['broken_lines'] == 1



def test_log_without_errors(tmp_path):
    log = tmp_path / 'server.log'
    log.write_text('2026-10-15 09:12:01 INFO 192.168.1.10 User login\n' \
    '2026-10-15 09:12:01 INFO 192.168.1.10 User login\n' \
    '2026-10-15 10:02:13 WARNING 192.168.1.10 Slow response\n' \
    '2026-10-15 10:31:12 INFO 192.168.1.35 User logout', encoding='utf-8')

    result = analyze_log(log)
    assert result['top_error_ip'] is None

def test_normal_log():
    lines = [
        '2026-10-15 09:15:44 ERROR 192.168.1.22 Database timeout',
        '2026-10-15 10:30:00 ERROR 192.168.1.22 Database timeout',
        '2026-10-15 10:31:12 INFO 192.168.1.35 User logout',
    ]
    assert analyze_lines(lines) == {
        'levels': {'INFO': 1, 'WARNING': 0, 'ERROR': 2},
        'top_error_ip': '192.168.1.22',
        'errors_by_hour': {'09': 1, '10': 1},
        'broken_lines': 0,
    }