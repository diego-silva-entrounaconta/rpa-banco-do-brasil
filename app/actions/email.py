import dotenv
import os
import pandas as pd
import io
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
from configuration import data


# Load environment variables from .env file
dotenv.load_dotenv()


# Access environment variables
sender = os.getenv("SENDER")
password = os.getenv("PASSWORD_EMAIL_SENDER")
recipient = os.getenv("RECIPIENT")


def create_excel():
    aqrv = pd.DataFrame(data=data.dados, columns=data.COLS)

    excel_file = io.BytesIO()

    with pd.ExcelWriter(excel_file, engine="xlsxwriter") as writer:
        aqrv.to_excel(writer, sheet_name="teste generate excel", index=False)

        worksheet = writer.sheets["teste generate excel"]

        for idx, col in enumerate(aqrv.columns):
            series = aqrv[col]
            max_len = (
                max((series.astype(str).map(len).max(), len(str(series.name)))) + 1
            )

            worksheet.set_column(idx, idx, max_len)

    return excel_file


def send_email():
    excel_file = create_excel()

    # Criar mensagem de e-mail
    msg = MIMEMultipart()
    msg["From"] = sender  # Seu endereço de e-mail
    msg["To"] = recipient  # Endereço de e-mail do destinatário
    msg["Subject"] = "Relátorio Banco do Brasil"

    # Adicionar corpo ao e-mail (texto ou HTML)
    body = """\
    <html>
    <body>
        <p>Prezados,</p>
        <p>Segue anexo o arquivo Excel com relatório do banco do Brasil.</p>
    </body>
    </html>
    """
    msg.attach(MIMEText(body, "html"))

    # Anexar o arquivo Excel ao e-mail
    part = MIMEBase("application", "octet-stream")
    part.set_payload(excel_file.getvalue())
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition", 'attachment; filename="generate_xls_teste.xlsx"'
    )
    msg.attach(part)

    # Configurações do servidor SMTP e autenticação
    smtp_server = "smtp.office365.com"  # Altere para o servidor SMTP correto
    port = 587  # Porta do servidor SMTP
    senha = password  # Sua senha de e-mail

    # Conectar e enviar e-mail
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
