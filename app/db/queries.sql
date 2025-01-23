CREATE TABLE accounts (
    id BIGSERIAL PRIMARY KEY,
    account_name VARCHAR(255) NOT NULL UNIQUE,
    account_number VARCHAR(50) UNIQUE,
    balance DECIMAL(10, 2) DEFAULT 0.00,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE transactions(
	id BIGSERIAL PRIMARY KEY,
	transaction_date TIMESTAMP NOT NULL,
	from_account BIGINT REFERENCES accounts(id) ON DELETE RESTRICT,
	to_account BIGINT REFERENCES accounts(id) ON DELETE RESTRICT,
	transaction_amount DECIMAL(10,2) NOT NULL CHECK (transaction_amount>0),
	remarks VARCHAR(255),
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)

-- Get all transactions
SELECT 
    t.id AS transaction_id,
    t.transaction_date,
    fa.account_name AS from_account_name,
    ta.account_name AS to_account_name,
    t.transaction_amount,
    t.remarks    
FROM 
    transactions t
JOIN 
    accounts fa ON t.from_account = fa.id
JOIN 
    accounts ta ON t.to_account = ta.id
ORDER BY 
    t.id ASC;
