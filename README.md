# Diaryme

Bem-vindo(a) à nossa plataforma de criação e gerenciamento de posts! Aqui, você pode exercitar a escrita de forma terapêutica e reflexiva, em um ambiente seguro e privado.

Link: https://diaryme.onrender.com/login

<a href='https://github.com/Carlos-Guilherme/Diaryme/edit/main/README.md#objetivo'>Objetivo</a> | 
<a href='https://github.com/Carlos-Guilherme/Diaryme/edit/main/README.md#seguran%C3%A7a-e-privacidade'>Segurança e privacidade</a>
<a href='https://github.com/Carlos-Guilherme/Diaryme/edit/main/README.md#limita%C3%A7%C3%B5es'>Limitações</a>
#
Nosso site é desenvolvido com Flask, uma poderosa ferramenta para a criação de aplicações web, e conta com recursos como o banco de dados SQLite e a biblioteca Flask-SQLalchemy, para garantir a segurança e o armazenamento adequado de suas informações.

Ao se cadastrar, você terá acesso a uma página de perfil onde poderá visualizar seus próprios posts, criar novos e editar ou excluir os que já foram publicados. Você também pode editar o seu próprio perfil, trocando o nome de usuário e a foto de perfil.

Para tornar a interface mais amigável e responsiva, utilizamos a ferramenta Bootstrap, que ajuda na organização visual das páginas e na adaptação a diferentes dispositivos.

Além disso, você receberá feedback instantâneo após cada ação realizada, graças às nossas mensagens flash. Tudo isso para tornar sua experiência ainda mais prazerosa e agradável.

Então, se você busca uma plataforma para a prática da escrita e reflexão, está no lugar certo! Venha exercitar a sua criatividade e conhecer pessoas que valorizam a arte de escrever. Cadastre-se agora mesmo e comece a criar seus posts!
#
![image](https://user-images.githubusercontent.com/72580077/234095394-21d86926-2162-41e5-a2e1-244cd5ae73cc.png)

### Objetivo
O objetivo da plataforma é oferecer aos usuários uma ferramenta para exercitar a escrita de forma terapêutica e reflexiva, em um ambiente seguro e privado. Para isso, seguimos todas as boas práticas de programação, garantindo a qualidade do código e a manutenibilidade da plataforma.

Nosso compromisso é oferecer aos usuários a melhor experiência de uso possível, garantindo a segurança e privacidade de seus dados e o máximo de praticidade e facilidade na utilização da plataforma.

### Segurança e privacidade
No caso da nossa plataforma, utilizamos o pacote Flask-Bcrypt para gerenciar a criptografia das senhas dos usuários.

Quando um novo usuário se registra na plataforma, a senha fornecida é criptografada antes de ser armazenada no banco de dados. Para isso, utilizamos uma função hash que é aplicada à senha fornecida pelo usuário. Essa função gera um hash de 60 caracteres que é armazenado no banco de dados no lugar da senha em si. Isso significa que, mesmo que um invasor tenha acesso ao banco de dados, ele não será capaz de ler as senhas reais dos usuários.

Além disso, utilizamos validações de login para garantir que apenas usuários registrados possam acessar a plataforma. Para isso, criamos um formulário de login com duas etapas de validação. A primeira etapa de validação é a validação do formulário em si. Isso garante que os campos do formulário sejam preenchidos corretamente antes que a validação da senha seja feita.

Na segunda etapa de validação, verificamos se a senha fornecida pelo usuário está correta. Para isso, comparamos o hash da senha fornecida pelo usuário com o hash armazenado no banco de dados. Se esses hashes forem iguais, o usuário é autenticado com sucesso e redirecionado para a página inicial da plataforma.

Outra boa prática utilizada na criação dos formulários foi o uso do pacote WTForms. Esse pacote nos permitiu criar formulários personalizados de uma forma simples e elegante, com validações customizáveis e mensagens de erro personalizadas.

Por fim, a plataforma também utiliza a tecnologia de sessions do Flask para gerenciar a autenticação e autorização dos usuários. As sessions permitem que a plataforma mantenha o estado do usuário entre as requisições, o que é essencial para garantir que apenas usuários autenticados possam acessar as páginas protegidas.

### Limitações
Nosso site atualmente é hospedado em um plano grauito de hospedagem da Render, ou seja, nosso site suporta apenas uma conexão por vez.
