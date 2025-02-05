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

# Função para gerar a mensagem com base no produto comprado
def gerar_mensagem(produto):
    if produto == "D-macro_1 mês":
        return """
        Olá!

        Obrigado por adquirir o D-Macro (1 mês). Aqui está o link para baixar o seu macro:
         https://www.mediafire.com/file/leq8z5tibprvs5e/dmacroV3_0502.rar/file

        Tutorial de instalação:
        https://www.youtube.com/watch?v=Am37V2oQR8w

        Caso o Chrome esteja bloqueando o download:
        https://www.youtube.com/watch?v=bZc-u40TlLs&pp=ygUaY2hyb21lIGJsb3F1ZWFuZG8gZG93bmxvYWQ%3D

        Qualquer dúvida, entre em contato conosco!
        """
    elif produto == "D-macro_3_meses":
        return """
        Olá!

        Obrigado por adquirir o D-Macro (3 meses). Aqui está o link para baixar o seu macro:
        https://www.mediafire.com/file/example/D-MACRO_3_meses.rar/file

        Tutorial de instalação:
        https://www.youtube.com/watch?v=Am37V2oQR8w

        Caso o Chrome esteja bloqueando o download:
        https://www.youtube.com/watch?v=bZc-u40TlLs&pp=ygUaY2hyb21lIGJsb3F1ZWFuZG8gZG93bmxvYWQ%3D

        Caso o antivirus esteja bloqueado o macro
        https://www.youtube.com/watch?v=T3uYbgkJGeM

        Qualquer dúvida, entre em contato conosco!
        """
    elif produto == "D-macro_vitalicio":
        return """
        Olá!

        Em alguns minutos o email com os links estarão chegando!

        Qualquer dúvida, entre em contato conosco!
        """
    elif produto == "d-trigger_1mes":
        return """
        Olá!

        Obrigado por adquirir o D-Trigger (1 mês). Aqui está o link para baixar o seu trigger:
        https://www.mediafire.com/file/i7p6tuupl7ph8u0/D-triggerV2.rar/file

        Tutorial de instalação:
        https://www.youtube.com/watch?v=keyhQ393eKE

        Caso o Chrome esteja bloqueando o download:
        https://www.youtube.com/watch?v=bZc-u40TlLs&pp=ygUaY2hyb21lIGJsb3F1ZWFuZG8gZG93bmxvYWQ%3D

        Caso o antivirus esteja bloqueado o macro
        https://www.youtube.com/watch?v=T3uYbgkJGeM

        Qualquer dúvida, entre em contato conosco!
        """
        elif produto == "WALL":
        return """
        Olá!

        Obrigado por adquirir o WALL (1 mês). Aqui está o link para baixar o seu trigger:
        https://www.mediafire.com/file/nd21qjkrhzeorgt/wall_04-02.rar/file

        tutorial:
        https://www.youtube.com/watch?v=t8Wue0a29XE&t=1s

        O JOGO ATUALIZA TODA SEMANA, ENTAO SE O WALL PARAR, CHAMA NO WHATSAPP PRA PEGAR AS ATUALIZAÇÕES DO WALL.
        
        Caso o Chrome esteja bloqueando o download:
        https://www.youtube.com/watch?v=bZc-u40TlLs&pp=ygUaY2hyb21lIGJsb3F1ZWFuZG8gZG93bmxvYWQ%3D

        Caso o antivirus esteja bloqueado o macro
        https://www.youtube.com/watch?v=T3uYbgkJGeM

        Qualquer dúvida, entre em contato conosco!
        """
    elif produto == "D-trigger_vitalicio":
        return """
        Olá!

        Obrigado por adquirir o D-Trigger Vitalício. Aqui está o link para baixar o seu trigger:
        https://www.mediafire.com/file/56vwg382mxd2yi1/Dtrigger-V.2.rar/file

        Tutorial de instalação:
        https://www.youtube.com/watch?v=keyhQ393eKE

        Caso o Chrome esteja bloqueando o download:
        https://www.youtube.com/watch?v=bZc-u40TlLs&pp=ygUaY2hyb21lIGJsb3F1ZWFuZG8gZG93bmxvYWQ%3D

        Qualquer dúvida, entre em contato conosco!
        """
    else:
        return """
        Olá!

        Obrigado pela sua compra. Estamos processando o seu pedido e entraremos em contato em breve.

        Qualquer dúvida, entre em contato conosco!
        """

# Função para enviar o e-mail
def enviar_email(destinatario, produto):
    # Gerar mensagem com base no produto
    mensagem = gerar_mensagem(produto)

    # Configurar e enviar o e-mail
    msg = MIMEText(mensagem, "plain")
    msg["Subject"] = f"Detalhes do Produto: {produto}"
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
        produto = data["data"]["items"][0]["title"]  # Nome do produto comprado
        enviar_email(email, produto)  # Envia o e-mail personalizado

    return jsonify({"status": "success"}), 200

# Inicia o servidor Flask
if __name__ == "__main__":
    app.run(port=5000)
