/**
 * Multilingual Agri-AI Assistant Chatbot Module
 */

function toggleChatbot() {
    const drawer = document.getElementById("chatbot-drawer");
    drawer.classList.toggle("translate-y-full");
    drawer.classList.toggle("opacity-0");
    drawer.classList.toggle("pointer-events-none");
}

async function sendChatMessage() {
    const input = document.getElementById("chat-input");
    const msg = input.value.trim();
    if (!msg) return;

    appendChatMessage("user", msg);
    input.value = "";

    try {
        const res = await fetch("/api/assistant/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                message: msg,
                language: currentLang
            })
        });
        const data = await res.json();
        appendChatMessage("assistant", data.reply, data.suggested_actions);
    } catch (err) {
        appendChatMessage("assistant", "Sorry, I am having trouble connecting to the agronomic server. Please try again.");
    }
}

function appendChatMessage(role, text, actions = []) {
    const chatBody = document.getElementById("chat-messages-container");
    const msgDiv = document.createElement("div");
    msgDiv.className = `flex ${role === 'user' ? 'justify-end' : 'justify-start'} mb-3`;

    const bubble = document.createElement("div");
    bubble.className = `max-w-[85%] p-3 rounded-2xl text-xs leading-relaxed ${
        role === 'user'
            ? 'bg-emerald-600 text-white rounded-br-none'
            : 'bg-slate-800 border border-slate-700 text-slate-200 rounded-bl-none'
    }`;
    bubble.innerHTML = `<p>${text}</p>`;

    if (actions && actions.length > 0) {
        const actionGroup = document.createElement("div");
        actionGroup.className = "flex flex-wrap gap-1.5 mt-2.5 pt-2 border-t border-slate-700/60";
        actions.forEach(act => {
            const btn = document.createElement("button");
            btn.className = "px-2 py-0.5 bg-slate-700/70 hover:bg-emerald-600/60 text-[11px] rounded text-emerald-300 transition";
            btn.textContent = act;
            btn.onclick = () => {
                document.getElementById("chat-input").value = act;
                sendChatMessage();
            };
            actionGroup.appendChild(btn);
        });
        bubble.appendChild(actionGroup);
    }

    msgDiv.appendChild(bubble);
    chatBody.appendChild(msgDiv);
    chatBody.scrollTop = chatBody.scrollHeight;
}
