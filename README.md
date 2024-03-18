# Projeto-Integrador-II-B

### Resumo:
Tendo por base os conceitos explorados nas disciplinas de **Segurança da Informação** e **Empreendedorismo**, bem como a partir da contextualização dos mesmos, feita na disciplina do Projeto Integrador II-B, os alunos irão sistematizar conhecimentos e empregá-los de forma prática a fim de conceber e implementar soluções para o enfrentamento de ataques cibernéticos de Força Bruta aos sistemas computacionais.

Este repositório será empregado para registro dos procedimentos e/ou programas desenvolvidos pelos Grupos. Os Grupos podem ser formados por 1, 2 ou 3 alunos.

### Documentos Guia 

* A atividade teórica (Entrega Parcial) do Projeto Integrador II-B está sistematizada neste **[documento](https://docs.google.com/document/d/1Em_dBCak86YgBbw-TmP5WTuPLX0AXukhA82_4V-PB8Y/edit?usp=sharing)**

* A descrição da atividade prática a ser desenvolvida pode ser acessada diretamente neste outro **[documento](https://docs.google.com/document/d/1llRsUmV8jtQPnpm_ZKTyPHc9mmyEcvvoGf9U9W20U0M/edit?usp=sharing)**

**Recursos de Software para Quebra de Senhas Discutidos. Outros poderão ser empregados a critério do grupo:**

* **Hashcat:** Este aplicativo pode ser utilizado tanto no MS-Windows como em distribuições Linux. Informações para uso do Hashcat estão disponíveis no link abaixo:
  * **[Tutoriais para uso do Hashcat (Windows e Linux)](https://github.com/adenauery/hashcat/wiki/Explorando-o--Hashcat)**. 

* **pi-ii-b-md5-cracker.py:** Programa em Python desenvolvido para quebra de Hashs MD5. Este programa já considera o alfabeto previsto pela atividade. Abaixo informações para o seu uso:
  * Obter o código do programa clicando neste [link](https://github.com/adenauery/Projeto-Integrador-II-B/blob/main/pi-ii-b-md5-cracker.py)
  * Criar no mesmo diretório em que for copiado o programa (pi-ii-b-md5-cracker.py) um arquivo com o nome "Arquivo-Hashes.txt" contendo as hashs a serem quebradas
  * Executar o progrma utilizando python3 pi-ii-b-md5-cracker.py
  * As senhas decorrentes das hashs quebradas iráo sendo colocadas em um arquivo denominado "Arquivo-Senhas.txt". Comandos de somente leitura, como o **cat** e o **tail**, podem ser utilizados para observar o conteúdo do arquivo "Arquivo-Senhas.txt" durante o processamento. Com o processamento interrompido, o mesmo pode ser lido inclusive por editores de texto.

### Hashs Produzidas Pelos Grupos

* As hashs produzidas pelos grupos estão disponíveis neste **[arquivo](https://github.com/adenauery/Projeto-Integrador-II-B/blob/main/hashs-md5-grupos.txt)**.
* O desafio será iniciado em **19/11/2022, 10h**, com a postagem das hashs

### Outras práticas exercitadas, mas que não irão fazer parte dos Relatórios Parcial e Final

Como verificar se um site é vulnerável a ataques de SQL Injection. Uma sequencia típica de procedimentos está disponível neste **[documento](https://github.com/adenauery/sqlmap/wiki/Explorando-o-SQLMAP)**

### Estatísticas de Ataques no Mundo
  * https://cybermap.kaspersky.com/pt/stats
