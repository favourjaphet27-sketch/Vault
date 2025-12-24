# Automated Bookkeeping Rules Engine (Backend API)

## Overview

This project is a backend automation engine designed to simplify bookkeeping workflows. It automatically categorizes financial transactions using user-defined rules, ensuring consistency, traceability, and reduced manual effort.

The system is API-first, built with Django and Django REST Framework, and is suitable for powering dashboards, mobile apps, or external accounting tools.

## Key Features

- Custom user authentication with JWT
- Transaction and account management
- Rule-based transaction classification
- Priority-based rule evaluation
- Automatic rule execution via signals
- Audit logging for all critical actions
- Secure, user-isolated data access

## System Architecture

- **Users**: create financial data and automation rules
- **Transactions**: store user transactions
- **Rules Engine**: evaluates transactions and assigns categories
- **Audit Logs**: track changes and system actions
- **Signals**: connect transaction creation to rule execution

## Core Apps

- `users`: authentication and user management
- `finance`: accounts, transactions, and categories
- `rules`: automation rules and rule engine logic
- `audit_logs`: system audit trail

## Rule Engine Logic

Rules are evaluated automatically when a transaction is created. Each rule contains conditions stored in a JSON structure and is applied based on priority.

Once a matching rule is found:

- The transaction is categorized
- Rule execution is recorded
- Audit logs are generated

Example rule conditions:

```json
{
  "description_contains": ["uber", "bolt"],
  "min_amount": 500
}

Authentication

Authentication is handled using JWT:

POST /api/auth/register/ → create user

POST /api/auth/login/ → obtain access and refresh tokens

POST /api/auth/token/refresh/ → refresh token

Finance

GET /api/finance/transactions/

POST /api/finance/transactions/

GET /api/finance/categories/

POST /api/finance/categories/

Rules

GET /api/rules/rules/

POST /api/rules/rules/

PATCH /api/rules/rules/{id}/

DELETE /api/rules/rules/{id}/

Audit Logs

GET /api/audit/logs/

Tech Stack

Python

Django

Django REST Framework

SimpleJWT

PostgreSQL / SQLite (development)

Deployment

The API is deployed on PythonAnywhere / Heroku and is publicly accessible for review.
```
