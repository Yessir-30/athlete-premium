import { renderUserProfile } from "./user.js";
import { renderNutrition } from "./nutrition.js";
import { renderTraining } from "./training.js";
import { renderProgress } from "./progress.js";

document.addEventListener("DOMContentLoaded", async () => {
  await renderUserProfile();
  await renderNutrition();
  await renderTraining();
  await renderProgress();
});
