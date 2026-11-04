-- ============================================================================
-- PROJETO: Sistema de Gerenciamento de Rotina de Skincare
-- ARQUIVO: DDL - Criação da Estrutura do Banco de Dados (.sql)
-- ============================================================================

-- ----------------------------------------------------------------------------
-- 1. ESTRUTURA BASE DO BANCO DE DADOS
-- ----------------------------------------------------------------------------
DROP DATABASE IF EXISTS skincare_db;
CREATE DATABASE skincare_db
  DEFAULT CHARACTER SET utf8mb4
  DEFAULT COLLATE utf8mb4_unicode_ci;

USE skincare_db;

-- ----------------------------------------------------------------------------
-- 2. CRIAÇÃO DAS TABELAS E RESTRIÇÕES (DDL)
-- ----------------------------------------------------------------------------

-- Tabela: Usuários
CREATE TABLE usuarios (
    id_usuario INT AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(120) NOT NULL,
    senha_hash VARCHAR(255) NOT NULL,
    tipo_pele ENUM('SECA', 'OLEOSA', 'MISTA', 'NORMAL', 'SENSIVEL') NULL,
    data_cadastro DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT pk_usuarios PRIMARY KEY (id_usuario),
    CONSTRAINT uk_usuarios_email UNIQUE (email)
);

-- Tabela: Marcas de Produtos
CREATE TABLE marcas (
    id_marca INT AUTO_INCREMENT,
    nome VARCHAR(80) NOT NULL,
    pais_origem VARCHAR(50) NULL,
    CONSTRAINT pk_marcas PRIMARY KEY (id_marca),
    CONSTRAINT uk_marcas_nome UNIQUE (nome)
);

-- Tabela: Categorias de Produtos
CREATE TABLE categorias (
    id_categoria INT AUTO_INCREMENT,
    nome VARCHAR(60) NOT NULL,
    descricao VARCHAR(255) NULL,
    CONSTRAINT pk_categorias PRIMARY KEY (id_categoria),
    CONSTRAINT uk_categorias_nome UNIQUE (nome)
);

-- Tabela: Ingredientes Ativos
CREATE TABLE ingredientes (
    id_ingrediente INT AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT NULL,
    CONSTRAINT pk_ingredientes PRIMARY KEY (id_ingrediente),
    CONSTRAINT uk_ingredientes_nome UNIQUE (nome)
);

-- Tabela: Produtos
CREATE TABLE produtos (
    id_produto INT AUTO_INCREMENT,
    id_marca INT NOT NULL,
    id_categoria INT NOT NULL,
    nome VARCHAR(120) NOT NULL,
    volume_ml DECIMAL(6,2) NULL,
    preco_estimado DECIMAL(8,2) NULL,
    CONSTRAINT pk_produtos PRIMARY KEY (id_produto),
    CONSTRAINT fk_produtos_marcas FOREIGN KEY (id_marca)
        REFERENCES marcas (id_marca)
        ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT fk_produtos_categorias FOREIGN KEY (id_categoria)
        REFERENCES categorias (id_categoria)
        ON DELETE RESTRICT ON UPDATE CASCADE
);

-- Tabela Associativa: Produto <-> Ingredientes (N:M)
CREATE TABLE produto_ingredientes (
    id_produto INT NOT NULL,
    id_ingrediente INT NOT NULL,
    concentracao_percentual DECIMAL(5,2) NULL, -- Ajustado para permitir até 100.00%
    CONSTRAINT pk_produto_ingredientes PRIMARY KEY (id_produto, id_ingrediente),
    CONSTRAINT fk_pi_produtos FOREIGN KEY (id_produto)
        REFERENCES produtos (id_produto)
        ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT fk_pi_ingredientes FOREIGN KEY (id_ingrediente)
        REFERENCES ingredientes (id_ingrediente)
        ON DELETE RESTRICT ON UPDATE CASCADE
);

-- Tabela: Rotinas (ex: "Rotina Matinal", "Rotina Noturna")
CREATE TABLE rotinas (
    id_rotina INT AUTO_INCREMENT,
    id_usuario INT NOT NULL,
    nome VARCHAR(60) NOT NULL,
    periodo ENUM('MANHA', 'TARDE', 'NOITE') NOT NULL,
    ativa BOOLEAN NOT NULL DEFAULT TRUE,
    CONSTRAINT pk_rotinas PRIMARY KEY (id_rotina),
    CONSTRAINT fk_rotinas_usuarios FOREIGN KEY (id_usuario)
        REFERENCES usuarios (id_usuario)
        ON DELETE CASCADE ON UPDATE CASCADE
);

-- Tabela Associativa: Itens/Etapas da Rotina (Rotina <-> Produtos N:M com ordem)
CREATE TABLE rotina_produtos (
    id_rotina INT NOT NULL,
    id_produto INT NOT NULL,
    ordem_passo INT NOT NULL,
    observacao_uso VARCHAR(150) NULL,
    CONSTRAINT pk_rotina_produtos PRIMARY KEY (id_rotina, id_produto),
    CONSTRAINT fk_rp_rotinas FOREIGN KEY (id_rotina)
        REFERENCES rotinas (id_rotina)
        ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT fk_rp_produtos FOREIGN KEY (id_produto)
        REFERENCES produtos (id_produto)
        ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT uk_rotina_ordem UNIQUE (id_rotina, ordem_passo)
);

-- Tabela: Registro Diário de Uso (Log de execução da rotina)
CREATE TABLE diario_execucao (
    id_execucao INT AUTO_INCREMENT,
    id_rotina INT NOT NULL,
    data_hora_execucao DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    observacoes_pele VARCHAR(255) NULL,
    sensibilidade_notada BOOLEAN NOT NULL DEFAULT FALSE,
    CONSTRAINT pk_diario_execucao PRIMARY KEY (id_execucao),
    CONSTRAINT fk_diario_rotinas FOREIGN KEY (id_rotina)
        REFERENCES rotinas (id_rotina)
        ON DELETE CASCADE ON UPDATE CASCADE
);

-- ----------------------------------------------------------------------------
-- 3. VERIFICAÇÃO PARA A DEMONSTRAÇÃO
-- ----------------------------------------------------------------------------
SHOW TABLES;
