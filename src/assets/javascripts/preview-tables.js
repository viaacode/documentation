document.querySelectorAll(".preview-table table").forEach((table) => {
  const rows = Array.from(table.tBodies).flatMap((body) => Array.from(body.rows)).slice(3);
  if (!rows.length) return;

  const columns = Array.from(table.rows).reduce((max, row) => Math.max(
    max, Array.from(row.cells).reduce((sum, cell) => sum + cell.colSpan, 0)
  ), 0);
  const footer = table.createTFoot().insertRow();
  footer.className = "preview-table-toggle";
  const cell = footer.insertCell();
  cell.colSpan = columns;
  const button = document.createElement("button");
  button.type = "button";
  cell.append(button);

  function setExpanded(expanded) {
    rows.forEach((row) => { row.hidden = !expanded; });
    button.setAttribute("aria-expanded", String(expanded));
    button.textContent = expanded ? "See less" : "See more";
  }

  button.addEventListener("click", () => {
    setExpanded(button.getAttribute("aria-expanded") !== "true");
  });
  setExpanded(false);
});
