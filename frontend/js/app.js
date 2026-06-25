const API_URL = "https://usuarios-eventos-app.onrender.com";

const form = document.getElementById("user-form");
const usersContainer = document.getElementById("users-container");
const searchInput = document.getElementById("search-input");
let usuarioEditandoId = null;
let usuariosGlobal = [];

form.addEventListener("submit", async (event) => {
    event.preventDefault();
    const user = {
        name: document.getElementById("name").value,
        email: document.getElementById("email").value
    };
    try {
        if (usuarioEditandoId) {
            const response = await fetch(`${API_URL}/usuarios/${usuarioEditandoId}`, {
                method: "PUT",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(user)
            });
            if (!response.ok) throw new Error("Error actualizando usuario");
            alert("Usuario actualizado");
            usuarioEditandoId = null;
            form.querySelector("button").textContent = "Crear";
        }
        else {
            const response = await fetch(`${API_URL}/usuarios`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(user)
            });
            if (!response.ok) throw new Error("Error creando usuario");
            alert("Usuario creado");
        }
        form.reset();
        obtenerUsuarios();
    } catch (error) {
        console.error(error);
        alert("Error en operación");
    }
});

async function obtenerUsuarios() {
    try {
        const response = await fetch(`${API_URL}/usuarios`);
        if (!response.ok) {
            throw new Error("Error consultando usuarios");
        }
        const usuarios = await response.json();
        usuariosGlobal = usuarios;
        mostrarUsuarios(usuarios);
    } catch (error) {
        console.error(error);
    }
}

function mostrarUsuarios(usuarios) {
    usersContainer.innerHTML = "";
    usuarios.forEach(usuario => {
        const card = document.createElement("div");
        card.classList.add("user-card");
        const fecha = new Date(usuario.created_at).toLocaleString();
        card.innerHTML = `
            <div class="user-info">
                <h3>${usuario.name}</h3>
                <p>${usuario.email}</p>
                <small>Fecha registro: ${new Date(usuario.created_at).toLocaleString()}</small>
            </div>
            <div class="user-actions">
                <button onclick="cargarFormularioEdicion(${usuario.id}, '${usuario.name}', '${usuario.email}')">
                    Editar
                </button>
                <button onclick="eliminarUsuario(${usuario.id})">
                    Eliminar
                </button>
            </div>
        `;
        usersContainer.appendChild(card);
    });
}
obtenerUsuarios();

async function eliminarUsuario(id) {
    const confirmacion = confirm("¿Seguro que quieres eliminar este usuario?");
    if (!confirmacion) return;
    try {
        const response = await fetch(`${API_URL}/usuarios/${id}`, {
            method: "DELETE"
        });
        if (!response.ok) {
            throw new Error("Error eliminando usuario");
        }
        alert("Usuario eliminado");
        obtenerUsuarios();
    } catch (error) {
        console.error(error);
        alert("Error eliminando usuario");
    }
}

function cargarFormularioEdicion(id, name, email) {
    usuarioEditandoId = id;
    document.getElementById("name").value = name;
    document.getElementById("email").value = email;
    const btn = form.querySelector("button");
    btn.textContent = "Actualizar usuario";
    form.scrollIntoView({
        behavior: "smooth",
        block: "center"
    });
    document.getElementById("name").focus();
}

function filtrarUsuarios(texto) {
    const filtrados = usuariosGlobal.filter(usuario => {
        return (
            usuario.name.toLowerCase().includes(texto.toLowerCase()) ||
            usuario.email.toLowerCase().includes(texto.toLowerCase())
        );
    });
    mostrarUsuarios(filtrados);
}

searchInput.addEventListener("input", (e) => {
    filtrarUsuarios(e.target.value);
});