import { apiGet, apiPost, apiPut } from "./api.js";

// FRONT → BACKEND → DB → BACKEND → FRONT

export async function loadDataFromApi(path, fallback) {
  try {
    const data = await apiGet(path);
    return data || fallback;
  } catch {
    return fallback;
  }
}

export async function saveDataToApi(path, payload) {
  return await apiPut(path, payload);
}
