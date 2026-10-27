document.querySelectorAll(".table-scroll").forEach((region) => {
  if (region.scrollWidth <= region.clientWidth)
    region.removeAttribute("tabindex");
});
