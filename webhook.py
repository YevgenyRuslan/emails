from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText

# Configuração do Flask
app = Flask(__name__)

# Configuração de e-mail
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_USER = "antifarmador2021@gmail.com"  # Substitua pelo seu e-mail
EMAIL_PASS = "ducc lqrq iwuu yqzr"  # Substitua pela sua senha ou App Password

# Função para enviar o produto por e-mail
def enviar_email(destinatario):
    # Mensagem personalizada
    mensagem = """
    Olá!

    Obrigado pela sua compra. Aqui estão as informações para utilizar o seu produto:

    **Link para baixar o macro:**
    https://www.mediafire.com/file/gp2syv5rkjnzx07/D-Macro21.rar/file

    **Tutorial:**
    https://www.youtube.com/watch?v=DhTZsmUc9F8

    **Se o Chrome estiver bloqueando o download:**
    https://www.youtube.com/watch?v=bZc-u40TlLs&pp=ygUaY2hyb21lIGJsb3F1ZWFuZG8gZG93bmxvYWQ%3D

    Caso tenha dúvidas, entre em contato conosco. Aproveite!
    """
    msg = MIMEText(mensagem, "plain")
    msg["Subject"] = "Seu Produto Digital: Macro para CS2"
    msg["From"] = EMAIL_USER
    msg["To"] = destinatario

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASS)
            server.sendmail(EMAIL_USER, destinatario, msg.as_string())
        print(f"E-mail enviado com sucesso para {destinatario}")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")

# Endpoint para receber o Webhook
@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json  # Dados enviados pelo Webhook
    print(f"Dados recebidos: {data}")

    # Verifica se o status do pagamento é "paid"
    if data["data"]["status"] == "paid":
        email = data["data"]["customer"]["email"]  # E-mail do cliente
        enviar_email(email)  # Envia o e-mail com o produto

    return jsonify({"status": "success"}), 200

# Inicia o servidor Flask
if __name__ == "__main__":
    app.run(port=5000)
