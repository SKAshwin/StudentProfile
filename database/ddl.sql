CREATE TABLE Module(
    code VARCHAR(7) NOT NULL,
    credits INT NOT NULL,
    PRIMARY KEY(code)
);

CREATE TABLE Student(
    id VARCHAR(8) NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE ModuleReport(
    score DECIMAL(11,9) NOT NULL,
    semester INT NOT NULL,
    code VARCHAR(7) NOT NULL,
    id VARCHAR(8) NOT NULL,
    PRIMARY KEY(code, id),
    FOREIGN KEY(code) REFERENCES Module(code),
    FOREIGN KEY(id) REFERENCES Student(id)
);


