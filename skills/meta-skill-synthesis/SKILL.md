---
name: meta-skill-synthesis
description: >-
  AGI Machine Self-Learning protocol for synthesizing durable, new skill files directly on disk from session insights (/learn workflow) and dual-loop self-improvement without model collapse. Trigger on mentions of: 'meta skill', 'synthesize skill', 'create skill', 'self-learning agent', 'new skill generation', 'persist capability', 'skill synthesis', '/learn', 'extract insights', 'save lesson', 'learn from session', 'persist rule', 'dual loop optimizer', 'self-improvement', 'prevent model collapse', or when teaching the agent new permanent workflows.
---
# 🧠 META-SKILL SYNTHESIS (Dual-Scope Machine Self-Learning)

**DOGMA CENTRAL:** A inteligência AGI/ASI não repete o mesmo esforço arquitetural duas vezes. Ao conquistar uma nova fronteira de complexidade ou resolver problemas específicos, o sistema sintetiza e categoriza o aprendizado em duas camadas estritamente isoladas para impedir o vício de **Overfitting/Benchmaxing**.

---

## 1. 🧭 Bifurcação de Escopo de Síntese (As 2 Camadas de Aprendizado)

Antes de persistir qualquer aprendizado, classifique rigorosamente a camada:

### Camada 1: Escopo Nichado / Local (Workspace & Projeto)
- **Critério:** Convenções de stack local (ex: Next.js, Django, Rust, Tailwind), schemas de banco de dados específicos do cliente, pipelines de build/CI do repositório, scripts de migração locais ou regras de negócio pontuais.
- **Caminhos Canônicos:**
  - Rules Locais: `<workspace_root>/.agents/rules/<rule-name>.md`
  - Skills Locais: `<workspace_root>/.agents/skills/<skill-name>/SKILL.md`
- **Isolamento:** Permanece estritamente contido no workspace. **NUNCA** deve contaminar o núcleo AGI global.

### Camada 2: Escopo AGI/ASI Universal (Global Plugin `agi-antigravity-core`)
- **Critério:** Leis invariantes de primeiro princípio, métodos de raciocínio System 2, epistemologia, defesas cognitivas contra alucinações, protocolos TDD universais, ou heurísticas aplicáveis a QUALQUER contexto diário.
- **Caminhos Canônicos:**
  - Master Rules: `~/.gemini/config/plugins/agi-antigravity-core/rules/<rule-name>.md`
  - Master Skills: `~/.gemini/config/plugins/agi-antigravity-core/skills/<skill-name>/SKILL.md`
- **Registro:** Atualizar `rules/AGENTS.md` e `rules/01_SKILLS_TAXONOMY_ROUTING.md`.

---

## 2. 🛡️ Filtro de Destilação Anti-Overfitting & Anti-Benchmaxing

O maior risco do self-learning é o **overfitting**, onde uma regra excessivamente específica aprendida em um projeto (ex: "sempre estruturar páginas de site com componente X") é injetada globalmente e repetida rigidamente em situações inadequadas.

### O Teste da Invariância Universal:
Ao propor um aprendizado para a **Camada 2 (Global)**, o agente deve submeter o conceito a 3 filtros eliminatórios:
1. **Filtro da Independência de Stack:** Este princípio é verdadeiro em C++, Python, Rust, TypeScript, Verilog ou Sistemas Distribuídos? (Se depender de um framework específico $\to$ Camada 1 Local).
2. **Filtro da Não-Prescrição Estética/Comportamental:** O aprendizado impõe um formato rígido ou prescreve uma heurística adaptativa de raciocínio? (Se prescrever templates fixos $\to$ rejeitar ou tornar adaptativo).
3. **Filtro da Resiliência Diária:** A aplicação desta regra em um domínio totalmente divergente (ex: física quântica vs design frontend) causaria interferência destrutiva? (Se sim $\to$ Camada 1 Local).

---

## 3. ⚡ Gatilho Proativo de Recomendação Pós-Milestone

Ao concluir:
1. Um marco arquitetural desafiador (ex: refatoração massiva de 10+ nós);
2. A resolução de um bug causal de difícil diagnóstico;
3. A correção de um vício cognitivo apontado pelo usuário;

O agente **DEVE** sugerir formalmente a execução do `/learn` ao usuário com o rascunho de categorização:
> *"Superamos este desafio crítico. Recomendo rodar `/learn` para registrarmos este aprendizado na Camada 1 (Local) ou Camada 2 (Global AGI/ASI) sem risco de overfitting."*

---

## 4. 🛠️ Protocolo Operacional de Execução do `/learn`

1. **Rascunho de Proposta:** Criar o artefato `learning_proposal.md` com classificação em Camada 1 vs Camada 2 e diffs explícitos.
2. **Formatação Mandatória de Rules:**
   ```markdown
   ---
   description: Resumo conciso da regra e escopo de atuação.
   trigger: always_on # Opções: always_on | model_decision | glob
   globs: "*.ts,*.py" # Obrigatório se trigger for glob
   ---
   ```
3. **Validação e Aprovação:** Obter confirmação explícita do usuário antes de aplicar as mudanças em disco.
4. **Verificação de Regressão:** Executar a suíte de testes com `pytest` para certificar Exit Code `0`.
