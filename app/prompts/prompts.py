from langchain_core.prompts import PromptTemplate

natural_language_answer_prompt="""Based on the data retrieved from our accounts and transactions database, I will provide you with a summary of the information.

Here's the columns of the accounts and transaction table for referrence.
accounts: id,account_name,account_number(optional),balance(currency INR),created_at,updated_at
transactions: id,transaction_date,from_account(foreign key ref from accounts table),to_account((foreign key ref from accounts table)),transaction_amount(currency INR),remarks(optional),created_at,updated_at

Always return account name for from_account and to_account.
Here is the mapping to consider for account id to account name.
1:Yatharth SBI
2:Chitrak
3:Sweety
4:Monil

The user asked: '{user_question}'

Here are the results by executing appropriate database query => query_results: {query_results}

Please generate a concise and informative response that includes:
- Consice answer of the user's question based on the query_results
- Always Use new lines to break the results for better readability in final response.
- Avoid redundency in headings or keys if possible and use bold letters for the keys.
- A friendly tone that is easy to understand.

### Output Format:  
Always return a JSON response as follows and nothing else:
{{
    "ai_answer": "Clear and concise answer generated for the user's question based on data provided",
}}
"""
NATURAL_LANGUAGE_ANSWER_PROMPT=PromptTemplate(
    template=natural_language_answer_prompt,
    input_variables=["user_question", "query_results"],
    partial_variables={"format_instructions": """Return your answer in the given json format only. No need to return any other leading or trailing lines.
                        Here's the example json format.
                       {{
                          "ai_answer": "Clear and concise answer generated for the user's question based on data provided",
                         }}
                       """}
)