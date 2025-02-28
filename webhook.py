from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText

# Configuração do Flask
app = Flask(__name__)

# Configuração de e-mail
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_USER = "antifarmador2021@gmail.com"  # Seu e-mail
EMAIL_PASS = "ducc lqrq iwuu yqzr"  # Substitua pela sua senha ou App Password

# Função para gerar a mensagem com base no produto comprado
def gerar_mensagem(produto):
    if produto == "D-macro_1 mês":
        return """
        Olá!

        Obrigado por adquirir o D-Macro (1 mês). Aqui está o link para baixar o seu macro:
        https://mega.nz/file/YEpxlTTb#QwQlBxjtFrcXA9_eGHulP3pua0NEKMDtbN9dg-O03rw

        Tutorial de instalação:
        https://www.youtube.com/watch?v=Am37V2oQR8w

        Caso o Chrome esteja bloqueando o download:
        https://www.youtube.com/watch?v=bZc-u40TlLs

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
        https://www.youtube.com/watch?v=bZc-u40TlLs

        Caso o antivirus esteja bloqueando o macro:
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
        https://www.mediafire.com/file/k9p05a7ord7lhr0/D-triggerV2.rar/file

        Tutorial de instalação:
        https://www.youtube.com/watch?v=keyhQ393eKE

        Caso o Chrome esteja bloqueando o download:
        https://www.youtube.com/watch?v=bZc-u40TlLs

        Caso o antivirus esteja bloqueando o macro:
        https://www.youtube.com/watch?v=T3uYbgkJGeM

        Qualquer dúvida, entre em contato conosco!
        """
    elif produto == "WALL":  # Aqui estava com erro de indentação
        return """
        Olá!

        Obrigado por adquirir o WALL (1 mês). Aqui está o link para baixar o seu trigger:
        https://www.mediafire.com/file/3a1jbwhcwlalvtv/wall_14-02.rar/file

        Tutorial:
        https://www.youtube.com/watch?v=bw1JIuvgnD8
        
        O JOGO ATUALIZA TODA SEMANA, ENTÃO SE O WALL PARAR, CHAME NO WHATSAPP PARA PEGAR AS ATUALIZAÇÕES DO WALL.

        Caso o Chrome esteja bloqueando o download:
        https://www.youtube.com/watch?v=bZc-u40TlLs

        Caso o antivirus esteja bloqueando o macro:
        https://www.youtube.com/watch?v=T3uYbgkJGeM

        Qualquer dúvida, entre em contato conosco!
        """
    elif produto == "D-trigger_vitalicio":
        return """
        Olá!

        Obrigado por adquirir o D-Trigger Vitalício. Aqui está o link para baixar o seu trigger:
        https://www.mediafire.com/file/k9p05a7ord7lhr0/D-triggerV2.rar/file

        Tutorial de instalação:
        https://www.youtube.com/watch?v=keyhQ393eKE

        Caso o Chrome esteja bloqueando o download:
        https://www.youtube.com/watch?v=bZc-u40TlLs

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
