# tema: k = verdade crua (preto) | y = comédia (amarelo) | w = coach/guru (branco)
# formato: ("frase", texto) ou ("dialogo", rotulo1, fala1, rotulo2, fala2)
# *palavra* = marca-texto | kicker = chamada de impacto (só nas frases de impacto)

K = [
 ("LEIA COM ATENÇÃO.", ("frase", "O mercado não parou.\n\n*Você* parou.")),
 ("REPITA ISSO.",      ("frase", "Ninguém compra imóvel pelo seu reels.\n\nCompra porque você *atendeu*.")),
 ("LEIA DE NOVO.",     ("frase", "Seu cliente não sumiu.\n\nComprou com quem *respondeu primeiro*.")),
 ("ANOTA.",            ("frase", "Imóvel no preço vende sozinho.\n\nO resto é *desculpa*.")),
 ("SEM FILTRO.",       ("frase", "Não sabe ler matrícula?\n\nVocê não é corretor.\nÉ *guia turístico*.")),
 ("LEIA COM ATENÇÃO.", ("frase", "Comissão não é salário.\n\nÉ *indenização*.")),
 ("MANDA PRO GRUPO.",  ("frase", "Posta “mais uma família realizada” toda semana.\n\nA *própria* ele não vê há meses.")),
 ("REPITA ISSO.",      ("frase", "Proprietário que recusa toda proposta não quer vender.\n\nQuer saber *quanto vale*.")),
 ("PRINTA.",           ("frase", "Dois anos de placa na frente não é exclusividade.\n\nÉ *imóvel caro*.")),
 ("SEM FILTRO.",       ("frase", "Corretor sem carteira não é autônomo.\n\nÉ *desempregado com CRECI*.")),
 ("LEIA DE NOVO.",     ("frase", "Ninguém te deve exclusividade.\n\nVocê deve *resultado*.")),
 ("MANDA PRO DONO.",   ("frase", "Imobiliária que cobra mensalidade do corretor\n\né *coworking com meta*.")),
 ("ANOTA.",            ("frase", "Dez visitas pra fechar?\n\nIsso não é cliente.\nÉ *plateia*.")),
 ("LEIA COM ATENÇÃO.", ("frase", "Desconto oferecido antes do pedido\n\nsai de um lugar só:\n*a sua comissão*.")),
 ("REPITA ISSO.",      ("frase", "Quem não fala de dinheiro na primeira conversa\n\ntrabalha *de graça* na última.")),
 ("SEM FILTRO.",       ("frase", "Lead não é cliente.\n\nÉ *curioso com WhatsApp*.")),
 ("PRINTA.",           ("frase", "Tabela nova toda semana não é estratégia.\n\nÉ *desespero*.")),
 ("ANOTA.",            ("frase", "Vender pra amigo:\n\ntrabalha de graça\ne *perde o amigo*.")),
 ("REPITA ISSO.",      ("frase", "Comissão não enriquece ninguém.\n\nEnriquece quem *reinveste*.")),
 ("LEIA DE NOVO.",     ("frase", "Proposta sem assinatura é conversa.\n\nConversa *não paga boleto*.")),
 ("SEM FILTRO.",       ("frase", "Imóvel bom não precisa de “URGENTE” no anúncio.\n\n*Corretor bom também não.*")),
]

Y = [
 (None, ("dialogo", "O CLIENTE DIZ", "“Vou pensar e te dou um retorno.”", "TRADUÇÃO", "Já comprou. Com o primo.\n*Usando a sua planta.*")),
 (None, ("frase", "Corretor não tem chefe.\n\nTem 47 clientes.\nTodos se acham *o chefe*.")),
 (None, ("dialogo", "O CLIENTE DIZ", "“Só quero dar uma olhadinha.”", "TRADUÇÃO", "Tchau, *sábado*.")),
 (None, ("frase", "Domingo, 23h47.\n“Ainda tá disponível?”\n\nNão. Faz quatro meses.\n*Mandei onze mensagens.*")),
 (None, ("dialogo", "O CLIENTE DIZ", "“Faz um precinho que eu fecho hoje.”", "TRADUÇÃO", "Não fecho.\nE o proprietário agora *acha que você é fraco*.")),
 (None, ("frase", "Todo cliente quer oportunidade.\n\n*Nenhum quer pagar por uma.*")),
 (None, ("dialogo", "O CLIENTE DIZ", "“Meu marido precisa ver também.”", "TRADUÇÃO", "Mais quatro visitas.\nNo fim ele acha *a sala pequena*.")),
 (None, ("frase", "1 ano de mercado: “Vou ficar rico.”\n5 anos: “Vou ficar.”\n15 anos: “*Vou.*”")),
 (None, ("dialogo", "O CLIENTE DIZ", "“Dinheiro não é problema.”", "TRADUÇÃO", "O problema é *não ter*.")),
 (None, ("frase", "Plantão de sábado.\n8 horas. 1 visita.\n\nEra o vizinho.\nProcurando *um corretor bom*.")),
 (None, ("frase", "Cliente de 15 milhões\npede desconto de 3 mil\n*na escritura*.")),
 (None, ("dialogo", "EXPECTATIVA", "Especialista em alto padrão.", "REALIDADE", "Mostra cobertura de 20 milhões.\n*Chega de Uber.*")),
 (None, ("frase", "Vista mar no alto padrão:\n\nabre a janela do banheiro,\nsobe na privada,\n*inclina 45 graus*.")),
 (None, ("dialogo", "EXPECTATIVA", "Exclusividade assinada.", "REALIDADE", "Na OLX. Com a placa do vizinho.\n*E mais três corretores.*")),
 (None, ("frase", "Comissão: 6%.\nDesgaste: 100%.\nPaciência: *negativa*.")),
 (None, ("frase", "Sexta, 18h.\nO mundo indo pro happy hour.\n\nVocê mostrando apê pra quem\n*“só quer conhecer”*.")),
]

W = [
 (None, ("dialogo", "O GURU DIZ", "“Mentalidade de abundância.”", "NA PRÁTICA", "*Em 12x no cartão.*")),
 (None, ("frase", "Ele te ensina a vender um imóvel por semana.\n\nEle vende *um curso por minuto*.")),
 (None, ("dialogo", "O GURU DIZ", "“Acorde às 5h.”", "NA PRÁTICA", "O cliente *acorda às 11*.")),
 (None, ("dialogo", "O GURU DIZ", "“Vendi 100 milhões em VGV.”", "NA PRÁTICA", "Na planilha. Do lançamento.\n*Que não saiu.*")),
 (None, ("frase", "Todo guru tem um método.\n\nNenhum mostra *a escritura*.")),
 (None, ("dialogo", "O GURU DIZ", "“Seja dono do seu tempo.”", "NA PRÁTICA", "Seja dono de *um link de checkout*.")),
 (None, ("frase", "Imersão de três dias com o maior corretor do Brasil.\n\nVoltei com caderno, camiseta\ne o *mesmo cliente que não responde*.")),
]

# novas (entram no fim da fila, sem mexer na numeração anterior)
EXTRA = [
 ("k", "SEM FILTRO.", ("frase", "Hackeiam o banco.\nHackeiam a Microsoft.\nHackeiam a sua cripto.\n\nTerreno ninguém hackeia.\n*No máximo, invadem.*")),
 ("k", "LEIA COM ATENÇÃO.", ("frase", "Hackeiam o banco.\nHackeiam o Google.\nHackeiam a sua cripto.\n\nImóvel ninguém hackeia.\nSó o cunhado.\n*No inventário.*")),
]

# lote 2 (20/11): patrimônio (p, preto), palavra de quem sabe (q, preto, citação), IA & Instagram (w, branco)
EXTRA2 = [
 ("p", "LEIA COM ATENÇÃO.", ("frase", "A bolsa cai.\nO banco quebra.\nA cripto some.\n\nEscritura registrada na gaveta\n*ninguém tira*.")),
 ("p", "ANOTA.", ("frase", "Escritura sem registro é papel.\n\n*Quem não registra não é dono.*")),
 ("p", "REPITA ISSO.", ("frase", "Dinheiro parado perde para a inflação.\n\n*Em silêncio. Todo mês.*")),
 ("p", "SEM FILTRO.", ("frase", "Juro alto assusta o comprador.\n\nE faz o vendedor *aceitar a proposta*.")),
 ("p", "LEIA DE NOVO.", ("frase", "Crise não acaba com patrimônio.\n\nAcaba com *quem estava alavancado*.")),
 ("p", "PRINTA.", ("frase", "Quem compra na euforia paga o pico.\n\nQuem compra no medo *escolhe o lote*.")),
 ("q", "PALAVRA DE QUEM SABE.", ("citacao", "“Seja medroso quando os outros forem gananciosos, e ganancioso quando os outros tiverem medo.”", "WARREN BUFFETT", "CARTA AOS ACIONISTAS DA BERKSHIRE, 1986", "O terreno bom aparece quando todo mundo está *com medo da eleição*.")),
 ("q", "PALAVRA DE QUEM SABE.", ("citacao", "“Preço é o que você paga. Valor é o que você leva.”", "WARREN BUFFETT", "CARTA AOS ACIONISTAS DA BERKSHIRE, 2008", "O cliente que pede desconto *nunca perguntou do valor*.")),
 ("q", "PALAVRA DE QUEM SABE.", ("citacao", "“Só quando a maré baixa você descobre quem estava nadando pelado.”", "WARREN BUFFETT", "CARTA AOS ACIONISTAS DA BERKSHIRE, 2001", "O juro sobe e aparece quem comprou dez na planta *sem caixa pra uma*.")),
 ("q", "PALAVRA DE QUEM SABE.", ("citacao", "“O dinheiro grande não está em comprar e vender. Está em esperar.”", "CHARLIE MUNGER", "SÓCIO DE WARREN BUFFETT NA BERKSHIRE", "Terreno é para quem sabe esperar. E *não precisa vender amanhã*.")),
 ("q", "PALAVRA DE QUEM SABE.", ("citacao", "“Inflação é imposto sem lei.”", "MILTON FRIEDMAN", "ECONOMISTA, NOBEL DE 1976", "Dinheiro parado paga esse imposto *todo mês, sem ver*.")),
 ("q", "PALAVRA DE QUEM SABE.", ("citacao", "“Compre terra. Eles não fabricam mais.”", "ATRIBUÍDA A MARK TWAIN", "NINGUÉM NUNCA ACHOU ONDE ELE DISSE ISSO", "Mas também *ninguém provou que está errado*.")),
 ("w", None, ("frase", "Corretor especialista em IA:\n\nusa o ChatGPT pra escrever\n*“oportunidade imperdível”*.")),
 ("w", None, ("frase", "Fez curso de IA no fim de semana.\n\nAinda não sabe *calcular o ITBI*.")),
 ("w", None, ("frase", "40 mil seguidores.\n\n*Nenhuma escritura.*")),
 ("w", None, ("dialogo", "O GURU DIZ", "“A IA vai substituir o corretor.”", "NA PRÁTICA", "Só o que *não sabe ler matrícula*.")),
 ("w", None, ("frase", "Reels com drone, trilha épica e frase motivacional.\n\nA metragem do imóvel? *Ninguém sabe.*")),
 ("w", None, ("dialogo", "O GURU DIZ", "“Seja especialista em Instagram.”", "NA PRÁTICA", "Seja especialista *em fechar*.")),
]

# 20/11: o branco deixou de ser "guru" e virou MODINHA (tom seco, sem "O GURU DIZ")
MODINHA = {
 4:  ("frase", "Todo corretor tem um podcast.\n\nNenhum tem *uma carteira de clientes*."),
 11: ("frase", "Curso de 997 reais pra aprender a vender imóvel.\n\nQuem vende de verdade *não tem tempo de gravar curso*."),
 18: ("frase", "Acordar às 5h não fecha negócio.\n\n*Atender às 22h fecha.*"),
 25: ("frase", "VGV no stories.\n\n*Escritura em lugar nenhum.*"),
 32: ("frase", "Mentoria de corretor com dois anos de mercado.\n\nO mentor *ainda está aprendendo*."),
 39: ("frase", "Mentalidade de dono não paga boleto.\n\n*Comissão paga.*"),
 43: ("frase", "Imersão, mentoria, masterclass.\n\nO cliente continua *sem responder*."),
 59: ("frase", "Corretor especialista em IA:\n\nusa o ChatGPT pra escrever\n*“oportunidade imperdível”*."),
 60: ("frase", "Fez curso de IA no fim de semana.\n\nAinda não sabe *calcular o ITBI*."),
 61: ("frase", "40 mil seguidores.\n\n*Nenhuma escritura.*"),
 62: ("frase", "A IA não vai substituir o corretor.\n\nVai substituir *o que só manda PDF*."),
 63: ("frase", "Reels com drone, trilha épica e frase motivacional.\n\nA metragem do imóvel? *Ninguém sabe.*"),
 64: ("frase", "Especialista em Instagram não é profissão.\n\n*Fechar negócio é.*"),
}

# 20/11 (feriado): posts para hoje
EXTRA3 = [
 ("y", None, ("frase", "Feriado.\n\nTodo mundo descansando.\nO corretor respondendo\n*“ainda tá disponível?”*.")),
 ("k", "ANOTA.", ("frase", "O cliente pesquisa imóvel no feriado.\n\nQuem responde no feriado\n*leva a venda*.")),
 ("y", None, ("frase", "Feriado prolongado:\n\nquatro dias de visita.\n*Zero proposta.*")),
]

# prints do Nelson (adaptados)
EXTRA4 = [
 ("w", None, ("frase", "O influencer diz que imóvel é o pior investimento do Brasil.\n\nGravou o vídeo\n*no apartamento quitado dele*.")),
 ("k", "SEM FILTRO.", ("frase", "Manda você dolarizar tudo e sair do país.\n\nEle mesmo\n*comprou terreno na praia*.")),
]
