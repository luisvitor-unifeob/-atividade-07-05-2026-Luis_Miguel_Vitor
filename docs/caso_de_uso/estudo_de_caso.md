<img width="394" height="808" alt="image" src="https://github.com/user-attachments/assets/5f1b9e40-86e0-423b-8dbf-082c230c6cc9" />


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
3. O administrador informa nome, endereço e capacidade.
4. O sistema valida e salva os dados.

**RF Relacionados:** RF01  
**RN Relacionadas:** RN04, RN05

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

**RF Relacionados:** RF02  
**RN Relacionadas:** RN04

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

**RF Relacionados:** RF03  
**RN Relacionadas:** RN01, RN02, RN05

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

**RF Relacionados:** RF04  
**RN Relacionadas:** RN03

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

**RF Relacionados:** RF05  
**RN Relacionadas:** RN05

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

**RF Relacionados:** RF06  
**RN Relacionadas:** RN04, RN05

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

**RF Relacionados:** RF07  
**RN Relacionadas:** RN03

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

**RF Relacionados:** RF08  
**RN Relacionadas:** RN03, RN04

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

**RF Relacionados:** RF09  
**RN Relacionadas:** RN03, RN05
