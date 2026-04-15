"""""
Título: Simulador de monitoramento de logs
Criar um script em Python que lê arquivos de log (ex.: Apache ou Nginx).
Detectar padrões suspeitos (ex.: múltiplas tentativas de login, acessos de IPs diferentes).
Gerar alertas simples (ex.: salvar em arquivo ou enviar e-mail).
👉 Impacto: demonstra aplicação prática de Segurança da Informação, lógica de detecção e monitoramento.




"""""



falhas_login500 = 0
falhas_login401 = 0
falhas_login300 = 0
acesso_200 = 0
with open("access.log", "r") as f:
    for linhas in f:
        if "500" in linhas:
            falhas_login500 += 1
            print("O servidor recebeu uma resposta inválida de outro servidor.")
        elif "401" in linhas:
            falhas_login401 += 1
            print("Falta autenticação ou credenciais inválidas.")
        elif "300" in linhas:
            falhas_login300 += 1
            print("Redirecionamento temporário.")
        elif "200" in linhas:
            acesso_200 += 1
            print("Requisição bem-sucedida, o conteúdo foi entregue normalmente.")


print("\nResumo:")
print(f"500: {falhas_login500}")
print(f"401: {falhas_login401}")
print(f"300: {falhas_login300}")
print(f"200: {acesso_200}")

