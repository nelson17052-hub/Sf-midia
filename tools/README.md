# Ferramentas do @imoveissemfiltro

- `frases.py`: banco de frases (K = verdade crua/preto, Y = comédia/amarelo, W = coach & guru/branco, EXTRA = novas no fim da fila). `*palavra*` = marca-texto.
- `legendas.py`: legendas por número + CTAs + hashtags.
- `build.py` gera `artes.html` e `ordem.txt`; `shot.js` tira os PNG 1080x1350 (Playwright).
- Fontes: Fraunces (fontsource-variable) + JetBrains Mono (`npm i @fontsource-variable/fraunces @fontsource/jetbrains-mono`).
- Saída para o Instagram: `img/nNNN.jpg` + `manifest.json` (ordem de postagem, legenda, alt, v).
- `send.html` (servido por raw.githack.com) fica aberto como popup do Instagram e envia as artes via postMessage para o IndexedDB `sf` do instagram.com.
- Página de aprovação (artifact do Claude) guarda status por post: pendente / aprovado / mudar / tirar.
- Horários: 07:40, 12:20, 19:10. Facebook e Threads sempre desligados no post.
