const content = window.HOMEPAGE_CONTENT;

const researchList = document.querySelector("#research-list");
if (researchList && content) {
  researchList.innerHTML = content.research.map((item, index) => `
    <article class="research-item">
      <h3>${item.title}</h3>
      <p>${item.description}</p>
    </article>
  `).join("");
}

function highlightName(authors) {
  return authors.replaceAll("X. Liu", '<span class="me">X. Liu</span>');
}

const publicationList = document.querySelector("#publication-list");
if (publicationList && content) publicationList.innerHTML = content.publications.map(item => `
  <li class="publication-item">
    <div class="publication-title">${item.title}${item.first ? '<span class="star" title="First-author paper">★</span>' : ""}</div>
    <p class="publication-authors">${highlightName(item.authors)}</p>
    <p class="publication-venue">${item.venue}</p>
    <div class="publication-links">
      ${item.doi ? `<a href="${item.doi}" target="_blank" rel="noreferrer">DOI</a>` : ""}
      <a href="${item.scholar}" target="_blank" rel="noreferrer">Scholar</a>
    </div>
  </li>
`).join("");

const menuButton = document.querySelector(".menu-button");
const nav = document.querySelector(".topbar nav");
menuButton.addEventListener("click", () => {
  const open = nav.classList.toggle("open");
  menuButton.setAttribute("aria-expanded", String(open));
});
nav.addEventListener("click", () => {
  nav.classList.remove("open");
  menuButton.setAttribute("aria-expanded", "false");
});

document.querySelectorAll(".year").forEach(element => {
  element.textContent = new Date().getFullYear();
});
