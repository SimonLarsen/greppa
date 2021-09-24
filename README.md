greppa
======

A CLI tool for grepping rows in binary tabular files through Pandas. 

## Usage

```bash
greppa "group == 'x' & y > 3" data.parquet result.parquet
```

Contents of `data.parquet`:

       x  y group
    0  1  7     x
    1  2  3     x
    2  3  4     x
    3  1  6     y
    4  2  8     y
    5  3  4     y

Contents of `result.parquet`:

       x  y group
    0  1  7     x
    2  3  4     x