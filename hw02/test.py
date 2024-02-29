import subprocess
import pytest

INTERPRETER = 'python3'

def run_script(filename, input_data=None):
    proc = subprocess.run(
        [INTERPRETER, filename],
        input='\n'.join(input_data if input_data else []),
        capture_output=True,
        text=True,
        check=False
    )
    return proc.stdout.strip()

test_data = {
    'fact': [
        (5, 120),
        (10, 3628800),
        (15, 1307674368000),
        (17, 355687428096000),
        (123, 12146304367025329675766243241881295855454217088483382315328918161829235892362167668831156960612640202170735835221294047782591091570411651472186029519906261646730733907419814952960000000000000000000000000000)
    ],
    'show_employee':
    [
        (['Иванов Иван Иванович', 30000], 'Иванов Иван Иванович: 30000 ₽'),
        (['Осин Кирилл Андреевич', 1330700], 'Осин Кирилл Андреевич: 1330700 ₽'),
        (['Репчанский Николай Евгеньевич', 70800], 'Репчанский Николай Евгеньевич: 70800 ₽'),
        (['Сазонов Иван Максимович'], 'Сазонов Иван Максимович: 100000 ₽'),
        (['Иванов Иван Иванович'], 'Иванов Иван Иванович: 100000 ₽')
    ],
    'sum_and_sub':
    [
        ([1.32, 21.1], (22.42, -19.78)),
        ([-3.14, 22.1], (18.96, -25.24)),
        ([1.3, -3], (-1.7, 4.3))
    ],
    "process_list_gen":
    [
        ([1, 2, 3, 7, 9, 1, 2, 8], [1, 4, 27, 343, 729, 1, 4, 64]),
        ([9, 12, 55, 12, 567, 12, -123], [729, 144, 166375, 144, 182284263, 144, -1860867]),
        ([-1, 4, 6, 34, -1, -34], [-1, 16, 36, 1156, -1, 1156])
    ],
    "process_list":
    [
        ([1, 2, 3, 7, 9, 1, 2, 8], [1, 4, 27, 343, 729, 1, 4, 64]),
        ([9, 12, 55, 12, 567, 12, -123], [729, 144, 166375, 144, 182284263, 144, -1860867]),
        ([-1, 4, 6, 34, -1, -34], [-1, 16, 36, 1156, -1, 1156])
    ],
    "my_sum":
    [
        ([1, 2, 3, 7, 9, 1, 2, 8], 33),
        ([9, 12, 55, 12, 567, 12], 667),
        ([-1, 4, 6, 34, -1, -34], 8)
    ],
    "my_sum_argv":
    [
        (['1', '2', '3', '4', '5'], 15),
        (['-1', '4', '6', '34', '-1', '-34'], 8),
        (['9', '12', '55', '12', '567', '12'], 667)
    ],
    "files_sort":
    [
        (['./test_dir_1/'], "tmp_2.py\ntmp_3.py\ntmp.txt\ntmp_1.txt"),
        (['./test_dir_2/'], "tmp.bin\ntmp_1.c\ntmp_2.c\ntmp_3.py"),
        (['./test_dir_3/'], "a.py\nb.py\nc.py\na.txt\nb.txt\nc.txt"),
    ],
    "file_search":
    [
        (['my_sum.py'], "def my_sum(*args):\nreturn sum(args)"),
        (['my_sum.pi'], "Файл my_sum.pi не найден."),
        (['fact.py'], "from functools import lru_cache\nimport time\n\n@lru_cache(10000)\ndef fact_rec(n: int) -> int:"),
    ],
    "fun":
    [
        ('lara@mospolytech.ru', True),
        ('brian-23@mospolytech.ru', True),
        ('britts_54@mospolytech.ru', True),
        ('britts_54@mospolytech.comru', False),
        ('britts!_54@mospolytech.ru', False)
    ],
    "fibonacci":
    [
        (["3"], '[0, 1, 1]'),
        (["5"], '[0, 1, 1, 8, 27]'),
        (["10"], '[0, 1, 1, 8, 27, 125, 512, 2197, 9261, 39304]'),
        [["25"], '[0, 1, 1, 8, 27, 125, 512, 2197, 9261, 39304, 166375, 704969, 2985984, '
 '12649337, 53582633, 226981000, 961504803, 4073003173, 17253512704, '
 '73087061741, 309601747125, 1311494070536, 5555577996431, 23533806109393, '
 '99690802348032]']
    ],
    "average_scores":
    [
        (("5 3", "89 90 78 93 80\n90 91 85 88 86\n91 92 83 89 90.5"), ['90.0', '91.0', '82.0', '90.0', '85.5']),
        (("3 6", "76 86 44\n89 94.3 4\n54 34.3 43\n67.67 24 3.3\n78 34.34 23\n98 76 54"), ['77.11166666666666', '58.15666666666667', '28.55'])
    ],
    "plane_angle":
    [
        (["4 2 3\n4 5 6\n7 6 23\n15 11 12"], ['109.0353268438445']),
        (["4 9 12\n45 12 5\n1 2 3\n45 23 17"], ['7.059938483884908']),
        (["45 12 32\n25 12 4\n12 21 3\n425 223 117"], ['53.12364094395001']),
        (["1 22 32\n251 312 14\n132 1 3\n125 23 5"], ['7.39411907312768']),
    ],
    "phone_number":
    [
        (["3\n07895462130\n89875641230\n9195969878"], ['+7 (789) 546-21-30', '+7 (919) 596-98-78', '+7 (987) 564-12-30']),
        (["2\n79102714182\n89197564344"], ['+7 (910) 271-41-82', '+7 (919) 756-43-44']),
        (["2\n79991112334\n06754321234"], ['+7 (675) 432-12-34', '+7 (999) 111-23-34'])
    ],
    "people_sort":
    [
        (["3\nMike Thomson 20 M\nRobert Bustle 32 M\nAndria Bustle 30 F"], ['Mr. Mike Thomson', 'Ms. Andria Bustle', 'Mr. Robert Bustle']),
        (["4\nMike Tyson 40 M\nRobert Dawny 45 M\nMarco Robby 40 F\nVladimir Medvedev 40 M"], ['Mr. Mike Tyson', 'Ms. Marco Robby', 'Mr. Vladimir Medvedev', 'Mr. Robert Dawny']),
        (["3\nOsin Kirill 21 M\nSome Female 12 F\nSome Boy 34 M"], ['Ms. Some Female', 'Mr. Osin Kirill', 'Mr. Some Boy'])
    ],
    "complex_numbers":
    [
        (["2 1\n5 6"], ['7.00+7.00i', '-3.00-5.00i', '4.00+17.00i', '0.26-0.11i', '2.24+0.00i', '7.81+0.00i']),
        (["4 5\n6 7"], ['10.00+12.00i', '-2.00-2.00i', '-11.00+58.00i', '0.69+0.02i', '6.40+0.00i', '9.22+0.00i']),
        (["5 3\n6 91"], ['11.00+94.00i', '-1.00-88.00i', '-243.00+473.00i', '0.04-0.05i', '5.83+0.00i', '91.20+0.00i'])
    ]


}

from fact import fact_it, fact_rec

@pytest.mark.parametrize("input_data, expected", test_data['fact'])
def test_fact_it(input_data, expected):
    assert fact_it(input_data) == expected

@pytest.mark.parametrize("input_data, expected", test_data['fact'])
def test_fact_rec(input_data, expected):
    assert fact_rec(input_data) == expected

from show_employee import show_employee

@pytest.mark.parametrize("input_data, expected", test_data['show_employee'])
def test_show_employee(input_data, expected):
    assert show_employee(*input_data) == expected

from sum_and_sub import sum_and_sub

@pytest.mark.parametrize("input_data, expected", test_data['sum_and_sub'])
def test_sum_and_sub(input_data, expected):
    assert sum_and_sub(*input_data) == pytest.approx(expected)

from process_list import process_list_gen, process_list

@pytest.mark.parametrize("input_data, expected", test_data['process_list_gen'])
def test_process_list_gen(input_data, expected):
    assert process_list_gen(input_data) == pytest.approx(expected)

@pytest.mark.parametrize("input_data, expected", test_data['process_list'])
def test_process_list(input_data, expected):
    assert process_list(input_data) == pytest.approx(expected)

from my_sum import my_sum

@pytest.mark.parametrize("input_data, expected", test_data['my_sum'])
def test_my_sum(input_data, expected):
    assert my_sum(*input_data) == pytest.approx(expected)

@pytest.mark.parametrize("input_data, expected", test_data['my_sum_argv'])
def test_my_sum_argv(input_data, expected):
    result = subprocess.run(['python3', '-m', 'my_sum_argv'] + input_data, capture_output=True, text=True)
    assert result.returncode == 0
    assert int(result.stdout.strip()) == expected

@pytest.mark.parametrize("input_data, expected", test_data['files_sort'])
def test_files_sort(input_data, expected):
    result = subprocess.run(['python3', '-m', 'files_sort'] + input_data, capture_output=True, text=True)
    assert result.stdout.strip() == expected

@pytest.mark.parametrize("input_data, expected", test_data['file_search'])
def test_file_search(input_data, expected):
    result = subprocess.run(['python3', '-m', 'file_search'] + input_data, capture_output=True, text=True)
    assert result.stdout.strip() == expected


from email_validation import fun

@pytest.mark.parametrize("input_data, expected", test_data['fun'])
def test_fun(input_data, expected):
    assert fun(input_data) == expected


@pytest.mark.parametrize("input_data, expected", test_data['fibonacci'])
def test_fibonacci(input_data, expected):
    assert run_script('fibonacci.py', input_data) == expected

@pytest.mark.parametrize("input_data, expected", test_data['average_scores'])
def test_average_scores(input_data, expected):
    assert run_script('average_scores.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['plane_angle'])
def test_plane_angle(input_data, expected):
    assert run_script('plane_angle.py', input_data).split('\n') == pytest.approx(expected)

@pytest.mark.parametrize("input_data, expected", test_data['phone_number'])
def test_phone_number(input_data, expected):
    assert run_script('phone_number.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['people_sort'])
def test_people_sort(input_data, expected):
    assert run_script('people_sort.py', input_data).split('\n') == expected


@pytest.mark.parametrize("input_data, expected", test_data['complex_numbers'])
def test_complex_numbers(input_data, expected):
    assert run_script('complex_numbers.py', input_data).split('\n') == expected
