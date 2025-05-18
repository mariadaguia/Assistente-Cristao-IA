# 🎶 Conforto biblico com IA

Um projeto que combina Inteligência Artificial, espiritualidade e música para oferecer **conforto emocional** a partir de um sentimento digitado pelo usuário. A aplicação usa agentes de IA para gerar versículos bíblicos, mensagens de conforto, sugestões de louvores e uma melodia personalizada — tudo isso apresentado em uma interface web interativa com player de áudio.

---

## ✨ Funcionalidades

- ✅ Identificação de sentimentos informados pelo usuário
- 📖 Geração de até 3 versículos bíblicos relacionados ao sentimento
- 💌 Criação de uma mensagem de conforto emocional
- 🎶 Sugestão de louvores cristãos relacionados ao tema
- 🎼 Geração de uma melodia personalizada com IA
- 🔊 Reprodução da música gerada diretamente no navegador

---

## 🖼️ Exemplo de uso

1. Usuário acessa a página e digita como está se sentindo (ex: "ansioso", "triste", "grato").
2. O sistema responde com:
   - Versículos bíblicos de apoio
   - Uma mensagem de conforto
   - Sugestão de louvores
   - Uma melodia gerada pelo modelo automaticamente
3. A música pode ser ouvida diretamente na página.

---

## ⚙️ Tecnologias usadas

- [Python 3.10+](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Google Generative AI (`google-generativeai`)](https://github.com/google/generative-ai-python)
- [Mido](https://mido.readthedocs.io/) para geração de arquivos MIDI
- [FluidSynth](https://www.fluidsynth.org/) para conversão de MIDI em WAV
- [HTML + JS] com `fetch` para comunicação assíncrona
- [Docker](https://www.docker.com/) para empacotamento e execução

---

## 🚀 Como executar

### Pré-requisitos

- Docker instalado
- Uma chave da API do [Google Gemini](https://aistudio.google.com/app/apikey)

### Configuração

1. Crie um arquivo `.env` com sua chave da API:

```env
GOOGLE_API_KEY=AIza...sua_chave_aqui...

![Status](https://img.shields.io/badge/status-em%20desenvolvimento-blue)
![Licença MIT](https://img.shields.io/badge/licença-MIT-green)
![Feito com ❤️](https://img.shields.io/badge/feito%20com-%E2%9D%A4-red)

## 🎥 Demonstração

![Demonstração](demo.gif)

