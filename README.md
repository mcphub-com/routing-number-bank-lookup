# Routing Number Bank Lookup MCP Server

## Overview

The Routing Number Bank Lookup MCP Server is a powerful tool designed to provide detailed information about banks, based on routing numbers. This service is essential for users who need to verify bank details for either Automated Clearing House (ACH) or wire transfer transactions. The server supports responses in both XML and JSON formats, making it versatile for different integration needs.

## Features

- **Bank Information Lookup**: Retrieve comprehensive information about a bank using its routing number. This feature is crucial for ensuring transaction integrity and confirming bank details.
- **Format Flexibility**: Choose between JSON and XML response formats. By default, the server returns data in JSON, but users can specify XML if needed.
- **Transaction Type Specification**: Determine the type of bank information required by specifying the transaction type – ACH, wire, or both. The default is set to ACH, reflecting the common usage scenario, but users can easily switch to wire or request both types of information.

## Usage Details

### Tools and Functions

- **Get Bank Info**: This is the primary function of the server. It allows users to input a routing number and retrieve the corresponding bank information.
  - **Parameters**:
    - **format**: (Optional) Specifies the response format. Accepted values are `json` and `xml`. If omitted, the response defaults to JSON.
    - **paymentType**: (Optional) Defines the type of information to retrieve. Accepted values are `ach`, `wire`, and `all`. If omitted, the server defaults to ACH.

### Tool Declaration

- **get_bank_info**: 
  - **Description**: This function fetches bank details based on the provided routing number and specified parameters.
  - **Parameters**:
    - **format**: Choose between `json` and `xml` for the response format. The default is `json`.
    - **paymentType**: Specify `ach` for ACH information, `wire` for wire transfer details, or `all` to receive both sets of information. The default is `ach`.

## Conclusion

The Routing Number Bank Lookup MCP Server is an invaluable resource for anyone needing to verify bank details quickly and accurately. Its flexibility in response formats and transaction types ensures it can meet a variety of needs, making it a reliable tool for financial and business operations.