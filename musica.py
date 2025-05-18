import mido
import random
import subprocess
import os
from mido import MidiFile, MidiTrack, Message, bpm2tempo, second2tick, MetaMessage
from mingus.containers import Note, Bar
from mingus.midi import midi_file_out


MIDI_PATH = "musica.mid"
WAV_PATH = "musica.wav"
SOUNDFONT_PATH = os.environ.get("SOUND_FONT_PATH", "/usr/share/sounds/sf2/FluidR3_GM.sf2")


notas_base = {
    'C': 0, 'C#': 1, 'Db': 1,
    'D': 2, 'D#': 3, 'Eb': 3,
    'E': 4, 'Fb': 4,
    'F': 5, 'E#': 5, 'F#': 6, 'Gb': 6,
    'G': 7, 'G#': 8, 'Ab': 8,
    'A': 9, 'A#': 10, 'Bb': 10,
    'B': 11, 'Cb': 11
}

def note_name_to_number(nome):
    nome = nome.strip().upper()

    if len(nome) == 3:  # ex: C#4, Bb3
        nota = nome[:2]
        oitava = int(nome[2])
    elif len(nome) == 2:  # ex: C4
        nota = nome[0]
        oitava = int(nome[1])
    else:
        raise ValueError(f"Formato inválido: {nome}")

    if nota not in notas_base:
        raise ValueError(f"Nota desconhecida: {nota}")

    semitom = notas_base[nota]
    return (oitava + 1) * 12 + semitom


# Gera um arquivo MIDI com notas simples (escala)
def gerar_midi_simples():
    bar = Bar()
    for nota in ["C", "D", "E", "F", "G", "A", "B", "C"]:
        bar + Note(nota)
    midi_file_out.write_Bar(MIDI_PATH, bar)

#Converte o MIDI para WAV com fluidsynth

def midi_para_wav():
    subprocess.run([
        "fluidsynth", "-ni", SOUNDFONT_PATH, MIDI_PATH,
        "-F", WAV_PATH, "-r", "44100"
    ], check=True)

def gerar_midi(notas):
    nome_arquivo="musica.mid"
    midi_file = MidiFile()
    track = MidiTrack()
    midi_file.tracks.append(track)

    bpm = 120 + random.randint(3, 100)
    track.append(MetaMessage('set_tempo', tempo=bpm2tempo(bpm)))

    track.append(Message('program_change', program=0, channel=0))

    notas = [n.strip() for n in notas.split(",") if n.strip()]
    duracoes = [1.0] * len(notas)
    tempo_atual = 0

    for i, nota_nome in enumerate(notas):
        nota_numero = note_name_to_number(nota_nome)
        duracao_em_ticks = int(second2tick(duracoes[i], midi_file.ticks_per_beat, bpm2tempo(bpm)))

        track.append(Message('note_on', note=nota_numero, velocity=64, time=tempo_atual, channel=0))
        track.append(Message('note_off', note=nota_numero, velocity=64, time=duracao_em_ticks, channel=0))
        tempo_atual = 0

    track.append(MetaMessage('end_of_track'))
    midi_file.save(nome_arquivo)
    print(f"🎵 Arquivo MIDI '{nome_arquivo}' gerado com sucesso!")