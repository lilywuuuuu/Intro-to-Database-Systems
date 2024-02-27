CREATE TABLE co_list (
    _code VARCHAR(10) not null,
    _start DATE,
    _group VARCHAR(50),
    primary key(_code)
);

CREATE TABLE code_name (
    _code VARCHAR(10) not null,
    _name VARCHAR(100),
    primary key(_code)
);

CREATE TABLE stock_prices (
_code VARCHAR(10) NOT NULL,
_date DATE,
_open FLOAT,
_high FLOAT,
_low FLOAT,
_close FLOAT,
_change FLOAT,
_change_percent FLOAT,
_volume FLOAT,
primary key(_code, _date)
);


