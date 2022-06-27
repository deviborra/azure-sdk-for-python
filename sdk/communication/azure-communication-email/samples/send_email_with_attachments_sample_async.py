# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
FILE: send_email_with_attachments_sample_async.py
DESCRIPTION:
    This sample demonstrates sending an email with an attachment. The Email client is 
    authenticated using a connection string.
USAGE:
    python send_email_with_attachment_async.py
    Set the environment variable with your own value before running the sample:
    1) COMMUNICATION_CONNECTION_STRING - the connection string in your ACS resource
    2) SENDER_ADDRESS - the address found in the linked domain that will send the email
    3) RECIPIENT_ADDRESS - the address that will receive the email
"""

import os
import sys
import asyncio
from azure.communication.email.aio import EmailClient
from azure.communication.email import (
    EmailContent,
    EmailRecipients,
    EmailAddress,
    EmailAttachment,
    EmailMessage
)

sys.path.append("..")

class EmailWithAttachmentSampleAsync(object):

    connection_string = os.getenv("COMMUNICATION_CONNECTION_STRING")
    sender_address = os.getenv("SENDER_ADDRESS")
    recipient_address = os.getenv("RECIPIENT_ADDRESS")
    
    async def send_email_with_attachment_async(self):
        # creating the email client
        email_client = EmailClient.from_connection_string(self.connection_string)

        # creating the email message
        content = EmailContent(
            subject="This is the subject",
            plain_text="This is the body",
            html= "<html><h1>This is the body</h1></html>",
        )

        recipients = EmailRecipients(
            to=[EmailAddress(email=self.recipient_address, display_name="Customer Name")]
        )

        attachment = EmailAttachment(
            name="readme.txt",
            attachment_type="txt",
            content_bytes_base64="ZW1haWwgdGVzdCBhdHRhY2htZW50" #cspell:disable-line
        )

        message = EmailMessage(
            sender=self.sender_address,
            content=content,
            recipients=recipients,
            attachments=[attachment]
        )

        async with email_client:
            try:
                # sending the email message
                response = await email_client.send(message)
                print("Message ID: " + response.message_id)
            except Exception:
                print(Exception)
                pass

if __name__ == '__main__':
    sample = EmailWithAttachmentSampleAsync()

    # Comment in this line if you are running this sample on Windows
    # asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    
    asyncio.run(sample.send_email_with_attachment_async())
