# BovespaTools

Scripts para aquisição de dados da Bolsa de Valores de São Paulo (BM&amp;fBovespa)

### Pré-requisitos:

BovespaTools atualmente depende de **Python 3.x** e suas seguintes bibliotecas: **scipy**, **numpy** e **selenium**.

### Plataformas testadas:

As seguintes plataformas foram testadas:

Plataforma | Resultado
---------- | ---------
Windows 10 + Python 3.4 | OK

### Configuração:

A biblioteca Selenium, responsável pela conexão com o navegador, está configurada para utilizar o navegador *Firefox*. Caso outro navegador queira ser utilizado, scripts devem ter a seguinte linha:

    driver = webdriver.Firefox()

Modificada para `driver = webdriver.Chrome()`, `driver = webdriver.Opera()` ou `driver = webdriver.Ie()`.

### Scripts:

**empresas-lista** - Lista as empresas registradas na BM&amp;fBovespa, fornecendo a *Razão Social*, o *Nome do Pegrão*, o *Segmento* e o *Código CVM* de cada uma.

    ./empresas-lista [--out=<arquivo-de-saida>]
    
`--out=<arquivo-de-saida>` (OPCIONAL) -- Arquivo para impressão da tabela, caso a extensão do arquivo seja `.mat`, a saída gerada será um arquivo *MatLab* formatado como matriz de células. Na ausência do parâmetro, a tabela é impressa na saída padrão.
    
**fii-lista** - Lista os Fundos de Investimento Imobiliário registradas na BM&amp;fBovespa, fornecendo a *Razão Social*, o *Fundo*, o *Segmento* e o *Código* de cada uma.

    ./fii-lista [--out=<arquivo-de-saida>]

`--out=<arquivo-de-saida>` (OPCIONAL) -- Arquivo para impressão da tabela, caso a extensão do arquivo seja `.mat`, a saída gerada será um arquivo *MatLab* formatado como matriz de células. Na ausência do parâmetro, a tabela é impressa na saída padrão.

**empresas-demons** - Coleta as demonstrações financeiras de um período de empresas registradas na BM&amp;fBovespa a partir do *Código CVM*, fornecendo a *Conta*, a *Descrição* e os *Períodos* de cada uma.

    ./empresas-demons --cvm=<trimestre> [--trim=<trimestre>] [--year=<ano>] [--mode=<modo>] [--out=<arquivo-de-saida>]

`--cvm=<trimestre>` (OBRIGATÓRIO) -- *Código CVM* da empresa de interesse.

`--trim=<trimestre>` (OPCIONAL) -- Trimestre de interesse para a coleta dos dados (1, 2, 3 ou 4). **Para o quarto trimestre, os dados serão referentes ao ano inteiro**. Na ausência do parâmetro, é assumido o trimestre anterior baseado na data atual do sistema, ex: 24/10/2015 pertence ao quarto trimestre, então será coletado o terceiro trimestre.

`--year=<ano>` (OPCIONAL) -- Ano de interesse para a coleta dos dados. Na ausência do parâmetro, é assumido o ano que consta na data atual do sistema.

`--mode=<modo>` (OPCIONAL) -- Modo de coleta de dados no formato `ABBB`, onde:
`A=` `i` -- DFs Individuais, `c` -- DFs Consolidadas.
`BBB=` `bpa` -- Balanço Patrimonial Ativo, `bpp` -- Balanço Patrimonial Passivo, `dre` -- Demonstração do Resultado, `dfc` -- Demonstração do Fluxo de Caixa. Na ausência do parâmetro, o *modo* é definido como `idre`.

`--out=<arquivo-de-saida>` (OPCIONAL) -- Arquivo para impressão da tabela, caso a extensão do arquivo seja `.mat`, a saída gerada será um arquivo *MatLab* formatado como matriz de células. Na ausência do parâmetro, a tabela é impressa na saída padrão.
