async function enviarSentimento() {
    const sentimento = document.getElementById("sentimento").value;
    if (!sentimento) return alert("Digite como você está se sentindo!");

    // Limpa antes de preencher
    document.getElementById("versiculo").innerText = "⏳ Buscando versículo...";
    document.getElementById("conforto").innerText = "";
    document.getElementById("louvores").innerText = "";
    document.getElementById("notas").innerText = "";

    const resposta = await fetch("/gerar", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ sentimento })
    });

    const dados = await resposta.json();

    document.getElementById("versiculo").innerText = dados.versiculos || "N/A";
    document.getElementById("conforto").innerText = dados.conforto || "N/A";
    document.getElementById("louvores").innerText = dados.louvores || "N/A";
    document.getElementById("notas").innerText = dados.notas || "N/A";

    // Exibe o áudio
    const player = document.getElementById("player");
    const source = document.getElementById("audioSource");
    source.src = dados.audio_url;
    player.load();
    player.style.display = "block";
}
