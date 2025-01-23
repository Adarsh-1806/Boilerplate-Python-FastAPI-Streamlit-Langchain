from pydantic import BaseModel,Field, constr,condecimal
from decimal import Decimal
from datetime import datetime
from typing import Optional

class AddTransactionRequest(BaseModel):
    """Request schema for add-transaction endpoint"""
    transaction_date: datetime = Field(..., description="The date and time of the transaction")
    from_account: int = Field(..., description="The account ID from which the amount is being transferred")
    to_account: int = Field(..., description="The account ID to which the amount is being transferred")
    transaction_amount: condecimal(gt=0, decimal_places=2) = Field(..., description="The amount of money being transferred, must be greater than 0")
    remarks: Optional[str] = Field(None, max_length=255, description="Optional remarks about the transaction")

class UpdateTransactionRequest(BaseModel):
    """Request schema for update-transaction endpoint"""
    id:int
    transaction_date: datetime = Field(..., description="The date and time of the transaction")
    from_account: int = Field(..., description="The account ID from which the amount is being transferred")
    to_account: int = Field(..., description="The account ID to which the amount is being transferred")
    transaction_amount: condecimal(gt=0, decimal_places=2) = Field(..., description="The amount of money being transferred, must be greater than 0")
    remarks: Optional[str] = Field(None, max_length=255, description="Optional remarks about the transaction")

class DeleteTransactionRequest(BaseModel):
    """Request schema for delete-transaction endpoint"""
    id:int