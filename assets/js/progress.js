import { apiGet, apiPost } from "./api.js";

export async function loadProgress() {
  return await apiGet("/progress/");
}

export async function addProgressEntry(weight, muscleMass, comment) {
  const payload = { weight, muscle_mass: muscleMass, comment };
  const created = await apiPost("/progress/", payload);
  renderProgress();
}

export async function renderProgress() {
  const entries = await loadProgress();
  const container = document.getElementById("progress-list");
  container.innerHTML = "";

  entries.forEach(e => {
    const item = document.createElement("div");
    item.textContent = `${e.weight} kg — ${e.muscle_mass} — ${e.comment ?? ""}`;
    container.appendChild(item);
  });
}
