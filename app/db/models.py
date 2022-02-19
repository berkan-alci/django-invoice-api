from .db import Base
from sqlalchemy.sql.expression import null, text
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy import Column, Integer, String, Boolean, Float


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    phone = Column(Integer, nullable=False)
    address = Column(String, nullable=False)
    postal_code = Column(Integer, nullable=False)
    city = Column(String, nullable=False)
    country = Column(String, nullable=False)
    is_verified = Column(Boolean, server_default="False", nullable=False)
    is_super = Column(Boolean, server_default="False", nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        server_default=text('now()'), nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True), server_default=text(
        'now()'), onupdate=text('now()'), nullable=False)


class Company(Base):
    __tablename__ = "company"

    id = Column(Integer, primary_key=True, nullable=False)
    owner_id = Column(Integer, ForeignKey(
        "users.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    company_name = Column(String, nullable=False)
    company_email = Column(String, unique=True, nullable=False)
    company_phone = Column(Integer, unique=True, nullable=False)
    company_address = Column(String, nullable=False)
    company_postal_code = Column(Integer, nullable=False)
    company_city = Column(String, nullable=False)
    btw_number = Column(String, unique=True, nullable=False)
    bank = Column(String, unique=True, nullable=False)
    swift_bic = Column(String, unique=True, nullable=False)
    iban = Column(String, unique=True, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        server_default=text('now()'), nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True), server_default=text(
        'now()'), onupdate=text('now()'), nullable=False)


class Clients(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, nullable=False)
    company_id = Column(Integer, ForeignKey(
        "company.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    recipient_name = Column(String, nullable=False)
    recipient_email = Column(String, unique=True, nullable=False)
    recipient_phone = Column(Integer, unique=True, nullable=False)
    recipient_address = Column(String, nullable=False)
    recipient_postal_code = Column(Integer, nullable=False)
    recipient_city = Column(String, nullable=False)
    recipient_country = Column(String, nullable=False)
    is_company = Column(String, server_default="False", nullable=False)
    recipient_vat_id = Column(String, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True),
                        server_default=text('now()'), nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True), server_default=text(
        'now()'), onupdate=text('now()'), nullable=False)


class ExpenseIncome(Base):
    __tablename__ = "expense_income"

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey(
        "users.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    comapny_id = Column(Integer, ForeignKey(
        "company.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=True)
    type = Column(String, nullable=False)
    category = Column(String, nullable=False)
    description = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        server_default=text('now()'), nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True), server_default=text(
        'now()'), onupdate=text('now()'), nullable=False)


class Unit(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, nullable=False)
    company_id = Column(Integer, ForeignKey(
        "company.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    invoice_id = Column(Integer, ForeignKey(
        "invoices.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    product_name = Column(String, nullable=False)
    product_description = Column(String, nullable=False)
    product_unit = Column(String, nullable=False)
    product_price = Column(Float, nullable=False)
    product_vat = Column(Float, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        server_default=text('now()'), nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True), server_default=text(
        'now()'), onupdate=text('now()'), nullable=False)


class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True, nullable=False)
    company_id = Column(Integer, ForeignKey(
        "company.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    recipient_id = Column(Integer, ForeignKey(
        "recipients.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    unit_id = Column(Integer, ForeignKey(
        "products.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    invoice_description = Column(String, nullable=False)
    due_date = Column(TIMESTAMP, nullable=False)
    is_paid = Column(Boolean, server_default="False", nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        server_default=text('now()'), nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True), server_default=text(
        'now()'), onupdate=text('now()'), nullable=False)
