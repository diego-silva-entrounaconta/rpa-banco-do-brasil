import dotenv
import os
import pandas as pd
import io
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
from app.configuration import data
from datetime import date


# Load environment variables from .env file
dotenv.load_dotenv()


# Access environment variables
sender = os.getenv("SENDER")
password = os.getenv("PASSWORD_EMAIL_SENDER")
recipient = os.getenv("RECIPIENT")


def create_excel():
    # Function responsible for creating excel

    # Fill lines with none if they are not complete
    for row in data.dados:
        if len(row) != len(data.COLS):
            row += [None] * (len(data.COLS) - len(row))

    # create excel
    aqrv = pd.DataFrame(data=data.dados, columns=data.COLS)
    excel_file = io.BytesIO()

    with pd.ExcelWriter(excel_file, engine="xlsxwriter") as writer:
        aqrv.to_excel(writer, sheet_name="Relatório Banco do Brasil", index=False)

        worksheet = writer.sheets["Relatório Banco do Brasil"]

        for idx, col in enumerate(aqrv.columns):
            series = aqrv[col]
            max_len = (
                max((series.astype(str).map(len).max(), len(str(series.name)))) + 1
            )

            worksheet.set_column(idx, idx, max_len)

    return excel_file


def send_email():
    # Function responsible for sending the email

    # Calling the function that creates excel
    excel_file = create_excel()

    # Create email message
    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = recipient
    msg["Subject"] = "Relátorio Banco do Brasil"

    # Add body to email (text or HTML)
    body = """\
    <html>
    <body>
        <p>Prezados,</p>
        <p>Segue anexo o arquivo Excel com relatório do banco do Brasil.</p>
    </body>
    </html>
    """
    msg.attach(MIMEText(body, "html"))

    # Attach the Excel file to the email
    part = MIMEBase("application", "octet-stream")
    part.set_payload(excel_file.getvalue())
    encoders.encode_base64(part)
    today_base = date.today()
    today = today_base.strftime("%d/%m/%Y")
    part.add_header(
        "Content-Disposition",
        f'attachment; filename="relatorio_banco_do_brasil_{today}.xlsx"',
    )
    msg.attach(part)

    # SMTP server settings and authentication
    smtp_server = "smtp.office365.com"  # Altere para o servidor SMTP correto
    port = 587  # Porta do servidor SMTP
    senha = password  # Sua senha de e-mail

    # Connect and send email
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(msg["From"], senha)
        server.sendmail(msg["From"], msg["To"], msg.as_string().encode("utf-8"))
        print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {str(e)}")
    finally:
        server.quit()
