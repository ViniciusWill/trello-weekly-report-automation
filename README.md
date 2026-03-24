 📊 Trello Weekly Report Automation

Automação desenvolvida em Python para processar exportações do Trello e gerar relatórios semanais organizados em Excel.

O projeto surgiu a partir de uma necessidade real: reduzir o trabalho manual envolvido na criação de relatórios de acompanhamento de tarefas, tornando o processo mais rápido, confiável e padronizado.

---

## 🧠 Regras de negócio tratadas

- Filtragem de tarefas que não representam progresso real
- Tratamento de inconsistências em apontamento de horas (ex: valores negativos como "-1h")
- Padronização de status e informações
- Tratamento de exceções para evitar falhas no processamento

---

## 🧪 Dados fictícios

Os dados utilizados neste projeto são **totalmente fictícios**, gerados automaticamente para simular exportações do Trello, sem qualquer relação com dados reais.

---

## ⚙️ Tecnologias utilizadas

- Python
- Pandas
- OpenPyXL

---


## ▶️ Como usar

### 🔹 Opção 1 — Execução rápida (recomendada)
1. Exporte os dados do Trello em formato `.xlsx` e com o nome 'trello'
2. Coloque o arquivo dentro da pasta: /INPUT
3. Execute o arquivo: iniciar.bat
4. O relatório será gerado automaticamente na pasta: output/

### 🔹 Opção 2 — Execução manual

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/trello-weekly-report-automation.git
```
2. Acesse a pasta do projeto: cd trello-weekly-report-automation
3. Instale as dependências:
```bash
    pip install -r requirements.txt
```
4. Adicione o arquivo .xlsx na pasta: INPUT/
5. Execute o script: python App/main.py
