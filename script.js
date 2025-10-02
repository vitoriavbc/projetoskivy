let itens = [];

// Carregar do localStorage ao iniciar
window.onload = () => {
  carregarLocalStorage();
  listarItens();
};

function adicionarItem() {
  const input = document.getElementById("inputItem");
  const valor = input.value.trim();

  if (valor === "") {
    exibirMensagem("Digite um item válido ❌", "red");
    return;
  }

  if (itens.includes(valor)) {
    exibirMensagem("Item duplicado ❌", "red");
    return;
  }

  itens.push(valor);
  salvarLocalStorage();
  listarItens();
  input.value = "";
  exibirMensagem("Item adicionado com sucesso ✅", "green");
}

function listarItens() {
  const lista = document.getElementById("lista");
  lista.innerHTML = "";

  itens.forEach((item, index) => {
    const li = document.createElement("li");

    const span = document.createElement("span");
    span.textContent = item;

    const btnEditar = document.createElement("button");
    btnEditar.textContent = "✏️ Editar";
    btnEditar.onclick = () => editarItem(index);

    const btnExcluir = document.createElement("button");
    btnExcluir.textContent = "🗑️ Excluir";
    btnExcluir.onclick = () => removerItem(index);

    li.appendChild(span);
    li.appendChild(btnEditar);
    li.appendChild(btnExcluir);
    lista.appendChild(li);
  });
}

function removerItem(index) {
  itens.splice(index, 1);
  salvarLocalStorage();
  listarItens();
  exibirMensagem("Item removido 🗑️", "orange");
}

function editarItem(index) {
  const input = document.getElementById("inputItem");
  input.value = itens[index];
  removerItem(index);
}

function salvarLocalStorage() {
  localStorage.setItem("lista", JSON.stringify(itens));
}

function carregarLocalStorage() {
  const dados = localStorage.getItem("lista");
  if (dados) {
    itens = JSON.parse(dados);
  }
}

function exibirMensagem(texto, cor) {
  const msg = document.getElementById("mensagem");
  msg.textContent = texto;
  msg.style.color = cor;
  setTimeout(() => {
    msg.textContent = "";
  }, 2000);
}
