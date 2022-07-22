# nonogram-solver
Solving the Nonogram (or maybe picross) puzzle using selenium

## Installation
Use this command to install the required libraries for this project.

```bash
pip install -r requirements.txt
```

## Usage
Run the following commands to run the main project.

```bash
cd nonogram_solver
python main.py
```

![](https://github.com/mohammad2goodarzi/nonogram-solver/blob/main/nonogram.gif)


You can run only the nonogram.py file using the following commands
```bash
cd nonogram_solver
python main.py
```

This is how nonogram.py works
```python
size = 5
rows_description = [
    [1, 2],
    [2, 2],
    [2, 1],
    [5],
    [1],
]
columns_description = [
    [5],
    [3],
    [1],
    [2, 1],
    [4],
]

nonogram = Nonogram(size=size, columns_description=columns_description, rows_description=rows_description)
print(nonogram.table)


# nonogram.table will be something like this
# 10011
# 11011
# 11001
# 11111
# 10000
```

## License
[MIT](https://choosealicense.com/licenses/mit/)