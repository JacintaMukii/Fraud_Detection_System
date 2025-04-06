from fastapi import FastAPI, Request
from pydantic import BaseModel
import openai
import os
import json
from datetime import datetime

app = FastAPI()

# Load credentials from environment variables
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-4o-kenya-hack")

# Initialize OpenAI client
client = openai.AzureOpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    api_version="2024-02-01",
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    azure_deployment=AZURE_OPENAI_DEPLOYMENT
)

# Pydantic model for request validation
class Transaction(BaseModel):
    TransactionDate: str
    PreviousTransactionDate: str
    Amount: float
    AccountBalance: float
    CustomerAge: int
    CustomerOccupation: str
    Channel: str
    Location: str
    DeviceID: str
    IP_Address: str
    LoginAttempts: int
    TransactionDuration: int
    MerchantID: str

def format_transaction(transaction: dict) -> dict:
    """Ensure datetime strings are in ISO 8601 format."""
    for key in ["TransactionDate", "PreviousTransactionDate"]:
        if key in transaction:
            try:
                transaction[key] = datetime.fromisoformat(transaction[key]).isoformat()
            except:
                pass  # Leave as-is if parsing fails
    return transaction

@app.post("/analyze")
async def analyze_fraud(transaction: Transaction):
    formatted = format_transaction(transaction.dict())
    
    prompt = (
        "Check kama hii transaction iko sawa. Toa analysis fupi na precise kwa lugha ya mtaa. "
        "Jibu na hizi sections: Risk Level, Reason, Advice. Hii ndio transaction: "
        + json.dumps(formatted)
    )
    
    try:
        response = client.chat.completions.create(
            model=AZURE_OPENAI_DEPLOYMENT,
            messages=[
                {
                    "role": "system",
                    "content": "Wewe ni mtaalam wa kugundua udanganyifu kwenye miamala ya kifedha. Toa majibu kwa Kiswahili/Sheng."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        result = response.choices[0].message.content
        return {"analysis": result}

    except Exception as e:
        return {"error": str(e)}

