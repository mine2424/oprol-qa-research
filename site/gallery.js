const query = document.querySelector("#query");
const mode = document.querySelector("#mode");
const sections = [...document.querySelectorAll(".gallery-content section")];

function updateGallery() {
  const terms = query.value
    .normalize("NFKC")
    .toLowerCase()
    .trim()
    .split(/\s+/)
    .filter(Boolean);
  let count = 0;
  sections.forEach((section) => {
    const text = (section.dataset.search + " " + section.textContent)
      .normalize("NFKC")
      .toLowerCase();
    section.hidden =
      !terms.every((term) => text.includes(term)) ||
      (mode.value !== "all" && !section.querySelector(".media." + mode.value));
    if (!section.hidden) count++;
    section.querySelectorAll(".media").forEach((media) => {
      media.hidden =
        mode.value !== "all" && !media.classList.contains(mode.value);
    });
    section.querySelectorAll(".image-label").forEach((label) => {
      label.hidden = mode.value === "video";
    });
    section.querySelectorAll(".video-label").forEach((label) => {
      label.hidden = mode.value === "image";
    });
    section.querySelectorAll("video").forEach((video) => {
      if (section.hidden || mode.value === "image") video.pause();
    });
    const shortcut = document.querySelector(`.index a[href="#${section.id}"]`);
    if (shortcut) shortcut.hidden = section.hidden;
  });
  document.querySelector("#count").textContent =
    `${count} / ${sections.length} 製品`;
  document.querySelector("#empty-results").hidden = count > 0;
}

query.addEventListener("input", updateGallery);
mode.addEventListener("change", updateGallery);
document.querySelector("#gallery-reset").addEventListener("click", () => {
  query.value = "";
  mode.value = "all";
  updateGallery();
  query.focus();
});

function revealProduct() {
  const section = sections.find(
    (item) => `#${item.id}` === window.location.hash,
  );
  if (!section) return;
  query.value = "";
  mode.value = "all";
  updateGallery();
  const picker = document.querySelector(".product-picker");
  if (picker) picker.open = false;
  section.querySelectorAll("details").forEach((details) => {
    details.open = true;
  });
  section.scrollIntoView();
  const heading = section.querySelector("h2");
  heading.tabIndex = -1;
  heading.focus({ preventScroll: true });
}

window.addEventListener("hashchange", revealProduct);
updateGallery();
revealProduct();
