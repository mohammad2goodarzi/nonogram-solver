import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from nonogrom_solver.nonogram import Nonogram


def choose_size():
    this_id = 'choose-diff-list'
    elem = browser.find_element(By.ID, this_id)
    elem.click()
    the_value = str(SIZE)
    option = elem.find_element(By.XPATH, f"//option[@value={the_value}]")
    option.click()
    new_game_id = 'new-game'
    new_game_button = browser.find_element(By.ID, new_game_id)
    new_game_button.click()


def find_descriptions(row_or_line, size):
    descriptions = []
    for number in range(size):
        this_id = f'container-desc-{row_or_line}-{number}'
        elem = browser.find_element(By.ID, this_id)
        desc = elem.text.split()
        desc = list(map(int, desc))
        descriptions.append(desc)
    return descriptions


def click_solved_table(table):
    for i in range(len(table)):
        for j in range(len(table[0])):
            if table[i][j] == '1':
                elem = browser.find_element(By.ID, f'grid-{i}-{j}')
                elem.click()


def play_game():
    desc_lines = find_descriptions('line', SIZE)
    desc_rows = find_descriptions('row', SIZE)

    table = Nonogram(SIZE, desc_lines, desc_rows)
    click_solved_table(table.table.table)
    alert = browser.switch_to.alert
    alert.accept()
    time.sleep(1)


def new_game():
    new_game_id = 'new-game'
    new_game_button = browser.find_element(By.ID, new_game_id)
    new_game_button.click()


browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get('https://picross.netlify.app/')

SIZE = 10
choose_size()

play_game()

new_game()
play_game()
