# Desafio de Automação — Talk a Bit (UFPE)

> Patrocínio **SIEG**. Tema: **automação web com Selenium**.
> Os pesos de pontuação ficam com a organização; havendo divergência entre este texto e o motor de avaliação, vale o motor.

## O que é

Você recebe o acesso a um **portal fiscal fictício** (o *Portal Nimbus*, sem qualquer marca ou órgão real). O portal lista **notas fiscais fake** e é **propositalmente hostil a robôs**: os campos do formulário de busca mudam de nome a cada sessão, a página demora de forma aleatória, a mesma informação aparece em layouts diferentes, e há armadilhas no caminho.

Seu objetivo: **automatizar a extração dos dados corretos com Selenium** e submetê-los ao nosso motor de avaliação. O placar é **ao vivo**.

## O que extrair

Extraia, de **todas as notas com status `Autorizada`**, o par:

- `chave` — a **chave de acesso** de 44 dígitos da nota;
- `valor` — o **valor total** da nota (em reais).

Notas `Cancelada` e `Denegada` **não** entram. Cada equipe recebe um **conjunto de dados próprio** (derivado do seu `teamToken`) — não adianta copiar a resposta da equipe ao lado.

## Como submeter

Ao terminar, seu bot faz um **`POST /api/submit`** com o payload:

```json
{# Desafio de Automação — Talk a Bit (UFPE)

> Patrocínio **SIEG**. Tema: **automação web com Selenium**.
> Os pesos de pontuação ficam com a organização; havendo divergência entre este texto e o motor de avaliação, vale o motor.

## O que é

Você recebe o acesso a um **portal fiscal fictício** (o *Portal Nimbus*, sem qualquer marca ou órgão real). O portal lista **notas fiscais fake** e é **propositalmente hostil a robôs**: os campos do formulário de busca mudam de nome a cada sessão, a página demora de forma aleatória, a mesma informação aparece em layouts diferentes, e há armadilhas no caminho.

Seu objetivo: **automatizar a extração dos dados corretos com Selenium** e submetê-los ao nosso motor de avaliação. O placar é **ao vivo**.

## O que extrair

Extraia, de **todas as notas com status `Autorizada`**, o par:

- `chave` — a **chave de acesso** de 44 dígitos da nota;
- `valor` — o **valor total** da nota (em reais).

Notas `Cancelada` e `Denegada` **não** entram. Cada equipe recebe um **conjunto de dados próprio** (derivado do seu `teamToken`) — não adianta copiar a resposta da equipe ao lado.

## Como submeter

Ao terminar, seu bot faz um **`POST /api/submit`** com o payload:

```json
{
  "teamToken": "SEU-TOKEN",
  "itens": [
    { "chave": "0000...44 dígitos", "valor": 1234.56 },
    { "chave": "1111...44 dígitos", "valor": 987.00 }
  ]
}
```

- `teamToken` é entregue no **credenciamento** e identifica sua equipe (sem ele, não há submissão).
- `valor` pode ir como número (`1234.56`) ou string no formato brasileiro (`"1.234,56"`) — o servidor normaliza.
- **Importante:** a resposta **não diz quais itens você acertou** — só confirma o recebimento e sua posição no placar. Isso é de propósito: o `/api/submit` não é um oráculo pra você adivinhar o gabarito.

O **kit do participante** traz o contrato completo do endpoint e os dados de acesso. Não há bot de exemplo — construir a automação do zero é o desafio.

## Regras

- **Selenium é obrigatório.** Linguagem **livre** (diferencial para **C#**).
- Você roda o Selenium na **sua própria máquina**, contra o site hospedado. **A SIEG não executa o seu código** — só valida o payload que você envia.
- Submissões são **limitadas a 10 tentativas**, com **30 segundos de cooldown** entre elas. Vale sempre o **seu melhor score**.
- Equipes de 3–4 pessoas. Duração: **4 horas**.
- **Sem ferramentas de IA.** É **proibido** usar assistentes de IA (ChatGPT, GitHub Copilot, Cursor, Claude e afins) para **gerar, completar ou depurar** o código durante o desafio. Consultar a **documentação oficial** (da linguagem, do Selenium) e fóruns é permitido. O objetivo é avaliar a **habilidade do time** — não a de operar uma IA.

## Verificação de habilidade (banca)

O placar decide o ranking; a **banca** decide o pódio. Antes da premiação, os
times mais bem colocados passam por uma **defesa técnica**:

- **Explicar o próprio código** — qualquer integrante deve conseguir percorrer a
  solução e justificar as decisões.
- **Adaptar ao vivo** — a banca pede **uma alteração na hora** (ex.: extrair
  também um novo campo, lidar com uma nova pegadinha), a ser implementada **sem
  IA**, em tempo limitado.
- **Não conseguir explicar/adaptar** o próprio código = **desclassificação**,
  independentemente da pontuação.
- **Uso comprovado de IA** durante o desafio = **desclassificação**.

> A organização pode conduzir o desafio (ou a defesa) em **ambiente controlado**
> (máquinas fornecidas, sem ferramentas de IA), a seu critério.

## Mecânicas anti-automação (níveis)

**N1–N4 são o núcleo obrigatório** — sem lidar com eles você não consegue extrair de forma confiável. **N5–N6 rendem bônus** — e o N5 merece atenção: parte das notas «Autorizada» só aparece depois de vencê-lo, e elas contam como itens normais, então deixá-las de fora custa pontos *além* do bônus.

| Nível | Tema |
|-------|------|
| **N1** | Localização dos elementos |
| **N2** | Tempo de resposta |
| **N3** | Estrutura da página |
| **N4** | Ruído e armadilhas na tela |
| **N5** *(bônus)* | Navegação difícil |
| **N6** *(bônus)* | Mudança de rodada |

Descobrir como cada frente se manifesta — e contorná-la — faz parte do desafio.

> ⚠️ Nem toda interação na tela é segura: certas armadilhas aplicam **penalidade** se você cair nelas.

## Pontuação# Desafio de Automação — Talk a Bit (UFPE)

> Patrocínio **SIEG**. Tema: **automação web com Selenium**.
> Os pesos de pontuação ficam com a organização; havendo divergência entre este texto e o motor de avaliação, vale o motor.

## O que é

Você recebe o acesso a um **portal fiscal fictício** (o *Portal Nimbus*, sem qualquer marca ou órgão real). O portal lista **notas fiscais fake** e é **propositalmente hostil a robôs**: os campos do formulário de busca mudam de nome a cada sessão, a página demora de forma aleatória, a mesma informação aparece em layouts diferentes, e há armadilhas no caminho.

Seu objetivo: **automatizar a extração dos dados corretos com Selenium** e submetê-los ao nosso motor de avaliação. O placar é **ao vivo**.

## O que extrair

Extraia, de **todas as notas com status `Autorizada`**, o par:

- `chave` — a **chave de acesso** de 44 dígitos da nota;
- `valor` — o **valor total** da nota (em reais).

Notas `Cancelada` e `Denegada` **não** entram. Cada equipe recebe um **conjunto de dados próprio** (derivado do seu `teamToken`) — não adianta copiar a resposta da equipe ao lado.

## Como submeter

Ao terminar, seu bot faz um **`POST /api/submit`** com o payload:

```json
{
  "teamToken": "SEU-TOKEN",
  "itens": [
    { "chave": "0000...44 dígitos", "valor": 1234.56 },
    { "chave": "1111...44 dígitos", "valor": 987.00 }
  ]
}
```

- `teamToken` é entregue no **credenciamento** e identifica sua equipe (sem ele, não há submissão).
- `valor` pode ir como número (`1234.56`) ou string no formato brasileiro (`"1.234,56"`) — o servidor normaliza.
- **Importante:** a resposta **não diz quais itens você acertou** — só confirma o recebimento e sua posição no placar. Isso é de propósito: o `/api/submit` não é um oráculo pra você adivinhar o gabarito.

O **kit do participante** traz o contrato completo do endpoint e os dados de acesso. Não há bot de exemplo — construir a automação do zero é o desafio.

## Regras

- **Selenium é obrigatório.** Linguagem **livre** (diferencial para **C#**).
- Você roda o Selenium na **sua própria máquina**, contra o site hospedado. **A SIEG não executa o seu código** — só valida o payload que você envia.
- Submissões são **limitadas a 10 tentativas**, com **30 segundos de cooldown** entre elas. Vale sempre o **seu melhor score**.
- Equipes de 3–4 pessoas. Duração: **4 horas**.
- **Sem ferramentas de IA.** É **proibido** usar assistentes de IA (ChatGPT, GitHub Copilot, Cursor, Claude e afins) para **gerar, completar ou depurar** o código durante o desafio. Consultar a **documentação oficial** (da linguagem, do Selenium) e fóruns é permitido. O objetivo é avaliar a **habilidade do time** — não a de operar uma IA.

## Verificação de habilidade (banca)

O placar decide o ranking; a **banca** decide o pódio. Antes da premiação, os
times mais bem colocados passam por uma **defesa técnica**:

- **Explicar o próprio código** — qualquer integrante deve conseguir percorrer a
  solução e justificar as decisões.
- **Adaptar ao vivo** — a banca pede **uma alteração na hora** (ex.: extrair
  também um novo campo, lidar com uma nov# Desafio de Automação — Talk a Bit (UFPE)

> Patrocínio **SIEG**. Tema: **automação web com Selenium**.
> Os pesos de pontuação ficam com a organização; havendo divergência entre este texto e o motor de avaliação, vale o motor.

## O que é

Você recebe o acesso a um **portal fiscal fictício** (o *Portal Nimbus*, sem qualquer marca ou órgão real). O portal lista **notas fiscais fake** e é **propositalmente hostil a robôs**: os campos do formulário de busca mudam de nome a cada sessão, a página demora de forma aleatória, a mesma informação aparece em layouts diferentes, e há armadilhas no caminho.

Seu objetivo: **automatizar a extração dos dados corretos com Selenium** e submetê-los ao nosso motor de avaliação. O placar é **ao vivo**.

## O que extrair

Extraia, de **todas as notas com status `Autorizada`**, o par:

- `chave` — a **chave de acesso** de 44 dígitos da nota;
- `valor` — o **valor total** da nota (em reais).

Notas `Cancelada` e `Denegada` **não** entram. Cada equipe recebe um **conjunto de dados próprio** (derivado do seu `teamToken`) — não adianta copiar a resposta da equipe ao lado.

## Como submeter

Ao terminar, seu bot faz um **`POST /api/submit`** com o payload:

```json
{
  "teamToken": "SEU-TOKEN",
  "itens": [
    { "chave": "0000...44 dígitos", "valor": 1234.56 },
    { "chave": "1111...44 dígitos", "valor": 987.00 }
  ]
}
```

- `teamToken` é entregue no **credenciamento** e identifica sua equipe (sem ele, não há submissão).
- `valor` pode ir como número (`1234.56`) ou string no formato brasileiro (`"1.234,56"`) — o servidor normaliza.
- **Importante:** a resposta **não diz quais itens você acertou** — só confirma o recebimento e sua posição no placar. Isso é de propósito: o `/api/submit` não é um oráculo pra você adivinhar o gabarito.

O **kit do participante** traz o contrato completo do endpoint e os dados de acesso. Não há bot de exemplo — construir a automação do zero é o desafio.

## Regras

- **Selenium é obrigatório.** Linguagem **livre** (diferencial para **C#**).
- Você roda o Selenium na **sua própria máquina**, contra o site hospedado. **A SIEG não executa o seu código** — só valida o payload que você envia.
- Submissões são **limitadas a 10 tentativas**, com **30 segundos de cooldown** entre elas. Vale sempre o **seu melhor score**.
- Equipes de 3–4 pessoas. Duração: **4 horas**.
- **Sem ferramentas de IA.** É **proibido** usar assistentes de IA (ChatGPT, GitHub Copilot, Cursor, Claude e afins) para **gerar, completar ou depurar** o código durante o desafio. Consultar a **documentação oficial** (da linguagem, do Selenium) e fóruns é permitido. O objetivo é avaliar a **habilidade do time** — não a de operar uma IA.

## Verificação de habilidade (banca)

O placar decide o ranking; a **banca** decide o pódio. Antes da premiação, os
times mais bem colocados passam por uma **defesa técnica**:

- **Explicar o próprio código** — qualquer integrante deve conseguir percorrer a
  solução e justificar as decisões.
- **Adaptar ao vivo** — a banca pede **uma alteração na hora** (ex.: extrair
  também um novo campo, lidar com uma nova pegadinha), a ser implementada **sem
  IA**, em tempo limitado.
- **Não conseguir explicar/adaptar** o próprio código = **desclassificação**,
  independentemente da pontuação.
- **Uso comprovado de IA** durante o desafio = **desclassificação**.

> A organização pode conduzir o desafio (ou a defesa) em **ambiente controlado**
> (máquinas fornecidas, sem ferramentas de IA), a seu critério.

## Mecânicas anti-automação (níveis)

**N1–N4 são o núcleo obrigatório** — sem lidar com eles você não consegue extrair de forma confiável. **N5–N6 rendem bônus** — e o N5 merece atenção: parte das notas «Autorizada» só aparece depois de vencê-lo, e elas contam como itens normais, então deixá-las de fora custa pontos *além* do bônus.

| Nível | Tema |
|-------|------|
| **N1** | Localização dos elementos |
| **N2** | Tempo de resposta |
| **N3** | Estrutura da página |
| **N4** | Ruído e armadilhas na tela |
| **N5** *(bônus)* | Navegação difícil |
| **N6** *(bônus)* | Mudança de rodada |

Descobrir como cada frente se manifesta — e contorná-la — faz parte do desafio.

> ⚠️ Nem toda interação na tela é segura: certas armadilhas aplicam **penalidade** se você cair nelas.

## Pontuação

`score = (itens corretos × pontosPorItemCorreto) − (itens incorretos × penalidadePorItemIncorreto) − penalidade_de_tempo − penalidade_honeypot + bônus_de_níveis`

> O score **nunca fica negativo**: se as # Desafio de Automação — Talk a Bit (UFPE)

> Patrocínio **SIEG**. Tema: **automação web com Selenium**.
> Os pesos de pontuação ficam com a organização; havendo divergência entre este texto e o motor de avaliação, vale o motor.

## O que é

Você recebe o acesso a um **portal fiscal fictício** (o *Portal Nimbus*, sem qualquer marca ou órgão real). O portal lista **notas fiscais fake** e é **propositalmente hostil a robôs**: os campos do formulário de busca mudam de nome a cada sessão, a página demora de forma aleatória, a mesma informação aparece em layouts diferentes, e há armadilhas no caminho.

Seu objetivo: **automatizar a extração dos dados corretos com Selenium** e submetê-los ao nosso motor de avaliação. O placar é **ao vivo**.

## O que extrair

Extraia, de **todas as notas com status `Autorizada`**, o par:

- `chave` — a **chave de acesso** de 44 dígitos da nota;
- `valor` — o **valor total** da nota (em reais).

Notas `Cancelada` e `Denegada` **não** entram. Cada equipe recebe um **conjunto de dados próprio** (derivado do seu `teamToken`) — não adianta copiar a resposta da equipe ao lado.

## Como submeter

Ao terminar, seu bot faz um **`POST /api/submit`** com o payload:

```json
{
  "teamToken": "SEU-TOKEN",
  "itens": [
    { "chave": "0000...44 dígitos", "valor": 1234.56 },
    { "chave": "1111...44 dígitos", "valor": 987.00 }
  ]
}
```

- `teamToken` é entregue no **credenciamento** e identifica sua equipe (sem ele, não há submissão).
- `valor` pode ir como número (`1234.56`) ou string no formato brasileiro (`"1.234,56"`) — o servidor normaliza.
- **Importante:** a resposta **não diz quais itens você acertou** — só confirma o recebimento e sua posição no placar. Isso é de propósito: o `/api/submit` não é um oráculo pra você adivinhar o gabarito.

O **kit do participante** traz o contrato completo do endpoint e os dados de acesso. Não há bot de exemplo — construir a automação do zero é o desafio.

## Regras

- **Selenium é obrigatório.** Linguagem **livre** (diferencial para **C#**).
- Você roda o Selenium na **sua própria máquina**, contra o site hospedado. **A SIEG não executa o seu código** — só valida o payload que você envia.
- Submissões são **limitadas a 10 tentativas**, com **30 segundos de cooldown** entre elas. Vale sempre o **seu melhor score**.
- Equipes de 3–4 pessoas. Duração: **4 horas**.
- **Sem ferramentas de IA.** É **proibido** usar assistentes de IA (ChatGPT, GitHub Copilot, Cursor, Claude e afins) para **gerar, completar ou depurar** o código durante o desafio. Consultar a **documentação oficial** (da linguagem, do Selenium) e fóruns é permitido. O objetivo é avaliar a **habilidade do time** — não a de operar uma IA.

## Verificação de habilidade (banca)

O placar decide o ranking; a **banca** decide o pódio. Antes da premiação, os
times mais bem colocados passam por uma **defesa técnica**:

- **Explicar o próprio código** — qualquer integrante deve conseguir percorrer a
  solução e justificar as decisões.
- **Adaptar ao vivo** — a banca pede **uma alteração na hora** (ex.: extrair
  também um novo campo, lidar com uma nova pegadinha), a ser implementada **sem
  IA**, em tempo limitado.
- **Não conseguir explicar/adaptar** o próprio código = **desclassificação**,
  independentemente da pontuação.
- **Uso comprovado de IA** durante o desafio = **desclassificação**.

> A organização pode conduzir o desafio (ou a defesa) em **ambiente controlado**
> (máquinas fornecidas, sem ferramentas de IA), a seu critério.

## Mecânicas anti-automação (níveis)

**N1–N4 são o núcleo obrigatório** — sem lidar com eles você não consegue extrair de forma confiável. **N5–N6 rendem bônus** — e o N5 merece atenção: parte das notas «Autorizada» só aparece depois de vencê-lo, e elas contam como itens normais, então deixá-las de fora custa pontos *além* do bônus.

| Nível | Tema |
|-------|------|
| **N1** | Localização dos elementos |
| **N2** | Tempo de resposta |
| **N3** | Estrutura da página |
| **N4** | Ruído e armadilhas na tela |
| **N5** *(bônus)* | Navegação difícil |
| **N6** *(bônus)* | Mudança de rodada |# Desafio de Automação — Talk a Bit (UFPE)

> Patrocínio **SIEG**. Tema: **automação web com Selenium**.
> Os pesos de pontuação ficam com a organização; havendo divergência entre este texto e o motor de avaliação, vale o motor.

## O que é

Você recebe o acesso a um **portal fiscal fictício** (o *Portal Nimbus*, sem qualquer marca ou órgão real). O portal lista **notas fiscais fake** e é **propositalmente hostil a robôs**: os campos do formulário de busca mudam de nome a cada sessão, a página demora de forma aleatória, a mesma informação aparece em layouts diferentes, e há armadilhas no caminho.

Seu objetivo: **automatizar a extração dos dados corretos com Selenium** e submetê-los ao nosso motor de avaliação. O placar é **ao vivo**.

## O que extrair

Extraia, de **todas as notas com status `Autorizada`**, o par:

- `chave` — a **chave de acesso** de 44 dígitos da nota;
- `valor` — o **valor total** da nota (em reais).

Notas `Cancelada` e `Denegada` **não** entram. Cada equipe recebe um **conjunto de dados próprio** (derivado do seu `teamToken`) — não adianta copiar a resposta da equipe ao lado.

## Como submeter

Ao terminar, seu bot faz um **`POST /api/submit`** com o payload:

```json
{
  "teamToken": "SEU-TOKEN",
  "itens": [
    { "chave": "0000...44 dígitos", "valor": 1234.56 },
    { "chave": "1111...44 dígitos", "valor": 987.00 }
  ]
}
```

- `teamToken` é entregue no **credenciamento** e identifica sua equipe (sem ele, não há submissão).
- `valor` pode ir como número (`1234.56`) ou string no formato brasileiro (`"1.234,56"`) — o servidor normaliza.
- **Importante:** a resposta **não diz quais itens você acertou** — só confirma o recebimento e sua posição no placar. Isso é de propósito: o `/api/submit` não é um oráculo pra você adivinh# Desafio de Automação — Talk a Bit (UFPE)

> Patrocínio **SIEG**. Tema: **automação web com Selenium**.
> Os pesos de pontuação ficam com a organização; havendo divergência entre este texto e o motor de avaliação, vale o motor.

## O que é

Você recebe o acesso a um **portal fiscal fictício** (o *Portal Nimbus*, sem qualquer marca ou órgão real). O portal lista **notas fiscais fake** e é **propositalmente hostil a robôs**: os campos do formulário de busca mudam de nome a cada sessão, a página demora de forma aleatória, a mesma informação aparece em layouts diferentes, e há armadilhas no caminho.

Seu objetivo: **automatizar a extração dos dados corretos com Selenium** e submetê-los ao nosso motor de avaliação. O placar é **ao vivo**.

## O que extrair

Extraia, de **todas as notas com status `Autorizada`**, o par:

- `chave` — a **chave de acesso** de 44 dígitos da nota;
- `valor` — o **valor total** da nota (em reais).

Notas `Cancelada` e `Denegada` **não** entram. Cada equipe recebe um **conjunto de dados próprio** (derivado do seu `teamToken`) — não adianta copiar a resposta da equipe ao lado.

## Como submeter

Ao terminar, seu bot faz um **`POST /api/submit`** com o payload:

```json
{
  "teamToken": "SEU-TOKEN",
  "itens": [
    { "chave": "0000...44 dígitos", "valor": 1234.56 },
    { "chave": "1111...44 dígitos", "valor": 987.00 }
  ]
}
```

- `teamToken` é entregue no **credenciamento** e identifica sua equipe (sem ele, não há submissão).
- `valor` pode ir como número (`1234.56`) ou string no formato brasileiro (`"1.234,56"`) — o servidor normaliza.
- **Importante:** a resposta **não diz quais itens você acertou** — só confirma o recebimento e sua posição no placar. Isso é de propósito: o `/api/submit` não é um oráculo pra você adivinhar o gabarito.
# Desafio de Automação — Talk a Bit (UFPE)

> Patrocínio **SIEG**. Tema: **automação web com Selenium**.
> Os pesos de pontuação ficam com a organização; havendo divergência entre este texto e o motor de avaliação, vale o motor.

## O que é

Você recebe o acesso a um **portal fiscal fictício** (o *Portal Nimbus*, sem qualquer marca ou órgão real). O portal lista **notas fiscais fake** e é **propositalmente hostil a robôs**: os campos do formulário de busca mudam de nome a cada sessão, a página demora de forma aleatória, a mesma informação aparece em layouts diferentes, e há armadilhas no caminho.

Seu objetivo: **automatizar a extração dos dados corretos com Selenium** e submetê-los ao nosso motor de avaliação. O placar é **ao vivo**.

## O que extrair

Extraia, de **todas as notas com status `Autorizada`**, o par:

- `chave` — a **chave de acesso** de 44 dígitos da nota;
- `valor` — o **valor total** da nota (em reais).

Notas `Cancelada` e `Denegada` **não** entram. Cada equipe recebe um **conjunto de dados próprio** (derivado do seu `teamToken`) — não adianta copiar a resposta da equipe ao lado.

## Como submeter

Ao terminar, seu bot faz um **`POST /api/submit`** com o payload:

```json
{
  "teamToken": "SEU-TOKEN",
  "itens": [
    { "chave": "0000...44 dígitos", "valor": 1234.56 },
    { "chave": "1111...44 dígitos", "valor": 987.00 }
  ]
}
```

- `teamToken` é entregue no **credenciamento** e identifica sua equipe (sem ele, não há submissão).
- `valor` pode ir como número (`1234.56`) ou string no formato brasileiro (`"1.234,56"`) — o servidor normaliza.
- **Importante:** a resposta **não diz quais itens você acertou** — só confirma o recebimento e sua posição no placar. Isso é de propósito: o `/api/submit` não é um oráculo pra você adivinhar o gabarito.

O **kit do participante** traz o contrato completo do endpoint e os dados de acesso. Não há bot de exemplo — construir a automação do zero é o desafio.

## Regras

- **Selenium é obrigatório.** Linguagem **livre** (diferencial para **C#**).
- Você roda o Selenium na **sua própria máquina**, contra o site hospedado. **A SIEG não executa o seu código** — só valida o payload que você envia.
- Submissões são **limitadas a 10 tentativas**, com **30 segundos de cooldown** entre elas. Vale sempre o **seu melhor score**.
- Equipes de 3–4 pessoas. Duração: **4 horas**.
- **Sem ferramentas de IA.** É **proibido** usar assistentes de IA (ChatGPT, GitHub Copilot, Cursor, Claude e afins) para **gerar, completar ou depurar** o código durante o desafio. Consultar a **documentação oficial** (da linguagem, do Selenium) e fóruns é permitido. O objetivo é avaliar a **habilidade do time** — não a de operar uma IA.

## Verificação de habilidade (banca)

O placar decide o ranking; a **banca** decide o pódio. Antes da premiação, os
times mais bem colocados passam por uma **defesa técnica**:

- **Explicar o próprio código** — qualquer integrante deve conseguir percorrer a
  solução e justificar as decisões.# Desafio de Automação — Talk a Bit (UFPE)

> Patrocínio **SIEG**. Tema: **automação web com Selenium**.
> Os pesos de pontuação ficam com a organização; havendo divergência entre este texto e o motor de avaliação, vale o motor.

## O que é

Você recebe o acesso a um **portal fiscal fictício** (o *Portal Nimbus*, sem qualquer marca ou órgão real). O portal lista **notas fiscais fake** e é **propositalmente hostil a robôs**: os campos do formulário de busca mudam de nome a cada sessão, a página demora de forma aleatória, a mesma informação aparece em layouts diferentes, e há armadilhas no caminho.

Seu objetivo: **automatizar a extração dos dados corretos com Selenium** e submetê-los ao nosso motor de avaliação. O placar é **ao vivo**.

## O que extrair

Extraia, de **todas as notas com status `Autorizada`**, o par:

- `chave` — a **chave de acesso** de 44 dígitos da nota;
- `valor` — o **valor total** da nota (em reais).

Notas `Cancelada` e `Denegada` **não** entram. Cada equipe recebe um **conjunto de dados próprio** (derivado do seu `teamToken`) — não adianta copiar a resposta da equipe ao lado.

## Como submeter

Ao terminar, seu bot faz um **`POST /api/submit`** com o payload:

```json
{
  "teamToken": "SEU-TOKEN",
  "itens": [
    { "chave": "0000...44 dígitos", "valor": 1234.56 },
    { "chave": "1111...44 dígitos", "valor": 987.00 }
  ]
}
```

- `teamToken` é entregue no **credenciamento** e identifica sua equipe (sem ele, não há submissão).
- `valor` pode ir como número (`1234.56`) ou string no formato brasileiro (`"1.234,56"`) — o servidor normaliza.
- **Importante:** a resposta **não diz quais itens você acertou** — só confirma o recebimento e sua posição no placar. Isso é de propósito: o `/api/submit` não é um oráculo pra você adivinhar o gabarito.

O **kit do participante** traz o contrato completo do endpoint e os dados de acesso. Não há bot de exemplo — construir a automação do zero é o desafio.

## Regras

- **Selenium é obrigatório.** Linguagem **livre** (diferencial para **C#**).
- Você roda o Selenium na **sua própria máquina**, contra o site hospedado. **A SIEG não executa o seu código** — só valida o payload que você envia.
- Submissões são **limitadas a 10 tentativas**, com **30 segundos de cooldown** entre elas. Vale sempre o **seu melhor score**.
- Equipes de 3–4 pessoas. Duração: **4 horas**.
- **Sem ferramentas de IA.** É **proibido** usar assistentes de IA (ChatGPT, GitHub Copilot, Cursor, Claude e afins) para **gerar, completar ou depurar** o código durante o desafio. Consultar a **documentação oficial** (da linguagem, do Selenium) e fóruns é permitido. O objetivo é avaliar a **habilidade do time** — não a de operar uma IA.

## Verificação de habilidade (banca)

O placar decide o ranking; a **banca** decide o pódio. Antes da premiação, os
times mais bem colocados passam por uma **defesa técnica**:

- **Explicar o próprio código** — qualquer integrante deve conseguir percorrer a
  solução e justificar as decisões.
- **Adaptar ao vivo** — a banca pede **uma alteração na hora** (ex.: extrair
  também um novo campo, lidar com uma nova pegadinha), a ser implementada **sem
  IA**, em tempo limitado.
- **Não conseguir explicar/adaptar** o próprio código = **desclassificação**,
  independentemente da pontuação.
- **Uso comprovado de IA** durante o desafio = **desclassificação**.

> A organização pode conduzir o desafio (ou a defesa) em **ambiente controlado**
> (máquinas fornecidas, sem ferramentas de IA), a seu critério.

## Mecânicas anti-automação (níveis)

**N1–N4 são o núcleo obrigatório** — sem lidar com eles você não consegue extrair de forma confiável. **N5–N6 rendem bônus** — e o N5 merece atenção: parte das notas «Autorizada» só aparece depois de vencê-lo, e elas contam como itens normais, então deixá-las de fora custa pontos *além* do bônus.

| Nível | Tema |
|-------|------|
| **N1** | Localização dos elementos |
| **N2** | Tempo de resposta |
| **N3** | Estrutura da página |
| **N4** | Ruído e armadilhas na tela |
| **N5** *(bônus)* | Navegação difícil |
| **N6** *(bônus)* | Mudança de rodada |

Descobrir como cada frente se manifesta — e contorná-la — faz parte do desafio.

> ⚠️ Nem toda interação na tela é segura: certas armadilhas aplicam **penalidade** se você cair nelas.

## Pontuação

`score = (itens corretos × pontosPorItemCorreto) − (itens incorretos × penalidadePorItemIncorreto) − penalidade_de_tempo − penalidade_honeypot + bônus_de_níveis`

> O score **nunca fica negativo**: se as penalidades passarem dos pontos, o placar mostra `0`.

- **Itens:** cada par `{chave, valor}` correto soma pontos; item errado desconta.
- **Tempo:** penalidade **linear por minuto** desde a **largada da sua equipe** (o relógio começa no seu **primeiro login bem-sucedido** no site-alvo), com teto.
- **Bônus de níveis:** **N5** é creditado ao extrair corretamente as notas que só existem atrás da navegação difícil — que **também somam como itens**; **N6** ao entregar um resultado correto após uma reorganização de rodada.
- **Honeypot:** penalidade fixa se sua equipe cair na armadilha.
- **Desempate:** maior score; havendo empate, menor tempo (submissão mais cedo).

## Fonte da verdade dos dados

O gabarito de cada equipe é gerado deterministicamente a partir do seu `(teamToken, round)` pelo **mesmo** módulo que alimenta o site e o corretor. Ou seja: o que você vê no portal é exatamente o que o corretor espera. Nada de gabarito "de fora".

- **Adaptar ao vivo** — a banca pede **uma alteração na hora** (ex.: extrair
  também um novo campo, lidar com uma nova pegadinha), a ser implementada **sem
  IA**, em tempo limitado.
- **Não conseguir explicar/adaptar** o próprio código = **desclassificação**,
  independentemente da pontuação.
- **Uso comprovado de IA** durante o desafio = **desclassificação**.

> A organização pode conduzir o desafio (ou a defesa) em **ambiente controlado**
> (máquinas fornecidas, sem ferramentas de IA), a seu critério.

## Mecânicas anti-automação (níveis)

**N1–N4 são o núcleo obrigatório** — sem lidar com eles você não consegue extrair de forma confiável. **N5–N6 rendem bônus** — e o N5 merece atenção: parte das notas «Autorizada» só aparece depois de vencê-lo, e elas contam como itens normais, então deixá-las de fora custa pontos *além* do bônus.

| Nível | Tema |
|-------|------|
| **N1** | Localização dos elementos |
| **N2** | Tempo de resposta |
| **N3** | Estrutura da página |
| **N4** | Ruído e armadilhas na tela |
| **N5** *(bônus)* | Navegação difícil |
| **N6** *(bônus)* | Mudança de rodada |

Descobrir como cada frente se manifesta — e contorná-la — faz parte do desafio.

> ⚠️ Nem toda interação na tela é segura: certas armadilhas aplicam **penalidade** se você cair nelas.

## Pontuação

`score = (itens corretos × pontosPorItemCorreto) − (itens incorretos × penalidadePorItemIncorreto) − penalidade_de_tempo − penalidade_honeypot + bônus_de_níveis`

> O score **nunca fica negativo**: se as penalidades passarem dos pontos, o placar mostra `0`.

- **Itens:** cada par `{chave, valor}` correto soma pontos; item errado desconta.
- **Tempo:** penalidade **linear por minuto** desde a **largada da sua equipe** (o relógio começa no seu **primeiro login bem-sucedido** no site-alvo), com teto.
- **Bônus de níveis:** **N5** é creditado ao extrair corretamente as notas que só existem atrás da navegação difícil — que **também somam como itens**; **N6** ao entregar um resultado correto após uma reorganização de rodada.
- **Honeypot:** penalidade fixa se sua equipe cair na armadilha.
- **Desempate:** maior score; havendo empate, menor tempo (submissão mais cedo).

## Fonte da verdade dos dados

O gabarito de cada equipe é gerado deterministicamente a partir do seu `(teamToken, round)` pelo **mesmo** módulo que alimenta o site e o corretor. Ou seja: o que você vê no portal é exatamente o que o corretor espera. Nada de gabarito "de fora".

O **kit do participante** traz o contrato completo do endpoint e os dados de acesso. Não há bot de exemplo — construir a automação do zero é o desafio.

## Regras

- **Selenium é obrigatório.** Linguagem **livre** (diferencial para **C#**).
- Você roda o Selenium na **sua própria máquina**, contra o site hospedado. **A SIEG não executa o seu código** — só valida o payload que você envia.
- Submissões são **limitadas a 10 tentativas**, com **30 segundos de cooldown** entre elas. Vale sempre o **seu melhor score**.
- Equipes de 3–4 pessoas. Duração: **4 horas**.
- **Sem ferramentas de IA.** É **proibido** usar assistentes de IA (ChatGPT, GitHub Copilot, Cursor, Claude e afins) para **gerar, completar ou depurar** o código durante o desafio. Consultar a **documentação oficial** (da linguagem, do Selenium) e fóruns é permitido. O objetivo é avaliar a **habilidade do time** — não a de operar uma IA.

## Verificação de habilidade (banca)

O placar decide o ranking; a **banca** decide o pódio. Antes da premiação, os
times mais bem colocados passam por uma **defesa técnica**:

- **Explicar o próprio código** — qualquer integrante deve conseguir percorrer a
  solução e justificar as decisões.
- **Adaptar ao vivo** — a banca pede **uma alteração na hora** (ex.: extrair
  também um novo campo, lidar com uma nova pegadinha), a ser implementada **sem
  IA**, em tempo limitado.
- **Não conseguir explicar/adaptar** o próprio código = **desclassificação**,
  independentemente da pontuação.
- **Uso comprovado de IA** durante o desafio = **desclassificação**.

> A organização pode conduzir o desafio (ou a defesa) em **ambiente controlado**
> (máquinas fornecidas, sem ferramentas de IA), a seu critério.

## Mecânicas anti-automação (níveis)

**N1–N4 são o núcleo obrigatório** — sem lidar com eles você não consegue extrair de forma confiável. **N5–N6 rendem bônus** — e o N5 merece atenção: parte das notas «Autorizada» só aparece depois de vencê-lo, e elas contam como itens normais, então deixá-las de fora custa pontos *além* do bônus.

| Nível | Tema |
|-------|------|
| **N1** | Localização dos elementos |
| **N2** | Tempo de resposta |
| **N3** | Estrutura da página |
| **N4** | Ruído e armadilhas na tela |
| **N5** *(bônus)* | Navegação difícil |
| **N6** *(bônus)* | Mudança de rodada |

Descobrir como cada frente se manifesta — e contorná-la — faz parte do desafio.

> ⚠️ Nem toda interação na tela é segura: certas armadilhas aplicam **penalidade** se você cair nelas.

## Pontuação

`score = (itens corretos × pontosPorItemCorreto) − (itens incorretos × penalidadePorItemIncorreto) − penalidade_de_tempo − penalidade_honeypot + bônus_de_níveis`

> O score **nunca fica negativo**: se as penalidades passarem dos pontos, o placar mostra `0`.

- **Itens:** cada par `{chave, valor}` correto soma pontos; item errado desconta.
- **Tempo:** penalidade **linear por minuto** desde a **largada da sua equipe** (o relógio começa no seu **primeiro login bem-sucedido** no site-alvo), com teto.
- **Bônus de níveis:** **N5** é creditado ao extrair corretamente as notas que só existem atrás da navegação difícil — que **também somam como itens**; **N6** ao entregar um resultado correto após uma reorganização de rodada.
- **Honeypot:** penalidade fixa se sua equipe cair na armadilha.
- **Desempate:** maior score; havendo empate, menor tempo (submissão mais cedo).

## Fonte da verdade dos dados

O gabarito de cada equipe é gerado deterministicamente a partir do seu `(teamToken, round)` pelo **mesmo** módulo que alimenta o site e o corretor. Ou seja: o que você vê no portal é exatamente o que o corretor espera. Nada de gabarito "de fora".
ar o gabarito.

O **kit do participante** traz o contrato completo do endpoint e os dados de acesso. Não há bot de exemplo — construir a automação do zero é o desafio.

## Regras

- **Selenium é obrigatório.** Linguagem **livre** (diferencial para **C#**).
- Você roda o Selenium na **sua própria máquina**, contra o site hospedado. **A SIEG não executa o seu código** — só valida o payload que você envia.
- Submissões são **limitadas a 10 tentativas**, com **30 segundos de cooldown** entre elas. Vale sempre o **seu melhor score**.
- Equipes de 3–4 pessoas. Duração: **4 horas**.
- **Sem ferramentas de IA.** É **proibido** usar assistentes de IA (ChatGPT, GitHub Copilot, Cursor, Claude e afins) para **gerar, completar ou depurar** o código durante o desafio. Consultar a **documentação oficial** (da linguagem, do Selenium) e fóruns é permitido. O objetivo é avaliar a **habilidade do time** — não a de operar uma IA.

## Verificação de habilidade (banca)

O placar decide o ranking; a **banca** decide o pódio. Antes da premiação, os
times mais bem colocados passam por uma **defesa técnica**:

- **Explicar o próprio código** — qualquer integrante deve conseguir percorrer a
  solução e justificar as decisões.
- **Adaptar ao vivo** — a banca pede **uma alteração na hora** (ex.: extrair
  também um novo campo, lidar com uma nova pegadinha), a ser implementada **sem
  IA**, em tempo limitado.
- **Não conseguir explicar/adaptar** o próprio código = **desclassificação**,
  independentemente da pontuação.
- **Uso comprovado de IA** durante o desafio = **desclassificação**.

> A organização pode conduzir o desafio (ou a defesa) em **ambiente controlado**
> (máquinas fornecidas, sem ferramentas de IA), a seu critério.

## Mecânicas anti-automação (níveis)

**N1–N4 são o núcleo obrigatório** — sem lidar com eles você não consegue extrair de forma confiável. **N5–N6 rendem bônus** — e o N5 merece atenção: parte das notas «Autorizada» só aparece depois de vencê-lo, e elas contam como itens normais, então deixá-las de fora custa pontos *além* do bônus.

| Nível | Tema |
|-------|------|
| **N1** | Localização dos elementos |
| **N2** | Tempo de resposta |
| **N3** | Estrutura da página |
| **N4** | Ruído e armadilhas na tela |
| **N5** *(bônus)* | Navegação difícil |
| **N6** *(bônus)* | Mudança de rodada |

Descobrir como cada frente se manifesta — e contorná-la — faz parte do desafio.

> ⚠️ Nem toda interação na tela é segura: certas armadilhas aplicam **penalidade** se você cair nelas.

## Pontuação

`score = (itens corretos × pontosPorItemCorreto) − (itens incorretos × penalidadePorItemIncorreto) − penalidade_de_tempo − penalidade_honeypot + bônus_de_níveis`

> O score **nunca fica negativo**: se as penalidades passarem dos pontos, o placar mostra `0`.

- **Itens:** cada par `{chave, valor}` correto soma pontos; item errado desconta.
- **Tempo:** penalidade **linear por minuto** desde a **largada da sua equipe** (o relógio começa no seu **primeiro login bem-sucedido** no site-alvo), com teto.
- **Bônus de níveis:** **N5** é creditado ao extrair corretamente as notas que só existem atrás da navegação difícil — que **também somam como itens**; **N6** ao entregar um resultado correto após uma reorganização de rodada.
- **Honeypot:** penalidade fixa se sua equipe cair na armadilha.
- **Desempate:** maior score; havendo empate, menor tempo (submissão mais cedo).

## Fonte da verdade dos dados

O gabarito de cada equipe é gerado deterministicamente a partir do seu `(teamToken, round)` pelo **mesmo** módulo que alimenta o site e o corretor. Ou seja: o que você vê no portal é exatamente o que o corretor espera. Nada de gabarito "de fora".


Descobrir como cada frente se manifesta — e contorná-la — faz parte do desafio.

> ⚠️ Nem toda interação na tela é segura: certas armadilhas aplicam **penalidade** se você cair nelas.

## Pontuação

`score = (itens corretos × pontosPorItemCorreto) − (itens incorretos × penalidadePorItemIncorreto) − penalidade_de_tempo − penalidade_honeypot + bônus_de_níveis`

> O score **nunca fica negativo**: se as penalidades passarem dos pontos, o placar mostra `0`.

- **Itens:** cada par `{chave, valor}` correto soma pontos; item errado desconta.
- **Tempo:** penalidade **linear por minuto** desde a **largada da sua equipe** (o relógio começa no seu **primeiro login bem-sucedido** no site-alvo), com teto.
- **Bônus de níveis:** **N5** é creditado ao extrair corretamente as notas que só existem atrás da navegação difícil — que **também somam como itens**; **N6** ao entregar um resultado correto após uma reorganização de rodada.
- **Honeypot:** penalidade fixa se sua equipe cair na armadilha.
- **Desempate:** maior score; havendo empate, menor tempo (submissão mais cedo).

## Fonte da verdade dos dados

O gabarito de cada equipe é gerado deterministicamente a partir do seu `(teamToken, round)` pelo **mesmo** módulo que alimenta o site e o corretor. Ou seja: o que você vê no portal é exatamente o que o corretor espera. Nada de gabarito "de fora".
penalidades passarem dos pontos, o placar mostra `0`.

- **Itens:** cada par `{chave, valor}` correto soma pontos; item errado desconta.
- **Tempo:** penalidade **linear por minuto** desde a **largada da sua equipe** (o relógio começa no seu **primeiro login bem-sucedido** no site-alvo), com teto.
- **Bônus de níveis:** **N5** é creditado ao extrair corretamente as notas que só existem atrás da navegação difícil — que **também somam como itens**; **N6** ao entregar um resultado correto após uma reorganização de rodada.
- **Honeypot:** penalidade fixa se sua equipe cair na armadilha.
- **Desempate:** maior score; havendo empate, menor tempo (submissão mais cedo).

## Fonte da verdade dos dados

O gabarito de cada equipe é gerado deterministicamente a partir do seu `(teamToken, round)` pelo **mesmo** módulo que alimenta o site e o corretor. Ou seja: o que você vê no portal é exatamente o que o corretor espera. Nada de gabarito "de fora".
a pegadinha), a ser implementada **sem
  IA**, em tempo limitado.
- **Não conseguir explicar/adaptar** o próprio código = **desclassificação**,
  independentemente da pontuação.
- **Uso comprovado de IA** durante o desafio = **desclassificação**.

> A organização pode conduzir o desafio (ou a defesa) em **ambiente controlado**
> (máquinas fornecidas, sem ferramentas de IA), a seu critério.

## Mecânicas anti-automação (níveis)

**N1–N4 são o núcleo obrigatório** — sem lidar com eles você não consegue extrair de forma confiável. **N5–N6 rendem bônus** — e o N5 merece atenção: parte das notas «Autorizada» só aparece depois de vencê-lo, e elas contam como itens normais, então deixá-las de fora custa pontos *além* do bônus.

| Nível | Tema |
|-------|------|
| **N1** | Localização dos elementos |
| **N2** | Tempo de resposta |
| **N3** | Estrutura da página |
| **N4** | Ruído e armadilhas na tela |
| **N5** *(bônus)* | Navegação difícil |
| **N6** *(bônus)* | Mudança de rodada |

Descobrir como cada frente se manifesta — e contorná-la — faz parte do desafio.

> ⚠️ Nem toda interação na tela é segura: certas armadilhas aplicam **penalidade** se você cair nelas.

## Pontuação

`score = (itens corretos × pontosPorItemCorreto) − (itens incorretos × penalidadePorItemIncorreto) − penalidade_de_tempo − penalidade_honeypot + bônus_de_níveis`

> O score **nunca fica negativo**: se as penalidades passarem dos pontos, o placar mostra `0`.

- **Itens:** cada par `{chave, valor}` correto soma pontos; item errado desconta.
- **Tempo:** penalidade **linear por minuto** desde a **largada da sua equipe** (o relógio começa no seu **primeiro login bem-sucedido** no site-alvo), com teto.
- **Bônus de níveis:** **N5** é creditado ao extrair corretamente as notas que só existem atrás da navegação difícil — que **também somam como itens**; **N6** ao entregar um resultado correto após uma reorganização de rodada.
- **Honeypot:** penalidade fixa se sua equipe cair na armadilha.
- **Desempate:** maior score; havendo empate, menor tempo (submissão mais cedo).

## Fonte da verdade dos dados

O gabarito de cada equipe é gerado deterministicamente a partir do seu `(teamToken, round)` pelo **mesmo** módulo que alimenta o site e o corretor. Ou seja: o que você vê no portal é exatamente o que o corretor espera. Nada de gabarito "de fora".


`score = (itens corretos × pontosPorItemCorreto) − (itens incorretos × penalidadePorItemIncorreto) − penalidade_de_tempo − penalidade_honeypot + bônus_de_níveis`

> O score **nunca fica negativo**: se as penalidades passarem dos pontos, o placar mostra `0`.

- **Itens:** cada par `{chave, valor}` correto soma pontos; item errado desconta.
- **Tempo:** penalidade **linear por minuto** desde a **largada da sua equipe** (o relógio começa no seu **primeiro login bem-sucedido** no site-alvo), com teto.
- **Bônus de níveis:** **N5** é creditado ao extrair corretamente as notas que só existem atrás da navegação difícil — que **também somam como itens**; **N6** ao entregar um resultado correto após uma reorganização de rodada.
- **Honeypot:** penalidade fixa se sua equipe cair na armadilha.
- **Desempate:** maior score; havendo empate, menor tempo (submissão mais cedo).

## Fonte da verdade dos dados

O gabarito de cada equipe é gerado deterministicamente a partir do seu `(teamToken, round)` pelo **mesmo** módulo que alimenta o site e o corretor. Ou seja: o que você vê no portal é exatamente o que o corretor espera. Nada de gabarito "de fora".

  "teamToken": "SEU-TOKEN",
  "itens": [
    { "chave": "0000...44 dígitos", "valor": 1234.56 },
    { "chave": "1111...44 dígitos", "valor": 987.00 }
  ]
}
```

- `teamToken` é entregue no **credenciamento** e identifica sua equipe (sem ele, não há submissão).
- `valor` pode ir como número (`1234.56`) ou string no formato brasileiro (`"1.234,56"`) — o servidor normaliza.
- **Importante:** a resposta **não diz quais itens você acertou** — só confirma o recebimento e sua posição no placar. Isso é de propósito: o `/api/submit` não é um oráculo pra você adivinhar o gabarito.

O **kit do participante** traz o contrato completo do endpoint e os dados de acesso. Não há bot de exemplo — construir a automação do zero é o desafio.

## Regras

- **Selenium é obrigatório.** Linguagem **livre** (diferencial para **C#**).
- Você roda o Selenium na **sua própria máquina**, contra o site hospedado. **A SIEG não executa o seu código** — só valida o payload que você envia.
- Submissões são **limitadas a 10 tentativas**, com **30 segundos de cooldown** entre elas. Vale sempre o **seu melhor score**.
- Equipes de 3–4 pessoas. Duração: **4 horas**.
- **Sem ferramentas de IA.** É **proibido** usar assistentes de IA (ChatGPT, GitHub Copilot, Cursor, Claude e afins) para **gerar, completar ou depurar** o código durante o desafio. Consultar a **documentação oficial** (da linguagem, do Selenium) e fóruns é permitido. O objetivo é avaliar a **habilidade do time** — não a de operar uma IA.

## Verificação de habilidade (banca)

O placar decide o ranking; a **banca** decide o pódio. Antes da premiação, os
times mais bem colocados passam por uma **defesa técnica**:

- **Explicar o próprio código** — qualquer integrante deve conseguir percorrer a
  solução e justificar as decisões.
- **Adaptar ao vivo** — a banca pede **uma alteração na hora** (ex.: extrair
  também um novo campo, lidar com uma nova pegadinha), a ser implementada **sem
  IA**, em tempo limitado.
- **Não conseguir explicar/adaptar** o próprio código = **desclassificação**,
  independentemente da pontuação.
- **Uso comprovado de IA** durante o desafio = **desclassificação**.

> A organização pode conduzir o desafio (ou a defesa) em **ambiente controlado**
> (máquinas fornecidas, sem ferramentas de IA), a seu critério.

## Mecânicas anti-automação (níveis)

**N1–N4 são o núcleo obrigatório** — sem lidar com eles você não consegue extrair de forma confiável. **N5–N6 rendem bônus** — e o N5 merece atenção: parte das notas «Autorizada» só aparece depois de vencê-lo, e elas contam como itens normais, então deixá-las de fora custa pontos *além* do bônus.

| Nível | Tema |
|-------|------|
| **N1** | Localização dos elementos |
| **N2** | Tempo de resposta |
| **N3** | Estrutura da página |
| **N4** | Ruído e armadilhas na tela |
| **N5** *(bônus)* | Navegação difícil |
| **N6** *(bônus)* | Mudança de rodada |

Descobrir como cada frente se manifesta — e contorná-la — faz parte do desafio.

> ⚠️ Nem toda interação na tela é segura: certas armadilhas aplicam **penalidade** se você cair nelas.

## Pontuação

`score = (itens corretos × pontosPorItemCorreto) − (itens incorretos × penalidadePorItemIncorreto) − penalidade_de_tempo − penalidade_honeypot + bônus_de_níveis`

> O score **nunca fica negativo**: se as penalidades passarem dos pontos, o placar mostra `0`.

- **Itens:** cada par `{chave, valor}` correto soma pontos; item errado desconta.
- **Tempo:** penalidade **linear por minuto** desde a **largada da sua equipe** (o relógio começa no seu **primeiro login bem-sucedido** no site-alvo), com teto.
- **Bônus de níveis:** **N5** é creditado ao extrair corretamente as notas que só existem atrás da navegação difícil — que **também somam como itens**; **N6** ao entregar um resultado correto após uma reorganização de rodada.
- **Honeypot:** penalidade fixa se sua equipe cair na armadilha.
- **Desempate:** maior score; havendo empate, menor tempo (submissão mais cedo).

## Fonte da verdade dos dados

O gabarito de cada equipe é gerado deterministicamente a partir do seu `(teamToken, round)` pelo **mesmo** módulo que alimenta o site e o corretor. Ou seja: o que você vê no portal é exatamente o que o corretor espera. Nada de gabarito "de fora".
