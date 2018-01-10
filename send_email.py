import win32com.client


def send_email(email_address, email_body):
    o = win32com.client.Dispatch("Outlook.Application")
    Msg = o.CreateItem(0)
    Msg.To = email_address
    Msg.Subject = "The Result from Spider"
    Msg.Body = email_body
    Msg.Send()