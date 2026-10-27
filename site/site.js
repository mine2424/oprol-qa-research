const normalize = (text) => text.normalize("NFKC").toLowerCase().trim();

document.querySelectorAll("[data-filter-root]").forEach((root) => {
  const input = root.querySelector("[data-filter-query]");
  const items = [...root.querySelectorAll("[data-filter-item]")];
  const update = () => {
    const terms = normalize(input.value).split(/\s+/).filter(Boolean);
    let count = 0;
    items.forEach((item) => {
      item.hidden = !terms.every((term) =>
        normalize(item.textContent).includes(term),
      );
      if (!item.hidden) count++;
    });
    root.querySelector("[data-filter-count]").textContent =
      `${count} / ${items.length} 件`;
    root.querySelector("[data-filter-empty]").hidden = count > 0;
  };
  input.addEventListener("input", update);
  root.querySelector("[data-filter-reset]").addEventListener("click", () => {
    input.value = "";
    update();
    input.focus();
  });
  update();
});

document.querySelectorAll(".page-toc details").forEach((details) => {
  const media = window.matchMedia("(min-width: 1100px)");
  const resize = () => {
    details.open = media.matches;
  };
  media.addEventListener("change", resize);
  resize();
});

document.querySelectorAll(".table-scroll").forEach((region) => {
  const resize = () => {
    const scrollable =
      region.scrollWidth > region.clientWidth ||
      region.scrollHeight > region.clientHeight;
    if (scrollable) region.tabIndex = 0;
    else region.removeAttribute("tabindex");
  };
  new ResizeObserver(resize).observe(region);
});

const viewer = document.querySelector("#image-viewer");
const full = document.querySelector("#image-full");
const imageStatus = document.querySelector("#image-status");
let origin = null;
full.addEventListener("load", () => {
  imageStatus.hidden = true;
});
full.addEventListener("error", () => {
  imageStatus.textContent =
    "画像を読み込めませんでした。「元画像を開く」から再度お試しください。";
  imageStatus.hidden = false;
});

document.querySelectorAll("main img").forEach((image) => {
  let trigger = image.closest("a");
  if (!trigger) {
    trigger = document.createElement("button");
    trigger.type = "button";
    trigger.className = "image-trigger";
    image.before(trigger);
    trigger.append(image);
  }
  trigger.setAttribute("aria-label", `${image.alt || "画面"}を拡大`);
  trigger.setAttribute("aria-haspopup", "dialog");
  trigger.addEventListener("click", (event) => {
    if (event.metaKey || event.ctrlKey || event.shiftKey || event.altKey)
      return;
    event.preventDefault();
    origin = trigger;
    imageStatus.textContent = "画像を読み込んでいます…";
    imageStatus.hidden = false;
    full.src = image.currentSrc || image.src;
    full.alt = image.alt;
    document.querySelector("#image-title").textContent =
      image.alt || "画面を拡大";
    document.querySelector("#image-original").href = full.src;
    viewer.showModal();
    document.body.classList.add("viewer-open");
  });
});
document
  .querySelector("#image-close")
  .addEventListener("click", () => viewer.close());
viewer.addEventListener("click", (event) => {
  if (event.target === viewer) viewer.close();
});
viewer.addEventListener("close", () => {
  document.body.classList.remove("viewer-open");
  full.removeAttribute("src");
  origin?.focus();
});
