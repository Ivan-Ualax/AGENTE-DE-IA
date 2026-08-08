const form = document.querySelector("#chat-form");
const input = document.querySelector("#message");
const button = document.querySelector("#send-button");
const messages = document.querySelector("#messages");

function addMessage(role, text, isError = false) {
  const article = document.createElement("article");
  article.className = `message ${role}${isError ? " error" : ""}`;

  const label = document.createElement("strong");
  label.textContent = role === "user" ? "MESTRE" : "IA";

  const paragraph = document.createElement("p");
  paragraph.textContent = text;

  article.append(label, paragraph);
  messages.append(article);
  article.scrollIntoView({ behavior: "smooth", block: "end" });
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  const message = input.value.trim();
  if (!message) return;

  addMessage("user", message);
  input.value = "";
  button.disabled = true;
  button.textContent = "Analisando...";

  try {
    const response = await fetch("/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message }),
    });

    const data = await response.json();
    if (!response.ok) throw new Error(data.detail || "Erro inesperado.");
    addMessage("assistant", data.reply);
  } catch (error) {
    addMessage("assistant", error.message, true);
  } finally {
    button.disabled = false;
    button.textContent = "Enviar";
    input.focus();
  }
});
