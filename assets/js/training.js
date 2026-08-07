import { apiGet, apiPost } from "./api.js";

export async function loadTraining() {
  return await apiGet("/training/");
}

export async function addTrainingSession(sessionType, notes) {
  const payload = { session_type: sessionType, notes };
  const created = await apiPost("/training/", payload);
  renderTraining();
}

export async function renderTraining() {
  const sessions = await loadTraining();
  const container = document.getElementById("training-list");
  container.innerHTML = "";

  sessions.forEach(s => {
    const item = document.createElement("div");
    item.textContent = `${s.session_type} — ${s.notes ?? ""}`;
    container.appendChild(item);
  });
}
