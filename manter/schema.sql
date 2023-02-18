DROP TABLE IF EXISTS cliente;
CREATE TABLE cliente(
    id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    nome text NOT NULL,
    cpf text NOT NULL,
    email text NOT NULL,
    data_cadastro TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO cliente(nome, cpf, email)
VALUES ('adm', '455.123.456-78', 'admin@test.org'),
    (
        "Maria Yean",
        "455.123.456-78",
        "mariam@gmail.com"
    ),
    (
        "Julio Ribeiro",
        "455.123.456-78",
        "julio@test.org"
    ),
    (
        "Iara Alves",
        "455.123.456-78",
        "iara@test.org"
    );