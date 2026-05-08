
<img width="394" height="808" alt="image" src="https://github.com/user-attachments/assets/7b7151d2-3e0f-4436-bcb5-d909cc7e3a86" />




### UC01 — Cadastrar Cinema
**Ator Principal:** Administrador

**Objetivo:** Permitir o cadastro de um novo cinema no sistema.

**Pré-condições:**
- Usuário autenticado como administrador.

**Pós-condições:**
- Cinema cadastrado e disponível no sistema.

**Fluxo Principal:**
1. O administrador acessa a opção de cadastro de cinema.
2. O sistema exibe o formulário de cadastro.
3. O administrador informa nome, endereço, franquia e capacidade maxima.
4. O sistema valida e salva os dados e cadastra o cinema.

<img width="220" height="61" alt="image" src="https://github.com/user-attachments/assets/2660c075-7696-45e6-aa87-65b6994a22bb" />



---

### UC02 — Cadastrar Filme
**Ator Principal:** Administrador

**Objetivo:** Permitir o cadastro de um novo filme no sistema.

**Pré-condições:**
- Usuário autenticado como administrador.

**Pós-condições:**
- Filme cadastrado e disponível para vinculação em sessões.

**Fluxo Principal:**
1. O administrador acessa a opção de cadastro de filme.
2. O sistema exibe o formulário de cadastro.
3. O administrador informa título, duração, gênero, sinopse, diretor e elenco.
4. O sistema valida e salva os dados.

<img width="220" height="63" alt="image" src="https://github.com/user-attachments/assets/f4a9fe4a-ebb0-4c95-9f38-7b3209fb141a" />


---

### UC03 — Cadastrar Sessão
**Ator Principal:** Funcionário

**Objetivo:** Permitir o cadastro de uma nova sessão vinculando filme e cinema.

**Pré-condições:**
- Filme e cinema previamente cadastrados no sistema.

**Pós-condições:**
- Sessão cadastrada e disponível para registro de público.

**Fluxo Principal:**
1. O funcionário acessa a opção de cadastro de sessão.
2. O sistema exibe os filmes e cinemas disponíveis.
3. O funcionário seleciona o filme, o cinema, e informa data, horário e sala.
4. O sistema valida o horário e salva a sessão.

<img width="220" height="63" alt="image" src="https://github.com/user-attachments/assets/f9f31e37-1163-4dbc-9e6c-4245f4a78b39" />


---

### UC04 — Registrar Público
**Ator Principal:** Funcionário

**Objetivo:** Registrar a quantidade de público presente em uma sessão.

**Pré-condições:**
- Sessão previamente cadastrada no sistema.

**Pós-condições:**
- Público registrado e contabilizado na sessão.

**Fluxo Principal:**
1. O funcionário acessa a opção de registro de público.
2. O sistema exibe as sessões disponíveis.
3. O funcionário seleciona a sessão e informa a quantidade de público.
4. O sistema valida a capacidade e salva o registro.
 
<img width="220" height="64" alt="image" src="https://github.com/user-attachments/assets/63b1f999-4b49-4d7d-ad6e-29ea5b8b3719" />


---

### UC05 — Listar Filmes em Cartaz
**Ator Principal:** Espectador

**Objetivo:** Permitir que o espectador consulte os filmes em cartaz em um cinema.

**Pré-condições:**
- Existir ao menos uma sessão cadastrada no cinema.

**Pós-condições:**
- Lista de filmes e horários exibida ao espectador.

**Fluxo Principal:**
1. O espectador seleciona um cinema.
2. O sistema busca as sessões disponíveis.
3. O sistema exibe os filmes em cartaz com seus respectivos horários.

<img width="220" height="58" alt="image" src="https://github.com/user-attachments/assets/3ee6b741-6fbb-476c-92df-5265f4fcebad" />


---

### UC06 — Consultar Sessões por Filme
**Ator Principal:** Espectador

**Objetivo:** Permitir que o espectador consulte as sessões disponíveis de um filme.

**Pré-condições:**
- Filme cadastrado com ao menos uma sessão vinculada.

**Pós-condições:**
- Sessões do filme exibidas com cinema, data e horário.

**Fluxo Principal:**
1. O espectador seleciona um filme.
2. O sistema busca todas as sessões vinculadas ao filme.
3. O sistema exibe as sessões com cinema, data e horário.

<img width="220" height="53" alt="image" src="https://github.com/user-attachments/assets/a8919763-afe4-4796-a158-7e52311f1bda" />


---

### UC07 — Consultar Total de Público por Sessão
**Ator Principal:** Administrador

**Objetivo:** Consultar o total de público registrado em uma sessão específica.

**Pré-condições:**
- Sessão cadastrada com ao menos um registro de público.

**Pós-condições:**
- Total de público da sessão exibido.

**Fluxo Principal:**
1. O administrador seleciona uma sessão.
2. O sistema soma todos os registros de público da sessão.
3. O sistema exibe o total.

<img width="220" height="52" alt="image" src="https://github.com/user-attachments/assets/4e8d01d0-9bc5-45aa-a41c-0f6fae60ba15" />


---

### UC08 — Consultar Total de Público por Filme
**Ator Principal:** Administrador

**Objetivo:** Consultar o total de público de todas as sessões de um filme.

**Pré-condições:**
- Filme cadastrado com ao menos uma sessão com público registrado.

**Pós-condições:**
- Total de público do filme exibido.

**Fluxo Principal:**
1. O administrador seleciona um filme.
2. O sistema soma o público de todas as sessões do filme.
3. O sistema exibe o total.

<img width="220" height="53" alt="image" src="https://github.com/user-attachments/assets/784f5897-2449-49a4-b14f-c27f6ad329b1" />


---

### UC09 — Consultar Total de Público por Cinema
**Ator Principal:** Administrador

**Objetivo:** Consultar o total de público de todas as sessões realizadas em um cinema.

**Pré-condições:**
- Cinema cadastrado com ao menos uma sessão com público registrado.

**Pós-condições:**
- Total de público do cinema exibido.

**Fluxo Principal:**
1. O administrador seleciona um cinema.
2. O sistema soma o público de todas as sessões do cinema.
3. O sistema exibe o total.

<img width="220" height="52" alt="image" src="https://github.com/user-attachments/assets/65c4da61-4b62-43cf-bd21-fb7706241985" />

