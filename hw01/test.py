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
    'python_if_else': [
        ('1', 'Weird'),
        ('4', 'Not Weird'),
        ('3', 'Weird'),
        ('6','Weird'),
        ('22', 'Not Weird')
    ],
    'arithmetic_operators': [
        (['1', '2'], ['3', '-1', '2']),
        (['10', '5'], ['15', '5', '50'])
    ],
    'division': [
        (['3', '5'], ['0', '0.6']),
        (['1', '1'], ['1', '1.0']),
        (['-4', '-8'], ['0', '0.5'])
    ],
    'loops': [
        ('3', ['0', '1', '4']),
        ('6', ['0', '1', '4', '9', '16', '25']),
        ('4', ['0', '1', '4', '9'])
    ],
    'print_function': [
        ('5', "12345"),
        ('9', "123456789"),
        ('4', "1234")
    ],
    "second_score": [
        (['5\n 2 3 6 6 5'], '5'),
        (['6\n 1 2 3 4 4 4'], '3'),
        (['6\n 1 1 1 1 1 1'], 'Not second place')
    ],
    "nested_list": [
        (['5\nHarry\n37.21\nBerry\n37.21\nTiny\n37.2\nAcrity\n41\nCharsh\n39'], ['Berry', 'Harry']),
        (['3\nKirill\n18.21\nDiana\n45.6\nAlina\n17.8'], ['Kirill']),
        (['4\nNastya\n77.7\nKolya\n43.21\nKane\n77.7\nDima\n45.5'], ['Dima'])
    ],
    "lists": [
        (["12\ninsert 0 5\ninsert 1 10\ninsert 0 6\nprint\nremove 6\nappend 9\nappend 1\nsort\nprint\npop\nreverse\nprint"], ["[6, 5, 10]", "[1, 5, 9, 10]", "[9, 5, 1]"]),
        (["3\ninsert 0 1\ninsert 0 2\nprint"], ["[2, 1]"]),
        (["4\ninsert 0 1\npop\npop\npop\nprint"], [""])
    ],
    "swap_case": [
        (["Www.MosPolytech.ru"], "wWW.mOSpOLYTECH.RU"),
        (["HelL0, WorLd!"], "hELl0, wORlD!"),
        (["i D0nE my HoMeWORk!!!!"], "I d0Ne MY hOmEworK!!!!")
    ],
    "split_and_join": [
        (["this is a string"], "this-is-a-string"),
        (["hello, world!"], "hello,-world!"),
        (["how are you?"], "how-are-you?"),
        (["it`snothinh!"], "it`snothinh!")
    ],
    "anagram": [
        (["cat\ntac"], "YES"),
        (["cat\ntaa"], "NO"),
        (["dog\ngoddam"], "NO"),
        (["name\namen"], "YES")
    ],
    "metro": [
        (["4\n1 3\n1 5\n2 3\n4 6\n3"], "1"),
        (["4\n1 3\n1 5\n2 3\n4 6\n2"], "3"),
        (["4\n1 3\n1 5\n2 3\n4 6\n1"], "2"),
        (["6\n1 2\n3 4\n5 6\n7 8\n9 10\n1 10\n2"], "1"),
        (["6\n1 2\n3 4\n5 6\n7 8\n9 10\n1 10\n1"], "2")
    ],
    "minion_game": [
        (["BANANA"], "Стюарт 12"),
        (["KIRILL"], "Стюарт 13"),
        (["ALINA"], "Кевин 9"),
        (["PYTHON"], "Стюарт 19")
    ],
    "is_leap": [
        (["2020"], "True"),
        (["2018"], "False"),
        (["3000"], "False"),
        (["1999"], "False"),
        (["2004"], "True")
    ],
    "happiness": [
        (["3 2\n1 5 3\n3 1\n5 7"], "1"),
        (["3 2\n1 5 3\n3 5\n5 1"], "1"),
        (["5 3\n1 2 3 4 5\n1 3 2\n3 5 1"], "2"),
    ],
    "pirate_ship": [
        (["20 3\nAPPLES 12 200\nROM 4 300\nSEAT 10 300"], "ROM 4.0 300.0\nSEAT 10.0 300.0\nAPPLES 6.0 100.0"),
        (["100 2\nBANANA 50 65\nORANGE 40 80"], "ORANGE 40.0 80.0\nBANANA 50.0 65.0")
    ],
    "matrix_mult": [
        (["3\n1 2 3\n4 5 6\n7 8 9\n-1 2 3\n 0 1 3\n3 4 5"], "8 16 24\n14 37 57\n20 58 90"),
        (["4\n-6 4 2 1\n5 6 0 3\n-5 -6 4 2\n4 5 6 7\n1 245 3 4\n-1 2 3 4\n5 6 3 1\n6 8 9 12"], "6 -1442 9 6\n17 1261 60 80\n33 -1197 -3 -16\n71 1082 108 126")
    ]
}

def test_hello_world():
    assert run_script('hello_world.py') == 'Hello, world!'

@pytest.mark.parametrize("input_data, expected", test_data['python_if_else'])
def test_python_if_else(input_data, expected):
    assert run_script('python_if_else.py', [input_data]) == expected

@pytest.mark.parametrize("input_data, expected", test_data['arithmetic_operators'])
def test_arithmetic_operators(input_data, expected):
    assert run_script('arithmetic_operators.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['division'])
def test_division(input_data, expected):
    assert run_script('division.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['loops'])
def test_loops(input_data, expected):
    assert run_script('loops.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['print_function'])
def test_print_function(input_data, expected):
    assert run_script('print_function.py', input_data) == expected

@pytest.mark.parametrize("input_data, expected", test_data['second_score'])
def test_second_score(input_data, expected):
    assert run_script('second_score.py', input_data) == expected


@pytest.mark.parametrize("input_data, expected", test_data['nested_list'])
def test_nested_list(input_data, expected):
    assert run_script('nested_list.py', input_data).split('\n') == expected


@pytest.mark.parametrize("input_data, expected", test_data['lists'])
def test_lists(input_data, expected):
    assert run_script('lists.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['swap_case'])
def test_swap_case(input_data, expected):
    assert run_script('swap_case.py', input_data) == expected

@pytest.mark.parametrize("input_data, expected", test_data['split_and_join'])
def test_split_and_join(input_data, expected):
    assert run_script('split_and_join.py', input_data) == expected

def test_max_word():
    assert run_script('max_word.py') == 'сосредоточенности'

def test_price_sum():
    assert run_script('price_sum.py') == '6842.84 5891.06 6810.9'

@pytest.mark.parametrize("input_data, expected", test_data['anagram'])
def test_anagram(input_data, expected):
    assert run_script('anagram.py', input_data) == expected

@pytest.mark.parametrize("input_data, expected", test_data['metro'])
def test_metro(input_data, expected):
    assert run_script('metro.py', input_data) == expected

@pytest.mark.parametrize("input_data, expected", test_data['minion_game'])
def test_minion_game(input_data, expected):
    assert run_script('minion_game.py', input_data) == expected


@pytest.mark.parametrize("input_data, expected", test_data['is_leap'])
def test_is_leap(input_data, expected):
    assert run_script('is_leap.py', input_data) == expected

@pytest.mark.parametrize("input_data, expected", test_data['happiness'])
def test_happiness(input_data, expected):
    assert run_script('happiness.py', input_data) == expected

@pytest.mark.parametrize("input_data, expected", test_data['pirate_ship'])
def test_pirate_ship(input_data, expected):
    assert run_script('pirate_ship.py', input_data) == expected

@pytest.mark.parametrize("input_data, expected", test_data['matrix_mult'])
def test_matrix_mult(input_data, expected):
    assert run_script('matrix_mult.py', input_data) == expected