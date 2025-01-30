from sqlalchemy import text
from fastapi import APIRouter,status,Request
from fastapi.responses import JSONResponse
from app.db.base_db import SessionLocal
from app.pydantic.transactions import AddTransactionRequest,UpdateTransactionRequest,DeleteTransactionRequest
from app.utils.helper import serialize_txn_data
from dotenv import load_dotenv
load_dotenv()

router = APIRouter()

@router.post('/add-transaction')
async def add_transaction(
    request:Request,
    request_params:AddTransactionRequest
):
    """
        API for adding account in master
    """
    transaction_date=request_params.transaction_date
    from_account=request_params.from_account
    to_account=request_params.to_account
    transaction_amount=request_params.transaction_amount
    remarks=request_params.remarks
    try:
        if from_account == to_account:
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={
                    "ok": False,
                    "detail": str("From Account and To Account can not be the same"),
                },
        )
        with SessionLocal() as db_conn:
            sql = text(f"""
                INSERT INTO 
                transactions ( transaction_date, from_account, to_account, transaction_amount, remarks ) 
                VALUES ( :transaction_date, :from_account, :to_account, :transaction_amount, :remarks );
            """)
            db_conn.execute(sql,{'transaction_date':transaction_date,'from_account':from_account,'to_account':to_account,'transaction_amount':transaction_amount,'remarks':remarks})
            db_conn.commit()
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={
                "ok": True,
                "detail": "account added successfully",
            },
    )
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "ok": False,
                "detail": str(e),
            },
        )
    
@router.get('/get-transactions')
async def get_transactions():
    """
        API for getting all transactions
    """
    try:
        with SessionLocal() as db_conn:
            sql = text(f"""
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
            """)
            result = db_conn.execute(sql)
            data=result.fetchall()
            data=serialize_txn_data(data)
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content=data
            )
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "ok": False,
                "detail": str(e),
            },
        )

@router.put('/update-transaction')
async def update_transaction(
    request:Request,
    request_params:UpdateTransactionRequest
):
    """
        API for updating an existing account
    """
    try:
        id=request_params.id
        transaction_date=request_params.transaction_date
        from_account=request_params.from_account
        to_account=request_params.to_account
        transaction_amount=request_params.transaction_amount
        remarks=request_params.remarks

        with SessionLocal() as db_conn:
            sql = text(f"""
                UPDATE transactions 
                SET transaction_date=:transaction_date, from_account=:from_account, to_account=:to_account, transaction_amount=:transaction_amount, remarks=:remarks, updated_at=CURRENT_TIMESTAMP
                WHERE id=:id"""
            )
            db_conn.execute(sql,{'transaction_date':transaction_date,'from_account':from_account,'to_account':to_account, 'transaction_amount':transaction_amount, 'remarks':remarks, 'id':id})
            db_conn.commit()
                       
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "ok": False,
                "detail": str(e),
            },
        )
    
@router.delete('/delete-transaction')
async def delete_transaction(
    request:Request,
    request_params:DeleteTransactionRequest
):
    """
        API for deleting an existing transaction
    """
    try:
        id=request_params.id
        with SessionLocal() as db_conn:
            sql = text(f"""DELETE FROM transactions 
                WHERE id=:id"""
            )
            db_conn.execute(sql,{'id':id})
            db_conn.commit()
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "ok": False,
                "detail": str(e),
            },
        )