import { loadDataFromApi, saveDataToApi } from "./core.js";

export async function loadUser() {
  return await loadDataFromApi("/user/", null);
}

export async function updateUserField(field, value) {
  const payload = { [field]: value };
  const updated = await saveDataToApi("/user/", payload);
  renderUserProfile(updated);
}

export async function renderUserProfile(user = null) {
  if (!user) user = await loadUser();
  if (!user || user.status === "empty") return;

  document.getElementById("user-name").textContent = user.first_name;
  document.getElementById("user-height").textContent = `${user.height} cm`;
  document.getElementById("user-weight").textContent = `${user.weight} kg`;
  document.getElementById("user-goal").textContent = `${user.goal_weight} kg`;
}
