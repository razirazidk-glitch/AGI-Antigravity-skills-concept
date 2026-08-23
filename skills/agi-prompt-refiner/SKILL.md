---
name: agi-prompt-refiner
description: >-
  MANDATORY when user input is brief (<= 200 chars), ambiguous, or missing enterprise constraints. Elevates naive requests into enterprise AGI specifications. Trigger on mentions of: 'refine prompt', 'improve prompt', 'format prompt', 'enhance requirement', 'AGI prompt', or whenever user input lacks explicit invariants, failure recovery, or verification criteria.
---
# AGI Prompt Refiner

## Core Directive
When the user asks you to "improve a prompt", "format a message", or "create an AGI level prompt" based on a simple input, you must act as a meta-prompt engineer. Do not execute the prompt's request; instead, analyze the user's intent, deconstruct the problem, and output a highly rigorous, theoretically grounded prompt that can be copy-pasted or executed later.

## 1. Deconstruction Phase
Analyze the user's brief input to extract:
- **Core Intent:** What is the actual goal?
- **Implicit Assumptions:** What is the user assuming without saying?
- **Missing Context:** What dependencies or parameters are missing?
- **Boundary Conditions:** What are the safety, architectural, or zero-trust constraints required for this task?

## 2. AGI/ASI Formulation Rules
When formatting the new prompt, it must adhere to the global AGI/ASI Neural Sector rigor:
- **Anti-Hallucination & Zero-Preconception Invariant:** The refiner is STRICTLY PROHIBITED from inventing theoretical models, exotic frameworks (e.g., Schrödinger operators, LBM, unverified libraries), or diagnosing specific components ("apontar pro pneu") unless explicitly cited in the user's prompt or proven on disk.
- **Agnostic Bottom-Up Archaeology Mandate:** For audits, codebase investigations, or large-scale refactoring, instruct the agent to execute a 1:1 node disassembly ($\forall v \in \mathcal{V}$) and map raw data lineage before dispatching adversarial tribunals.
- **Zero-Trust Falsification:** Instruct the executing agent to verify all assumptions before proceeding.
- **Topological & Graph Mapping:** If the task involves code or architecture, instruct the agent to build an Abstract Syntax Tree (AST) or Directed Acyclic Graph (DAG) mental model.
- **Information-Theoretic Constraints:** Instruct the agent to minimize Shannon Entropy (uncertainty) and maximize explicit evidence (Citations/Pointers).
- **Format:** Use markdown code blocks (` ```markdown `) to encapsulate the final refined prompt so the user can easily copy it.

## 3. Official Slash Command Recommendation Engine
When refining a prompt or interacting with the user, evaluate the scope and **proactively recommend the appropriate official slash command**:

| Task Complexity / Scope | Recommended Slash Command | How to Recommend |
|---|---|---|
| **Multi-step project, app, game, deep build, refactor** | `/goal` | Prefix prompt with `/goal` and explain that it enables continuous, uninterrupted execution loops until 100% completion. |
| **Ambiguous design choices / interactive alignment** | `/grill-me` | Suggest using `/grill-me` to conduct an interactive interview before execution. |
| **Web search, web app testing, live scraping** | `/browser` | Suggest using `/browser` to delegate web browsing actions. |
| **Large parallel project / multi-agent swarm** | `/teamwork-preview` | Suggest using `/teamwork-preview` for collaborative agent teams. |
| **Workflow / pattern crystallization** | `/learn` | Suggest using `/learn` to persist discovered workflows into permanent skills. |

---

## 4. The Output Template
Present the result to the user in the following structure:

1. **Brief Analysis:** Explain *why* you added certain constraints, what was missing, and how the prompt enforces agnostic bottom-up discovery.
2. **Recommended Slash Command:** State clearly which slash command is best suited for this execution (e.g., `/goal`).
3. **The Refined Prompt:** Provide the exact text inside a markdown code block starting with the recommended slash command if applicable (e.g., `/goal ...`).

### Example Refined Prompt Structure (Deep Audit & Archaeology)
```markdown
/goal INICIAR EXCAVAÇÃO ARQUEOLÓGICA FORENSE E AUDITORIA 1:1 DE BAIXO PARA CIMA DO PROJETO [NOME].

### 🚫 1. LEI DO AGNOSTICISMO & ZERO-PRECONCEPÇÃO
- Proibido formular hipóteses prematuras ou isolar um único componente antes de mapear 100% da árvore de arquivos.
- Proibido inventar tecnologias não verificadas; todo diagnóstico deve nascer da evidência material coletada nó a nó.

### 🛠️ 2. FASE 1: DESMONTAGEM MECÂNICA & INVENTÁRIO 1:1 (∀v ∈ V)
1. **Catalogação por Nó:** Caminho, LOC, dependências de entrada, interfaces exportadas e mutabilidade.
2. **Eliminação de Código Morto:** Análise de alcance no AST para purgar arquivos órfãos e lógicas zumbis.
3. **Grafo de Linhagem de Dados:** Rastreamento exato: Ingestão de Dados -> Transformadores -> Consumidores -> Sinks.

### 🔬 3. FASE 2: FORENSE DE ANOMALIAS MATERIAIS
1. **Paridade Empírica:** Auditar divergências entre simulação/backtest e runtime de produção/live.
2. **Calibração de Thresholds:** Identificar filtros excessivamente restritivos que bloqueiam sinais válidos.
3. **Persistência & Telemetria:** Projetar/implementar banco de dados ACID/WAL e observabilidade estruturada nó a nó.

### 🔴🔵 4. FASE 3: TRIBUNAL ADVERSARIAL VIA SUBAGENTES (C_max <= 2)
Despachar Red Team e Blue Team operando exclusivamente sobre os nós anômalos identificados na Fase 1.

### 📦 5. ENTREGÁVEIS OBRIGATÓRIOS
1. PROJECT_BRAIN.md (Topologia viva e mapa causal de 100% dos nós).
2. AUDIT_REPORT.md (Laudo forense das patologias eliminadas).
3. ARCHITECTURE.md & CONTRACTS.md (Especificação institucional e contratos tipados).
4. Suíte de Testes Automatizados (100% green, exit code 0).
```



