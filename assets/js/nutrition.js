import { apiGet, apiPut } from "./api.js";

export async function loadNutrition() {
  return await apiGet("/nutrition/");
}

export async function updateNutritionField(field, value) {
  const payload = { [field]: value };
  const updated = await apiPut("/nutrition/", payload);
  renderNutrition(updated);
}

export async function renderNutrition(data = null) {
  if (!data) data = await loadNutrition();
  if (!data) return;

  document.getElementById("nutri-calories").textContent = data.calories ?? "-";
  document.getElementById("nutri-proteins").textContent = data.proteins ?? "-";
  document.getElementById("nutri-hydration").textContent = data.hydration ?? "-";
}
