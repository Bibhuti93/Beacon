from browser_use.llm import ChatGoogle
from browser_use import BrowserSession, Agent
from dotenv import load_dotenv
from openai import OpenAI
import os
import subprocess
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import Flow
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
load_dotenv()

import asyncio

llmModel = os.getenv("LLM_MODEL")
browserLLMModel = os.getenv("BROWSER_LLM_MODEL")
authJSON = os.getenv("GOOGLE_DOCS_AUTH_JSON")

def googleDocs(docType,docTitle,docContent):
    
    # Set up the OAuth 2.0 flow
    flow = InstalledAppFlow.from_client_secrets_file(
    authJSON,
    scopes=['https://www.googleapis.com/auth/documents']
    )
    
    # Run the flow and get credentials
    credentials = flow.run_local_server(port=0)
    
    # Initialize the Docs service
    service = build('docs', 'v1', credentials=credentials)

    # Create a new document
    document = service.documents().create(body={'title': docTitle}).execute()
    document_id = document.get('documentId')
    print(f"Created document with title: {document.get('title')}")
    
    # Open an existing document
    document = service.documents().get(documentId=document_id).execute()
    
    # Define the requests for inserting text
    requests = [
        {
            'insertText': {
                'location': {
                    'index': 1,
                },
                'text': docContent
            }
        }
    ]
    
    # Execute the batch update
    result = service.documents().batchUpdate(
    documentId=document_id, body={'requests': requests}).execute()
    
    # Read document content
    content = document.get('body').get('content')
    print("Document content:", content)

def get_main_chrome_pid():
    # Run tasklist command filtered for chrome.exe
    result = subprocess.run(['tasklist', '/FI', 'IMAGENAME eq chrome.exe'], capture_output=True, text=True)

    lines = result.stdout.splitlines()

    for line in lines:
        if 'chrome.exe' in line:
            parts = line.split()
            if len(parts) >= 2:
                return parts[1]  # Return the first PID found (main process)

    return None

def useBrowser(query):
    
    chrome_pid = get_main_chrome_pid()

    if chrome_pid:
        print("Main Google Chrome Process PID:", chrome_pid)
        browser_session = BrowserSession(
        headless=False,
        browser_pid=chrome_pid,
        keep_alive=True)
    else:
        print("Google Chrome is not running. So defaulting to browser-use Chromium.")
        browser_session = BrowserSession(
        headless=True)
        
    llm = ChatGoogle(model=browserLLMModel)

    async def main():
        agent = Agent(
            task=query,
            llm=llm,
            browser_session=browser_session
        )
        result = await agent.run()
        return result.final_result()
        
    final_result = asyncio.run(main())
    return final_result
        
def useLLM(query):
    client = OpenAI(
    api_key = os.getenv("GOOGLE_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )
    
    # Make a chat completion request
    response = client.chat.completions.create(
        model=llmModel,
        messages=[
            {"role": "system", "content": "Generate replies in one line only. Be specific as possible. Should you need to present multiple lines then do it as bulletted points. Ask for user input when needed as numbered points."},
            {"role": "user", "content": query}
        ]
    )
    
    # Print the response
    return response.choices[0].message.content
    