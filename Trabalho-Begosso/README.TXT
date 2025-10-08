1) Operações básicas :white_check_mark:
1.1) Inclusão de novos registros nas tabelas. :white_check_mark:
1.2) Consulta de registros das tabelas. :white_check_mark:
1.3) Exclusão de registros das tabelas. :white_check_mark:
1.4) Leitura exaustiva das tabelas. :white_check_mark:
A busca, inclusão e exclusão devem ser realizadas utilizando o índice em árvore binária.

2) Ao exibir um aluno na tabela Alunos, o programa deverá buscar o código do curso na tabela de Cursos e exibir a Descrição. :white_check_mark:
2.1) Buscar o código da cidade na tabela de Cidades e exibir a Descrição e o Estado. :white_check_mark:

3) Ao exibir um autor na tabela Autores, o programa deverá buscar o código da cidade na tabela de Cidades e exibir o nome da cidade e o Estado.

4) Ao incluir ou consultar dados na Tabela Livros, o programa deverá:
4.1) Buscar o código do autor na tabela Autores e exibir o nome do autor e o nome e estado de sua cidade.
4.2) Buscar o código da categoria na tabela Categorias e exibir a descrição da categoria.
4.3) O atributo disponibilidade serve para indicar se o livro está disponível para empréstimo ou se já está emprestado.

5) Ao incluir ou consultar dados na Tabela Empréstimos, o programa deverá:
5.1) Solicitar o código do livro e verificar na tabela Livros se o mesmo encontra-se disponível para empréstimo. Se não estiver disponível, emitir uma mensagem e não solicitar os demais dados.
5.2) Exibir o nome do livro e o nome da categoria.
5.3) Buscar o código do aluno na tabela Alunos e exibir seu nome e o nome de sua cidade. :white_check_mark:
5.4) A data do empréstimo deverá ser a data do dia atual e a data de devolução deverá ser 7 dias além da data atual.
5.5) Após a confirmação do empréstimo, marcar a disponibilidade do livro como "emprestado" e o atributo devolvido como "Não".

6) Permitir a realização da devolução do livro:
6.1) Verificar na tabela de empréstimos se o livro encontra-se dentro do prazo de devolução. Se estiver atrasado, exibir uma mensagem.
6.2) Após a confirmação da devolução, marcar a disponibilidade do livro como "disponível" e marcar o atributo devolvido como "Sim".

7) Permitir as seguintes consultas:
7.1) Livros que estão emprestado 
7.2) Livros que estão com a devolução atrasada 
7.3) Quantidade de livros emprestados por período (data inicial e data final) 

8) Ler todos os registros da tabela de Livros e exibi-los em ordem crescente de Código do Livro. Os seguintes dados deverão ser mostrados:
Cod_Livro, título, Nome do Autor, Nome da Categoria, disponibilidade
Ao final, mostrar a quantidade livros disponíveis e a quantidade total de livros que estão emprestados.








