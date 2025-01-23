from pydantic import BaseModel,Field, constr
from decimal import Decimal

class AddAccountRequest(BaseModel):
    """Request schema for add-account endpoint"""
    account_name: constr(max_length=255) = Field(..., title="Account Name", description="Name of the account")
    account_number: constr(max_length=50) = Field(..., title="Account Number", description="Unique account number")
    balance: Decimal = Field(0.00, title="Balance", description="Current balance of the account")

class UpdateAccountRequest(BaseModel):
    """Request schema for update-account endpoint"""
    id:int
    account_name: constr(max_length=255) = Field(..., title="Account Name", description="Name of the account")
    account_number: constr(max_length=50) = Field(..., title="Account Number", description="Unique account number")
    balance: Decimal = Field(0.00, title="Balance", description="Current balance of the account")

class DeleteAccountRequest(BaseModel):
    """Request schema for delete-account endpoint"""
    id:int