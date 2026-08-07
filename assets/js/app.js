// ===============================
// Athlete Premium – Version 0.2
// Gestion du profil + LocalStorage
// ===============================

// Profil par défaut
const defaultUser = {
    name: "Athlete",
    age: 20,
    weight: 70,
    height: 175,
    goal: "Hypertrophie"
};

// ===============================
// Chargement / Sauvegarde
// ===============================

function loadUser() {
    try {
        const data = localStorage.getItem("athleteUser");
        return data ? JSON.parse(data) : null;
    } catch (e) {
        console.error("Erreur chargement user :", e);
        return null;
    }
}

function saveUser() {
    try {
        localStorage.setItem("athleteUser", JSON.stringify(user));
    } catch (e) {
        console.error("Erreur sauvegarde user :", e);
    }
}

// ===============================
// Initialisation
// ===============================

let user = loadUser() || defaultUser;

// ===============================
// Mise à jour de l'interface
// ===============================

function updateUI() {
    const nameEl = document.getElementById("user-name");
    const weightEl = document.getElementById("user-weight");
    const ageEl = document.getElementById("user-age");
    const heightEl = document.getElementById("user-height");
    const goalEl = document.getElementById("user-goal");

    if (nameEl) nameEl.textContent = user.name;
    if (weightEl) weightEl.textContent = user.weight + " kg";
    if (ageEl) ageEl.textContent = user.age + " ans";
    if (heightEl) heightEl.textContent = user.height + " cm";
    if (goalEl) goalEl.textContent = user.goal;
}

// ===============================
// Formulaire de modification
// ===============================

function initProfileForm() {
    const form = document.getElementById("profile-form");
    if (!form) return;

    form.addEventListener("submit", (e) => {
        e.preventDefault();

        user.name = form.name.value;
        user.age = parseInt(form.age.value);
        user.weight = parseFloat(form.weight.value);
        user.height = parseFloat(form.height.value);
        user.goal = form.goal.value;

        saveUser();
        updateUI();

        alert("Profil mis à jour !");
    });
}

// ===============================
// Démarrage
// ===============================
// Connexion avec les modules
if (typeof initUserModule === "function") initUserModule(user);
if (typeof initTrainingModule === "function") initTrainingModule(user);
if (typeof initProgressModule === "function") initProgressModule(user);
if (typeof initNutritionModule === "function") initNutritionModule(user);

document.addEventListener("DOMContentLoaded", () => {
    updateUI();
    initProfileForm();
});
