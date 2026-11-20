# Rotina automática do @imoveissemfiltro

Quem roda: uma tarefa programada do Claude, com o computador do Nelson ligado e o app do Claude aberto
(o Instagram fica logado no navegador do app, aba do instagram.com, conta **@imoveissemfiltro**).

## Peças
- **Página de aprovação** (artifact): https://claude.ai/artifact/PW44kp9WSQ7X7B7EnxyvUL
  - banco `posts/nNNN`: `n, seq, bloco, data (AAAA-MM-DD), hora (07:40|12:20|19:10), cat, frase, legenda, alt, status (pendente|aprovado|mudar|tirar), nova_frase, nova_legenda, programado, img, v`
  - imagens publicadas como arquivos `img/nNNN.jpg` do próprio artifact
- **Repositório** nelson17052-hub/Sf-midia: `img/`, `manifest.json`, `kit.json` (fontes+css+mascote), `specs.json` (HTML de cada arte), `send.html`, `tools/`
- **Instagram (IndexedDB `sf` do instagram.com)**: `items` (arte JPEG + legenda + alt por número) e `kv` (`kit`, `specs`).
  Com o kit lá, a arte nova pode ser gerada DENTRO do Instagram com `__itemFromSpec({n, html, legenda, alt, v})`, sem clique do Nelson.

## A cada execução
1. Ler o banco da página (`ArtifactData list posts`).
2. Injetar `tools/ig-helpers.js` na aba do Instagram (javascript_tool). Conferir que a conta logada é @imoveissemfiltro.
3. Para cada post com `status == aprovado`, `programado != true` e data/hora no futuro (pelo menos 30 min à frente):
   - se a arte não está no IndexedDB ou `v` mudou: gerar com `__itemFromSpec` (spec = HTML da seção gerado por `tools/build.py` + `mkstatic.py` + `extract.js`, com o mascote trocado por `%M%`).
   - `__prep(n, data)` → foco em Minutes + tecla real dos dígitos → foco em Hours + tecla real → `__finish(data, hh, mm)`.
   - marcar `programado: true` no banco (com if_version).
4. Para cada post com `status == mudar`: reescrever a frase/legenda pedida (`nova_frase` / `nova_legenda`), regerar a arte no
   container (tools/), publicar a imagem nova no artifact (mesmo caminho `img/nNNN.jpg`), atualizar o doc (`frase`, `legenda`, `alt`, `v+1`,
   `status: pendente`, limpar `nova_*`) e o spec no repo.
5. A rotina roda só em dias úteis, às 14h47 (o PC fica ligado à tarde no escritório). Manter de 10 a 15 dias de posts na fila (3 por dia): se os posts futuros
   (pendentes + aprovados não publicados) cobrirem menos de 10 dias, criar blocos de 9 frases novas até cobrir 15 dias
   (regras abaixo), gerar artes, publicar no artifact + banco (`status: pendente`) e avisar o Nelson.
6. Conferir em instagram.com/scheduled_content/ (`__cards()`) que os posts entraram com legenda. ATENÇÃO: o primeiro post programado
   de cada sessão às vezes fica sem legenda depois de salvo. Abra o card vazio, rode `__setCaption(item.legenda)` + `__setAlt(item.alt)` e clique em Salvar.
7. Avisar o Nelson só quando houver algo para ele: bloco novo para aprovar, ou erro.

## Regras de conteúdo
- Português do Brasil, tom seco, sarcástico, curto. Nada de coach, nada de "O GURU DIZ".
- Cores: preto = verdade crua / patrimônio / palavra de quem sabe (citação real, com fonte); amarelo = comédia (cliente, alto padrão, plantão);
  branco = Modinha (IA, Instagram, cursos, mentoria) no tom seco.
- Por bloco de 9: ~4 pretos, 3 amarelos, 2 brancos. Frases de impacto (preto) levam chamada: LEIA COM ATENÇÃO. / REPITA ISSO. / ANOTA. / PRINTA. / SEM FILTRO. / LEIA DE NOVO.
- Citações só com autoria verificável; se a autoria for duvidosa, dizer isso na arte.
- Nunca prometer rentabilidade, nunca citar empreendimento, cliente ou operação real. Perfil anônimo: nunca citar Nelson, Grupo DOMMA ou empresas dele.
- Legenda: 1 linha ácida + CTA (marca o corretor / manda pro grupo) + `#corretordeimoveis #mercadoimobiliario #corretor #imoveis #semfiltro`.
- No post: Facebook e Threads SEMPRE desligados.

## Notas de 20/11
- O Chrome do Nelson ("NELSON", Claude no Chrome) também tem o @imoveissemfiltro (troca de conta pelo menu Mais → Trocar de perfil, sem senha)
  e o IndexedDB `sf` dele já tem as 66 artes + o kit. No Chrome dá para abrir a janelinha send.html com clique da extensão; o Nelson só precisa
  clicar em "Open the page" no aviso do githack. No Chrome o "Programar" demora: clicar e depois esperar a confirmação em chamadas separadas (limite de 45 s por chamada).
- O Instagram recusou programar além de ~45 posts na fila ("Não foi possível programar o post"). Programe o que couber e deixe o resto para os dias seguintes,
  conforme os posts forem saindo.
