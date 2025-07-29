import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/mikescogan-xbWFolmaQx/api/routing-number-bank-lookup'

mcp = FastMCP('routing-number-bank-lookup')

@mcp.tool()
def get_bank_info(format: Annotated[Union[str, None], Field(description="Accepted values: json, xml Default value: json Description: if you don't put this, it will default to json. if you need an XML response, add the query param into the url like this https://routing-number-bank-lookup.p.rapidapi.com/api/v1/121000248?format=xml")] = None,
                  paymentType: Annotated[Union[str, None], Field(description="Accepted values: ach, wire, all Default value: ach Description: if you don't put this, it will default to ACH. Bank information is a little different depending on whether you're trying to use the ACH system or the Wire Transfer system. You define what you want here. For example, if you need the Wire Transfer information, you'd add the query param into the url like this https://routing-number-bank-lookup.p.rapidapi.com/api/v1/121000248?paymentType=wire. Generally ACH info is the most common, so if you don't know what any of this stuff means just leave this blank and let it default to ACH. You may also get both ACH and Wire information at the same time by passing paymentType=all")] = None) -> dict: 
    '''See https://rapidapi.com/mikescogan-xbWFolmaQx/api/routing-number-bank-lookup/tutorials/how-to-use-and-examples for full instructions'''
    url = 'https://routing-number-bank-lookup.p.rapidapi.com/api/v1/121000248'
    headers = {'x-rapidapi-host': 'routing-number-bank-lookup.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'format': format,
        'paymentType': paymentType,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
