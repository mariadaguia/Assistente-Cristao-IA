# Imagem base
FROM python:3.10-slim

# Diretório de trabalho
WORKDIR /app

# Copia o projeto para o container
COPY . /app

# Variáveis para instalação silenciosa
ENV DEBIAN_FRONTEND=noninteractive

# Instala dependências do sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    libasound2-dev \
    libsndfile1-dev \
    fluidsynth \
    ffmpeg \
    wget \
    curl \
    fluid-soundfont-gm \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Atualiza o pip
RUN pip install --upgrade pip

# Instala bibliotecas Python necessárias
RUN pip install --root-user-action=ignore --no-cache-dir \
    flask \
    mingus \
    music21 \
    google-genai \
    google-adk \
    ipython \
    jupyter\
    python-dotenv \
    mido

RUN pip install --upgrade google-generativeai

# Define variável de ambiente para a API do Gemini
ENV GOOGLE_API_KEY=""

# Define variável padrão da soundfont
ENV SOUND_FONT_PATH="/usr/share/sounds/sf2/FluidR3_GM.sf2"

# Expõe a porta usada no app.py
EXPOSE 4000

# Roda o servidor Flask
CMD ["python", "app.py"]
