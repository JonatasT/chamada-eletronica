# Chamada eletrônica

### Introdução:

Proposta de solução para uma versão eletrônica e colaborativa/descentralizada da chamada de presença, para a disciplina CIC0105 - Engenharia de Software 2023.1

A 'Chamada eletrônica' é uma alternativa ao sistema atual de tomada de presença de alunos nas aulas presenciais ministradas na Universidade de Brasília - UnB. Entende-se por pertinente a apresentação de uma proposta digital que, além de permitir o gerenciamento do fluxo de frequência dos alunos, diminua o risco de erros provenientes de falha humana e economize papel.

### Funcionalidades do Sistema:

Registro online de Presença: Os participantes poderão marcar sua presença de forma eletrônica, utilizando um formulário web. O sistema registrará automaticamente a data, hora e local da presença, garantindo a precisão e integridade dos dados.

**Colaboração e Descentralização:** O sistema permitirá que diversos usuários, como professores, alunos ou funcionários, lancem registros de presença de forma colaborativa. A persistência dos dados de presença se dará através de um banco de dados descentralizado, como o SQLite ou o MongoDB, utilizando como por exemplo o Flask como framework web para a comunicação com o banco de dados. Isso nos entregará transparência, imutabilidade e segurança dos dados.

**Acesso Controlado e Autenticação:** O sistema terá recursos de controle de acesso e autenticação, utilizando recursos de autenticação de bibliotecas especializadas, ou mesmo do framework empregado. Apenas usuários autorizados, como os professores ou administradores, poderão registrar a presença, garantindo a segurança do sistema.

**Notificações e Lembretes:** O sistema poderá enviar notificações e lembretes automáticos aos participantes para registrar sua presença, utilizando recursos de e-mails ou outros caminhos de comunicação, evitando esquecimentos ou atrasos.

**Relatórios e Análises:** O sistema poderá gerar relatórios e análises pormenorizados sobre a presença dos participantes, utilizando bibliotecas de visualização de dados integradas ao framework utilizado. Isso permitirá que os administradores ou responsáveis acompanhem o comparecimento em tempo real, identifiquem tendências e tomem decisões informadas com base nos dados coletados.