const q = document.querySelector("#query"),
  m = document.querySelector("#mode"),
  ss = [...document.querySelectorAll("section")];
function update() {
  let n = 0;
  for (const s of ss) {
    const text = (s.dataset.search + " " + s.textContent).toLowerCase(),
      ok =
        text.includes(q.value.toLowerCase()) &&
        (m.value === "all" || !!s.querySelector(".media." + m.value));
    s.hidden = !ok;
    if (ok) n++;
    for (const e of s.querySelectorAll(".media"))
      e.hidden =
        (m.value === "video" && !e.classList.contains("video")) ||
        (m.value === "image" && !e.classList.contains("image"));
    for (const e of s.querySelectorAll(".image-label"))
      e.hidden = m.value === "video";
    for (const e of s.querySelectorAll(".video-label"))
      e.hidden = m.value === "image";
  }
  document.querySelector("#count").textContent =
    n + " / " + ss.length + " 製品";
  document.querySelector("#empty-results").hidden = n > 0;
}
q.addEventListener("input", update);
m.addEventListener("change", update);
update();
