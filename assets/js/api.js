const API_BASE = "http://127.0.0.1:8000";

export async function apiGet(path) {
  const res = await fetch(API_BASE + path);
  return await res.json();
}

export async function apiPost(path, payload) {
  const res = await fetch(API_BASE + path, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload)
  });
  return await res.json();
}

export async function apiPut(path, payload) {
  const res = await fetch(API_BASE + path, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload)
  });
  return await res.json();
}
