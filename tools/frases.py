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
